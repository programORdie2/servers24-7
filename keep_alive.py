from flask import Flask
from threading import Thread
import os
import settings
from bitcoin import update

app = Flask(__name__)

@app.route('/')
def root():
  return settings.VERSION

@app.get('/update')
def reload():
  update()
  return 'done'

def run():
  app.run(host='0.0.0.0', port=8080)

def ka():
  Thread(target=run).start()