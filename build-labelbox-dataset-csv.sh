#!/bin/bash

echo "imageUrl,externalId"
find phenocam.sr.unh.edu -name "*.jpg" | while read line; do
    echo "https://$line,$(basename $line)"
done
