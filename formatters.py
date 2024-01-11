from enums import Restructured_columns

ammo_types = [
    {
        "items": ["live ammunition", "flechette shells", "0.22-caliber bullets"],
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
        ],
        "type": Restructured_columns.AMMUNITION_AIR_EXPLOSIVES,
    },
    {
        "items": ["knife", "rock"],
        "type": Restructured_columns.AMMUNITION_MELEE_WEAPONS,
    },
    {
        "items": [
            "teargas canister",
            "rubber-coated metal bullets",
            "sponge rounds",
            "flare bomb",
            "stun grenade",
        ],
        "type": Restructured_columns.AMMUNITION_OTHER,
    },
]

injury_types = [
    {
        "items": ["gunfire"],
        "type": Restructured_columns.AMMUNITION_FIREARMS,
    },
    {
        "items": ["shelling"],
        "type": Restructured_columns.AMMUNITION_AIR_EXPLOSIVES,
    },
    {
        "items": [
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
        "items": ["hit by a vehicle", "fire"],
        "type": Restructured_columns.AMMUNITION_OTHER,
    },
]


def llm_get_ammunition_by_notes(notes):
    # TODO: use LLM to fill data
    print(notes)


# for sorted args which have data
def format_ammunition(ammunition: str) -> str:
    """fit ammunition column data into newly created categories"""
    for item in ammo_types:
        if ammunition in item["items"]:
            return item["type"]

    raise ValueError("Unknown ammunition type")

