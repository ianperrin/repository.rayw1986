# -*- coding: utf-8 -*-		
		
import xbmc,xbmcaddon,xbmcgui		
addon = xbmcaddon.Addon('plugin.video.genesis')
autoit = addon.getSetting('autoplay_library')

def settings():
		xbmc.executebuiltin('Addon.OpenSettings(plugin.video.genesis)')

def autoplay():
		if autoit == 'true':
			addon.setSetting('autoplay_library','false')
		else:
			addon.setSetting('autoplay_library','true')
			
def clear_cache():
		xbmc.executebuiltin('XBMC.RunAddon(plugin.video.genesis,action=clearCache)')
		
def clear_sources():
		xbmc.executebuiltin('XBMC.RunAddon(plugin.video.genesis,action=clearSources)')
		
def update_folders():
		xbmc.executebuiltin('XBMC.RunAddon(plugin.video.genesis,action=updateLibrary&query=tool)')
		
def trakt_collection():
		xbmc.executebuiltin('XBMC.RunAddon(plugin.video.genesis,action=moviesToLibrary&query=tool&url=traktcollection)')
	
def trakt_watchlist():
		xbmc.executebuiltin('XBMC.RunAddon(plugin.video.genesis,action=moviesToLibrary&query=tool&url=traktwatchlist)')
		
def trakt_tv_collection():
		xbmc.executebuiltin('XBMC.RunAddon(plugin.video.genesis,action=tvshowsToLibrary&query=tool&url=traktcollection)')
	
def trakt_tv_watchlist():
		xbmc.executebuiltin('XBMC.RunAddon(plugin.video.genesis,action=tvshowsToLibrary&query=tool&url=traktwatchlist)')
		
def imdb_watchlist():
		xbmc.executebuiltin('XBMC.RunAddon(plugin.video.genesis,action=moviesToLibrary&query=tool&url=imdbwatchlist)')
		
def imdb_tv_watchlist():
		xbmc.executebuiltin('XBMC.RunAddon(plugin.video.genesis,action=tvshowsToLibrary&query=tool&url=imdbwatchlist)')
		
def search():
		xbmc.executebuiltin('XBMC.RunAddon(plugin.video.genesis,action=searchNavigator)')

if __name__ == '__main__':
		dialog = xbmcgui.Dialog()
		funcs = (
			settings,
			autoplay,
			clear_cache,
			clear_sources,
			update_folders
		)
		ret = dialog.select('Genesis Library Options', ['Genesis Settings', 'Toggle Autoplay', 'Clear Cache...', 'Clear Sources...', 'Update Folders...', '[B]TRAKT[/B] : Import Collection...', '[B]TRAKT[/B] : Import Watchlist...', '[B]TRAKT[/B] : Import TV Collection...', '[B]TRAKT[/B] : Import TV Watchlist...', '[B]IMDB[/B] : Import Watchlist...', '[B]IMDB[/B] : Import TV Watchlist...', 'Search Genesis'])
		if ret == 0:
			settings()
		if ret == 1:
			autoplay()
		if ret == 2:
			clear_cache()
		if ret == 3:
			clear_sources()
		if ret == 4:
			update_folders()
		if ret == 5:
			trakt_collection()
		if ret == 6:
			trakt_watchlist()
		if ret == 7:
			trakt_tv_collection()
		if ret == 8:
			trakt_tv_watchlist()
		if ret == 9:
			imdb_watchlist()
		if ret == 10:
			imdb_tv_watchlist()
		if ret == 11:
			search()