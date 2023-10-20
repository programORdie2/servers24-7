projectID = '851049923'

import scratchattach as scratch3
import urllib.request, urllib.error
import requests, numpy
from PIL import Image
import session as external_session

session = external_session.session

conn = session.connect_cloud(projectID) 
client = scratch3.CloudRequests(conn)

def download_followers(u='progamordie'):
    response = requests.get(f"https://following-check.1tim.repl.co/api/{u}/?following=programORdie").json()
    follower = response['following']
    return follower

def download_file(url, dst_path):
    try:
        with urllib.request.urlopen(url) as web_file:
            data = web_file.read()
            with open(dst_path, mode='wb') as local_file:
                local_file.write(data)
    except urllib.error.URLError as e:
        print(e)

def resize_image(file='img.png', width=40, height=30):
    img = Image.open(file)
    size = (int(width), int(height))
    img.thumbnail(size)
    img.save(file)

def get_image_data(url, width, height):
    download_file(url, 'img.png')
    resize_image(width=width, height=height)
    image_from_pil = Image.open('img.png').convert("RGB")
    img = numpy.array(image_from_pil)
    img_data = []
    img_data.append(img.shape[0]) #Add the height
    img_data.append(img.shape[1])
    for h in img:
        for w in h:
            for rgb in w:
                img_data.append(int(rgb/2.55))
    return img_data

@client.request
def check(u):
    print(u)
    if str(download_followers(u)) == 'True':
        print(' is a follower!')
        return 1
    else:
        print(' is not a follower!')
        return 0

@client.request
def user_pfp(user, h_r):
    print(user)
    uid = requests.get('https://scratchdb.lefty.one/v3/user/info/' + user)
    uid = uid.json()
    try:
        uid = str(uid['id'])
    except KeyError:
        print('PDNE')
        return 'PDNE'
    link = 'https://uploads.scratch.mit.edu/get_image/user/' + uid + '_90x90.png'
    o = get_image_data(link, (float(h_r)+1)*20, (float(h_r)+1)*20)
    return o

@client.request
def project_image(pid, hr):
    print(pid)
    link = 'https://uploads.scratch.mit.edu/get_image/project/' + pid + '_100x80.png'
    
    o = get_image_data(link, (float(hr)+1)*20, (float(hr)+1)*15)
    return o

@client.request
def studio_thumbnail(sid, hr):
    print(sid)
    link = 'https://uploads.scratch.mit.edu/get_image/gallery/' + sid + '_170x100.png'
    o = get_image_data(link, (float(hr)+1)*20, (float(hr)+1)*15)
    return o

@client.event
def on_ready():
  print('Image Request Handler Ready')

def start():
  client.run(thread=True)
