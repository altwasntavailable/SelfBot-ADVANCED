from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
    return "Selfbot has been turned on. Made with <3 by ALT#0540"

def run():
  app.run(host='0.0.0.0',port=9090)

def keep_alive():  
    t = Thread(target=run)
    t.start()