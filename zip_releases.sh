#!/bin/sh

python3 build.py

# cat VERSION_INFO.txt
pack_version=$(cat VERSION_INFO.txt | awk '{print $1}')
game_version=$(cat VERSION_INFO.txt | awk '{print $2}')

cd build/pack

path="../../releases/pixel-consistency-${pack_version}-${game_version}.zip"

if [ -e ${path} ]; then
    echo "File ${path} already exists"
else
    zip -r ${path} assets pack.png pack.mcmeta LICENSE.txt -x "*.kra~" -x "*.png~"
fi
