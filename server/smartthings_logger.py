from bottle import request, route, run
import json
import requests
import ipgetter
import pdb
import csv
# from datetime import datetime

# The client ID and client secret of the SmartApp
# Not used, but may be useful later on
client_id = '70763167-59b3-46e0-b47d-84156b78fa68'
client_secret = 'ea7e7f90-d262-42d9-9e8f-49994da82b9c'

# The authorization token for the SmartApp
# Lasts 50 years, so don't really need to keep getting new ones
oath_token = '00f36ac7-8d33-4a7a-9491-1ff270afcbd0'

myip = str(ipgetter.myip())

port = 3000
# Route for receiving new logs from the SmartApp
# Occurs every time the state of one of the devices changes
@route('/log', method='POST')
def log():
	with open('logs.csv', 'a+') as f:
		fields = ['time', 'id', 'state']
		# request.json['time'] = datetime.fromtimestamp(int(request.json['time'])/1000).strftime('%m-%d-%Y %H:%M:%S')
		writer = csv.DictWriter(f, fieldnames=fields)
		writer.writerow(request.json)

def subscribe(api_endpoint):
	resp = requests.put(api_endpoint+'/subscribe?loggeruri=http%3A%2F%2F'+myip+'%3A'+str(port)+'%2Flog', headers={'Authorization': 'Bearer '+oath_token})

# Method for discovering the endpoint exposed by the SmartApp
def discover_endpoint():
	resp = requests.get('https://graph.api.smartthings.com/api/smartapps/endpoints', headers={'Authorization': 'Bearer '+oath_token})
	return resp.json()[0]['uri']


# URL for getting the code
# https://graph.api.smartthings.com/oauth/authorize?response_type=code&client_id=70763167-59b3-46e0-b47d-84156b78fa68&scope=app&redirect_uri=http%3A%2F%2Flocalhost

# URL for getting the authorization token
# https://graph.api.smartthings.com/oauth/token?grant_type=authorization_code&client_id=70763167-59b3-46e0-b47d-84156b78fa68&client_secret=ea7e7f90-d262-42d9-9e8f-49994da82b9c&code=ris76D&scope=app&redirect_uri=http%3A%2F%2Flocalhost

# curl command for getting the endpoint
# curl -H "Authorization: Bearer 00f36ac7-8d33-4a7a-9491-1ff270afcbd0" https://graph.api.smartthings.com/api/smartapps/endpoints

if __name__ == "__main__":
	api_endpoint = discover_endpoint()
	subscribe(api_endpoint)
	run(host='0.0.0.0', port=port)









