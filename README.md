Pywalblur
=========

Blur your background on window open (and gif background too !)

![](https://github.com/Di-KaZ/pywalblur/blob/master/demo.gif)

Dependencies
------------

Required :
- Your window manager have to be [EWMH](https://en.wikipedia.org/wiki/Extended_Window_Manager_Hints) compliant for this to work.
- [ewmh](https://pypi.org/project/ewmh/0.1.2/)
- [python-xlib](https://github.com/python-xlib/python-xlib)
- [imagemagick](https://github.com/ImageMagick/ImageMagick)

For png, jpg, ect:
- [hsetroot](https://github.com/himdel/hsetroot)
or
- [feh](https://github.com/derf/feh)

For gifs:
- [xwinwrap](https://github.com/ujjwal96/xwinwrap)
- [mpv]()

Installing
----------
After installing all the dependencies, simply run pywalblur or install in your path with

```bash
pip install ewmh
python3 -m pip install Xlib
git clone https://github.com/Di-KaZ/pywalblur.git
cd pywalblur
make install
```

Options
-------

Here is the list of avalible options:

| short | long               | description                                                               |
| :---: | :----------------: | :-------------------------------------------:                             |
| -h    | --help             | show this help message and exit                                           |
| -s    | --refresh-rate     | interval of check                                                         |
| -q    | --quiet            | no print                                                                  |
| -a    | --animation        | add 'animation' (experimental) / deactivate blur on gifs                  |
| -n    | --window-number    | WINDOW_NUMBER number of window before blur                                |
| -b    | --backend          | BACKEND backend to display wallpaper could be feh or hsetroot default=feh |
| -c    | --create-cache     | create cache without launching                                            |
| -C    | --create-cache-dir | create cache for every file in directory                                  |
| -w    | --wallpaper        | wallpaper path(gif still experimental)                                    |
| -r    | --remove           | remove cached wallpaper corresponding to path                             |
| -R    | --remove-all       | remove all cached wallpaper                                               |