#!/bin/bash

cd /home/liikt/discord/Ooyodo/

PULL=`git pull`

if [[ ${PULL} != 'Already up-to-date.' ]]; then
    ./kill.sh || true
    python3 ooyodo.py &
    echo -e '\nRestarted Ooyodo\n----------------------------------\n' >> log/ooyolog
    echo 'restarted'
fi
