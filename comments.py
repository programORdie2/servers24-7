import scratchattach as scratch3
import requests
import os
import session as scratchattach_external_session

session = scratchattach_external_session.session
conn = session.connect_cloud(868625764) 
client = scratch3.CloudRequests(conn)

def get_comments(type, id):
  if type == 'user':
    md = 'username'
  else:
    md = 'id'
  url = f'https://apis.scratchconnect.eu.org/comments/{type}/?{md}={id}&limit=10&page=1'
  response = requests.get(url).json()
  try:
    error = response['Info']
    return error
  except:
    pass
  data = []
  for comment in response:    
    data.append(comment['User'])
    data.append(comment['Content'])
    data.append('0')
    for reply in comment['Replies']:
      data.append(reply['User'])
      data.append(reply['Content'])
      data.append('1')
      if len(data) > 5000:
        break
    if len(data) > 5000:
      break
  return data

@client.event
def on_ready():
  print('Comments Request Handler Ready')

@client.request
def load(u, t):
  print('Comments of', u, 'requested by', client.get_requester(), 'whit type', t)
  r = get_comments(t, u)
  return r

def start():
  client.run(thread=True)
