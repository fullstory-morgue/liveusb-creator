#!/usr/bin/env python
from distutils.core import setup

def install(**args):
    args['package_dir'] = {'liveusb-creator' : '.'}
    args['packages'] = ['liveusb-creator', 
                          'liveusb-creator.liveusb', 
                          'liveusb-creator.liveusb.urlgrabber']
    return setup(**args)

if __name__ == '__main__' :
    install()
