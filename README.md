Pywalblur
=========

Blur your background on window open

![](https://github.com/Di-KaZ/pywalblur/blob/master/demo.gif)

Dependencies
------------

- Your window manager have to be [EWMH](https://en.wikipedia.org/wiki/Extended_Window_Manager_Hints) compliant for this to work.
- [hsetroot](https://github.com/himdel/hsetroot)
- [wmctrl](https://github.com/Conservatory/wmctrl)
- [imagemagick](https://github.com/ImageMagick/ImageMagick)

Options
-------

| short | long               | description                                   |
| :---: | :----------------: | :-------------------------------------------: |
|  -h   | --help             | show this help message and exit               |
|  -r   | --refresh-rate     | interval of check                             |
|  -q   | --quiet            | no print                                      |
|  -a   | --animation        | add 'animation'(experimental)                 |
|  -c   | --create-cache     | create cache without launching                |
|  -G   | --create-cache-all | create cache for every file in dit            |
|  -w   | --wallpaper        | wallpaper path                                |
|  -g   | --wallpapergif     | wallpaper path as gif(not yet implemented)    |
|  -d   | --delete           | delete cached wallpaper corresponding to path |
|  -C   | --clear            | clear all cached wallpaper                    |