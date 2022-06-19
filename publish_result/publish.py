import sys
import os
import json
import requests

def publish():

   print("The building branch is " + os.environ.get("BRANCH", "trainingapp.log"))
   pullid = "1"
   payload = {
      "body": "First Header | Second Header\n------------ | -------------\nContent from cell 1 | Content from cell 2\nContent in the first column | Content in the second column"
   }
   try:
      result = requests.post(f"https://api.github.com/repos/blazerguns/MyMcService/issues/{id}/comments".format(id=pullid),
                     data=json.dumps(payload),
                     headers={'Content-Type': 'application/json',
                              'Accept': 'application/vnd.github.v3.raw+json',
                              'Authorization': 'token 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'})
      print("The response is sent")
   except requests.exceptions.RequestException:
         print("Error at resource check")

if __name__ == '__main__':
    publish()
