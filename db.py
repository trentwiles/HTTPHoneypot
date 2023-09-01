import requests
import json

rdb_endpoint = json.loads(open('config.json').read())["restdb_endpoint"]
rdb_api_key = json.loads(open('config.json').read())["rdp_api_key"]

def checkAPI(ip):
    r = requests.get("https://"+ rdb_endpoint + ".restdb.io/rest/addys", headers={"x-apikey": rdb_api_key})
    for record in r.json()[0]:
        if record["ips"] == str(ip):
            return True
        
    return False

def addIP(ip):
    r = requests.post("https://"+ rdb_endpoint + ".restdb.io/rest/addys", headers={"x-apikey": rdb_api_key}, data={"ips": ip})
    if r.status_code == 200:
        return True
    else:
        return False
    
def clear():
    r = requests.get("https://"+ rdb_endpoint + ".restdb.io/rest/addys", headers={"x-apikey": rdb_api_key})
    for record in r.json()[0]:
        x = requests.delete("https://"+ rdb_endpoint + ".restdb.io/rest/addys/" + str(record["_id"]), headers={"x-apikey": rdb_api_key})