import json
import random

abilitiesDictionary = dict(
    Archer="Shoot", Knight="Defense", Healer="Heal"
)

FIRST_NAMES = [
    "Reginmax",
    "Dinotine",
    "Ferumvia",
    "Nathkenmeri",
    "Hildichel",
    "Shaseph",
    "Cuthman",
    "Laygar",
    "Eadlaf",
    "Damen",
    "Andwaru",
    "Paulgarald",
    "Roldra",
    "Leka",
    "Jeffever",
    "Somark",
    "An-ke",
    "Elina",
    "Sereron",
    "Nechell",
]
LAST_NAMES = [
    "Dragonrain",
    "Bravebane",
    "Staffgrey",
    "Bowpaladin",
    "Elvencloakgray",
    "Arrowcat",
    "Summerlight",
    "The Brave",
    "Shieldmoor",
    "Chasewalk",
    "Dwarfrunner",
    "Landmountain",
    "Summershield",
    "Dawnsunthunder",
    "Ragetall",
    "Glidedragon",
    "Bowelven",
    "Mournehound",
    "Gliderpower",
    "Houndbat",
]


IMAGE_BASE_URL = (
    "https://gateway.pinata.cloud/ipfs/QmTaAKME8MrRvQjrg3LwmGztMcsCiTEn5qT9345MLUFg9Q/"
)

jsonCount = 50


def createJsons():
    for tokenId in range(1, jsonCount + 1):
        generateJson(tokenId)


def generateJson(tokenId):
    tokenId = int(tokenId)
    troopName = "%s %s" % (
        FIRST_NAMES[random.randint(0, len(FIRST_NAMES) - 1)],
        LAST_NAMES[random.randint(0, len(LAST_NAMES) - 1)],
    )

    image_url = IMAGE_BASE_URL + "%s.png" % tokenId

    attributes = []

    levelWeights = [0.5, 0.25, 0.125, 0.0625, 0.0625]
    levels = [1, 2, 3, 4, 5]
    level = random.choices(levels, levelWeights)[0]

    baseHealth = 100
    healthBoostIndex = 20
    health = baseHealth + random.randint(
        (level - 1) * healthBoostIndex, level * healthBoostIndex
    )

    baseDamage = 15
    damageBoostIndex = 5
    damage = baseDamage + random.randint(
        (level - 1) * damageBoostIndex, level * damageBoostIndex
    )

    troopClass = random.choice(["Archer", "Knight", "Healer"])

    special = 0
    if troopClass == "Archer":
        baseSpecial = 2
        specialBoostIndex = 1
        special = baseSpecial + random.randint(
            (level - 1) * specialBoostIndex, level * specialBoostIndex
        )
        _add_attribute(attributes, "Shot distance", special)

    elif troopClass == "Knight":
        baseSpecial = 5
        specialBoostIndex = 3
        special = baseSpecial + random.randint(
            (level - 1) * specialBoostIndex, level * specialBoostIndex
        )
        _add_attribute(attributes, "Shield level", special)
    elif troopClass == "Healer":
        baseSpecial = 10
        specialBoostIndex = 5
        special = baseSpecial + random.randint(
            (level - 1) * specialBoostIndex, level * specialBoostIndex
        )
        _add_attribute(attributes, "Heal amount", special)

    _add_attribute(attributes, "Level", level, "number")
    _add_attribute(attributes, "Health", health, "number")
    _add_attribute(attributes, "Damage", damage, "number")
    _add_attribute(attributes, "Class", troopClass)
    _add_attribute(attributes, "Special ability", abilitiesDictionary.get(troopClass))
    with open("output/jsons/%s.json" % tokenId, "w") as file:
        json.dump(
            {
                "name": troopName,
                "description": "Brave pixel troop named %s." % troopName,
                "image": image_url,
                "attributes": attributes,
            },
            file,
        )


def _add_attribute(existing, attribute_name, value, display_type=None):
    trait = {"trait_type": attribute_name, "value": value}
    if display_type:
        trait["display_type"] = display_type
    existing.append(trait)


createJsons()
