print('Creating alive page ...')
from flask import Flask
import flask
from threading import Thread
import qr as qrcode
import settings
from bitcoin import update

app = Flask(__name__)

print('Done.')

print('Importing Request Handlers ...')
import comments
import image
import messages
import scratchatgpt
import stats
import iss
import swivbd
import people_in_space
import scratchipedia
import bitcoin, upload
print('Done.')

print('Starting request Handlers ...')
Thread(target=iss.start).start()
comments.start()
image.start()
messages.start()
scratchatgpt.start()
stats.start()
swivbd.start()
people_in_space.start()
scratchipedia.start()
bitcoin.start()
upload.start()
qrcode.start()
print('Done.')


@app.route('/qrcode/')
def qr():
  return flask.redirect('https://tools.programORdie.repl.co/qr')

@app.route('/qrcode/view/<code>')
def dwnload_qr(code):
  return qrcode.pageView(code)

@app.route('/qrcode/download/<code>')
def view_qr(code):
  return qrcode.pageDownload(code)

@app.route('/')
def root():
  return settings.VERSION

@app.get('/update')
def reload():
  update()
  return 'done'

app.run(host='0.0.0.0', port=8080)