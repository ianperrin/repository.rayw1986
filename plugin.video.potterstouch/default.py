import urllib,urllib2,re,xbmcplugin,xbmcgui,os,sys,datetime
import plugintools

fanart = xbmc.translatePath(os.path.join('special://home/addons/plugin.video.potterstouch', 'fanart.jpg'))

def CATEGORIES():
        addDir('Video Podcast','http://www.lightsource.com/ministry/the-potters-house/subscribe/podcast.xml',1,'http://media.salemwebnetwork.com/ZCast/Shared/ImageTypes/HostImages/the-potters-house/the-potters-house-1400x1400.jpg')
        addDir('Audio Podcast','http://www.oneplace.com/ministries/the-potters-touch/subscribe/podcast.xml',2,'http://media.salemwebnetwork.com/ZCast/Shared/ImageTypes/HostImages/the-potters-touch/the-potters-touch-1400x1400.jpg')
		
def VIDEO(url):
    find_url=url.find('?')+1
    keep_url=url[:find_url]
    
    iconimage=""
    req = urllib2.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
    response = urllib2.urlopen(req)
    link=response.read()
    response.close()

    # Extract items from feed
    pattern = ""
    matches = plugintools.find_multiple_matches(link,"<item>(.*?)</item>")
    
    for entry in matches:
        
        # Not the better way to parse XML, but clean and easy
        title = plugintools.find_single_match(entry,"<title>(.+?)</title>").replace("&amp;","&").replace("&#39;","'")
        plot = plugintools.find_single_match(entry,"<description>(.+?)</description>").replace("&amp;","&").replace("&#39;","'")
        thumbnail = "http://media.salemwebnetwork.com/ZCast/Shared/ImageTypes/HostImages/the-potters-house/the-potters-house-1400x1400.jpg"
        url = plugintools.find_single_match(entry,'<enclosure url="(.+?)"').replace("&amp;","&")
        date = plugintools.find_single_match(entry,'<pubDate>.+?, (.+?) 12:00:00 GMT</pubDate>').replace("&amp;","&")

        plugintools.add_item( action="play" , title='['+date+'] '+title , plot=plot , url=url , thumbnail=thumbnail , folder=True )
		
def AUDIO(url):
    find_url=url.find('?')+1
    keep_url=url[:find_url]
    
    iconimage=""
    req = urllib2.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
    response = urllib2.urlopen(req)
    link=response.read()
    response.close()

    # Extract items from feed
    pattern = ""
    matches = plugintools.find_multiple_matches(link,"<item>(.*?)</item>")
    
    for entry in matches:
        
        # Not the better way to parse XML, but clean and easy
        title = plugintools.find_single_match(entry,"<title>(.+?)</title>").replace("&amp;","&").replace("&#39;","'")
        plot = plugintools.find_single_match(entry,"<description>(.+?)</description>").replace("&amp;","&").replace("&#39;","'")
        thumbnail = "http://media.salemwebnetwork.com/ZCast/Shared/ImageTypes/HostImages/the-potters-touch/the-potters-touch-1400x1400.jpg"
        url = plugintools.find_single_match(entry,'<enclosure url="(.+?)"').replace("&amp;","&")
        date = plugintools.find_single_match(entry,'<pubDate>.+?, (.+?) 12:00:00 GMT</pubDate>').replace("&amp;","&")

        plugintools.add_item( action="play" , title='['+date+'] '+title , plot=plot , url=url , thumbnail=thumbnail , folder=True )

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
		
def addLink(name,url,iconimage):
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        liz.setProperty('fanart_image', fanart)
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=url,listitem=liz)
        return ok

def addDir(name,url,mode,iconimage):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setProperty('fanart_image', fanart)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
        
              
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
print "URL: "+str(url)
print "Name: "+str(name)

if mode==None or url==None or len(url)<1:
        print ""
        CATEGORIES()
	
elif mode==1:
        print ""+url
        VIDEO(url)

elif mode==2:
        print ""+url
        AUDIO(url)
		

xbmcplugin.endOfDirectory(int(sys.argv[1]))
