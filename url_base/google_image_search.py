# Code attribution: https://gist.github.com/genekogan/ebd77196e4bf0705db51f86431099e57#gistcomment-2267063

import argparse
import json
import logging
import os
import uuid
import sys
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
from .url_common import get_image_name


REQUEST_HEADER = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36"
}


def configure_logging(level=logging.ERROR):
    logger = logging.getLogger()
    logger.setLevel(level)
    handler = logging.StreamHandler()
    handler.setFormatter(
        logging.Formatter("[%(asctime)s %(levelname)s %(module)s]: %(message)s")
    )
    logger.addHandler(handler)
    return logger


logger = configure_logging()


def _get_soup(url, header):
    response = urlopen(Request(url, headers=header))
    return BeautifulSoup(response, "html.parser")


def _get_query_url(query):
    return "https://www.google.co.in/search?q=%s&source=lnms&tbm=isch" % query


def _extract_images_from_soup(soup):
    image_elements = soup.find_all("div", {"class": "rg_meta"})
    metadata_dicts = [json.loads(e.text) for e in image_elements]
    link_type_records = [(d["ou"], d["ity"]) for d in metadata_dicts]
    return link_type_records


def _get_raw_image(url):
    req = Request(url, headers=REQUEST_HEADER)
    resp = urlopen(req)
    return resp.read()


def _save_image(raw_image, image_name, save_directory):
    os.makedirs(save_directory, exist_ok=True)
    save_path = os.path.join(save_directory, image_name)
    with open(save_path, "wb+") as image_file:
        image_file.write(raw_image)


def extract_image_links(query, num_images):
    """Extract the image url and the file type based on a query.
    
    Args:
        query (str): Text to search.
        num_images (int): Max number of image links to return.
    
    Returns:
        list of tuples: List of tuples of (image_url, image_type)

    Examples:
        >>> r = extract_image_links("Batman", 1)
        >>> r[0] # doctest: +ELLIPSIS
        ('http...jpg', 'jpg')
    """
    query = "+".join(query.split())
    url = _get_query_url(query)
    logger.info("Souping")
    soup = _get_soup(url, REQUEST_HEADER)
    logger.info("Extracting image urls")
    link_type_records = _extract_images_from_soup(soup)
    return link_type_records[:num_images]


def download_images_to_dir(images, save_directory):
    """Download a set of image urls to disk
    
    Args:
        images (list of tuples): List of images urls and image types.
        save_directory (str): Folder.

    Examples:
        >>> from pybase.url_base.url_common import get_image_name
        >>> with TemporaryDirectory() as td:
        ...     r = extract_image_links("Batman", 1)
        ...     download_images_to_dir(r, td)
        ...     filename = get_image_name(r[0][0])
        ...     os.path.exists(os.path.join(td, filename))
        True
    """
    num_images = len(images)
    for i, (url, image_type) in enumerate(images):
        try:
            logger.info("Making request (%d/%d): %s", i, num_images, url)
            raw_image = _get_raw_image(url)
            image_name = get_image_name(url)
            _save_image(raw_image, image_name, save_directory)
        except Exception as e:
            logger.exception(e)


def run(query, save_directory, num_images=100):
    logger.info("Extracting image links")
    images = extract_image_links(query, num_images)
    logger.info("Downloading images")
    download_images_to_dir(images, save_directory)
    logger.info("Finished")


def main():
    parser = argparse.ArgumentParser(description="Scrape Google images")
    parser.add_argument(
        "-s", "--search", default="bananas", type=str, help="search term"
    )
    parser.add_argument(
        "-n", "--num_images", default=1, type=int, help="num images to save"
    )
    parser.add_argument(
        "-d", "--directory", default=".", type=str, help="save directory"
    )
    args = parser.parse_args()
    run(args.search, args.directory, args.num_images)


if __name__ == "__main__":
    main()
