#!/bin/sh
rm build/* -r

mkdir build
cp source/pack.png build
cp source/pack.mcmeta build
cp source/LICENSE.txt build
cp source/assets build -r

#cd "$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
# rm releases/*
#cp pack_template.mcmeta pack.mcmeta
#sed -i sed -i '' "s/%PACK_FORMAT%/7/g" pack.mcmeta

# set -x

# cd build/assets
# pwd
# recursively_cd
# find build/assets -maxdepth 1 -type f | while read file; do cp -f $(readlink $file) $file; done

rsync -a --progress --delete ./build/ ../../22/pixel-consistency

