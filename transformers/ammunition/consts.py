from data.col_names import TransformedColumns

ammo_types = [
    {
        "items": [
            "live ammunition",
            "flechette shells",
            "0.22-caliber bullets",
            "gunfire",
        ],
        "type": TransformedColumns.AMMUNITION_FIREARMS,
    },
    {
        "items": ["explosive belt", "bomb", "car bomb", "grenade"],
        "type": TransformedColumns.AMMUNITION_GROUND_EXPLOSIVES,
    },
    {
        "items": [
            "shell",
            "missile",
            "mortar fire",
            "phosphorus shell",
            "Qassam rocket",
            "rocket",
            "grad rocket",
            "shelling",
        ],
        "type": TransformedColumns.AMMUNITION_AIR_EXPLOSIVES,
    },
    {
        "items": [
            "knife",
            "rock",
            "being bludgeoned with an axe",
            "stones throwing",
            "beating",
            "physical assault",
            "physically assaulted",
            "Strangulation",
            "stabbing",
        ],
        "type": TransformedColumns.AMMUNITION_MELEE_WEAPONS,
    },
    {
        "items": [
            "teargas canister",
            "rubber-coated metal bullets",
            "sponge rounds",
            "flare bomb",
            "stun grenade",
            "hit by a vehicle",
            "fire",
        ],
        "type": TransformedColumns.AMMUNITION_OTHER,
    },
]
