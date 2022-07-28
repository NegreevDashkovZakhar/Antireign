import json
from random import Random

from PIL import Image

FIRST_NAMES = ['Herbie', 'Sprinkles', 'Boris', 'Dave', 'Randy', 'Captain']
LAST_NAMES = ['Starbelly', 'Fisherton', 'McCoy']

IMAGE_BASE_URL = "https://gateway.pinata.cloud/ipfs/QmSs8inkakFyLv7HPYFpKrphabm9vu1DrjzAHtn1g669xv/"

BODIES_LENGTH = 3
HEADS_LENGTH = 3


def createJsons():
    tokenId = 1
    for body in range(1, BODIES_LENGTH+1):
        for head in range(1, HEADS_LENGTH+1):
            generateJson(tokenId)
            tokenId += 1


def generateJson(tokenId):
    tokenId = int(tokenId)
    num_first_names = len(FIRST_NAMES)
    num_last_names = len(LAST_NAMES)
    creature_name = '%s %s' % (
        FIRST_NAMES[tokenId % num_first_names], LAST_NAMES[tokenId % num_last_names])

    image_url = IMAGE_BASE_URL+'%s.png' % tokenId

    # attributes = []
    # _add_attribute(attributes, 'Base', BASES, token_id)
    # _add_attribute(attributes, 'Eyes', EYES, token_id)
    # _add_attribute(attributes, 'Mouth', MOUTH, token_id)
    with open('output/jsons/%s.json' % tokenId, 'a') as file:
        json.dump({
            'name': creature_name,
            'description': 'Brave pixel troop named %s.' % creature_name,
            'image': image_url
            # 'external_url': 'https://openseacreatures.io/%s' % tokenId,
            # 'attributes': attributes
        },
            file)


def _add_attribute(existing, attribute_name, options, token_id, display_type=None):
    trait = {
        'trait_type': attribute_name,
        'value': options[token_id % len(options)]
    }
    if display_type:
        trait['display_type'] = display_type
    existing.append(trait)


createJsons()
