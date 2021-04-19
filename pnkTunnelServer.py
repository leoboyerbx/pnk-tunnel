#!/usr/bin/env python3

import sys
import json
import time
from urllib import request


if __name__ == '__main__':

    host = sys.argv[1] + '.tn.leoboyer.dev'
    port = sys.argv[2]
    tunnel_id = host + '-' + port
    
    print('Creating tunnel to your localhost')

    caddy_add_route_request = {
        "@id": tunnel_id,
        "match": [{
            "host": [host],
        }],
        "handle": [{
            "handler": "reverse_proxy",
            "upstreams":[{
                "dial": ':' + port
            }]
        }]
    }

    body = json.dumps(caddy_add_route_request).encode('utf-8')
    headers = {
        'Content-Type': 'application/json'
    }
    create_url = 'http://127.0.0.1:20201/config/apps/http/servers/srv0/routes'
    req = request.Request(method='POST', url=create_url, headers=headers)
    request.urlopen(req, body)

    print("Tunnel created successfully.")
    print("Visit https://" + host + "/ to access your local server")

    while True:
        try:
            time.sleep(1)
        except KeyboardInterrupt:

            print("Cleaning up tunnel")
            delete_url = 'http://127.0.0.1:20201/id/' + tunnel_id
            req = request.Request(method='DELETE', url=delete_url)
            request.urlopen(req)
            break