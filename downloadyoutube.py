from flask import Flask, abort, request 
from flask_cors import CORS, cross_origin
import json
import urllib.request
import urllib.parse
import re
import webbrowser
import pytube 
from pathlib import Path
# home = str(Path.home())
home = '/home/jeevan/Downloads'

app = Flask(__name__)
CORS(app)

@app.route('/videourl', methods=['POST']) 
def foo():
    message=''
    status=True
    path=''
    if not request.json:
        abort(400)
    videourl=request.json["videourl"]
    SAVE_PATH = home
    try:
        yt = pytube.YouTube(videourl)
        stream = yt.streams.first()
        stream.download(SAVE_PATH)
        message="video downloaded Successfully"
        status=True
        path=SAVE_PATH
    except pytube.exceptions.RegexMatchError:
        print('The Regex pattern did not return any matches for the video: {}'.format(videourl))
        message="No matches for this URL"
        status=False
        path=''
    except pytube.exceptions.ExtractError:
        print ('An extraction error occurred for the video: {}'.format(videourl))
        message="No matches for this URL"
        status=False
        path=''
    except pytube.exceptions.VideoUnavailable:
        print('The following video is unavailable: {}'.format(videourl))
        message="No matches for this URL"
        status=False
        path=''
    return json.dumps({"msg":message,"status":status,"path":path})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
