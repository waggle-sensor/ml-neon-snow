# NEON Image Data Plugins, Tools and Examples

## Tasks

### Scraping Image URLs

You can use the `get-neon-image-urls.py` tool to scrape the list of image URLs within in a time range from a list of NEON sites:

```bash
./get-neon-image-urls.py \
    2021-01-01 \
    2021-01-03 \
    NEON.D01.BART.DP1.00042 \
    NEON.D10.CPER.DP1.00042 \
    NEON.D09.WOOD.DP1.00042 > urls.txt
```

```bash
$ cat urls.txt
https://phenocam.sr.unh.edu/data/archive/NEON.D01.BART.DP1.00042/2021/01/NEON.D01.BART.DP1.00042_2021_01_01_061505.jpg
https://phenocam.sr.unh.edu/data/archive/NEON.D01.BART.DP1.00042/2021/01/NEON.D01.BART.DP1.00042_2021_01_01_063006.jpg
https://phenocam.sr.unh.edu/data/archive/NEON.D01.BART.DP1.00042/2021/01/NEON.D01.BART.DP1.00042_2021_01_01_064506.jpg
...
```

### Downloading Image List Locally (Optional)

Once you create an image list, you can quickly download these locally using the `download-image-list.sh` tool.

```bash
./download-image-list.sh urls.txt
```

This will download and save the images into a `phenocam.sr.unh.edu` directory with the same structure as their site.

```bash
$ find phenocam.sr.unh.edu
phenocam.sr.unh.edu
phenocam.sr.unh.edu/data
phenocam.sr.unh.edu/data/archive
phenocam.sr.unh.edu/data/archive/NEON.D05.TREE.DP1.00042
phenocam.sr.unh.edu/data/archive/NEON.D05.TREE.DP1.00042/2021
phenocam.sr.unh.edu/data/archive/NEON.D05.TREE.DP1.00042/2021/01
phenocam.sr.unh.edu/data/archive/NEON.D05.TREE.DP1.00042/2021/01/NEON.D05.TREE.DP1.00042_2021_01_07_124505.jpg
phenocam.sr.unh.edu/data/archive/NEON.D05.TREE.DP1.00042/2021/01/NEON.D05.TREE.DP1.00042_2021_01_18_121506.jpg
phenocam.sr.unh.edu/data/archive/NEON.D05.TREE.DP1.00042/2021/01/NEON.D05.TREE.DP1.00042_2021_01_20_123006.jpg
...
```

### Creating Labelbox Import CSV

Once you create an image list, we can generate a CSV which can be imported into Labelbox using the `build-labelbox-import-csv.sh` tool.

```bash
./build-labelbox-import-csv.sh urls.txt > my-dataset.csv
```

This file can now be uploaded to Labelbox by:

1. Login to Labelbox and go to Datasets -> Add dataset.
2. Upload CSV file.
3. Set "Column to label" as imageUrl and "External ID" to externalId.
4. Start upload.
