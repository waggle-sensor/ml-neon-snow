#!/bin/bash

echo "imageUrl,externalId"
while read url < "$1"; do
    echo "$url,$(basename $url)"
done
