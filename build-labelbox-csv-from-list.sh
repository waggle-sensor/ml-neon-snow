#!/bin/bash

if [ -z "$1" ]; then
    echo "usage: $0 url-list-file"
    exit 1
fi

echo "imageUrl,externalId"
while read url < "$1"; do
    echo "$url,$(basename $url)"
done
