#!/usr/bin/env python3
import datetime
import re
from urllib.request import urlopen

image_re = re.compile(r"/data/archive/.*?\.jpg")

def get_images(site, year, month, day):
    with urlopen(f"https://phenocam.sr.unh.edu/webcam/browse/{site}/{year:04}/{month:02}/{day:02}/") as f:
        text = f.read().decode()
    for url in image_re.findall(text):
        print("https://phenocam.sr.unh.edu"+url)

def daterange(start, end):
    date = start
    while date < end:
        yield date
        date += datetime.timedelta(days=1)

sites = [
    "NEON.D01.BART.DP1.00042",
    "NEON.D10.CPER.DP1.00042",
    "NEON.D09.WOOD.DP1.00042",
    "NEON.D05.TREE.DP1.00042",
    "NEON.D05.UNDE.DP1.00042",
]

for site in sites:
    for date in daterange(datetime.date(2020, 11, 1), datetime.date(2021, 2, 1)):
        get_images(site, date.year, date.month, date.day)
