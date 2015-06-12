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
		#Busted Open Nation
        channel="UCD_0Hz0876LEnfGxhkTMaLA"
        addDir("Busted Open Nation",'https://www.youtube.com/feeds/videos.xml?channel_id='+channel+'',13,'https://yt3.ggpht.com/-gPVwlRPjlSY/AAAAAAAAAAI/AAAAAAAAAAA/1JoUK2ZCMKY/s300-c-k-no/photo.jpg')
        #Pro Wrestling Cast
        channel="UCtS2zUbq91D2sWqkPH9UkZQ"
        addDir("Pro Wrestling Cast",'https://www.youtube.com/feeds/videos.xml?channel_id='+channel+'',13,'https://yt3.ggpht.com/-n42rVdokppM/AAAAAAAAAAI/AAAAAAAAAAA/Y4YwR0AdVSc/s352-c-k-no/photo.jpg')
        #Pro Wrestling Report
        channel="maxsports"
        addDir("Pro Wrestling Report",'https://www.youtube.com/feeds/videos.xml?user='+channel+'',13,'https://yt3.ggpht.com/-2uMdgaBCZk0/AAAAAAAAAAI/AAAAAAAAAAA/YX454E01E-s/s352-c-k-no/photo.jpg')
		#WrestleTalk TV
        channel="WrestletalkTV"
        addDir("WrestleTalk TV",'https://www.youtube.com/feeds/videos.xml?user='+channel+'',13,'https://yt3.ggpht.com/-GhhGrJWqON4/AAAAAAAAAAI/AAAAAAAAAAA/RF1aZIqr3NY/s352-c-k-no/photo.jpg')
		#Wrestling Roundtable
        channel="WrestlingRoundtable"
        addDir("Wrestling Roundtable",'https://www.youtube.com/feeds/videos.xml?user='+channel+'',13,'https://i.ytimg.com/i/yCTT2VVfThDZ3dk4kzKlzw/mq1.jpg')
		
