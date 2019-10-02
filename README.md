Pywalblur
=========

Blur your background on window open

![](https://github.com/Di-KaZ/pywalblur/blob/master/demo.gif)

Dependencies
------------

Required :
- Your window manager have to be [EWMH](https://en.wikipedia.org/wiki/Extended_Window_Manager_Hints) compliant for this to work.
- [wmctrl](https://github.com/Conservatory/wmctrl)
- [imagemagick](https://github.com/ImageMagick/ImageMagick)

For png, jpg, ect:
- [hsetroot](https://github.com/himdel/hsetroot)

For gifs:
- [xwinwrap](https://github.com/ujjwal96/xwinwrap)
- [mpv]()

Installing
----------
After installing all the dependencies, simply run pywalblur or install in your path with

```bash
git clone https://github.com/Di-KaZ/pywalblur.git
cd pywalblur
make install
```

Options
-------

Here is the list of avalible options:

| short | long               | description                                            |
| :---: | :----------------: | :-------------------------------------------:          |
|  -h   | --help             | show this help message and exit                        |
|  -s   | --refresh-rate     | interval of check                                      |
|  -q   | --quiet            | no print                                               |
|  -a   | --animation        | add 'animation'(experimental) / deactivate blur on gif |
|  -c   | --create-cache     | create cache without launching                         |
|  -C   | --create-cache-dir | create cache for every file in dir                     |
|  -w   | --wallpaper        | wallpaper path                                         |
|  -r   | --remove           | remove cached wallpaper corresponding to path          |
|  -R   | --remove-all       | remove all cached wallpaper                            |