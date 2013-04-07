##########################################################################
#
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
import sys
import subprocess


def _compare_version(base, current):
	'''Compare between versions of python'''
	def _normalize(v):
		return [int(x) for x in re.sub(r'(\.0+)*$','', v).split(".")]
	return cmp(_normalize(base), _normalize(current))


def _get_version():
	'''Get the current version of python'''
	return '%d.%d' % sys.version_info[:2]


CalledProcessError = subprocess.CalledProcessError


def call(*popenargs, **kwargs):
	'''Run command with arguments and wait for completing'''
	subprocess.call(*popenargs, **kwargs)


def check_call(*popenargs, **kwargs):
	'''Run command with arguments and wait for completing.
	
	If the exit code was non-zero it raises a CalledProcessError.
	'''
	subprocess.check_call(*popenargs, **kwargs)


def check_output(*popenargs, **kwargs):
	'''Run command with arguments and return its output as a byte string.
	
	If the exit code was non-zero it raises a CalledProcessError.
	'''
	base_version = '2.6'
	curver = _get_version()
	compret = _compare_version(base_version, curver)
	if compret == '1':
		# check_output supported only for 2.7 or later
		return subprocess.check_output(*popenargs, **kwargs)
	else:
		process = subprocess.Popen(stdout=subprocess.PIPE, *popenargs, **kwargs)
		output, unused_err = process.communicate()
		retcode = process.poll()
		if retcode:
			cmd = kwargs.get("args")
			if cmd is None:
				cmd = popenargs[0]
			raise subprocess.CalledProcessError(retcode, cmd, output=output)
		return output
