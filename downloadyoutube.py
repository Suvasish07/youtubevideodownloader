from flask import Flask, abort, request 
from flask_cors import CORS, cross_origin
import json
import urllib.request
import urllib.parse
import re
import webbrowser
import pytube 
from pytube import YouTube
from time import sleep

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
    videoInfo=[]
    if not request.json:
        abort(400)
    videourl=request.json["videourl"]
    SAVE_PATH = home
    if "https://www.youtube.com/watch?v=" in videourl:
        try:
            yt = pytube.YouTube(videourl)
            # stream = yt.streams.first()
            # stream.download(SAVE_PATH)
            # message="video downloaded Successfully"
            status=True
            title=yt.title
            thumbnailurl=yt.thumbnail_url
            linkurl=videourl
            item={"title":title,"thumbnailurl":thumbnailurl,"linkurl":videourl}
            videoInfo.append(item)
            # path=SAVE_PATH
        except pytube.exceptions.RegexMatchError:
            print('The Regex pattern did not return any matches for the video: {}'.format(videourl))
            # message="No matches for this URL"
            videoInfo=[]
            status=False
            # path=''
        except pytube.exceptions.ExtractError:
            print ('An extraction error occurred for the video: {}'.format(videourl))
            # message="No matches for this URL"
            videoInfo=[]
            status=False
            # path=''
        except pytube.exceptions.VideoUnavailable:
            print('The following video is unavailable: {}'.format(videourl))
            # message="No matches for this URL"
            videoInfo=[]
            status=False
            # path=''
        return json.dumps({"data":videoInfo,"status":status})
    else:
        query_string = urllib.parse.urlencode({"search_query" : videourl})
        html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
        search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
        
        videoURLList=[]

        for name in search_results:
            videoURLList.append("http://www.youtube.com/watch?v="+ name)

        videoURLList = list(set(videoURLList))
        count=0
        videolist=[]
        listlength=round(len(videoURLList)/3)
        for link in videoURLList:
            count +=1
            if(count==listlength):
                break
            yt=pytube.YouTube(link)
            sleep(1)
            title=yt.title
            print(title)
            print(count)
            thumbnailurl=yt.thumbnail_url
            item={"title":title,"thumbnailurl":thumbnailurl,"linkurl":link}
            videolist.append(item)
            yt=[]
        return json.dumps({"data":videolist,"status":True})



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
