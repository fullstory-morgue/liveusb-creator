releases = (
    {
        'name': 'sidux-2008-02-erebos-pre1-kde-lite (i686)',
        'url': 'http://debian.tu-bs.de/project/sidux/preview/sidux-2008-02-erebos-pre1-kde-lite-i386-200806032235.iso',
    },
    {
        'name': 'sidux-2008-02-erebos-pre1-kde-lite (amd64)',
        'url': 'http://debian.tu-bs.de/project/sidux/preview/sidux-2008-02-erebos-pre1-kde-lite-amd64-200806032247.iso',
    },
    {
        'name': 'sidux-2008-01-nyx-kde-lite (i686)',
        'url': 'http://debian.tu-bs.de/project/sidux/release/sidux-2008-01-nyx-kde-lite-i386-200804112335.iso',
    },
    {
        'name': 'sidux-2008-01-nyx-kde-lite (amd64)',
        'url': 'http://debian.tu-bs.de/project/sidux/release/sidux-2008-01-nyx-kde-full-i386-amd64-200804120127.iso',
    },
    {
        'name': 'sidux-2008-01-nyx-kde-full (i686/amd64)',
        'url': 'http://debian.tu-bs.de/project/sidux/release/sidux-2008-01-nyx-kde-full-i386-amd64-200804120127.iso',
    },
)


'''
from urlgrabber import *
url = "http://debian.tu-bs.de/project/sidux/release"
fo = urlopen(url)
data = fo.read()
for i in data.split('"'):
    if i.endswith('iso'):
        print i
'''