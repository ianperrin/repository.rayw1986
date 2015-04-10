import urllib,urllib2,re,xbmcplugin,xbmcgui,os,sys,datetime
import plugintools
import settings



DATA_PATH = settings.data_path()
ADDON = settings.addon()
WATCHED_FILE = settings.watched_videos_file()
FAVOURITES_FILE = settings.favourite_feds_file()

youtube_url = 'plugin://plugin.video.youtube/?action=play_video&videoid=%s'
fanart = xbmc.translatePath(os.path.join('special://home/addons/plugin.video.iwn', 'fanart.jpg'))
art = xbmc.translatePath(os.path.join('special://home/addons/plugin.video.iwn/art', ''))
stream = xbmc.translatePath(os.path.join('special://home/addons/plugin.video.iwn/stream', ''))

def CATEGORIES():
        #addLink("LIVE!",stream + 'live.strm',art + 'live.png')
        addDirMain('My Promotions','url',14,art + 'favourites.png')
        addDirMain('Podcasts & Live Shows','url',15,art + 'podcast.png')
        addDirMain('American Indy','url',16,art + 'usa.png')
        addDirMain('Canadian Indy','url',19,art + 'canada.png')
        addDirMain('British Indy','url',18,art + 'uk.png')
        addDirMain('European Indy','url',17,art + 'europe.png')
        addDirMain('Australian Indy','url',20,art + 'aus.png')
        addDirMain('Singapore Indy','url',21,art + 'singapore.png')
        addDirMain('Brazilian Indy','url',22,art + 'brazil.png')

def YOUTUBE_LIST():
        #Pro Wrestling Cast
        channel="UCtS2zUbq91D2sWqkPH9UkZQ"
        addDir("Pro Wrestling Cast",'http://gdata.youtube.com/feeds/api/users/'+channel+'/uploads?start-index=1&max-results=50',13,'https://yt3.ggpht.com/-n42rVdokppM/AAAAAAAAAAI/AAAAAAAAAAA/Y4YwR0AdVSc/s352-c-k-no/photo.jpg')
        #Pro Wrestling Report
        channel="maxsports"
        addDir("Pro Wrestling Report",'http://gdata.youtube.com/feeds/api/users/'+channel+'/uploads?start-index=1&max-results=50',13,'https://yt3.ggpht.com/-2uMdgaBCZk0/AAAAAAAAAAI/AAAAAAAAAAA/YX454E01E-s/s352-c-k-no/photo.jpg')
		#WrestleTalk TV
        channel="WrestletalkTV"
        addDir("WrestleTalk TV",'http://gdata.youtube.com/feeds/api/users/'+channel+'/uploads?start-index=1&max-results=50',13,'https://yt3.ggpht.com/-GhhGrJWqON4/AAAAAAAAAAI/AAAAAAAAAAA/RF1aZIqr3NY/s352-c-k-no/photo.jpg')
		#Wrestling Roundtable
        channel="WrestlingRoundtable"
        addDir("Wrestling Roundtable",'http://gdata.youtube.com/feeds/api/users/'+channel+'/uploads?start-index=1&max-results=50',13,'https://i.ytimg.com/i/yCTT2VVfThDZ3dk4kzKlzw/mq1.jpg')
		
