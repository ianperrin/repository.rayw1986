# -*- coding: utf-8 -*-		

'''
    Genesis Context Menu Tools Add-on
    Copyright (C) 2015 rayw1986

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''
		
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
		
def import_options():
		dialog = xbmcgui.Dialog()
		funcs = (
			trakt_collection,
			trakt_watchlist,
			trakt_tv_collection,
			trakt_tv_watchlist,
			imdb_watchlist,
			imdb_tv_watchlist,
		)
		ret = dialog.select('Genesis Import Options', ['[B]TRAKT[/B] : Import Collection...', '[B]TRAKT[/B] : Import Watchlist...', '[B]TRAKT[/B] : Import TV Collection...', '[B]TRAKT[/B] : Import TV Watchlist...', '[B]IMDB[/B] : Import Watchlist...', '[B]IMDB[/B] : Import TV Watchlist...'])
		if ret > -1:
			funcs[ret]()
			
if __name__ == '__main__':
		dialog = xbmcgui.Dialog()
		funcs = (
			settings,
			autoplay,
			clear_cache,
			clear_sources,
			update_folders,
			search,
			import_options
		)
		ret = dialog.select('Genesis Library Options', ['Genesis Settings', 'Toggle Autoplay', 'Clear Cache', 'Clear Sources', 'Update Folders', 'Search Genesis', 'Library Import Options...'])
		if ret > -1:
			funcs[ret]()