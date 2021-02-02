# NEON Image Data Plugins, Tools and Examples

## Tools

```bash
./get-neon-image-urls.py \
    2021-01-01 \
    2021-01-03 \
    NEON.D01.BART.DP1.00042 \
    NEON.D10.CPER.DP1.00042 \
    NEON.D09.WOOD.DP1.00042 > urls.txt
```

This will scrape a list of all image URLs between the start and end dates from each site of the form:

```bash
$ cat urls.txt
https://phenocam.sr.unh.edu/data/archive/NEON.D01.BART.DP1.00042/2021/01/NEON.D01.BART.DP1.00042_2021_01_01_061505.jpg
https://phenocam.sr.unh.edu/data/archive/NEON.D01.BART.DP1.00042/2021/01/NEON.D01.BART.DP1.00042_2021_01_01_063006.jpg
https://phenocam.sr.unh.edu/data/archive/NEON.D01.BART.DP1.00042/2021/01/NEON.D01.BART.DP1.00042_2021_01_01_064506.jpg
...
```
