# -*- coding: utf-8 -*-

"""Get Lat-Lng

Be sure to symlink this program to your /usr/local/bin/get-latlng

Usage:
  get-latlng ship new <name>...
  get-latlng ship <name> move <x> <y> [--speed=<kn>]
  get-latlng ship shoot <x> <y>
  get-latlng mine (set|remove) <x> <y> [--moored | --drifting]
  get-latlng my <latlng>
  get-latlng (-h | --help)
  get-latlng --version

Options:
  -h --help     Show this screen.
  --version     Show version.
  --speed=<kn>  Speed in knots [default: 10].
  --moored      Moored (anchored) mine.
  --drifting    Drifting mine.

"""
from docopt import docopt
import requests
#from pprint import pprint

#import float

def geocode(address):
    output_type = 'json'
    #urllib.urlencode({'output': 'csv','q': address})))[0].split(',')[2:]])
    payload = {
        'address' : address,
        'api_key' : 'AIzaSyB2Zm5HJ1SaB7ZD36sHjsitnwSO2b1zJfs',
    }
    target_url = "https://maps.googleapis.com/maps/api/geocode/%s" % ( output_type, )
    #pprint(payload)

    #return tuple([float(s) for s in list(requests.get('http://maps.google.com/maps/geo'))])
    r = requests.get(target_url, params=payload)
    #return r.text
    return list(r)

if __name__ == "__main__":
    arguments = docopt(__doc__, version='Get Lat-Lng')
    #print(arguments)
    if arguments['my']:
        ll = arguments['<latlng>']
        print geocode(ll)
