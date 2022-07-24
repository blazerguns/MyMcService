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
print(json.dumps(response, indent=4))