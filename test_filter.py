import imagetools
from PIL import Image
from io import BytesIO
import requests

def test_filter():
    image = Image.open('test_files/image.jpg')
    assert imagetools.apply_filter('blur', image)
    assert imagetools.apply_filter('sharpen', image)
    assert imagetools.apply_filter('smooth', image)
    assert imagetools.apply_filter('smooth+', image)