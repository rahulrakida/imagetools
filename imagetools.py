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

from PIL import Image, ImageFilter
import argparse
import random

def apply_filter(operation, infile):
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
        quit(1)
    
    return outfile


def main():
    # get operation, filename from command line options
    parser = argparse.ArgumentParser(description="command-line tool, adds filters to images")
    parser.add_argument('operation', help='Operation to perform on the image.')
    parser.add_argument('filename', help='Image file path/name')
    parser.add_argument('--show', help='Show output image after saving', action='store_true')
    args = parser.parse_args()

    # print(args)

    # open image, close if invalid
    try:
        infile = Image.open(args.filename)
    except:
        print("error: invalid image file. maybe this file ain't exist?")
        quit(2)
    
    outfile = apply_filter(args.operation, infile)

    outfile_name = f'image-{str(random.choice(range(1000,10000)))}.png'

    # save the new image
    outfile.save(outfile_name)
    if args.show:
        print("Showing file")
        outfile.show()

if __name__ == '__main__':
    main()