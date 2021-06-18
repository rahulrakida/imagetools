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
import PIL
import argparse
import random

"""
parser = argparse.ArgumentParser(description="command-line tool, adds filters to images")
parser.add_argument('operation', help='Operation to perform on the image.')
parser.add_argument('filename', help='Image file path/name')
parser.parse_args()
"""

infile = PIL.Image.open('image.png')
outfile = infile.filter(PIL.ImageFilter.BLUR)
outfile.show()
