import urllib,urllib2,re,xbmcplugin,xbmcgui,os,sys,datetime
import plugintools
import settings



DATA_PATH = settings.data_path()
ADDON = settings.addon()
WATCHED_FILE = settings.watched_videos_file()
FAVOURITES_FILE = settings.favourite_clubs_file()

youtube_url = 'plugin://plugin.video.youtube/?action=play_video&videoid=%s'
fanart = xbmc.translatePath(os.path.join('special://home/addons/plugin.video.thefa', 'fanart.jpg'))
art = xbmc.translatePath(os.path.join('special://home/addons/plugin.video.thefa/resources/logos', ''))
fanart = xbmc.translatePath(os.path.join('special://home/addons/plugin.video.thefa/resources/fanart', ''))

def CATEGORIES():
        addDirMain('My Clubs','url',14,art + 'favourites.png')
        addDirMain('Premier League','url',15,art + 'premierleague.png')
        #addDirMain('Championship','url',16,art + 'championship.png')
        #addDirMain('League One','url',19,art + 'league1.png')
        #addDirMain('League Two','url',18,art + 'league2.png')

def PREMIER_LEAGUE():
        addDir("AFC Bournemouth",'https://www.youtube.com/feeds/videos.xml?user=officiacherries',13,art + 'afcbournemouth.png')
        addDir("Arsenal",'https://www.youtube.com/feeds/videos.xml?user=ArsenalTour',13,art + 'arsenal.png')
        addDir("Aston Villa",'https://www.youtube.com/feeds/videos.xml?user=avfcofficial',13,art + 'astonvilla.png')
        addDir("Chelsea",'https://www.youtube.com/feeds/videos.xml?user=chelseafc',13,art + 'chelsea.png')
        addDir("Crystal Palace",'https://www.youtube.com/feeds/videos.xml?user=OfficialCPFC',13,art + 'crystalpalace.png')
        addDir("Everton",'https://www.youtube.com/feeds/videos.xml?user=OfficialEverton',13,art + 'everton.png')
        addDir("Leicester City",'https://www.youtube.com/feeds/videos.xml?user=LCFCOfficial',13,art + 'leicestercity.png')
        addDir("Liverpool",'https://www.youtube.com/feeds/videos.xml?user=LiverpoolFC',13,art + 'liverpool.png')
        addDir("Manchester City",'https://www.youtube.com/feeds/videos.xml?user=mcfcofficial',13,art + 'mancity.png')
        addDir("Manchester United",'https://www.youtube.com/feeds/videos.xml?playlist_id=PLvAI_5iW-ATVLjlSAyKWKi-4w423CS1hl',13,art + 'manutd.png')
        addDir("Newcastle United",'https://www.youtube.com/feeds/videos.xml?user=NUFCOfficial1892',13,art + 'newcastle.png')
        addDir("Norwich City",'https://www.youtube.com/feeds/videos.xml?user=NCFCTube',13,art + 'norwich.png')
        addDir("Southampton",'https://www.youtube.com/feeds/videos.xml?user=theofficialsaints',13,art + 'southampton.png')
        addDir("Stoke City",'https://www.youtube.com/feeds/videos.xml?channel=UCmFPjHUFr0hyE6eFGvCm7IA',13,art + 'stoke.png')
        addDir("Sunderland",'https://www.youtube.com/feeds/videos.xml?user=sunderlandafc',13,art + 'sunderland.png')
        addDir("Swansea City",'https://www.youtube.com/feeds/videos.xml?user=SWANSPLAYER',13,art + 'swansea.png')
        addDir("Tottenham Hotspur",'https://www.youtube.com/feeds/videos.xml?user=spursofficial',13,art + 'tottenham.png')
        addDir("Watford",'https://www.youtube.com/feeds/videos.xml?user=WatfordFCofficial',13,art + 'watford.png')
        addDir("West Bromwich Albion",'https://www.youtube.com/feeds/videos.xml?user=OfficialAlbion',13,art + 'wba.png')
        addDir("West Ham United",'https://www.youtube.com/feeds/videos.xml?channel=UCCNOsmurvpEit9paBOzWtUg',13,art + 'westham.png')

		
def FAVOURITES():
    if os.path.isfile(FAVOURITES_FILE):
        s = read_from_file(FAVOURITES_FILE)
        search_list = s.split('\n')
        for list in search_list:
            if list != '':
                list = list.split('|')
                name = list[0]
                url = list[1]
                iconimage = list[2]
                prefix = ''
                addDir(name,url,13,iconimage)


################################Youtube Channels#####################################		
		
def YOUTUBE_CHANNELS(url):
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
    matches = plugintools.find_multiple_matches(link,"<entry>(.*?)</entry>")
    
    for entry in matches:
        
        # Not the better way to parse XML, but clean and easy
        title = plugintools.find_single_match(entry,'<titl[^>]+>([^<]+)</title>').replace('&amp;','&').replace('&quot;','"')
        date = plugintools.find_single_match(entry,'<published>(.+?)T')
        plot = plugintools.find_single_match(entry,"<media\:descriptio[^>]+>([^<]+)</media\:description>")
        thumbnail = plugintools.find_single_match(entry,'<media\:thumbnail url="(.+?)"')
        video_id = plugintools.find_single_match(entry,'http\://www.youtube.com/watch\?v\=(.+?)"')
        play_url = 'plugin://plugin.video.youtube/play/?video_id='+video_id

        plugintools.add_item( action="play" , title='('+date+') '+title , plot=plot , url=play_url , fanart=thumbnail , thumbnail=thumbnail , folder=True )

	
	
