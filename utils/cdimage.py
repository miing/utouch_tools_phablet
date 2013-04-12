##########################################################################
#
# Copyright (c) 2013 Canonical Ltd.
# Copyright (c) 2013 Miing.org <samuel.miing@gmail.com>
# 
# This program is free software: you can redistribute it and/or modify 
# it under the terms of the the GNU General Public License version 3, 
# as published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranties of
# MERCHANTABILITY, SATISFACTORY QUALITY or FITNESS FOR A PARTICULAR
# PURPOSE.  See the applicable version of the GNU General Public
# License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
##########################################################################


import re
import requests

from config import settings


def _get_elements(uri):
    '''Scraps cdimage and returns a list of relevant links as elements.'''
    request = requests.get(uri).content
    html_elements = filter(
        lambda x: '<li><a href=' in x and
        'Parent Directory' not in x and
        'daily' not in x,
        request.split('\n'))
    elements_inter = [re.sub('<[^>]*>', '', i) for i in html_elements]
    elements = [i.strip().strip('/') for i in elements_inter]
    return elements


def _get_releases(uri):
    releases = [{'release': i, 'uri': uri + i} for i in _get_elements(uri)]
    return releases


def _get_revisions(uri):
    return _get_elements(uri)


def get_available_revisions(cdimage_uri):
	'''Returns all the releases available for a given cdimage project.'''
	settings.LOG.info('Retriving revisions available from %s' % cdimage_uri)
	releases = _get_releases(cdimage_uri)
	for release in releases:
		release['revisions'] = _get_revisions(release['uri'])
	return releases


def display_revisions(revisions):
    for series in revisions:
        settings.LOG.info('Available releases:')
        if series.has_key('revisions'):
            for rev in series['revisions']:
                print '\t%s/%s' % (series['release'], rev)
        else:
            settings.LOG.warning('No releases for %s available' % rev['release']) 
