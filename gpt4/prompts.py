"""this module contains templates for gpt-4 chat API"""


def create_from_template(ctx: str, example: str) -> str:
    """a basic template for gpt-4 API prompts"""
    template = f"""
  Answer questions as truthfully as possible using the CONTEXT below and nothing else. Always skip any additional comments. Use  TEMPLATE for reference how to answer.
  CONTEXT###
  {ctx}
  ###
  
  TEMPLATE###
  {example}
  ###
  
  [user prompt goes right below]
  """

    return template


killed_by_assistant_prompt = create_from_template(
    ctx="""
1. the user prompt is a list of comma-separated descriptions of Palestinians and Insraelis who died in ongoing Israeli-Palestinian conflicts. 
2. Match each description from the list to one of the categories listed below and return an ordered array of categories. The categories are:
a) 'killed_by_palestinian" - the person was killed by a palestinian citizen or fighter,
b) 'killed_by_idf" - the person was killed by an israeli who serves in the military and other israeli security forces,
c) 'killed_by_israeli' - the person was killed by an israeli who must NOT be from israeli army or israeli security forces.
d) "unknown" - there's no enough certain information about the killer of the person.
3. If You are uncertain, do NOT assume anything and select "unknown" category
  """,
    example="""
example prompt #1: ['Killed during IDF incursion into the el-Burej refugee camp', ' A civilian killed in Hamas bomb attack']

answer: ["killed_by_idf", "killed_by_palestinian"]

example_prompt #2: ["Died in a fire exchange between unknown people", "Beaten to death by an israeli settler who was his neighbor on the street"]

answer: ["unknown", "killed_by_israeli"]
  """,
)

ammunition_assistant_prompt = create_from_template(
    ctx="""
1. the user prompt is a list of comma-separated descriptions of Palestinians and Insraelis who died in ongoing Israeli-Palestinian conflicts. 
2. Match each description from the list to one of the categories listed below and return an ordered array of categories. The categories are:
      a) "ammunition_firearms" - all firearms which use round ammunition
      b) "ammunition_ground_explosives" - explosives that are activated and detonated on the ground like car bombs, suicide belts, bombs and grenades
      c) "ammunition_air_explosives" - explosives which are shot from air or long distance, this included mortars, shell bombs, air bombs, rockets and missiles,
      d) "ammunition_melee_weapons" - melee weapons and martial arts
      e) "ammunition_other" - unknown or none of the above, e.g. fire and car (or when missing information)
f) "unknown" - there's no enough certain information about the weapon used.
3. If You are uncertain, do NOT assume anything and select "unknown" category
  """,
    example="""
example prompt #1: ['Killed during IDF incursion into the el-Burej refugee camp', ' A civilian killed in Hamas bomb attack']

answer: ["ammunition_fireamrs", "ammunition_groud_explosives"]

example_prompt #2: ["Died in a fire exchange between unknown people", "Beaten to death by an israeli settler who was his neighbor on the street"]

answer: ["ammunition_fireamrs", "melee_weapons"]
  """,
)
