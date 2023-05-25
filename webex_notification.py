import requests
import json
import time

def send_webex_message(token,text):
    token = 'Bearer '+token
    m={
#   "roomId": whole_json["data"]["roomId"],
   "text" : text,
   "toPersonEmail":"email-id"
#    "parentId" : whole_json['data']['id'],
}
    r = requests.post('https://webexapis.com/v1/messages', data=json.dumps(m),
                  headers={'Authorization': token,'Content-Type': 'application/json'})
    
    return r

token=''

while True:
    time.sleep(1)
    send_webex_message(token,"Hii")