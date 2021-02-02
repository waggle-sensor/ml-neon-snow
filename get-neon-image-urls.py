#!/usr/bin/env python3
import argparse
from datetime import datetime, timedelta
import re
from urllib.request import urlopen


def get_image_urls(site, year, month, day):
    with urlopen(f"https://phenocam.sr.unh.edu/webcam/browse/{site}/{year:04}/{month:02}/{day:02}/") as f:
        text = f.read().decode()
    for url in re.findall(r"/data/archive/.*?\.jpg", text):
        yield "https://phenocam.sr.unh.edu"+url


def daterange(start, end):
    date = start
    while date < end:
        yield date
        date += timedelta(days=1)


def parsedate(s):
    return datetime.strptime(s, "%Y-%m-%d")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("start_date", type=parsedate, help="start date (YYYY-MM-DD)")
    parser.add_argument("end_date", type=parsedate, help="end date (YYYY-MM-DD)")
    parser.add_argument("sites", nargs="*", help="list of sites")
    args = parser.parse_args()

    for site in args.sites:
        for date in daterange(args.start_date, args.end_date):
            for url in get_image_urls(site, date.year, date.month, date.day):
                print(url, flush=True)


if __name__ == "__main__":
    main()
