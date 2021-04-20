#!/bin/bash
if [ $# -eq 0 ]
  then
    echo "PnkTunnel: Secure tunnel to localhost via LBXS"
    echo "----------------------------------------------"
    echo "          This is the client script           "
    echo "----------------------------------------------"
    echo "Usage: pnktunnel PORT SUBDOMAIN"
    echo
    exit
fi

ssh -p 8022 -t -R 9001:localhost:$1 leo@daintree.lbxs.dev pnktunnel $2 9001
