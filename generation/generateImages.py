import json
import random

from PIL import Image

BASES_LENGTH = 2
EYES_LENGTH = 3
MOUTHS_LENGTH = 2
CLOTHES_LENGTH = 3
HATS_LENGTH = 4

ids = []
for i in range(
    1, BASES_LENGTH * EYES_LENGTH * MOUTHS_LENGTH * CLOTHES_LENGTH * HATS_LENGTH + 1
):
    ids.append(i)

random.shuffle(ids)


def createImages():
    tokenId = 0
    for base in range(1, BASES_LENGTH + 1):
        for clothe in range(1, CLOTHES_LENGTH + 1):
            for mouth in range(1, MOUTHS_LENGTH + 1):
                for hat in range(1, HATS_LENGTH + 1):
                    for eye in range(1, EYES_LENGTH + 1):
                        generateImage(base, eye, clothe, mouth, hat, tokenId)
                        tokenId += 1


def generateImage(base, eye, clothe, mouth, hat, tokenId):
    tokenId = ids[tokenId]
    _compose_image(
        [
            "images/base.png",
            "images/bases/%s.png" % base,
            "images/eyes/%s.png" % eye,
            "images/clothes/%s.png" % clothe,
            "images/hats/%s.png" % hat,
            "images/mouths/%s.png" % mouth,
        ],
        tokenId,
    )


def _compose_image(image_files, token_id, path="creature"):
    composite = None
    for image_file in image_files:
        foreground = Image.open(image_file).convert("RGBA")

        if composite:
            composite = Image.alpha_composite(composite, foreground)
        else:
            composite = foreground

    output_path = "output/images/%s.png" % token_id
    composite.save(output_path)


createImages()
