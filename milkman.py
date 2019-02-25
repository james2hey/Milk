from io import BytesIO
from PIL import Image
import requests


def create_milkman(avatar_url):
    bottom = Image.open('resources/img/milkman.jpg').convert('RGBA')
    top = Image.open(BytesIO(requests.get(avatar_url, stream=True).content)).convert('RGBA')
    bottom.paste(top, (170, 50), top)

    bottom.convert('RGB').save('temp/milkman.jpg')
    return 'temp/milkman.jpg'


def create_spillman(avatar_url):
    bottom = Image.open('resources/img/spill0.jpg').convert('RGBA')
    print(requests.get(avatar_url, stream=True).content)
    profile_image = BytesIO(requests.get(avatar_url, stream=True).content)
    profile_image.seek(0)
    top = Image.open(profile_image).resize((48, 48)).rotate(90).convert('RGBA')
    bottom.paste(top, (260, 205), top)

    bottom.convert('RGB').save('temp/spillman.jpg')
    return 'temp/spillman.jpg'

