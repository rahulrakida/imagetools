import imagetools
from PIL import Image
from io import BytesIO
import requests
import random

def test_filter():
    image = Image.open('test_files/image.jpg')
    assert imagetools.apply_filter('blur', image)
    assert imagetools.apply_filter('sharpen', image)
    assert imagetools.apply_filter('smooth', image)
    assert imagetools.apply_filter('smooth+', image)
    content_bytes = requests.get('https://picsum.photos/{}/{}'.format(random.randint(100, 999), random.randint(100, 999))).content
    image_download = Image.open(BytesIO(content_bytes))
    assert imagetools.apply_filter('blur', image_download)
    assert imagetools.apply_filter('sharpen', image_download)
    assert imagetools.apply_filter('smooth', image_download)
    assert imagetools.apply_filter('smooth+', image_download)

if __name__ == "__main__":
    test_filter()