def YOUTUBE_LIST_USA():
		#AAW: Professional Wrestling Redefined
        channel="AAWPro"
        addDir("AAW: Professional Wrestling Redefined",'https://www.youtube.com/feeds/videos.xml?user='+channel+'',13,'https://yt3.ggpht.com/-nZOP3h1NSPg/AAAAAAAAAAI/AAAAAAAAAAA/LHxy0sNH2iY/s300-c-k-no/photo.jpg')
		#All Pro Wrestling
        channel="allprowrestling"
        addDir("All Pro Wrestling",'https://www.youtube.com/feeds/videos.xml?user='+channel+'',13,'https://yt3.ggpht.com/-5spMsdiMyYw/AAAAAAAAAAI/AAAAAAAAAAA/Z-pyiYMzZi4/s300-c-k-no/photo.jpg')
		#Allied Independent Wrestling Federations
        channel="aiwfwrestling"
        addDir("Allied Independent Wrestling Federations",'https://www.youtube.com/feeds/videos.xml?user='+channel+'',13,'https://yt3.ggpht.com/-CWhpFKyb3YQ/AAAAAAAAAAI/AAAAAAAAAAA/kE1IAW1bSDA/s300-c-k-no/photo.jpg')
		#AML Wrestling
        channel="AMLWrestling"
        addDir("AML Wrestling",'https://www.youtube.com/feeds/videos.xml?user='+channel+'',13,'https://yt3.ggpht.com/-heKizL3-cR0/AAAAAAAAAAI/AAAAAAAAAAA/ZmUMqTTJr_4/s352-c-k-no/photo.jpg')
		#Combat Zone Wrestling
        channel="CZWNews"
        addDir("Combat Zone Wrestling",'https://www.youtube.com/feeds/videos.xml?user='+channel+'',13,'https://yt3.ggpht.com/-JrecmbZv7zI/AAAAAAAAAAI/AAAAAAAAAAA/nTueYHRs8nI/s352-c-k-no/photo.jpg')
		#Covey Pro Wrestling
        channel="CoveyProTV"
        addDir("Covey Pro Wrestling",'https://www.youtube.com/feeds/videos.xml?user='+channel+'',13,'https://yt3.ggpht.com/-zlaT_RsiYdY/AAAAAAAAAAI/AAAAAAAAAAA/bKbLbAqqniw/s300-c-k-no/photo.jpg')
		#CWF Mid-Atlantic Wrestling
        channel="CWFMidAtlantic"
        addDir("CWF Mid-Atlantic Wrestling",'https://www.youtube.com/feeds/videos.xml?user='+channel+'',13,'https://yt3.ggpht.com/-8J6A5XijYy4/AAAAAAAAAAI/AAAAAAAAAAA/8C-kWNwbG_c/s352-c-k-no/photo.jpg')
		#Enigma Pro Wrestling
        channel="ENIGMAProWrestling"
        addDir("Enigma Pro Wrestling",'https://www.youtube.com/feeds/videos.xml?user='+channel+'',13,'https://yt3.ggpht.com/-1Ay9nMtX9xo/AAAAAAAAAAI/AAAAAAAAAAA/o9f6omQ-BQo/s300-c-k-no/photo.jpg')
		#Future Stars of Wrestling
        channel="FutureStarsWrestling"
        addDir("Future Stars of Wrestling",'https://www.youtube.com/feeds/videos.xml?user='+channel+'',13,art + 'fsw.png')
		#Global Championship Wrestling
        channel="GCWProWrestling"
        addDir("Global Championship Wrestling",'https://www.youtube.com/feeds/videos.xml?user='+channel+'',13,'https://yt3.ggpht.com/-6k19G9dr3r8/AAAAAAAAAAI/AAAAAAAAAAA/mKG2_IyJvt8/s352-c-k-no/photo.jpg')
		#IWA Mid-South Wrestling
        channel="IWAMidsouthWrestling"
        addDir("IWA Mid-South Wrestling",'https://www.youtube.com/feeds/videos.xml?user='+channel+'',13,'https://yt3.ggpht.com/-kdZ2wu9J370/AAAAAAAAAAI/AAAAAAAAAAA/W357OeuZDYg/s300-c-k-no/photo.jpg')
		#Kansas City Metro Pro
        channel="KCMetroPro"
        addDir("Kansas City Metro Pro",'https://www.youtube.com/feeds/videos.xml?user='+channel+'',13,art +'kcmp.png')
		#New England Championship Wrestling
        channel="necwwrestling"
        addDir("New England Championship Wrestling",'https://www.youtube.com/feeds/videos.xml?user='+channel+'',13,'https://yt3.ggpht.com/-c3OD4KeSl7s/AAAAAAAAAAI/AAAAAAAAAAA/po-86nhJzQg/s300-c-k-no/photo.jpg')
		#New Revolution Wrestling
        channel="NRWRevolution"
        addDir("New Revolution Wrestling",'https://www.youtube.com/feeds/videos.xml?user='+channel+'',13,'https://yt3.ggpht.com/-kDPvVqdCJ0s/AAAAAAAAAAI/AAAAAAAAAAA/8sXZvrbaBa4/s300-c-k-no/photo.jpg')
		#NWA Midwest Championship Wrestling
        channel="SEWProwrestling"
        addDir("NWA Midwest Championship Wrestling",'https://www.youtube.com/feeds/videos.xml?user='+channel+'',13,art + 'nwamcw.png')
		#NWA Southern All Star Wrestling
        channel="krizull"
        addDir("NWA Southern All Star Wrestling",'https://www.youtube.com/feeds/videos.xml?user='+channel+'',13,'https://yt3.ggpht.com/-F_0MLHbd8l8/AAAAAAAAAAI/AAAAAAAAAAA/SjAu13CBfhs/s300-c-k-no/photo.jpg')
		#Pennsylvania Premiere Wrestling
        channel="UC9Vcdw2lNEWR_AmVsELmsOg"
        addDir("Pennsylvania Premiere Wrestling",'https://www.youtube.com/feeds/videos.xml?channel_id='+channel+'',13,'https://yt3.ggpht.com/-pzNgORZsruQ/AAAAAAAAAAI/AAAAAAAAAAA/eujMhhrQ7cg/s352-c-k-no/photo.jpg')
		#Pro Wrestling Arizona
        channel="RPWNWA"
        addDir("Pro Wrestling Arizona",'https://www.youtube.com/feeds/videos.xml?user='+channel+'',13,'https://yt3.ggpht.com/-Aog3gQeRPsM/AAAAAAAAAAI/AAAAAAAAAAA/Nkb_v16Eh5k/s300-c-k-no/photo.jpg')
		#Pro Wrestling Battleground
        channel="BattlegroundOfficial"
        addDir("Pro Wrestling Battleground",'https://www.youtube.com/feeds/videos.xml?user='+channel+'',13,'https://yt3.ggpht.com/-8jJopZ1aO2Y/AAAAAAAAAAI/AAAAAAAAAAA/N5fOuiJrXx4/s352-c-k-no/photo.jpg')
		#Pro Wrestling Syndicate
        channel="ETapout"
        addDir("Pro Wrestling Syndicate",'https://www.youtube.com/feeds/videos.xml?user='+channel+'',13,art + 'pws.png')
		#Reality of Wrestling
        channel="TheBookerTROW"
        addDir("Reality of Wrestling",'https://www.youtube.com/feeds/videos.xml?user='+channel+'',13,art + 'row.png')
		#Tier 1 Wrestling
        channel="UCJi4aiPuqxcI_WIa4Fz3B9A"
        addDir("Tier 1 Wrestling",'https://www.youtube.com/feeds/videos.xml?channel_id='+channel+'',13,'https://yt3.ggpht.com/-tJGdDiqEl2I/AAAAAAAAAAI/AAAAAAAAAAA/tF2Ny3-t0-A/s352-c-k-no/photo.jpg')
		#Ultra Championship Wrestling-Zero
        channel="NWAUCWZERO"
        addDir("Ultra Championship Wrestling-Zero",'https://www.youtube.com/feeds/videos.xml?user='+channel+'',13,'https://yt3.ggpht.com/-rFbPY6UXsbQ/AAAAAAAAAAI/AAAAAAAAAAA/U4t7VLax6Bs/s300-c-k-no/photo.jpg')
		#Vanguard Championship Wrestling
        channel="jstep009"
        addDir("Vanguard Championship Wrestling",'https://www.youtube.com/feeds/videos.xml?user='+channel+'',13,'https://yt3.ggpht.com/-cT8O0X49FgE/AAAAAAAAAAI/AAAAAAAAAAA/cUllNw5WzXk/s300-c-k-no/photo.jpg')
		#West Coast Wrestling Connection
        channel="WCWCPresents"
        addDir("West Coast Wrestling Connection",'https://www.youtube.com/feeds/videos.xml?user='+channel+'',13,'https://yt3.ggpht.com/-zpDKDSbCyQw/AAAAAAAAAAI/AAAAAAAAAAA/5yOz1k-2nP4/s300-c-k-no/photo.jpg')
		#West Virginia Championship Wrestling
        channel="WVCWTV"
        addDir("West Virginia Championship Wrestling",'https://www.youtube.com/feeds/videos.xml?user='+channel+'',13,'https://yt3.ggpht.com/-Prke6jG5Sz0/AAAAAAAAAAI/AAAAAAAAAAA/X8990e58pB8/s352-c-k-no/photo.jpg')
		
