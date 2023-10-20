import scratchattach as scratch3
import requests, time
import session as scratch

ses = scratch.session
cloud = ses.connect_cloud("860615065")

def start():
  while True:
    print('Refeshing ISS ...')
    response = requests.get('http://api.open-notify.org/iss-now.json').json()
    response = response['iss_position']
    lon = str(response['longitude'])
    lat = str(response['latitude'])
    cloud.set_var('lon', lon)
    cloud.set_var('lat', lat)
    print('done')
    time.sleep(60)
