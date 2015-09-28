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
icon = addon.getAddonInfo('icon')

title = "Genesis"
text_on = "Autoplay Toggled On"
text_off = "Autoplay Toggled Off"
time = 5000

def settings():
		xbmc.executebuiltin('Addon.OpenSettings(plugin.video.genesis)')

def autoplay():
		if autoit == 'true':
			addon.setSetting('autoplay_library','false')
			xbmc.executebuiltin('Notification(%s, %s, %d, %s)'%(title, text_off, time, icon))
		else:
			addon.setSetting('autoplay_library','true')
			xbmc.executebuiltin('Notification(%s, %s, %d, %s)'%(title, text_on, time, icon))
			
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
		
def browse_movies_genres():
		xbmc.executebuiltin('XBMC.RunAddon(plugin.video.genesis,action=movieGenres)')
		
def browse_movies_years():
		xbmc.executebuiltin('XBMC.RunAddon(plugin.video.genesis,action=movieYears)')
		
def browse_movies_people():
		xbmc.executebuiltin('XBMC.RunAddon(plugin.video.genesis,action=moviePersons)')
		
def browse_movies_cert():
		xbmc.executebuiltin('XBMC.RunAddon(plugin.video.genesis,action=movieCertificates)')
		
def browse_movies_featured():
		xbmc.executebuiltin('XBMC.RunAddon(plugin.video.genesis,action=movies&url=featured)')
		
def browse_movies_watching():
		xbmc.executebuiltin('XBMC.RunAddon(plugin.video.genesis,action=movies&url=trending)')
		
def browse_movies_popular():
		xbmc.executebuiltin('XBMC.RunAddon(plugin.video.genesis,action=movies&url=popular)')
		
def browse_movies_voted():
		xbmc.executebuiltin('XBMC.RunAddon(plugin.video.genesis,action=movies&url=views)')
		
def browse_movies_boxoffice():
		xbmc.executebuiltin('XBMC.RunAddon(plugin.video.genesis,action=movies&url=boxoffice)')
		
def browse_movies_oscars():
		xbmc.executebuiltin('XBMC.RunAddon(plugin.video.genesis,action=movies&url=oscars)')
		
def browse_movies_theaters():
		xbmc.executebuiltin('XBMC.RunAddon(plugin.video.genesis,action=movies&url=theaters)')
		
def browse_movies_latest():
		xbmc.executebuiltin('XBMC.RunAddon(plugin.video.genesis,action=movies&url=added)')
		
def browse_movies_fav():
		xbmc.executebuiltin('XBMC.RunAddon(plugin.video.genesis,action=movieFavourites)')
	
def browse_tv_genres():
		xbmc.executebuiltin('XBMC.RunAddon(plugin.video.genesis,action=tvGenres)')
		
def browse_tv_years():
		xbmc.executebuiltin('XBMC.RunAddon(plugin.video.genesis,action=tvYears)')
		
def browse_tv_networks():
		xbmc.executebuiltin('XBMC.RunAddon(plugin.video.genesis,action=tvNetworks)')
		
def browse_tv_watching():
		xbmc.executebuiltin('XBMC.RunAddon(plugin.video.genesis,action=tvshows&url=trending)')
		
def browse_tv_popular():
		xbmc.executebuiltin('XBMC.RunAddon(plugin.video.genesis,action=tvshows&url=popular)')
		
def browse_tv_today():
		xbmc.executebuiltin('XBMC.RunAddon(plugin.video.genesis,action=tvshows&url=airing)')
		
def browse_tv_returning():
		xbmc.executebuiltin('XBMC.RunAddon(plugin.video.genesis,action=tvshows&url=active)')
		
def browse_tv_new():
		xbmc.executebuiltin('XBMC.RunAddon(plugin.video.genesis,action=tvshows&url=premiere)')
		
def browse_tv_rated():
		xbmc.executebuiltin('XBMC.RunAddon(plugin.video.genesis,action=tvshows&url=rating)')
		
