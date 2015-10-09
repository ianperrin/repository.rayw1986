"""
 Author: RayW1986

 This program is free software: you can redistribute it and/or modify
 it under the terms of the GNU General Public License as published by
 the Free Software Foundation, either version 3 of the License, or
 (at your option) any later version.

 This program is distributed in the hope that it will be useful,
 but WITHOUT ANY WARRANTY; without even the implied warranty of
 MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 GNU General Public License for more details.

 You should have received a copy of the GNU General Public License
 along with this program.  If not, see <http://www.gnu.org/licenses/>.
 
 """

import urllib,urllib2,re,xbmcplugin,xbmcgui,os,sys,datetime
from resources.lib.common_variables import *
from resources.lib.directory import *
from resources.lib.youtubewrapper import *
from resources.lib.watched import * 

fanart = xbmc.translatePath(os.path.join('special://home/addons/plugin.video.paramount_vault', 'fanart.jpg'))
art = xbmc.translatePath(os.path.join('special://home/addons/plugin.video.paramount_vault/resources/img', ''))

def CATEGORIES():
        addDir('Genres','url',10,art + 'genres.png')
        addDir(''+translate(30020)+'','PLd0LhgZxFkVKIpeVjT-YpcFjar53lWBGN',1,art + 'digital.png')
        addDir('Clips','url',11,art + 'clips.png')

def GENRES():
        addDir(''+translate(30012)+'','PLd0LhgZxFkVII3x-u6Ogh90iEepCLjKcW',1,art + 'action.png')
        addDir(''+translate(30013)+'','PLd0LhgZxFkVI7ds18u2o-qVluJfREYsIf',1,art + 'classics.png')
        addDir(''+translate(30014)+'','PLd0LhgZxFkVINkUJWrXd3AdGkrPGfpByw',1,art + 'comedy.png')
        addDir(''+translate(30015)+'','PLd0LhgZxFkVLtg4IZ-1jgGPmwZyhR-66o',1,art + 'drama.png')
        addDir(''+translate(30016)+'','PLd0LhgZxFkVKnyj6NIMTwGfL-KqBtGyFZ',1,art + 'horror.png')
        addDir(''+translate(30017)+'','PLd0LhgZxFkVJFsvRos55jeIKHKBmfN2uA',1,art + 'scifi.png')
        addDir(''+translate(30018)+'','PLd0LhgZxFkVJ4iI_mkUiHjwhW3c98GoLC',1,art + 'thriller.png')
        addDir(''+translate(30019)+'','PLd0LhgZxFkVLB8Zs8bQP5B-bnLimzY0FC',1,art + 'western.png')
		
def CLIPS():
        addDir(''+translate(30021)+'','PLd0LhgZxFkVJ1S9fZ9TjswtfrpfTGfAXT',1,art + 'clips.png')
        addDir(''+translate(30022)+'','PLd0LhgZxFkVJ7PD3Mdo7WD5jL-dDyplY3',1,art + 'clips.png')
        addDir(''+translate(30024)+'','PLd0LhgZxFkVKx1S1JvQ0qXq5Dvo5xdTjG',1,art + 'clips.png')
        addDir(''+translate(30027)+'','PLd0LhgZxFkVLsqP2Z6l6ggpiSTlXgW2U1',1,art + 'clips.png')
        addDir(''+translate(30023)+'','PLd0LhgZxFkVLe-6YG0jpuHOkoF4pvJ9iK',1,art + 'clips.png')
        addDir(''+translate(30025)+'','PLd0LhgZxFkVL55x-i3lh69edUMsqXAX53',1,art + 'clips.png')
        addDir(''+translate(30026)+'','PLd0LhgZxFkVIKnRU3OjfCsMuZyYrS1OAu',1,art + 'clips.png')
        addDir(''+translate(30028)+'','PLd0LhgZxFkVLakUwUfF4P4Qyra8g1RNA9',1,art + 'clips.png')
        addDir(''+translate(30029)+'','PLd0LhgZxFkVIqSbTkv7SH2LSbqeJBFV1u',1,art + 'clips.png')
        addDir(''+translate(30030)+'','PLd0LhgZxFkVIp36bvo-NiQv3FmYnkAFrc',1,art + 'clips.png')
        addDir(''+translate(30031)+'','PLd0LhgZxFkVJzprewn1hKuO6wzji-tvlE',1,art + 'clips.png')
        addDir(''+translate(30032)+'','PLd0LhgZxFkVJD0W8yRhCZpooiOChFCfuU',1,art + 'clips.png')
		
def get_params():
        param=[]
        paramstring=sys.argv[2]
        if len(paramstring)>=2:
                params=sys.argv[2]
                cleanedparams=params.replace('?','')
                if (params[len(params)-1]=='/'):
                        params=params[0:len(params)-2]
                pairsofparams=cleanedparams.split('&')
                param={}
                for i in range(len(pairsofparams)):
                        splitparams={}
                        splitparams=pairsofparams[i].split('=')
                        if (len(splitparams))==2:
                                param[splitparams[0]]=splitparams[1]
                                
        return param


params=get_params()
url=None
name=None
mode=None
iconimage=None
page = None
token = None

try: url=urllib.unquote_plus(params["url"])
except: pass
try: name=urllib.unquote_plus(params["name"])
except: pass
try: mode=int(params["mode"])
except:
	try: 
		mode=params["mode"]
	except: pass
try: iconimage=urllib.unquote_plus(params["iconimage"])
except: pass
try: token=urllib.unquote_plus(params["token"])
except: pass
try: page=int(params["page"])
except: page = 1

print ("Mode: "+str(mode))
print ("URL: "+str(url))
print ("Name: "+str(name))
print ("iconimage: "+str(iconimage))
print ("Page: "+str(page))
print ("Token: "+str(token))

		
def addDir(name,url,mode,iconimage):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setProperty('fanart_image', fanart)
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok

def create_directory(dir_path, dir_name=None):
    if dir_name:
        dir_path = os.path.join(dir_path, dir_name)
    dir_path = dir_path.strip()
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    return dir_path

if mode==None or url==None or len(url)<1:
        print ""
        CATEGORIES()
       
elif mode==1:
        return_youtubevideos(name,url,token,page)

elif mode==5: 
        play_youtube_video(url)

elif mode==6:
        mark_as_watched(url)

elif mode==7:
        removed_watched(url)

elif mode==8:
        add_to_bookmarks(url)

elif mode==9:
        remove_from_bookmarks(url)
		
elif mode==10:
        print ""+url
        GENRES()
		
elif mode==11:
        print ""+url
        CLIPS()
		
xbmcplugin.endOfDirectory(int(sys.argv[1]))
