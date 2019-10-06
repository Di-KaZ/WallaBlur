#!/bin/python3
import sys
import os
import argparse
import logging
from pathlib import Path
import cache
import draw

def limits_refresh(arg):
    try:
        f = float(arg)
    except ValueError:
        raise argparse.ArgumentTypeError("Must be a floating point number")
    if f < 0 or f > 1:
        raise argparse.ArgumentTypeError("Argument must be 0 > [val] < 1 ")
    return f

if __name__ == "__main__":
    # PARSER
    parser = argparse.ArgumentParser(description="Blur wallpaper on window open.")
    bluring_grp = parser.add_mutually_exclusive_group()
    bluring_grp.add_argument('-w', '--wallpaper', type=str, default=None, help="wallpaper path")
    bluring_grp.add_argument('-C', '--create-cache-dir', type=str, default=None, help="create cache for every file in directory")
    bluring_grp.add_argument('-c', '--create-cache', type=str, default=None, help="create cache without launching")
    bluring_grp.add_argument('-r', '--remove', type=str, default=None, help="remove cached wallpaper corresponding to path")
    bluring_grp.add_argument('-R', '--remove-all', action='store_true', help="remove all cached wallpaper")
    parser.add_argument     ('-q', '--quiet', action='store_true', help="no output")
    parser.add_argument     ('-f', '--blur-strength', type=str, default="4", help="blur strength applied to cache")
    parser.add_argument     ('-s', '--refresh-rate', type=limits_refresh, default=0.1, help="interval of main loop")
    parser.add_argument     ('-n', '--window-number', type=int, default=1, help="number of window before blur")
    parser.add_argument     ('-b', '--backend', type=str, default="feh", help="backend to display wallpaper could be feh or hsetroot default=feh")
    args = parser.parse_args()
    # if no argument
    if len(sys.argv[1:]) == 0:
        parser.print_usage() # print usage
        parser.exit()
    if args.quiet:
        logging.basicConfig(format='%(message)s', level=logging.WARN)
    else:
        logging.basicConfig(format='%(message)s', level=logging.INFO)
    cachedir = Path(Path.home() / ".cache/Walanblur")
    if not cachedir.exists():
        cachedir.mkdir()
        logging.info(f"Created cache dir in '{cachedir}'.")
    # cache options
    if args.create_cache_dir:
        cache.generate_cache_directory(args, cachedir)
        exit(0)
    if args.create_cache:
        cache.generate_cache(Path(args.create_cache), cachedir, args)
        exit(0)
    # remove options
    if args.remove:
        cache.remove_cache(args, cachedir)
        exit(0)
    if args.remove_all:
        cache.remove_cache_all(args, cachedir)
        exit(0)
    # drawing background
    if args.wallpaper:
        draw.draw_loops(args, cachedir)