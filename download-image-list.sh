#!/bin/bash

if [ -z "$1" ]; then
    echo "usage: $0 url-list-file"
    exit 1
fi

wget -r -N -i "$1"
