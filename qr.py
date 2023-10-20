import scratchattach as scratch3
from PIL import Image
import random, qrcode, base64, numpy, os, time
import flask, session
import datetime as dt
from threading import Thread

session = session.session
conn = session.connect_cloud('897390438')
client = scratch3.CloudRequests(conn)

logo = Image.open('qrcodelogo.png')
basewidth = 50
wpercent = (basewidth / float(logo.size[0]))
hsize = int((float(logo.size[1]) * float(wpercent)))
logo = logo.resize((basewidth, hsize), Image.LANCZOS)

db = {}

def delete(name):
  time.sleep(10)
  os.remove(name)

def pageView(code):
  name = UnzipDownload(code)
  code2 = 'static/'+code
  open(code2, 'wb').write(name)
  Thread(target=delete, args=[code2]).start()
  i = 'https://server.programordie.repl.co/' + code2
  return flask.render_template('qr.html', image=i, d=code)

def pageDownload(code):
  name = UnzipDownload(code)
  code2 = 'static/'+code
  open(code2, 'wb').write(name)
  Thread(target=delete, args=[code2]).start()
  return flask.send_file(code2, as_attachment=True)

def gen_qr(bg, mc, url):
  now=str(dt.datetime.now().strftime('%H-%M-%S'))
  QRID = f'QRcode{now}'
  QRcode = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H)
  QRcode.add_data(url)
  QRcode.make()
  QRcode = QRcode.make_image(fill_color=mc, back_color=bg).convert('RGB')
  pos = ((QRcode.size[0] - logo.size[0]) // 2,
         (QRcode.size[1] - logo.size[1]) // 2)
  QRcode.paste(logo, pos)
  QRcode.save(f'{QRID}.png')
  return f'{QRID}.png'

def makeDownloadableZip(name):
    b64 = base64.b64encode(open(name, 'rb').read()).decode('utf-8')
    db[name] = b64

def UnzipDownload(name):
    data = db[name]
    data = base64.b64decode(data)
    return data

@client.request
def qr(data: str, color: str, bg: str):
    print(f'QRcode {data}, {color}, {bg}.')
    name = gen_qr(bg, color, data)
    makeDownloadableZip(name)
    os.remove(name)
    all_data = [f'https://server.programORdie.repl.co/qrcode/view/{name}']
    return all_data

@client.event
def on_ready():
    print("Request handler is running")
  
def start():
  client.run(thread=True)
