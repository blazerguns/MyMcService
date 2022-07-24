import os
import json
from pygitapi import HubAPI


token = os.environ.get("TOKEN", "")
print(" Token " + token)
h = HubAPI(token)
query = '''
         {
            repository(name: "MyMcService", owner: "blazerguns") {
               vulnerabilityAlerts(first: 100) {
                  nodes {
                     createdAt
                     dismissedAt
                     securityVulnerability {
                        package {
                              name
                        }
                        advisory {
                              description
                        }
                     }
                  }
               }
            }
         }
         '''
response = h.custom_query(query)
json_object = json.dumps(response, indent=4)
# Writing to sample.json
with open("../publish_result/sca_result.json", "w") as outfile:
   outfile.write(json_object)