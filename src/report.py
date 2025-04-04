import logging
import argparse
import json
import pathlib
import requests
from . import libutil

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


def get_session():
    key = 'session'
    if key not in resources:
        resources[key] = requests.Session()
    return resources[key]


def get_json_file( fn ):
    if not fn:
        raise UserWarning( 'missing json filename' )
    key = f'{fn}.json'
    if key not in resources:
        resources[key] = pathlib.Path( key )
    return resources[key]


def get_RP_groups():
    key = 'rp_groups'
    if key not in resources:
        fn = get_json_file( key )
        update_needed = True
        if fn.exists():
            # check age
            args = get_args()
            max_age_secs = args.cache_timeout * 86400
            if fn.stat().st_mtime < max_age_secs:
                update_needed = False
        if update_needed:
            # get data from api
            server = 'operations-api.access-ci.org'
            path = 'wh2/cider/v1/access-active-groups/'
            params = { 'format': 'json' }
            url = f'https://{server}/{path}'
            response = api_get( url, params )
            data = response.json()
            # write the new data to file
            with fn.open( mode='w' ) as fh:
                json.dump( data, fh )
            # save the new data directly since we already have it
            resources[key] = data
        else:
            # Read data from cache file
            with fn.open() as fh:
                json_data = json.load( fh )
                resources[key] = json_data
    return resources[key]


def api_go( method, url, **kw ):
    logging.debug( f'{method} {url}, {pprint.pformat(kw)}' )
    s = get_session()
    # to use personal access token, must disable netrc function in requests
    # s.trust_env = False
    # s.headers = {
    #     "Accept": "application/json",
    #     "Content-Type": "application/json",
    #     }
    r = s.request( method, url, **kw )
    logging.debug( f'RETURN CODE .. {r}' )
    # logging.debug( f'RETURN HEADERS .. {r.headers}' )
    r.raise_for_status()
    return r


def api_get( url, params=None ):
    return api_go( method='GET', url=url, params=params )


def run():
    args = get_args()
    # pprint.pprint( args )
    rp_groups = get_RP_groups()
    pprint.pprint( rp_groups )


if __name__ == '__main__':
    args = get_args()
    libutil.setup_logging( args )
    run()