def YOUTUBE_LIST_USA():
		#AAW: Professional Wrestling Redefined
        channel="AAWPro"
        addDir("AAW: Professional Wrestling Redefined",'http://gdata.youtube.com/feeds/api/users/'+channel+'/uploads?start-index=1&max-results=50',13,'https://yt3.ggpht.com/-nZOP3h1NSPg/AAAAAAAAAAI/AAAAAAAAAAA/LHxy0sNH2iY/s300-c-k-no/photo.jpg')
		#All Pro Wrestling
        channel="allprowrestling"
        addDir("All Pro Wrestling",'http://gdata.youtube.com/feeds/api/users/'+channel+'/uploads?start-index=1&max-results=50',13,'https://yt3.ggpht.com/-5spMsdiMyYw/AAAAAAAAAAI/AAAAAAAAAAA/Z-pyiYMzZi4/s300-c-k-no/photo.jpg')
		#AML Wrestling
        channel="AMLWrestling"
        addDir("AML Wrestling",'http://gdata.youtube.com/feeds/api/users/'+channel+'/uploads?start-index=1&max-results=50',13,'https://yt3.ggpht.com/-heKizL3-cR0/AAAAAAAAAAI/AAAAAAAAAAA/ZmUMqTTJr_4/s352-c-k-no/photo.jpg')
		#Combat Zone Wrestling
        channel="CZWNews"
        addDir("Combat Zone Wrestling",'http://gdata.youtube.com/feeds/api/users/'+channel+'/uploads?start-index=1&max-results=50',13,'https://yt3.ggpht.com/-JrecmbZv7zI/AAAAAAAAAAI/AAAAAAAAAAA/nTueYHRs8nI/s352-c-k-no/photo.jpg')
		#CWF Mid-Atlantic Wrestling
        channel="CWFMidAtlantic"
        addDir("CWF Mid-Atlantic Wrestling",'http://gdata.youtube.com/feeds/api/users/'+channel+'/uploads?start-index=1&max-results=50',13,'https://yt3.ggpht.com/-8J6A5XijYy4/AAAAAAAAAAI/AAAAAAAAAAA/8C-kWNwbG_c/s352-c-k-no/photo.jpg')
		#Future Stars of Wrestling
        channel="FutureStarsWrestling"
        addDir("Future Stars of Wrestling",'http://gdata.youtube.com/feeds/api/users/'+channel+'/uploads?start-index=1&max-results=50',13,art + 'fsw.png')
		#Global Championship Wrestling
        channel="GCWProWrestling"
        addDir("Global Championship Wrestling",'http://gdata.youtube.com/feeds/api/users/'+channel+'/uploads?start-index=1&max-results=50',13,'https://yt3.ggpht.com/-6k19G9dr3r8/AAAAAAAAAAI/AAAAAAAAAAA/mKG2_IyJvt8/s352-c-k-no/photo.jpg')
		#Kansas City Metro Pro
        channel="KCMetroPro"
        addDir("Kansas City Metro Pro",'http://gdata.youtube.com/feeds/api/users/'+channel+'/uploads?start-index=1&max-results=50',13,art +'kcmp.png')
		#New England Championship Wrestling
        channel="necwwrestling"
        addDir("New England Championship Wrestling",'http://gdata.youtube.com/feeds/api/users/'+channel+'/uploads?start-index=1&max-results=50',13,'https://yt3.ggpht.com/-c3OD4KeSl7s/AAAAAAAAAAI/AAAAAAAAAAA/po-86nhJzQg/s300-c-k-no/photo.jpg')
		#New Revolution Wrestling
        channel="NRWRevolution"
        addDir("New Revolution Wrestling",'http://gdata.youtube.com/feeds/api/users/'+channel+'/uploads?start-index=1&max-results=50',13,'https://yt3.ggpht.com/-kDPvVqdCJ0s/AAAAAAAAAAI/AAAAAAAAAAA/8sXZvrbaBa4/s300-c-k-no/photo.jpg')
		#NWA Midwest Championship Wrestling
        channel="SEWProwrestling"
        addDir("NWA Midwest Championship Wrestling",'http://gdata.youtube.com/feeds/api/users/'+channel+'/uploads?start-index=1&max-results=50',13,art + 'nwamcw.png')
		#NWA Southern All Star Wrestling
        channel="krizull"
        addDir("NWA Southern All Star Wrestling",'http://gdata.youtube.com/feeds/api/users/'+channel+'/uploads?start-index=1&max-results=50',13,'https://yt3.ggpht.com/-F_0MLHbd8l8/AAAAAAAAAAI/AAAAAAAAAAA/SjAu13CBfhs/s300-c-k-no/photo.jpg')
		#Pennsylvania Premiere Wrestling
        channel="UC9Vcdw2lNEWR_AmVsELmsOg"
        addDir("Pennsylvania Premiere Wrestling",'http://gdata.youtube.com/feeds/api/users/'+channel+'/uploads?start-index=1&max-results=50',13,'https://yt3.ggpht.com/-pzNgORZsruQ/AAAAAAAAAAI/AAAAAAAAAAA/eujMhhrQ7cg/s352-c-k-no/photo.jpg')
		#Pro Wrestling Battleground
        channel="BattlegroundOfficial"
        addDir("Pro Wrestling Battleground",'http://gdata.youtube.com/feeds/api/users/'+channel+'/uploads?start-index=1&max-results=50',13,'https://yt3.ggpht.com/-8jJopZ1aO2Y/AAAAAAAAAAI/AAAAAAAAAAA/N5fOuiJrXx4/s352-c-k-no/photo.jpg')
		#Pro Wrestling Syndicate
        channel="ETapout"
        addDir("Pro Wrestling Syndicate",'http://gdata.youtube.com/feeds/api/users/'+channel+'/uploads?start-index=1&max-results=50',13,art + 'pws.png')
		#Reality of Wrestling
        channel="TheBookerTROW"
        addDir("Reality of Wrestling",'http://gdata.youtube.com/feeds/api/users/'+channel+'/uploads?start-index=1&max-results=50',13,art + 'row.png')
		#Tier 1 Wrestling
        channel="UCJi4aiPuqxcI_WIa4Fz3B9A"
        addDir("Tier 1 Wrestling",'http://gdata.youtube.com/feeds/api/users/'+channel+'/uploads?start-index=1&max-results=50',13,'https://yt3.ggpht.com/-tJGdDiqEl2I/AAAAAAAAAAI/AAAAAAAAAAA/tF2Ny3-t0-A/s352-c-k-no/photo.jpg')
		#Ultra Championship Wrestling-Zero
        channel="NWAUCWZERO"
        addDir("Ultra Championship Wrestling-Zero",'http://gdata.youtube.com/feeds/api/users/'+channel+'/uploads?start-index=1&max-results=50',13,'https://yt3.ggpht.com/-rFbPY6UXsbQ/AAAAAAAAAAI/AAAAAAAAAAA/U4t7VLax6Bs/s300-c-k-no/photo.jpg')
		#West Coast Wrestling Connection
        channel="WCWCPresents"
        addDir("West Coast Wrestling Connection",'http://gdata.youtube.com/feeds/api/users/'+channel+'/uploads?start-index=1&max-results=50',13,'https://yt3.ggpht.com/-zpDKDSbCyQw/AAAAAAAAAAI/AAAAAAAAAAA/5yOz1k-2nP4/s300-c-k-no/photo.jpg')
		#West Virginia Championship Wrestling
        channel="WVCWTV"
        addDir("West Virginia Championship Wrestling",'http://gdata.youtube.com/feeds/api/users/'+channel+'/uploads?start-index=1&max-results=50',13,'https://yt3.ggpht.com/-Prke6jG5Sz0/AAAAAAAAAAI/AAAAAAAAAAA/X8990e58pB8/s352-c-k-no/photo.jpg')
		
