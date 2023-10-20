import requests
import scratchattach as scratch3
import session as scratch

session = scratch.session
conn = session.connect_cloud(869247117) 
client = scratch3.CloudRequests(conn)

def get_astros():
  response = requests.get('http://api.open-notify.org/astros.json').json()
  data = []
  for who in response['people']:
    data.append(str(who['name']))
    data.append(str(who['craft']))
  data.append(str(response['number']))
  return data

@client.event
def on_ready():
  print('Astros Request handler ready')

@client.request
def r():
  print('Astros requested by', client.get_requester())
  r = get_astros()
  return r
def start():
  client.run(thread=True)
