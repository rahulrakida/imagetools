# imagetools
## a command-line tool for adding filters to images
[![Codacy 
Badge](https://app.codacy.com/project/badge/Grade/c290e907e73a441dad0ef53ff10d1455)](https://www.codacy.com/gh/rahulrakida/imagetools/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=rahulrakida/imagetools&amp;utm_campaign=Badge_Grade)
[![tests](https://github.com/rahulrakida/imagetools/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/rahulrakida/imagetools/actions/workflows/main.yml) 
[![CodeQL](https://github.com/rahulrakida/imagetools/actions/workflows/codeql-analysis.yml/badge.svg?branch=main)](https://github.com/rahulrakida/imagetools/actions/workflows/codeql-analysis.yml)
[![Code size]([![CodeQL](https://github.com/rahulrakida/imagetools/actions/workflows/codeql-analysis.yml/badge.svg?branch=main)])]

### [Video Demo](https://youtu.be/z2hX0aL_PFM): [https://youtu.be/z2hX0aL_PFM](https://youtu.be/z2hX0aL_PFM)
#### Description

One day, I was thinking about ideas for a [CS50](https://cs50.harvard.edu/x/2021) final project, and I thought
about adding filters to an image on the command-line. There are countless MOBILE
apps for doing this, but I had never actually heard of a command-line image
editor. So, I created my own.

#### imagetools.py

The program uses 4 predefined filters from the PIL.ImageFilter module: `BLUR`,
`SHARPEN`, `SMOOTH`, and `SMOOTH_MORE`. The input image is loaded as a `PIL.Image`
object, and converted using the method `PIL.Image.filter()`. The image is then saved
as a PNG with a random filename: `image-[4 digit random number].png`.

#### test_files/image.png

This is a test file for use in GitHub Actions. 
Feel free to use it for testing on your own PC.

#### README.md

This document, outlining the features of imagetools.

##### LICENSE

A copy of the GNU General Public License, the license this program falls under.
More information at the bottom of this document.

#### Features
-   Blur: `blur`
-   Sharpen: `sharpen`
-   Smooth: `smooth`, `smooth+`

#### TODO
-   GUI (low priority)

#### Prerequisites
-   Python 3.6 or later
-   pip

#### Instructions

```bash
git clone https://github.com/rahulrakida/imagetools.git
cd imagetools
pip3 install -r requirements.txt
```

For usage, type `python3 imagetools.py --help`

#### GNU General Public License 3.0

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

You should have received [a copy of the GNU General Public License](https://github.com/rahulrakida/imagetools/blob/main/LICENSE)
along with this program.  If not, see [https://www.gnu.org/licenses/](https://www.gnu.org/licenses/).