def YOUTUBE_LIST_EURO():
		#NEW European Championship Wrestling
        channel="NEW1Wrestling"
        addDir("NEW European Championship Wrestling",'http://gdata.youtube.com/feeds/api/users/'+channel+'/uploads?start-index=1&max-results=50',13,'https://yt3.ggpht.com/-3oel4-UHSoQ/AAAAAAAAAAI/AAAAAAAAAAA/L0cGTumwMtE/s352-c-k-no/photo.jpg')
		#Swiss Power Wrestling
        channel="spwofficiel"
        addDir("Swiss Power Wrestling",'http://gdata.youtube.com/feeds/api/users/'+channel+'/uploads?start-index=1&max-results=50',13,'https://yt3.ggpht.com/-xJAu9jWMPgk/AAAAAAAAAAI/AAAAAAAAAAA/IrBmABWd6p0/s352-c-k-no/photo.jpg')
		#Westside Xtreme Wrestling
        channel="wXwGER"
        addDir("Westside Xtreme Wrestling",'http://gdata.youtube.com/feeds/api/users/'+channel+'/uploads?start-index=1&max-results=50',13,'https://yt3.ggpht.com/-xSUbMnM2cDY/AAAAAAAAAAI/AAAAAAAAAAA/ovw0emo58fg/s352-c-k-no/photo.jpg')
		
def YOUTUBE_LIST_UK():
		#Insane Championship Wrestling
        channel="ICWOnline"
        addDir("Insane Championship Wrestling",'http://gdata.youtube.com/feeds/api/users/'+channel+'/uploads?start-index=1&max-results=50',13,'https://yt3.ggpht.com/-KjeljPNP9YE/AAAAAAAAAAI/AAAAAAAAAAA/8RPpUd5lIvE/s300-c-k-no/photo.jpg')
		#Preston City Wrestling
        channel="tovus"
        addDir("Preston City Wrestling",'http://gdata.youtube.com/feeds/api/users/'+channel+'/uploads?start-index=1&max-results=50',13,'https://yt3.ggpht.com/-0lEC8cSLl9E/AAAAAAAAAAI/AAAAAAAAAAA/UYTy5eeXm-Y/s900-c-k-no/photo.jpg')
		#Revolution Pro Wrestling
        channel="IPWrestlinguk"
        addDir("Revolution Pro Wrestling",'http://gdata.youtube.com/feeds/api/users/'+channel+'/uploads?start-index=1&max-results=50',13,art + 'revprouk.png')
		
