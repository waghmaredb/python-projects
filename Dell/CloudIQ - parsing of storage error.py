payload = {
    "system_display_identifier": "FNM00190100981",
    "system_name": "UnityXT-480F",
    "system_model": "Unity 480F",
    "timestamp": 1620476550458,
    "timestamp_iso8601": "2021-05-08T12:22Z",
    "current_score": 70,
    "new_issues": [
        {
            "id": "A247D6992C8BA3B97F328D473E9E2E4DD9976270340FB50FD6ADC22B167825FB",
            "impact": -5,
            "description": "The file system 'albtestFS02' is predicted to run out of space within a quarter.",
            "resolution": "Consider increasing the size of the file system.",
            "rule_id": "FILESYSTEM_FULL_WITHIN_24HOURS_RULE",
            "category": "CAPACITY",
            "impacted_objects": [
                {
                    "object_native_id": "fs_178",
                    "object_name": None,
                    "object_id": "CKM00192702174__FILESYSTEM__fs_178",
                    "object_native_type": "FILESYSTEM"
                }
            ]
        }
    ],
    "resolved_issues": []
}

### Create a virtual environment
### py -m venv env

###https://www.nylas.com/blog/use-python-requests-module-rest-apis/
###https://www.geeksforgeeks.org/json-loads-in-python/
###https://developer.dell.com/apis/2748/versions/1.0/docs?nodeUri=docs%2FGetting%20Started%2F02-Making-the-first-call.md

##import json
##print(type(json.dumps(payload)))

#import requests
#import json
#response = requests.get("http://api.open-notify.org/astros.json")
#res_json = json.loads(response.content)
#print(type(res_json))
#print(res_json["people"])

###"rule_id": "FILESYSTEM_FULL_WITHIN_QUARTER_RULE"
###"rule_id": "FILESYSTEM_FULL_WITHIN_MONTH_RULE"
###"rule_id": "FILESYSTEM_FULL_WITHIN_WEEK_RULE"
###"rule_id": "FILESYSTEM_FULL_WITHIN_24HOURS_RULE"

# match rule-id from payload
rule1 = "FILESYSTEM_FULL_WITHIN_QUARTER_RULE"
rule2 = "FILESYSTEM_FULL_WITHIN_MONTH_RULE"
rule3 = "FILESYSTEM_FULL_WITHIN_WEEK_RULE"
rule4 = "FILESYSTEM_FULL_WITHIN_24HOURS_RULE"

incoming_issue = (payload["new_issues"][0]["rule_id"])
msg = ("Storage System" + (payload["system_name"]) + " will run out of space in 24 hours")

if incoming_issue == rule1:
    print("Storage System" + (payload["system_name"]) + " will run out of space in 24 hours")
elif incoming_issue == rule2:
    print("Storage System" + (payload["system_name"]) + " will run out of space in 1 month")
elif incoming_issue == rule3:
    print("Storage System" + (payload["system_name"]) + " will run out of space in 1 week")
elif incoming_issue == rule4:
    print("Storage System" + (payload["system_name"]) + " will run out of space in 24 hours")
else:
    print("No rule matched")

# extract display identifier
system_display_identifier = payload["system_display_identifier"]
print("\nStorage system serial number is " + payload["system_display_identifier"])

# API call to CIQ to login to get a token
import requests
import json

url = "https://cloudiq.apis.dell.com/auth/oauth/v2/token"
#authentication_payload = ('user', 'password')
header = {'Content-Type': 'application/x-www-form-urlencoded'}
data = {'grant_type': 'client_credentials', 'client_id': 'l77aecb2d3661f4e7f9da8e6d79b7c14ef', 'client_secret': '3c79c1ddbba244cf929ab752a4c89dbc'}
token = requests.post(url, data=data, headers=header)

#print(token)

response = (token.json())
#print(response)
print("\nAccess Token is " + response["access_token"])

# send API to call to CIQ to get the system IP address
ciq_system_ip = requests.get("https://cloudiq.apis.dell.com/PROD/CIQ_PublicAPI_PRD/rest/v1/storage_systems/" + system_display_identifier + "?select=ALL", headers={"Authorization": "Bearer " + response["access_token"]})

#print(ciq_system_ip)

ciq_system_ip_response = (ciq_system_ip.json())
print("\nSystem IP Address is " + ciq_system_ip_response["ipv4_address"])
# https://cloudiq.apis.dell.com/PROD/CIQ_PublicAPI_PRD/rest/v1/storage_systems/FNM00190100981?select=ALL
# https://cloudiq.apis.dell.com/PROD/CIQ_PublicAPI_PRD/rest/v1/storage_systems/FNM00190100981?select=ipv4_address
# Not demonstrated - send API call to Unity to extend

### for POST requests