############################################################################################

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

def addDirMain(name,url,mode,iconimage):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setProperty('fanart_image', fanart)
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
		
def addDir(name,url,mode,iconimage):
        contextMenuItems = []
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
        ok=True
        nameurl="%s|%s|%s" % (name,url,iconimage)
        if favourites_index(nameurl) < 0:
            contextMenuItems.append(('Add to My Clubs', 'XBMC.RunPlugin(%s?mode=103&url=%s)'% (sys.argv[0], urllib.quote_plus(nameurl))))
        else:
            name = name
            contextMenuItems.append(('Remove from My Clubs', 'XBMC.RunPlugin(%s?mode=104&url=%s)'% (sys.argv[0], urllib.quote_plus(nameurl))))
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.addContextMenuItems(contextMenuItems, True)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        liz.setProperty('fanart_image', fanart)
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
		
def addDirVideo(prefix,name,url,mode,iconimage):
        contextMenuItems = []
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
        ok=True
        nameurl="%s|%s" % (name,url)
        if watched_index(url) < 0:
            contextMenuItems.append(('Mark as Watched', 'XBMC.RunPlugin(%s?mode=101&url=%s)'% (sys.argv[0], url)))
        else:
            name = '[COLOR cyan]' + "<< " + '[/COLOR]' + name
            contextMenuItems.append(('Remove from Watched List', 'XBMC.RunPlugin(%s?mode=102&url=%s)'% (sys.argv[0], url)))
        if favourites_index(nameurl) < 0:
            contextMenuItems.append(('Save to Favourites', 'XBMC.RunPlugin(%s?mode=103&url=%s)'% (sys.argv[0], urllib.quote_plus(nameurl))))
        else:
            name = '[COLOR gold]' + "+  " + '[/COLOR]' + name
            contextMenuItems.append(('Remove from Favourites', 'XBMC.RunPlugin(%s?mode=104&url=%s)'% (sys.argv[0], urllib.quote_plus(nameurl))))
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.addContextMenuItems(contextMenuItems, True)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        liz.setProperty('fanart_image', fanart)
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz)
        return ok
        
              
params=get_params()
url=None
name=None
mode=None



def create_directory(dir_path, dir_name=None):
    if dir_name:
        dir_path = os.path.join(dir_path, dir_name)
    dir_path = dir_path.strip()
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    return dir_path

def create_file(dir_path, file_name=None):
    if file_name:
        file_path = os.path.join(dir_path, file_name)
    file_path = file_path.strip()
    if not os.path.exists(file_path):
        f = open(file_path, 'w')
        f.write('')
        f.close()
    return file_path

def write_to_file(path, content, append=False, silent=False):
    try:
        if append:
            f = open(path, 'a')
        else:
            f = open(path, 'w')
        f.write(content)
        f.close()
        return True
    except:
        if not silent:
            print("Could not write to " + path)
        return False

def read_from_file(path, silent=False):
    try:
        f = open(path, 'r')
        r = f.read()
        f.close()
        return str(r)
    except:
        if not silent:
            print("Could not read from " + path)
        return None
		
def watched_index(url):
    try:
        content = read_from_file(WATCHED_FILE)
        line = str(url)
        lines = content.split('\n')
        index = lines.index(line)
        return index
    except:
        return -1 #Not subscribed
		
def favourites_index(url):
    try:
        content = read_from_file(FAVOURITES_FILE)
        line = str(url)
        lines = content.split('\n')
        index = lines.index(line)
        return index
    except:
        return -1

def watched(url,filename):
    if filename==WATCHED_FILE:
        index = watched_index(url)
    else:
        index = favourites_index(url)
    if index >= 0:
        return
    content = str(url) + '\n'
    write_to_file(filename, content, append=True)
    xbmc.executebuiltin("Container.Refresh")
    
def unwatched(url,filename):
    if filename==WATCHED_FILE:
        index = watched_index(url)
    else:
        index = favourites_index(url)
    if index >= 0:
        content = read_from_file(filename)
        lines = content.split('\n')
        lines.pop(index)
        s = ''
        for line in lines:
            if len(line) > 0:
                s = s + line + '\n'
        
        if len(s) == 0:
            os.remove(filename)
        else:
            write_to_file(filename, s)
        xbmc.executebuiltin("Container.Refresh")

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
        LESSON_LIST(url)
        
elif mode==2:
        print ""+url
        PLAY_VIDEO(url,name)
		
elif mode==11:
        print ""+url
        LESSON_DIR()
		
elif mode==12:
        print ""+url
        SONG_DIR()
	
elif mode==13:
        print ""+url
        YOUTUBE_CHANNELS(url)

elif mode==14:
        FAVOURITES()
		
elif mode==15:
        print ""+url
        PREMIER_LEAGUE()
		
elif mode==16:
        print ""+url
        YOUTUBE_LIST_USA()
		
elif mode==101:
        watched(url,filename=WATCHED_FILE)
		
elif mode==102:
        unwatched(url,filename=WATCHED_FILE)
		
elif mode==103:
        watched(url,filename=FAVOURITES_FILE)
		
elif mode==104:
        unwatched(url,filename=FAVOURITES_FILE)
		

xbmcplugin.endOfDirectory(int(sys.argv[1]))
