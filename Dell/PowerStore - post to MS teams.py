## PowerStore REST API related project

# post to MS Teams channel
import requests
import json
from hurry.filesize import size, iec

powerstore_ip = "https://127.0.0.1"
powerstore_user = "admin"
powerstore_pass = "password"
hosts_uri = "/api/rest/host?select=id,name,description"
host_mapping_uri = "/api/rest/host_volume_mapping?select=id,host_id,volume_id"
volumes_uri = "/api/rest/volume?select=id,name,size"
get_hosts = requests.get(powerstore_ip + hosts_uri, verify=False, auth=(powerstore_user, powerstore_pass))
get_host_mapping = requests.get(powerstore_ip + host_mapping_uri, verify=False, auth=(powerstore_user, powerstore_pass))
get_volumes = requests.get(powerstore_ip + volumes_uri, verify=False, auth=(powerstore_user, powerstore_pass))
#print(get_hosts.status_code)
#print(get_hosts.json())
print("\nHost Name in PowerStore is " + get_hosts.json()[0]["name"])

powerstore_token = (get_hosts.headers['DELL-EMC-TOKEN'])
#print("\nPowerStore Token is " + powerstore_token)

#print(get_host_mapping.status_code)
#print(get_host_mapping.json())
#print(get_volumes.json()[0]["size"])

volume_size = size(get_volumes.json()[0]["size"], system=iec)
print("\nSize in bytes is " + str(volume_size))

print("\nVolume Name Mapped to host " + get_hosts.json()[0]["name"] + " is " + get_volumes.json()[0]["name"])

print("\nVolume size allocated to host " + get_hosts.json()[0]["name"] + " is " + volume_size)


# extract capacity report from powerstore and send to MS Teams channel
import pymsteams

msteamswebhook = pymsteams.connectorcard("ms-teams-webhook-link")
msteamswebhook.text("\nVolume size allocated to host " + get_hosts.json()[0]["name"] + " is " + volume_size)
msteamswebhook.send()




