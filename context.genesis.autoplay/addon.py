# -*- coding: utf-8 -*-		
		
import xbmc,xbmcaddon		
addon = xbmcaddon.Addon('plugin.video.genesis')
autoit = addon.getSetting('autoplay_library')
if __name__ == '__main__':
    if autoit == 'true':
        addon.setSetting('autoplay_library','false')
    else:
        addon.setSetting('autoplay_library','true')