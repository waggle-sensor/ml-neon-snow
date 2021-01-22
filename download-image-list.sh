#!/bin/bash

if [ -z "$*" ]; then
    echo "usage: $0 url-list-files ..."
    exit 1
fi

for file in $*; do
    wget -r -N -i "$file"
done
