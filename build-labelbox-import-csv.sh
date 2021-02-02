#!/bin/bash

if [ -z "$*" ]; then
    echo "usage: $0 url-list-files ..."
    exit 1
fi

echo "imageUrl,externalId"

for file in $*; do
    while read url; do
        echo "$url,$(basename $url)"
    done < "$file"
done
