#    imagetools - command-line tool, adds filters to images
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


parser = argparse.ArgumentParser(description="command-line tool, adds filters to images")
parser.add_argument('operation', help='Operation to perform on the image.')
parser.add_argument('filename', help='Image file path/name')
args = parser.parse_args()

# print(args)

try:
    infile = Image.open(args.filename)
except:
    print("error: invalid image file. maybe this file ain't exist?")
    quit(1)
if args.operation == 'blur':
    outfile = infile.filter(ImageFilter.BLUR)
elif args.operation == 'sharpen':
    outfile = infile.filter(ImageFilter.SHARPEN)
else:
    print("error: invalid operation (not in: blur, sharpen)")
    quit(1)
outfile.save(f'image-{str(random.choice(range(start=1000,stop=10000)))}.png') # This saves the file under a random filename
