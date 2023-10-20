import scratchattach as scratch3
import requests
import session as scratch

session = scratch.session
conn = session.connect_cloud(867546059) 
client = scratch3.CloudRequests(conn)

def get_count(user):
  user = str(user)
  proxy = 'https://apis.scratchconnect.eu.org/free-proxy/get?url='
  response = requests.get(proxy + f'https://api.scratch.mit.edu/users/{user}/messages/count')
  response = response.json()
  try:
    count = str(response['count'])
  except:
    count = 'You need to enter a VALID username!'
  return count

@client.event
def on_ready():
  print('Message Request handler ready')

@client.request
def load(u):
  print('Messages of', u, 'requested by', client.get_requester())
  r = get_count(u)
  print(r)
  return r

def start():
  client.run(thread=True)
