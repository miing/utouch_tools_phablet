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


import os

from config import settings
from utils.subproc import call, check_call


def download(uri, target):
	'''Downloads an artifact into target.'''
	settings.LOG.info('Downloading %s' % uri)
    
	if uri.startswith(settings.UTOUCH_BASE_URI):
		check_call(['wget', '-c', uri, '-O', target])
	else:
	check_call(['curl', '-C', '-', uri, '-o', target])


class DownloadManager(object):
	'''Interface to downloading.'''
	def __init__(self, base_uri, images_dir, artifact_list, offline=False):
		if not os.path.isdir(images_dir):
			raise RuntimeError('Directory %s does not exist or is not a '
                               'direcotry' % images_dir)
		self._base_uri = base_uri
		self._images_dir = images_dir
		self._artifact_list = artifact_list
		self._targets = {}
		self._files = {}
		self._offline = offline

	@property
	def files(self):
		return self._files

	def download(self):
		'''Downloads arget_uri.'''
		for artifact in self._artifact_list:
			if not artifact:
				continue
			target = os.path.join(self._download_dir, '%s' % (artifact))
			self._files[artifact] = target
			if self._offline:
				continue
			uri = '%s/%s' % (self._base_uri, artifact)
			md5file = '%s.md5sum' % target
			md5uri = '%s.md5sum' % uri
			if self.is_downloaded(target, md5file):
				continue
			download(uri, target)
			download(md5uri, md5file)
			self.validate(md5file)
			if artifact.endswith('.gz'):
				call(['gunzip', target])
				self._files[artifact] = os.path.splitext(target)[0]

	def is_downloaded(self, target, md5file):
		'''Verify if a download is complete by validating againts it's hash.'''
		try:
			self.validate(md5file)
		except CalledProcessError:
			return False
		else:
			return True

	def validate(self, artifact):
		'''Validates downloaded files against md5sum.'''
		check_call(['md5sum', '-c', '%s' % artifact], 
        		   cwd=self._images_dir)