def YOUTUBE_LIST_EURO():
		#German Wrestling Federation
        channel="WrestlingGWF"
        addDir("German Wrestling Federation",'https://www.youtube.com/feeds/videos.xml?user='+channel+'',13,'https://yt3.ggpht.com/-ERydrBnitYQ/AAAAAAAAAAI/AAAAAAAAAAA/l5G_iBlAV2I/s300-c-k-no/photo.jpg')
		#NEW European Championship Wrestling
        channel="NEW1Wrestling"
        addDir("NEW European Championship Wrestling",'https://www.youtube.com/feeds/videos.xml?user='+channel+'',13,'https://yt3.ggpht.com/-3oel4-UHSoQ/AAAAAAAAAAI/AAAAAAAAAAA/L0cGTumwMtE/s352-c-k-no/photo.jpg')
		#Swiss Power Wrestling
        channel="spwofficiel"
        addDir("Swiss Power Wrestling",'https://www.youtube.com/feeds/videos.xml?user='+channel+'',13,'https://yt3.ggpht.com/-xJAu9jWMPgk/AAAAAAAAAAI/AAAAAAAAAAA/IrBmABWd6p0/s352-c-k-no/photo.jpg')
		#Westside Xtreme Wrestling
        channel="wXwGER"
        addDir("Westside Xtreme Wrestling",'https://www.youtube.com/feeds/videos.xml?user='+channel+'',13,'https://yt3.ggpht.com/-xSUbMnM2cDY/AAAAAAAAAAI/AAAAAAAAAAA/ovw0emo58fg/s352-c-k-no/photo.jpg')
		
def YOUTUBE_LIST_UK():
		#EPW Wrestling
        channel="EPWWRESTLETV"
        addDir("EPW Wrestling",'https://www.youtube.com/feeds/videos.xml?user='+channel+'',13,'https://yt3.ggpht.com/-L3qkJpnGOWc/AAAAAAAAAAI/AAAAAAAAAAA/66DMw73K88M/s300-c-k-no/photo.jpg')
		#Insane Championship Wrestling
        channel="ICWOnline"
        addDir("Insane Championship Wrestling",'https://www.youtube.com/feeds/videos.xml?user='+channel+'',13,'https://yt3.ggpht.com/-KjeljPNP9YE/AAAAAAAAAAI/AAAAAAAAAAA/8RPpUd5lIvE/s300-c-k-no/photo.jpg')
		#Preston City Wrestling
        channel="tovus"
        addDir("Preston City Wrestling",'https://www.youtube.com/feeds/videos.xml?user='+channel+'',13,'https://yt3.ggpht.com/-0lEC8cSLl9E/AAAAAAAAAAI/AAAAAAAAAAA/UYTy5eeXm-Y/s900-c-k-no/photo.jpg')
		#Revolution Pro Wrestling
        channel="IPWrestlinguk"
        addDir("Revolution Pro Wrestling",'https://www.youtube.com/feeds/videos.xml?user='+channel+'',13,art + 'revprouk.png')
		
