#!/usr/bin/env python
from distutils.core import setup

def install(**kwargs):
    kwargs['name'] = 'liveusb-creator'
    kwargs['description']  = 'installing live operating systems on to USB flash drives'
    kwargs['version']      = '0.0.11'
    kwargs['author']       = 'Horst Tritremmel'
    kwargs['author_email'] = 'hjt@sidux.com'
    kwargs['url']          = 'http://sidux.com'
    kwargs['license']      = 'GPLv2'

    ''' dirs with .py files '''
    kwargs['package_dir']  = {'liveusb-creator' : '.'}
    kwargs['packages'] = ['liveusb-creator', 
                          'liveusb-creator.liveusb', 
                          'liveusb-creator.liveusb.urlgrabber']
    return setup(**kwargs)

if __name__ == '__main__' :
    install()
