import scratchattach as scratch3
from replit import db
import session as scratch

from hugchat import hugchat

chatbot = hugchat.ChatBot(cookie_path="cookie.json")

session = scratch.session
conn = session.connect_cloud("851753734") 
client = scratch3.CloudRequests(conn)

def get_response(message):
  return str(chatbot.chat(message))

def clear_db():
  global db
  i = input('sure?')
  if i == 'y':
    key = db.keys()
    for each in key:
      try:
        del db[each]
      except:
        pass

@client.request
def chat(arguments):
  print('request')
  try:
    who = client.get_requester()
    print(who + ' : ' + arguments)
    if arguments in db.keys():
      a = db[arguments]
      print('in db')
    else:
      a = get_response(arguments)
      db[arguments] = a
      print('not in db')
    print(a)
    if a == None or a == '':
      a = 'Max. chat requests reached. Please try again in 5 minutes.'
    return a
  except Exception as e:
    print(e)
    
@client.event
def on_ready():
  print('ScratchatGPT Request Handler Ready')
  
def start():
  client.run(thread=True)
