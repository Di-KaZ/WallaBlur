from ewmh import EWMH
from time import sleep
from subprocess import Popen, DEVNULL, STDOUT
from pathlib import Path, PurePath
import cache


def draw_loop_img(args, cachedir):
    

def draw_loops(args, cachedir):
    filepath = Path(args.wallpaper)
    if not filepath.exists:
        cache.generate_cache(args, cachedir)
    if filepath.suffix == ".gif":
        draw_loop_gif(args, cachedir)
    else:
        draw_loop_img(args, cachedir)
