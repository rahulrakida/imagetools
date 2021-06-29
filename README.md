# imagetools
## a command-line tool for adding filters to images
[![tests](https://github.com/rahulrakida/imagetools/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/rahulrakida/imagetools/actions/workflows/main.yml)
### [Video Demo](https://youtu.be/z2hX0aL_PFM): [https://youtu.be/z2hX0aL_PFM](https://youtu.be/z2hX0aL_PFM)
### Description:

One day, I was thinking about ideas for a [CS50](https://cs50.harvard.edu/x/2021) final project, and I thought
about adding filters to an image on the command-line. There are countless MOBILE
apps for doing this, but I had never actually heard of a command-line image
editor. So, I created my own.

The program uses 4 predefined filters from the PIL.ImageFilter module: `BLUR`,
`SHARPEN`, `SMOOTH`, and `SMOOTH_MORE`. The input image is loaded as a `PIL.Image`
object, and converted using the method `PIL.Image.filter()`. The image is then saved
as a PNG with a random filename: `image-[4 digit random number].png`.

#### Features
- Blur: `blur`
- Sharpen: `sharpen`
- Smooth: `smooth`, `smooth+`

#### TODO
- GUI (low priority)
- ~~Video demo (medium priority)~~ - DONE

#### Dependencies
- python3
- python3-pip

#### Instructions

```bash
git clone https://github.com/rahulrakida/imagetools.git
cd imagetools
pip3 install -r requirements.txt
```

For usage, type `python3 imagetools.py --help`

#### License

    imagetools - a command-line program for adding filters to images
    Copyright (C) 2021 Rahul Wavare

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see [https://www.gnu.org/licenses/](https://www.gnu.org/licenses/).