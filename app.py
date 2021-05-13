import os

from flask import Flask, Response, redirect

RECURLY_PUBLIC_KEY = os.environ['RECURLY_PUBLIC_KEY']

PUBLIC_DIR_PATH = os.getenv('PUBLIC_DIR_PATH', './public')
app = Flask(__name__, static_folder=PUBLIC_DIR_PATH, static_url_path='')

@app.route("/", methods=['GET'])
def index():
  return redirect('index.html')

@app.route("/config", methods=['GET'])
def config_js():
  return Response("window.recurlyConfig = { publicKey: '" + RECURLY_PUBLIC_KEY + "' }", mimetype='application/javascript')