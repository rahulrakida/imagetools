#!/usr/bin/python
#    imagetools - command-line tool for adding filters to images
#    Copyright (C) 2021 Rahul Wavare
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.

from PIL import Image, ImageFilter, UnidentifiedImageError
from requests.exceptions import RequestException
from io import BytesIO
import requests
import os.path
import argparse
import random
import typing
import PIL

def apply_filter(operation: str, infile: PIL.Image.Image) -> PIL.Image.Image:
    """\
    Apply a filter to an image.
    Valid values for operation:
    blur, sharpen, smooth, smooth+\
    """
    if operation == 'blur':
        outfile = infile.filter(ImageFilter.BLUR)
    elif operation == 'sharpen':
        outfile = infile.filter(ImageFilter.SHARPEN)
    elif operation == 'smooth':
        outfile = infile.filter(ImageFilter.SMOOTH)
    elif operation == 'smooth+':
        outfile = infile.filter(ImageFilter.SMOOTH_MORE)
    else:
        print("error: invalid operation (not in: blur, sharpen, smooth, smooth+)")
        raise NotImplementedError
    return outfile

def main():
    # get operation, filename from command line options
    parser = argparse.ArgumentParser(description='command-line tool, adds filters to images')
    parser.add_argument('operation', help='Operation to perform on the image.')
    parser.add_argument('filename', help='Image file path/name')
    parser.add_argument('--show', help='Show output image after saving', action='store_true')
    parser.add_argument('--url', help='Treat filename as a URL', action='store_true')
    args = parser.parse_args()

    # open image, close if invalid
    try:
        if args.url:
            print("--url option detected, connecting to " + args.filename)
            infile = Image.open(BytesIO(requests.get(args.filename).content))
        else:
            infile = Image.open(args.filename)
    except UnidentifiedImageError:
        print("This file is an invalid image.")
        quit(2)
    except FileNotFoundError:
        print("This file does not exist.")
        quit(4)
    except RequestException:
        print("There was an error with the HTTP request.\nDid you use the --url option on a file path?")
        quit(5)
    except Exception as e:
        print("Unidentified error. This may be a bug.\nPlease send a report at:\nhttps://github.com/rahulrakida/imagetools/issues with below exception.")
        raise e
    
    outfile = apply_filter(args.operation, infile)
    i = 0
    outfile_name = None
    while True:
        i = i + 1
        outfile_name = "image-{}.png".format(str(random.choice(range(1000,10000))))
        if i >= 10000: # Incredibly rare case in which there are no output filenames available.
            print("error: no possibilities for output filename (How did you manage to get this error?)")
            quit(3)

        if not os.path.exists(outfile_name):
            break

    # save the new image
    outfile.save(outfile_name)
    if args.show:
        print("Showing file")
        outfile.show()

if __name__ == '__main__':
    main()
