from ewmh import EWMH
from time import sleep
from subprocess import Popen, DEVNULL, STDOUT
from pathlib import Path, PurePath
import cache
import backend

ewmh = EWMH()

def get_windows_number():
    window_number = 0
    active_desktop = ewmh.getCurrentDesktop()
    windows = ewmh.getClientList()
    for window in windows:
        if ewmh.getWmDesktop(window) == active_desktop:
            window_number += 1
    return window_number

def draw_loop_img(args, cachedir):
    is_blured = False
    wall_path = Path(args.wallpaper)
    cachepath = Path(cachedir, wall_path.stem)
    normal = Path(cachepath, wall_path.stem + "normal" + wall_path.suffix)
    blured = Path(cachepath, wall_path.stem + "blur" + wall_path.suffix)
    Popen(backend.display_backend[args.backend](normal)).wait()
    while True:
        if get_windows_number() >= args.window_number:
            if not is_blured:
                Popen(backend.display_backend[args.backend](blured))
                is_blured = True
        else:
            if is_blured:
                Popen(backend.display_backend[args.backend](normal))            
                is_blured = False
        sleep(args.refresh_rate)

def sub_loop_gif(dirpath, filename, max_index, back, current_index):
    img_path = Path(dirpath, filename.stem + "-" + str(current_index) + ".png")
    Popen(backend.display_backend[back](img_path))

def draw_loop_gif(args, cachedir):
    wall_path = Path(args.wallpaper)
    cachepath = Path(cachedir, wall_path.stem)
    blured = Path(cachepath, "blur")
    normal = Path(cachepath, "normal")
    current_index = 0
    current_path = normal
    max_index = len(list(normal.glob('*')))
    while True:
        if get_windows_number() >= args.window_number:
            if current_path != blured:
                current_path = blured
        else:
            if current_path == blured:
                current_path = normal
        sub_loop_gif(current_path, wall_path, max_index, args.backend, current_index)
        current_index = current_index + 1 if current_index + 1 < max_index else 0
        sleep(args.refresh_rate)

def draw_loops(args, cachedir):
    filepath = Path(args.wallpaper)
    cache.generate_cache(filepath, cachedir, args)
    if filepath.suffix == ".gif":
        draw_loop_gif(args, cachedir)
    else:
        draw_loop_img(args, cachedir)