def YOUTUBE_LIST_CANADA():
		#Smash Wrestling
        channel="SmashWrestling1"
        addDir("Smash Wrestling",'http://gdata.youtube.com/feeds/api/users/'+channel+'/uploads?start-index=1&max-results=50',13,'https://yt3.ggpht.com/-bzmLZk_wO54/AAAAAAAAAAI/AAAAAAAAAAA/dY9FmQ8SBz0/s300-c-k-no/photo.jpg')
		#Victory Commonwealth Wrestling
        channel="wrestlecrisis"
        addDir("Victory Commonwealth Wrestling",'http://gdata.youtube.com/feeds/api/users/'+channel+'/uploads?start-index=1&max-results=50',13,'https://yt3.ggpht.com/-WQdqnx_rn0Y/AAAAAAAAAAI/AAAAAAAAAAA/peHwinYc4aU/s352-c-k-no/photo.jpg')
		
def YOUTUBE_LIST_AUS():
		#Snakepit Adelaide Pro Wrestling
        channel="PowerslamTV"
        addDir("Snakepit Adelaide Pro Wrestling",'http://gdata.youtube.com/feeds/api/users/'+channel+'/uploads?start-index=1&max-results=50',13,art + 'snakepit.png')
		
def YOUTUBE_LIST_SINGAPORE():
		#Singapore Pro Wrestling
        channel="wrestlesingapore"
        addDir("Singapore Pro Wrestling",'http://gdata.youtube.com/feeds/api/users/'+channel+'/uploads?start-index=1&max-results=50',13,'https://yt3.ggpht.com/-MpE47zBs9aA/AAAAAAAAAAI/AAAAAAAAAAA/XC4Ho1FBaIA/s300-c-k-no/photo.jpg')
		
def YOUTUBE_LIST_BRAZIL():
		#Brazilian Wrestling Federation
        channel="BWFBrazil"
        addDir("Brazilian Wrestling Federation",'http://gdata.youtube.com/feeds/api/users/'+channel+'/uploads?start-index=1&max-results=50',13,'https://yt3.ggpht.com/-MkqsVZlsq8o/AAAAAAAAAAI/AAAAAAAAAAA/8Yz_5lUeGKw/s300-c-k-no/photo.jpg')
		
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
        title = plugintools.find_single_match(entry,"<titl[^>]+>([^<]+)</title>").replace("&amp;","&")
        plot = plugintools.find_single_match(entry,"<media\:descriptio[^>]+>([^<]+)</media\:description>")
        thumbnail = plugintools.find_single_match(entry,"<media\:thumbnail url='([^']+)'")
        video_id = plugintools.find_single_match(entry,"http\://www.youtube.com/watch\?v\=([^\&]+)\&").replace("&amp;","&")
        play_url = "plugin://plugin.video.youtube/?path=/root/video&action=play_video&videoid="+video_id

        plugintools.add_item( action="play" , title=title , plot=plot , url=play_url , fanart=thumbnail , thumbnail=thumbnail , folder=True )
    
    # Calculates next page URL from actual URL
    start_index = int( plugintools.find_single_match( link ,"start-index=(\d+)") )
    max_results = int( plugintools.find_single_match( link ,"max-results=(\d+)") )
    next_page_url = keep_url+"start-index=%d&max-results=%d" % ( start_index+max_results , max_results)

    addDir("Next Page",next_page_url,13,"")
	
	
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
            contextMenuItems.append(('Add to My Promotions', 'XBMC.RunPlugin(%s?mode=103&url=%s)'% (sys.argv[0], urllib.quote_plus(nameurl))))
        else:
            name = name
            contextMenuItems.append(('Remove from My Promotions', 'XBMC.RunPlugin(%s?mode=104&url=%s)'% (sys.argv[0], urllib.quote_plus(nameurl))))
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
        YOUTUBE_LIST()
		
elif mode==16:
        print ""+url
        YOUTUBE_LIST_USA()
		
elif mode==17:
        print ""+url
        YOUTUBE_LIST_EURO()
		
elif mode==18:
        print ""+url
        YOUTUBE_LIST_UK()
		
elif mode==19:
        print ""+url
        YOUTUBE_LIST_CANADA()
		
elif mode==20:
        print ""+url
        YOUTUBE_LIST_AUS()
		
elif mode==21:
        print ""+url
        YOUTUBE_LIST_SINGAPORE()
		
elif mode==22:
        print ""+url
        YOUTUBE_LIST_BRAZIL()
		
elif mode==101:
        watched(url,filename=WATCHED_FILE)
		
elif mode==102:
        unwatched(url,filename=WATCHED_FILE)
		
elif mode==103:
        watched(url,filename=FAVOURITES_FILE)
		
elif mode==104:
        unwatched(url,filename=FAVOURITES_FILE)
		

xbmcplugin.endOfDirectory(int(sys.argv[1]))
