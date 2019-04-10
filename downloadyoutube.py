from flask import Flask, abort, request 
from flask_cors import CORS, cross_origin
import json
import urllib.request
import urllib.parse
import re
import webbrowser
import pytube 
from pathlib import Path
home = str(Path.home())

app = Flask(__name__)
CORS(app)

@app.route('/videourl', methods=['POST']) 
def foo():
    if not request.json:
        abort(400)
    videourl=request.json["videourl"]
    SAVE_PATH = home
    yt = pytube.YouTube(videourl)
    stream = yt.streams.first()
    stream.download(SAVE_PATH)
    return json.dumps({"msg":"video downloaded in :"+SAVE_PATH})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
