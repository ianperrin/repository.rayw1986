import urllib,urllib2,re,xbmcplugin,xbmcgui,os,sys,datetime,string
import plugintools
import xbmcaddon

fanart    = 'special://home/addons/plugin.video.tvcatchup_rw/fanart.jpg'

def play(url):
	resolved = url
	item     = xbmcgui.ListItem(path=resolved)
	xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, item)
	
def open_url(url):
	req      = urllib2.Request(url)
	req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
	response = urllib2.urlopen(req)
	link     = response.read()
	link     = cleanHex(link)
	response.close()
	return link
	
def addLink(name,url,mode,iconimage):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setProperty('fanart_image', iconimage)
        liz.setProperty("IsPlayable","true")
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)
        return ok

def addDir(name,url,mode,iconimage):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setProperty('fanart_image', iconimage)
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok

def cleanHex(text):
    def fixup(m):
        text = m.group(0)
        if text[:3] == "&#x": return unichr(int(text[3:-1], 16)).encode('utf-8')
        else: return unichr(int(text[2:-1])).encode('utf-8')
    try :return re.sub("(?i)&#\w+;", fixup, text.decode('ISO-8859-1').encode('utf-8'))
    except:return re.sub("(?i)&#\w+;", fixup, text.encode("ascii", "ignore").encode('utf-8'))
	
def	tvcatchup(url):
    url       = url
    iconimage = ""
    req       = urllib2.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
    response  = urllib2.urlopen(req)
    link      = response.read()
    response.close()

    pattern = ""
    matches = plugintools.find_multiple_matches(link,"jwplayer(.*?)</script>")
    
    for entry in matches:
       
        url = plugintools.find_single_match(entry,"file: '(.+?)'")

        play(url)