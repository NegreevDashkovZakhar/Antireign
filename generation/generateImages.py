import json
import random

from PIL import Image

IMAGE_BASE_URL = "qweewqqweqweq/"

BASES_LENGTH = 3
EYES_LENGTH = 4
MOUTHS_LENGTH = 2
CLOTHES_LENGTH = 3

ids = []
for i in range(1,BASES_LENGTH*EYES_LENGTH*MOUTHS_LENGTH*CLOTHES_LENGTH+1):
    ids.append(i)

random.shuffle(ids)

def createImages():
    tokenId = 0
    for base in range(1, BASES_LENGTH+1):
        for clothe in range(1, CLOTHES_LENGTH+1):
            for mouth in range(1, MOUTHS_LENGTH+1):
                for eye in range(1, EYES_LENGTH+1):
                    generateImage(base, eye, clothe, mouth, tokenId)
                    tokenId += 1


def generateImage(base, eye, clothe, mouth,tokenId):
    tokenId = ids[tokenId]
    _compose_image(['images/bases/%s.png' % base,
                    'images/eyes/%s.png' % eye,
                    'images/clothes/%s.png' % clothe,
                    'images/mouths/%s.png' % mouth],
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
