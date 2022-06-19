import sys
import os
import json
import requests

def publish():

   branch = os.environ.get("BRANCH", "")
   token = os.environ.get("GHKEYS", "")
   print("The token is " + token)
   pullid = "1"
   payload = {
      "body": "First Header | Second Header\n------------ | -------------\nContent from cell 1 | Content from cell 2\nContent in the first column | Content in the second column"
   }
   try:
      result = requests.post(f"https://api.github.com/repos/blazerguns/MyMcService/issues/{id}/comments".format(id=pullid),
                     data=json.dumps(payload),
                     headers={'Content-Type': 'application/json',
                              'Accept': 'application/vnd.github.v3.raw+json',
                              'Authorization': 'token {val}'.format(val=token)})
      print("The response is sent")
   except requests.exceptions.RequestException:
         print("Error at resource check")

if __name__ == '__main__':
    publish()
