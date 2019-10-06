from shlex import split

def backend_feh(path_to_img):
    return split(f"feh --bg-fill {path_to_img}")

def backend_hsetroot(path_to_img):
    return split(f"hsetroot -cover {path_to_img}")

display_backend = {
    'feh'      : backend_feh,
    'hsetroot' : backend_hsetroot
}