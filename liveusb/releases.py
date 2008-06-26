releases = (
    {
        'name': 'sidux-2008-02-kde-lite-i386',
        'url': 'http://debian.tu-bs.de/project/sidux/release/sidux-2008-02-erebos-kde-lite-i386-200806252044.iso',
    },
    {
        'name': 'sidux-2008-02-kde-lite-amd64',
        'url': 'http://debian.tu-bs.de/project/sidux/release/sidux-2008-02-erebos-kde-lite-amd64-200806252050.iso',
    },
    {
        'name': 'sidux-2008-02-kde-full-i386-amd64',
        'url': 'http://debian.tu-bs.de/project/sidux/release/sidux-2008-02-erebos-kde-full-i386-amd64-200806251839.iso',
    },
    {
        'name': 'sidux-2008-02-xfce-i386',
        'url': 'http://debian.tu-bs.de/project/sidux/release/sidux-2008-02-erebos-xfce-i386-200806252100.iso',
    },
    {
        'name': 'sidux-2008-02-xfce-amd64',
        'url': 'http://debian.tu-bs.de/project/sidux/release/sidux-2008-02-erebos-xfce-amd64-200806252108.iso',
    },
)

'''

from urlgrabber import *

url = "http://debian.tu-bs.de/project/sidux/release"

urlret  = "ok"
release = ""
try:
    fo = urlopen(url)
except:
    print '%s not found!' % url
    urlret = "no"
    releases = (
        {
            'name': 'url not found)',
            'url': 'http://debian.tu-bs.de/project/sidux/release',
        }
    )

if urlret == 'ok':
    data = fo.read()
    for i in data.split('"'):
        if i.endswith('iso'):
            release = "%s{'url': '%s/%s', 'name': '%s'}, " % (release, url, i, i)


releases = (release)

print releases
'''
