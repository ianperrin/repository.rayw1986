import urllib,urllib2,re,xbmcplugin,xbmcgui,xbmcvfs,os,sys,datetime,string,hashlib,net,xbmc
import xbmcaddon
from resources.lib.modules.common import *
from resources.lib.modules.plugintools import *

icon      = xbmc.translatePath(os.path.join('special://home/addons/plugin.video.tvcatchup_rw', 'icon.jpg'))
fanart    = xbmc.translatePath(os.path.join('special://home/addons/plugin.video.tvcatchup_rw', 'fanart.jpg'))

def main():
    url       = 'https://tvcatchup.com/'
    iconimage = ""
    req       = urllib2.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
    response  = urllib2.urlopen(req)
    link      = response.read()
    response.close()

    pattern = ""
    matches = plugintools.find_multiple_matches(link,'<p class="channelsicon" style="">(.*?)</div>')
    
    for entry in matches:
       
        getchannel = plugintools.find_single_match(entry,'alt="Watch (.+?)"')
        gettitle   = plugintools.find_single_match(entry,'<br/> (.+?) </a>').replace("&#039;","'")
        name       = getchannel+' - '+gettitle
        geturl     = plugintools.find_single_match(entry,'<a href="(.+?)">')
        url        = 'http://tvcatchup.com' + geturl
        iconimage  = plugintools.find_single_match(entry,'src="(.+?)"')

        addLink(name,url,2,iconimage)
		
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

try:
        url=urllib.unquote_plus(params["url"])
except:
        pass
try:
        name=urllib.unquote_plus(params["name"])
except:
        pass
try:
        mode=int(params["mode"])
except:
        pass

print "Mode: "+str(mode)
print "Name: "+str(name)

if mode==None or url==None or len(url)<1:
        print ""
        main()
	
elif mode==1: play(url)
elif mode==2: tvcatchup(url)


xbmcplugin.endOfDirectory(int(sys.argv[1]))
