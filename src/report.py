import json
import pathlib
import requests

import pprint

# Module level resources
resources = {}

def get_args( params=None ):
    key = 'args'
    if key not in resources:
        constructor_args = {
            'formatter_class': argparse.RawDescriptionHelpFormatter,
            'description': 'Software modules per resourceid or groupid',
        }
        parser = argparse.ArgumentParser( **constructor_args )
        parser.add_argument( '-d', '--debug', action='store_true' )
        parser.add_argument( '-v', '--verbose', action='store_true' )
        parser.add_argument( '-f', '--force', action='store_true',
            help='Force update cache from web API')
        parser.add_argument( '-t', '--cache_timeout',
            type=int,
            default=1,
            help='Max age, in days, to use cached data (default: %(default)s)')
        args = parser.parse_args( params )
        resources[key] = args
    return resources[key]


def run():
    args = get_args()
    pprint.pprint( args )

if __name_ == '__main__':
    get_args()
    run()
