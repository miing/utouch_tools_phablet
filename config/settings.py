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


import platform
import logging


#####################
# Base Dependencies #
#####################
SYSTEM_NAME = platform.system()
MACHINE_TYPE = platform.machine()
if SYSTEM_NAME == 'Linux':
	# Linux based platforms
	DISTRO_NAME = (platform.linux_distribution())[0]
	if DISTRO_NAME in ('Debian', 'Ubuntu'):
		# Debian based distros
		LPKG = "dpkg -l %s 2> /dev/null | grep '^ii' | wc -l"
		IPKG = "sudo apt-get -y install %s"
		BASE_DEPENDENCIES = [
			'git-core',
			'bzr',
			'curl',
			'build-essential',
			'gnupg',
			'flex', 
			'bison',
			'gperf',
			'zip',
			'libc6-dev',
			'x11proto-core-dev',
			'libgl1-mesa-dev',
			'g++-multilib',
			'mingw32',
			'tofrodos',
			'python-markdown',
			'libxml2-utils',
			'xsltproc',
			'schedtool'
		]
		if MACHINE_TYPE in ('i686', 'i586', 'i486', 'i386'):
			BASE_DEPENDENCIES += [
				'libncurses5-dev',
				'libx11-dev',
				'libreadline6-dev',
				'libgl1-mesa-glx',
				'zlib1g-dev'
			]
		elif MACHINE_TYPE in ('x86_64'):
			BASE_DEPENDENCIES += [
				'libncurses5-dev:i386',
				'libx11-dev:i386',
				'libreadline6-dev:i386',
				'libgl1-mesa-glx:i386',
				'zlib1g-dev:i386'
			]
			try:
				import argparse
			except ImportError:
				BASE_DEPENDENCIES += [
					'python-argparse'
				]
			try:
				import requests
			except ImportError:
				BASE_DEPENDENCIES += [
					'python-requests'
				]
		else:
			BASE_DEPENDENCIES = None
	elif DISTRO_NAME in ('SuSE', 'Fedora', 'Centos', 'Redhat'):
		# RPM based distros
		LPKG = None
		IPKG = None
		BASE_DEPENDENCIES = None
	else:
		# Not supported distros
		LPKG = None
		IPKG = None
		BASE_DEPENDENCIES = None
elif SYSTEM_NAME == 'MacOS':
	# MacOS platforms
	LPKG = None
	IPKG = None
	BASE_DEPENDENCIES = None
elif SYSTEM_NAME == 'Windows':
	# Windows platforms
	LPKG = None
	IPKG = None
	BASE_DEPENDENCIES = None
else:
	# Unknown platforms
	LPKG = None
	IPKG = None
	BASE_DEPENDENCIES = None


#####################
# Repositories      #
#####################
# Depending on Cyanogenmod
CYANOGENMOD_REPO_INIT = 'git://phablet.ubuntu.com/CyanogenMod/android.git'
CYANOGENMOD_REPO_BRANCH = 'phablet-10.1'

# Depending on Ubuntu
UBUNTU_ANDROID_PATH = 'ubuntu'
UBUNTU_ANDROID_REPOS = {
    'ubuntu/hybris': 'lp:phablet-extras/libhybris',
    'ubuntu/platform-api': 'lp:platform-api',
}
UBUNTU_TOUCH_REPOS = {
	'xxxx/xxxx': 'lp:xxxx/xxxx',
}


#####################
# Devices           #
#####################
# All target devices for Ubuntu Touch available for now
UTOUCH_VALID_DEVICES = (
	'mako',
	'maguro',
	'manta',
	'grouper',
)
UTOUCH_VALIDATE_DEVICE = True

#####################
# Images            #
#####################
# Locations to download from
UTOUCH_IMAGES_DIR = 'images'
UTOUCH_BASE_URI = 'http://cdimage.ubuntu.com'
UTOUCH_IMAGES_URI = '%s/ubuntu-touch-preview/' % UTOUCH_BASE_URI
UTOUCH_DOWNLOAD_URI = \
	'%s/ubuntu-touch-preview/daily-preinstalled/current' % UTOUCH_BASE_URI

# Images to flash into target device
UTOUCH_IMAGE = 'quantal-preinstalled-phablet-armhf.zip'
UTOUCH_DEVICE_FILE = 'quantal-preinstalled-armel+%s.zip'
UTOUCH_SYSTEM_IMG = 'quantal-preinstalled-system-armel+%s.img'
UTOUCH_BOOT_IMG = 'quantal-preinstalled-boot-armel+%s.img'
UTOUCH_RECOVERY_IMG = 'quantal-preinstalled-recovery-armel+%s.img'
UTOUCH_RECOVERY_SCRIPT_TEMPLATE = '''boot-recovery
--update_package={0}/{1}
--user_data_update_package={0}/{2}
reboot
'''


#####################
# Legal             #
#####################
UTOUCH_LEGAL_ACCEPTED_PATH = '~/.phablet_accepted'
UTOUCH_LEGAL_NOTICE = '''"Touch Developer Preview for Ubuntu" is released for free
non-commercial use. It is provided without warranty, even the implied
warranty of merchantability, satisfaction or fitness for a particular
use. See the licence included with each program for details.

Some licences may grant additional rights; this notice shall not limit
your rights under each program's licence. Licences for each program
are available in the usr/share/doc directory. Source code for Ubuntu
can be downloaded from archive.ubuntu.com. Ubuntu, the Ubuntu logo
and Canonical are registered trademarks of Canonical Ltd. All other
trademarks are the property of their respective owners.

"Touch Preview for Ubuntu" is released for limited use due to the
inclusion of binary hardware support files. The original components
and licenses can be found at:
https://developers.google.com/android/nexus/drivers.
'''


#####################
# Logging           #
#####################
LOG_NAME = 'phablet'
logging.basicConfig(level=logging.DEBUG)
LOG = logging.getLogger(LOG_NAME)
