import logging
from shutil import copyfile, rmtree
from subprocess import Popen, DEVNULL, STDOUT
from pathlib import Path, PurePath
from shlex import split

def generate_cache_gif(filepath, cachedir, blur):
    cachepath = Path(cachedir, filepath.stem)
    if cachepath.exists():
        logging.info(f"Cache for '{filepath.stem}' exist.")
        return
    cachepath.mkdir()
    logging.info(f"Generating cache for '{filepath.stem}'...")
    normal = Path(cachepath, "normal")
    blured = Path(cachepath, "blur")
    normal.mkdir()
    blured.mkdir()
    Popen(split(f"convert -coalesce {filepath} {normal / filepath.stem}.png")).wait()
    Popen(split(f"convert -coalesce -blur 0x{blur} {filepath} {blured / filepath.stem}.png")).wait()
    logging.info("Done !")

def generate_cache_image(filepath, cachedir, blur):
    cachepath = Path(cachedir, filepath.stem)
    if cachepath.exists():
        logging.info(f"Cache for '{filepath.stem}' exist.")
        return
    cachepath.mkdir()
    logging.info(f"Generating cache for '{filepath.stem}'...")
    normal = Path(cachepath, filepath.stem + "normal" + filepath.suffix)
    blured = Path(cachepath, filepath.stem + "blur" + filepath.suffix)
    copyfile(filepath, normal)
    Popen(split(f"convert -blur 0x{blur} {filepath} {cachepath / blured}")).wait()
    logging.info("Done !")

def generate_cache(filepath, cachedir, args):
    if filepath.suffix == ".gif":
        generate_cache_gif(filepath, cachedir, args.blur_strength)
    else:
        generate_cache_image(filepath, cachedir, args.blur_strength)

def generate_cache_directory(args, cachedir):
    cache_from = Path(args.create_cache_dir)
    cache_to_generate = list(cache_from.glob("*"))
    for i, generate in enumerate(cache_to_generate, 1):
        logging.info(f"==>{i}/{len(cache_to_generate)}")
        generate_cache_image(cache_from / generate, cachedir, args.blur_strength)
    logging.info(f"Done processing '{cache_from}'")

def remove_cache(args, cachedir):
    to_remove = Path(cachedir / Path(args.remove).stem)
    if to_remove.exists():
        if input(f"Delete '{to_remove.name}' ? [Y/N] ").upper() == "Y":
            rmtree(to_remove)
            logging.info(f"==> removed cache for '{to_remove}'.")
        else:
            logging.info("==> aborting.")

def remove_cache_all(args, cachedir):
    if cachedir.exists():
        if input("remove ALL cached wallpaper ? [Y/N] ").upper() == "Y":
            rmtree(cachedir)
            logging.info(f"==> removed cache.")
        else:
            logging.info("==> aborting.")