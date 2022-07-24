from email import message
from importlib.resources import path
import sys
import os
import io
import json
from unicodedata import category
import requests


def send_data(payload, pullid, token):
   url = "https://api.github.com/repos/blazerguns/MyMcService/issues/{id}/comments".format(id=pullid)
   try:
      result = requests.post(url, data=json.dumps(payload),
                     headers={'Content-Type': 'application/json',
                              'Accept': 'application/vnd.github.v3.raw+json',
                              'Authorization': 'token {val}'.format(val=token)}).json()
      print("The response is sent ====> "+ str(result))
   except requests.exceptions.RequestException:
         print("Error at resource check")

def publish():

   branch = os.environ.get("BRANCH", "")
   token = os.environ.get("TOKEN", "")
   pullid = os.environ.get("PULL", "")
   print("Branch " + branch + " Token " + token + " pull id "+ pullid)

   pullid = "1"
   if (pullid == ""):
      return 0
   # Open the pylint file
   if os.path.isfile("pylint_results.json") and os.access("pylint_results.json", os.R_OK):
      # checks if file exists
      with open('pylint_results.json') as json_file:
         json_data = json.load(json_file)
         table_data = ''
         header = "PyLint Result:\n| Type | Path | Message |\n--- | --- | --- |\n"
         for entry in json_data:
            table_data += "| {type} | {path} | {message} |\n".format(type=entry['type'], path=entry['path'] + ':' + str(entry['line']), message=entry['message'])
         #"First Header | Second Header\n------------ | -------------\nContent from cell 1 | Content from cell 2\nContent in the first column | Content in the second column"
         payload = {
            "body": header + table_data
         }
         send_data(payload, pullid, token)

   # Open the sast file
   if os.path.isfile("sast_result.json") and os.access("sast_result.json", os.R_OK):
      # checks if file exists
      with open('sast_result.json') as json_file:
         json_data = json.load(json_file)
         table_data = ''
         header = "SAST Result:\n| Type | Category | Path | Message |\n--- | --- | --- | --- |\n"
         for entry in json_data:
            table_data += "| {type} | {category} | {path} | {message} |\n".format(type=entry['rule']['security_severity_level'],
                                                                                  category=entry['rule']['description'],
                                                                                  path=entry['most_recent_instance']['location']['path'] + ':' + str(entry['most_recent_instance']['location']['start_line']),
                                                                                  message=entry['most_recent_instance']['message']['text'])
         payload = {
            "body": header + table_data
         }
         send_data(payload, pullid, token)

   # Open the sca file
   if os.path.isfile("sca_result.json") and os.access("sca_result.json", os.R_OK):
      # checks if file exists
      with open('sca_result.json') as json_file:
         json_data = json.load(json_file)
         table_data = ''
         header = "SCA Result:\n| Type | Message |\n--- | --- |\n"
         for entry in json_data["repository"]["vulnerabilityAlerts"]["nodes"]:
            table_data += "| {type} | {message} |\n".format(type=entry['securityVulnerability']['package']['name'],
                                                            message=entry['securityVulnerability']['advisory']['description'])
         payload = {
            "body": header + table_data
         }
         send_data(payload, pullid, token)

if __name__ == '__main__':
    publish()
