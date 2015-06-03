# -*- coding: utf-8 -*-

"""Get Lat-Lng

Be sure to symlink this program to your /usr/local/bin/get-latlng

Usage:
  get-latlng my <latlng>
  get-latlng (-h | --help)
  get-latlng --version

Options:
  -h --help     Show this screen.
  --version     Show version.

"""
from docopt import docopt
import requests
from keys import *


def geocode(address):
    output_type = 'json'
    payload = {
        'address': address,
        'api_key': k,
    }
    target_url = "https://maps.googleapis.com/maps/api/geocode/%s" % (
        output_type, )
    r = requests.get(target_url, params=payload)
    return list(r)

if __name__ == "__main__":
    arguments = docopt(__doc__, version='Get Lat-Lng')
    if arguments['my']:
        ll = arguments['<latlng>']
        print geocode(ll)
