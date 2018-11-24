from io import BytesIO
from PIL import Image
import requests


def create_milkman(avatar_url):
    bottom = Image.open('resources/img/milkman.jpg').convert('RGBA')
    top = Image.open(BytesIO(requests.get(avatar_url, stream=True).content)).convert('RGBA')
    bottom.paste(top, (170, 50), top)

    b = BytesIO()
    bottom.save(b, format='bmp')
    b.seek(0)
    return 'resources/img/milkman.bmp'

