from data.col_names import Restructured_columns

ammo_types = [
    {
        "items": [
            "live ammunition",
            "flechette shells",
            "0.22-caliber bullets",
            "gunfire",
        ],
        "type": Restructured_columns.AMMUNITION_FIREARMS,
    },
    {
        "items": ["explosive belt", "bomb", "car bomb", "grenade"],
        "type": Restructured_columns.AMMUNITION_GROUND_EXPLOSIVES,
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
        "type": Restructured_columns.AMMUNITION_AIR_EXPLOSIVES,
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
        "type": Restructured_columns.AMMUNITION_MELEE_WEAPONS,
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
        "type": Restructured_columns.AMMUNITION_OTHER,
    },
]
