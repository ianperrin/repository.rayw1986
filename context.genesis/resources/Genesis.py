
import xbmc
import simplejson 

ADDONID = 'plugin.video.genesis'


def log(text):
    try:
        output = '%s' % str(text)
        xbmc.log(output, xbmc.LOGDEBUG)
    except:
        pass



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
    options = []
    path    = params['path']

    try:
        if not path.lower().startswith('plugin://%s/' % ADDONID):
            return options

        params = get_params(path)

        if 'action' not in params:
            return options

        if 'source' not in params:
            return options

        action = params['action']

        if not (action == 'playItem' or action == 'play'):
            return options

        options.append('Download item')

        return options
    except Exception, e:
        xbmc.log('Error in add : %s' % str(e), xbmc.LOGDEBUG)

    return options


def process(option, params):
    import urllib
    
    path   = params['path']
    image  = params['thumb']

    params   = get_params(path)
    name     = urllib.unquote_plus(params['name'])
    source   = urllib.unquote_plus(params['source'])[1:-1]
    source   = simplejson.loads(source)
    url      = source['url']
    provider = source['provider']

    cmd  = 'plugin://plugin.video.genesis/?'
    cmd += 'action=download'
    cmd += '&name=%s'     % urllib.quote_plus(name)
    cmd += '&image=%s'    % urllib.quote_plus(image)
    cmd += '&url=%s'      % urllib.quote_plus(url)
    cmd += '&provider=%s' % urllib.quote_plus(provider)

    xbmc.executebuiltin('XBMC.Container.Update(%s)' % cmd)