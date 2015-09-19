
#
#  This Program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2, or (at your option)
#  any later version.
#
#  This Program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with XBMC; see the file COPYING.  If not, write to
#  the Free Software Foundation, 675 Mass Ave, Cambridge, MA 02139, USA.
#  http://www.gnu.org/copyleft/gpl.html
#

#elif action == 'resolve':
#    import xbmcgui
#    import xbmcplugin

#    from resources.lib.sources import sources
#    url      = sources().sourcesResolve(url, provider)
#    listitem = xbmcgui.ListItem(name)

#    try:
#        xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=url, listitem=listitem)
#        xbmcplugin.endOfDirectory(int(sys.argv[1]))
#    except Exception, e:
#        pass


import xbmc
import xbmcgui
import simplejson 

ADDONID = 'plugin.video.genesis'


def fileSystemSafe(text):
    import re
    text = re.sub('[:\\/*?\<>|"]+', '', text)
    return text.strip()



def log(text):
    try:
        output = '%s' % str(text)
        
        print output
        xbmc.log(output, xbmc.LOGDEBUG)
    except:
        pass



def setKodiSetting(setting, value):
    setting = '"%s"' % setting

    if isinstance(value, list):
        text = ''
        for item in value:
            text += '"%s",' % str(item)

        text  = text[:-1]
        text  = '[%s]' % text
        value = text

    elif isinstance(value, bool):
        value = 'true' if value else 'false'

    elif not isinstance(value, int):
        value = '"%s"' % value

    query = '{"jsonrpc":"2.0", "method":"Settings.SetSettingValue","params":{"setting":%s,"value":%s}, "id":1}' % (setting, value)
    log(query)
    response = xbmc.executeJSONRPC(query)
    log(response)


def getKodiSetting(setting):
    try:
        setting = '"%s"' % setting
 
        query = '{"jsonrpc":"2.0", "method":"Settings.GetSettingValue","params":{"setting":%s}, "id":1}' % (setting)
        log(query)
        response = xbmc.executeJSONRPC(query)
        log(response)

        response = simplejson.loads(response)                

        if response.has_key('result'):
            if response['result'].has_key('value'):
                return response ['result']['value'] 
    except:
        pass

    return None



def get_params(path):
    params = {}
    path   = path.split('?', 1)[-1]
    pairs  = path.split('&')

    for pair in pairs:
        split = pair.split('=')
        if len(split) > 1:
            params[split[0]] = split[1]

    return params


def add(params):
    options = [] #['Genesis settings']

    path = params['path']

    try:
        if not path.lower().startswith('plugin://%s/' % ADDONID):
            return options

        params = get_params(path)

        if 'action' not in params:
            return options

        if 'url' not in params:
            return options

        if 'provider' not in params:
            return options

        action = params['action']

        if not (action == 'playItem' or action == 'play'):
            return options

        options.append('Download')

        return options
    except Exception, e:
        xbmc.log('Error in add : %s' % str(e), xbmc.LOGDEBUG)

    return options


def process(option, params):
    #if option == 0:
    #    xbmc.executebuiltin('Addon.OpenSettings(%s)' % ADDONID)
    #    return

    import urllib

    path   = params['path']
    params = get_params(path)

    path = path.replace('?action=playItem', '?action=resolve')
    path = path.replace('?action=play',     '?action=resolve')
    path = urllib.quote_plus(path)

    try:
        webserver = getKodiSetting('services.webserver')
        if not webserver:
            setKodiSetting('services.webserver', True)
    except Exception, e:
        log('Error obtaining webserver enabled setting : ' % str(e))

    port     = 80
    username = 'kodi'
    password = ''

    try:
        port     = int(getKodiSetting('services.webserverport'))
        username = getKodiSetting('services.webserverusername')
        password = getKodiSetting('services.webserverpassword')
    except Exception, e:
        log('Error obtaining webserver credentials : %s' % str(e))


    req  = 'http://127.0.0.1:%d/jsonrpc?request={"jsonrpc":"2.0","method":"Files.GetDirectory","params":{"directory":"%s"},"id":1}' % (port, path)

    log('Genesis request : %s' % req)

    try:       
        import urllib2
        req  = urllib2.Request(req)

        if len(password) > 0:
            import base64
            base64string = base64.encodestring('%s:%s' % (username, password))[:-1]
            authheader   = 'Basic %s' % base64string
            req.add_header('Authorization', authheader)

        resp = urllib2.urlopen(req, timeout=10).read()

        log('Response from Genesis')
        log(resp)

        resp = simplejson.loads(resp) 

        result = resp['result']
        file   = result['files'][0]
        url    = file['file']
        name   = file['label']

        try:
             download(fileSystemSafe(name), url)
        except Exception, e:
            xbmc.log('Error in download : %s' % str(e), xbmc.LOGDEBUG)

    except Exception, e:
        log('Error in process : %s' % str(e))
        xbmcgui.Dialog().ok('', 'Failed to download', 'No response from server')

    #reset if necessary
    if not webserver:
        setKodiSetting('services.webserver', False)


def download(name, url):
    import urllib
    import re
    import xbmc
    import sfile
    import xbmcaddon
    import os

    agent   = None
    referer = None
    cookie  = None

    if '|' in url:
        url, items = url.split('|', 1)
        items = items.split('&', 1)

        for item in items:
            params = item.split('=', 1)
            if params[0] == 'Referer':
                referer = urllib.unquote_plus(params[1])
            if params[0] == 'User-Agent':
                agent = urllib.unquote_plus(params[1])    
            if params[0] == 'Cookie':
                agent = urllib.unquote_plus(params[1])    

    name = re.sub('\/:*?"<>|', '', name).strip('.')

    content = re.compile('(.+?)\sS(\d*)E\d*$').findall(name)

    addon = xbmcaddon.Addon(ADDONID)

    if len(content) == 0:
        dest = addon.getSetting('movie_library')
        dest = os.path.join(dest, name)
    else:
        dest = addon.getSetting('tv_library')
        dest = os.path.join(dest, content[0][0])
        dest = os.path.join(dest, 'Season %01d' % int(content[0][1]))

    sfile.makedirs(dest)

    ext = 'mp4'
    try:
        ext = url.rsplit['.', 1][-1]
        if not ext in ['mp4', 'mkv', 'flv', 'avi', 'mpg']: 
            ext = 'mp4'
    except:
        ext = 'mp4'

    dest = os.path.join(dest, name + '.' + ext)

    title = addon.getAddonInfo('name')

    import download
    download.download(url, dest, title, referer=referer, agent=agent, cookie=cookie)