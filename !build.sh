#!/bin/sh
rsync -a --progress --delete --copy-links source/pack/ build
rsync -a --delete ./build/ ../../22/pixel-consistency
