import scratchattach as scratch3
import session as scratch
import json
from pycoingecko import CoinGeckoAPI

sid = "873221123"
try:
  session = scratch.session

  conn = session.connect_cloud(sid) 
  client = scratch3.CloudRequests(conn)
except:
  pass
bc = CoinGeckoAPI()

def update():
  eur = bc.get_price(ids='bitcoin', vs_currencies='eur')['bitcoin']["eur"]
  usd = bc.get_price(ids='bitcoin', vs_currencies='usd')['bitcoin']["usd"]
  db = json.loads(open('db.json').read())
  del db['eur'][0]
  db['eur'].append(int(eur))
  del db['usd'][0]
  db['usd'].append(int(usd))
  db = json.dumps(db)
  open('db.json', 'w').write(db)

def get():
  eur = bc.get_price(ids='bitcoin', vs_currencies='eur')['bitcoin']["eur"]
  usd = bc.get_price(ids='bitcoin', vs_currencies='usd')['bitcoin']["usd"]
  db = json.loads(open('db.json').read())
  data = [str(int(eur)), str(int(usd))]
  for each in db['eur']:
    data.append(str(each))
  for each in db['usd']:
    data.append(str(each))
  return data

def get_response():
  t = get()
  return t

try:
  @client.request
  def stats():
    r = get_response()
    return r 
except:
  pass

def start():
  try:
    client.run(thread=True)
  except:
    pass