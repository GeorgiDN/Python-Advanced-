def draw_cards(*args, **kwargs):
    spell_cards = []
    monster_cards = []

    def fill_collection(card, _type):
        if _type == "spell":
            spell_cards.append(card)
        elif _type == "monster":
            monster_cards.append(card)

    for card, _type in args:
        fill_collection(card, _type)

    for card, _type in kwargs.items():
        fill_collection(card, _type)

    spell_cards.sort()
    monster_cards.sort(reverse=True)

    result = []

    if monster_cards:
        result.append('Monster cards:')
        for card in monster_cards:
            result.append(f'  ***{card}')
    if spell_cards:
        result.append('Spell cards:')
        for card in spell_cards:
            result.append(f'  $$${card}')

    return '\n'.join(result)


# print(draw_cards(("cyber dragon", "monster"), freeze="spell",))
# print(draw_cards(("celtic guardian", "monster"), ("earthquake", "spell"), ("fireball", "spell"), raigeki="spell", destroy="spell",))
# print(draw_cards(("brave attack", "spell"), ("freeze", "spell"), lightning_bolt="spell", fireball="spell",))



###########################################################################################################################


# def draw_cards(*args, **kwargs):
#     spell_cards = []
#     monster_cards = []

#     for data in args:
#         card_name = data[0]
#         card_type = data[1]
#         spell_cards.append(card_name) if card_type == "spell" else monster_cards.append(card_name)

#     for card_name, card_type in kwargs.items():
#         spell_cards.append(card_name) if card_type == "spell" else monster_cards.append(card_name)

#     result = ''
#     if monster_cards:
#         sorted_monster_cards = sorted(monster_cards, reverse=True)
#         result += "Monster cards:\n"
#         result += '\n'.join([f"  ***{monster}" for monster in sorted_monster_cards])

#     if spell_cards:
#         sorted_spell_cards = sorted(spell_cards)
#         result += "\n" + "Spell cards:\n"
#         result += '\n'.join([f"  $$${spell_name}" for spell_name in sorted_spell_cards])

#     return result.strip()



###################################################################################################################
# def draw_cards(*args, **kwargs):
#     spell_cards = []
#     monster_cards = []
#
#     for data in args:
#         card_name = data[0]
#         card_type = data[1]
#         spell_cards.append(card_name) if card_type == "spell" else monster_cards.append(card_name)
#
#     for card_name, card_type in kwargs.items():
#         spell_cards.append(card_name) if card_type == "spell" else monster_cards.append(card_name)
#
#     result = ''
#     if monster_cards:
#         sorted_monster_cards = sorted(monster_cards, reverse=True)
#         result += "Monster cards:\n"
#         for monster in sorted_monster_cards:
#             result += f"  ***{monster}\n"
#
#     if spell_cards:
#         sorted_spell_cards = sorted(spell_cards)
#         result += "Spell cards:\n"
#         for spell_name in sorted_spell_cards:
#             result += f"  $$${spell_name}\n"
#
#     return result.strip()
#
#
# # print(draw_cards(("cyber dragon", "monster"), freeze="spell",))
# # print(draw_cards(("celtic guardian", "monster"), ("earthquake", "spell"), ("fireball", "spell"), raigeki="spell", destroy="spell",))
# # print(draw_cards(("brave attack", "spell"), ("freeze", "spell"), lightning_bolt="spell", fireball="spell",))
