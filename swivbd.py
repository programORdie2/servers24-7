import scratchattach as scratch3
import requests
import session as scratch

session = scratch.session
conn = session.connect_cloud(868990002) 
client = scratch3.CloudRequests(conn)

def string(i):
  i = str(i)
  i = i.replace('\n', '')
  i = i.replace('  ', ' ')
  return i

def get_wivbd(u):
  user = str(u)
  url = f'https://programordie-1-b6431438.deta.app/swivbd/get?user={user}&max=10'
  response = requests.get(url).json()
  try:
    error = response['message']
    return error
  except:
    pass
  data = []
  for message in response:
    data.append(string(message['message']))
    data.append(string(message['time']))
  return data

@client.event
def on_ready():
  print('SWIVBD Request handler ready')

@client.request
def load(u):
  print('WIVBD of', u, 'requested by', client.get_requester())
  r = get_wivbd(u)
  print('Responding')
  return r

def start():
  client.run(thread=True)