def YOUTUBE_LIST_CANADA():
		#Canadian Wrestling's Elite
        channel="cwelite1"
        addDir("Canadian Wrestling's Elite",'https://www.youtube.com/feeds/videos.xml?user='+channel+'',13,'https://yt3.ggpht.com/-NjP-SwI1m7Q/AAAAAAAAAAI/AAAAAAAAAAA/196yZZhRqxw/s300-c-k-no/photo.jpg')
		#Legend City Wrestling
        channel="lcwnl"
        addDir("Legend City Wrestling",'https://www.youtube.com/feeds/videos.xml?user='+channel+'',13,'https://yt3.ggpht.com/-68Spmeaxnr4/AAAAAAAAAAI/AAAAAAAAAAA/i5KjhTRjEUk/s300-c-k-no/photo.jpg')
		#Smash Wrestling
        channel="SmashWrestling1"
        addDir("Smash Wrestling",'https://www.youtube.com/feeds/videos.xml?user='+channel+'',13,'https://yt3.ggpht.com/-bzmLZk_wO54/AAAAAAAAAAI/AAAAAAAAAAA/dY9FmQ8SBz0/s300-c-k-no/photo.jpg')
		#Victory Commonwealth Wrestling
        channel="wrestlecrisis"
        addDir("Victory Commonwealth Wrestling",'https://www.youtube.com/feeds/videos.xml?user='+channel+'',13,'https://yt3.ggpht.com/-WQdqnx_rn0Y/AAAAAAAAAAI/AAAAAAAAAAA/peHwinYc4aU/s352-c-k-no/photo.jpg')
		
def YOUTUBE_LIST_AUS():
		#Pacific Pro Wrestling
        channel="PacificProWrestling"
        addDir("Pacific Pro Wrestling",'https://www.youtube.com/feeds/videos.xml?user='+channel+'',13,'https://yt3.ggpht.com/-aSDZo8PsdCw/AAAAAAAAAAI/AAAAAAAAAAA/w6uWd1FErK4/s300-c-k-no/photo.jpg')
		#Riot City Wrestling
        channel="RiotCityWrestling"
        addDir("Riot City Wrestling",'https://www.youtube.com/feeds/videos.xml?user='+channel+'',13,'https://yt3.ggpht.com/-UBbKPonG-V8/AAAAAAAAAAI/AAAAAAAAAAA/kTZuelxvuuo/s300-c-k-no/photo.jpg')
		#Snakepit Adelaide Pro Wrestling
        channel="PowerslamTV"
        addDir("Snakepit Adelaide Pro Wrestling",'https://www.youtube.com/feeds/videos.xml?user='+channel+'',13,art + 'snakepit.png')
		
def YOUTUBE_LIST_SINGAPORE():
		#Singapore Pro Wrestling
        channel="wrestlesingapore"
        addDir("Singapore Pro Wrestling",'https://www.youtube.com/feeds/videos.xml?user='+channel+'',13,'https://yt3.ggpht.com/-MpE47zBs9aA/AAAAAAAAAAI/AAAAAAAAAAA/XC4Ho1FBaIA/s300-c-k-no/photo.jpg')
		
def YOUTUBE_LIST_BRAZIL():
		#Brazilian Wrestling Federation
        channel="BWFBrazil"
        addDir("Brazilian Wrestling Federation",'https://www.youtube.com/feeds/videos.xml?user='+channel+'',13,'https://yt3.ggpht.com/-MkqsVZlsq8o/AAAAAAAAAAI/AAAAAAAAAAA/8Yz_5lUeGKw/s300-c-k-no/photo.jpg')
		
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
        thumbnail = plugintools.find_single_match(entry,'<media\:thumbnail url="(.+?)"')
        video_id = plugintools.find_single_match(entry,'http\://www.youtube.com/watch\?v\=(.+?)"')
        play_url = 'plugin://plugin.video.youtube/play/?video_id='+video_id

        plugintools.add_item( action="play" , title=title , plot=plot , url=play_url , fanart=thumbnail , thumbnail=thumbnail , folder=True )
	
	
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
