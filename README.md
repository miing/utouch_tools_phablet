# Phablet for Ubuntu Touch

Provides initializing a build environment, downloading the source tree,
setting up a target device to build, flashing images for Ubuntu Touch.

***

## Initializing a build environment

To setup a build environment before building Ubuntu Touch, the first thing
you need is just run the following command:

	./starter -b /path/to/your/target/directory
     

## Downloading the source tree

The whole source tree for Ubuntu Touch is generally divided into two parts
to some extent, Android and Ubuntu. According to this aspect, therefore, there
are two options provided to download the source tree for Android and Ubuntu,
separately, as described below:

	./starter -a -j 4 /path/to/your/target/directory # for Android
	
	./starter -u /path/to/your/target/directory # for Ubuntu Touch
	
For the two parts of sources, however, all you need to do is just run the command:

	./starter -a -j 4 -u /path/to/your/target/directory # for Android and Ubuntu Touch

Note that for the source for Ubuntu Touch, for now, only get the android-side
Ubuntu Touch sources, instead of the whole parts for it.


## Setting up a target device

Pretty straightforward, for setting up a target device to build, so only follow 
the following:

	./starter -d TARGET_DEVICE /path/to/your/target/directory
	
Note that there are only four target devices supported out there as of the time 
of writing, covering *maguro*, *mako*, *manta*, *grouper*.

For more information on what devices are being supported, take a look at [Devices](https://wiki.ubuntu.com/Touch/Devices).


## Putting it all together

For the above three steps, as a matter of fact, it is most likely to place them into
an all-in-one step like this:

	./starter -b -a -j 4 -u /path/to/your/target/directory


## Flash images

TODO


## References

 - http://source.android.com/source/index.html
 - https://wiki.ubuntu.com/Touch/Porting
 
 
***
 
# Author

Samuel Mi <samuel.miing@gmail.com> from Miing.org
