import json
from random import Random

from PIL import Image

IMAGE_BASE_URL = "qweewqqweqweq/"

BODIES_LENGTH = 3
HEADS_LENGTH = 3


def createImages():
    tokenId = 1
    for body in range(1, BODIES_LENGTH+1):
        for head in range(1, HEADS_LENGTH+1):
            generateImage(body, head, tokenId)
            tokenId += 1


def generateImage(body, head, tokenId):
    _compose_image(['images/bodies/%s.png' % body,
                    'images/heads/%s.png' % head],
                   tokenId)


def _compose_image(image_files, token_id, path='creature'):
    composite = None
    for image_file in image_files:
        foreground = Image.open(image_file).convert('RGBA')

        if composite:
            composite = Image.alpha_composite(composite, foreground)
        else:
            composite = foreground

    output_path = 'output/images/%s.png' % token_id
    composite.save(output_path)
    return IMAGE_BASE_URL + '%s.png' % token_id


createImages()
