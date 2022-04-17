#!/bin/bash

set -e

if [ $# -lt 2 ]; then
    echo "USAGE: sh Display_img.sh IMG_LIST PORT"
    exit 1
fi

python3 ./convert_list_to_xml.py -i $1

if [ $? != 0 ]; then
    echo "Convertion Failed!"
    eixt 2
else
    echo "Convertion Finished!"
fi

python3 -m http.server $2 --bind 0.0.0.0
