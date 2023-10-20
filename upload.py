import scratchattach as scratch3
import requests, os
import session as scratch

url = os.environ['upload_url']
sid = "877978019"
session = scratch.session
conn = session.connect_cloud(sid) 
client = scratch3.CloudRequests(conn)

@client.request
def upload(id, who):
  who = str(who)
  print(f'Upload {id} by {who}')
  r = requests.get(url + who + '&id=' + str(id))
  if '1' in r.text:
    return 1
  else:
    return 0

@client.event
def on_ready():
  print('Upload ready!')

def start():
  client.run(thread=True)