def browse_tv_voted():
		xbmc.executebuiltin('XBMC.RunAddon(plugin.video.genesis,action=tvshows&url=views)')
		
def browse_tv_calendars():
		xbmc.executebuiltin('XBMC.RunAddon(plugin.video.genesis,action=calendars)')
		
def browse_tv_latesteps():
		xbmc.executebuiltin('XBMC.RunAddon(plugin.video.genesis,action=calendar&url=added)')
		
def browse_tv_faveps():
		xbmc.executebuiltin('XBMC.RunAddon(plugin.video.genesis,action=episodeFavourites)')
		
def browse_tv_fav():
		xbmc.executebuiltin('XBMC.RunAddon(plugin.video.genesis,action=tvFavourites)')
		
def browse_channels():
		xbmc.executebuiltin('XBMC.RunAddon(plugin.video.genesis,action=channels)')
		
def browse_mygen():
		xbmc.executebuiltin('XBMC.RunAddon(plugin.video.genesis,action=myNavigator)')
		
def browse_latestmov():
		xbmc.executebuiltin('XBMC.RunAddon(plugin.video.genesis,action=movieWidget)')
		
def browse_latesteps():
		xbmc.executebuiltin('XBMC.RunAddon(plugin.video.genesis,action=tvWidget)')
		
def browse_calendars():
		xbmc.executebuiltin('XBMC.RunAddon(plugin.video.genesis,action=calendars)')
		
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
			
def browse():
		dialog = xbmcgui.Dialog()
		funcs = (
			browse_movies,
			browse_tv,
			browse_channels,
			browse_mygen,
			browse_latestmov,
			browse_latesteps,
			browse_calendars,
		)
		ret = dialog.select('Browse Genesis', ['Movies', 'TV Shows', 'Channels', 'My Genesis', 'Latest Movies', 'Latest Episodes', 'TV Calendar'])
		if ret > -1:
			funcs[ret]()
			
def browse_movies():
		dialog = xbmcgui.Dialog()
		funcs = (
			browse_movies_genres,
			browse_movies_years,
			browse_movies_people,
			browse_movies_cert,
			browse_movies_featured,
			browse_movies_watching,
			browse_movies_popular,
			browse_movies_voted,
			browse_movies_boxoffice,
			browse_movies_oscars,
			browse_movies_theaters,
			browse_movies_latest,
			browse_movies_fav,
		)
		ret = dialog.select('Browse Genesis', ['Genres', 'Years', 'People', 'Certificates', 'Featured', 'People Watching', 'Most Popular', 'Most Voted', 'Box Office', 'Oscar Winners', 'In Theaters', 'Latest Movies', 'Favourites'])
		if ret > -1:
			funcs[ret]()
	
def browse_tv():
		dialog = xbmcgui.Dialog()
		funcs = (
			browse_tv_genres,
			browse_tv_years,
			browse_tv_networks,
			browse_tv_watching,
			browse_tv_popular,
			browse_tv_today,
			browse_tv_returning,
			browse_tv_new,
			browse_tv_rated,
			browse_tv_voted,
			browse_tv_calendars,
			browse_tv_latesteps,
			browse_tv_faveps,
			browse_tv_fav,
		)
		ret = dialog.select('Browse Genesis', ['Genres', 'Years', 'Networks', 'People Watching', 'Most Popular', 'Airing Today', 'Returning TV Shows', 'New TV Shows', 'Highly Rated', 'Most Voted', 'TV Calendar', 'Latest Episodes', 'Favourite Episodes', 'Favourites'])
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
			browse,
			import_options
		)
		ret = dialog.select('Genesis Library Options', ['Genesis Settings', 'Toggle Autoplay', 'Clear Cache', 'Clear Sources', 'Update Folders', 'Search Genesis', 'Browse Genesis', 'Library Import Options...'])
		if ret > -1:
			funcs[ret]()