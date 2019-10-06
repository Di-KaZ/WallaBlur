Pywalblur
=========

Blur Your backround when window are opened now with gif !

![](https://github.com/Di-KaZ/pywalblur/blob/master/demo.gif)

Dependencies
------------

Required :
- Your window manager have to be [EWMH](https://en.wikipedia.org/wiki/Extended_Window_Manager_Hints) compliant for this to work.
- [imagemagick](https://github.com/ImageMagick/ImageMagick)
In order to display background pywalblur use a background setter like these :
- [hsetroot](https://github.com/himdel/hsetroot)
- [feh](https://github.com/derf/feh)

You can change backend using -b flag see Options

Installing
----------

```shell
pip install pywalblur
```

Options
-------

Here is the list of avalible options:

| short | long               | description                                                       |
| :---: | :----------------: | :-------------------------------------------:                     |
| -h    | --help             | show this help message and exit                                   |
| -w    | --wallpaper        | wallpaper path                                                    |
| -C    | --create-cache-dir | create cache for every file in directory                          |
| -c    | --create-cache     | create cache without launching                                    |
| -r    | --remove           | remove cached wallpaper corresponding to path                     |
| -R    | --remove-all       | remove all cached wallpaper                                       |
| -f    | --blur-strength    | blur strength applied to cache                                    |
| -s    | --refresh-rate     | interval of main loop                                             |
| -n    | --window-number    | number of window before blur                                      |
| -b    | --backend          | backend to display wallpaper could be feh or hsetroot default=feh |
| -q    | --quiet            | no output                                                         |