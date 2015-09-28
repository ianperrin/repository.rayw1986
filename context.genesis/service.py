
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

import xbmcaddon
import xbmcvfs
import os


def read(filename):
    f = xbmcvfs.File(filename, 'r')
    content = f.read()
    f.close()
    return content


def main():
    sf      = 'plugin.program.super.favourites'
    cm      = 'context.genesis'

    sf_path = xbmcaddon.Addon(sf).getAddonInfo('profile')
    cm_path = xbmcaddon.Addon(cm).getAddonInfo('path')

    plugin   = os.path.join(sf_path, 'Plugins')
    resource = os.path.join(cm_path, 'resources')

    src     = os.path.join(resource, 'Genesis.py')
    dst     = os.path.join(plugin,   'Genesis.py')

    try:    xbmcvfs.mkdirs(plugin)
    except: pass

    if read(src) == read(dst):
        return

    xbmcvfs.copy(src, dst)


try:    
    main()
except Exception, e:
    print 'Genesis context menu - error copying SF script %s' % str(e)
