def team_lineup(*args):
    football_information = {}

    for player, country in args:
        if country not in football_information:
            football_information[country] = []
        football_information[country].append(player)

    sort_football_information = dict(sorted(football_information.items(), key=lambda x: (-len(x[1]), x[0])))

    result = ''
    for country, player_name in sort_football_information.items():
        result += f"{country}:\n"
        result += "  -" + f"\n  -".join(player_name) + "\n"

    return result.strip()


# print(team_lineup(("Harry Kane", "England"),
#                   ("Manuel Neuer", "Germany"),
#                   ("Raheem Sterling", "England"),
#                   ("Toni Kroos", "Germany"),
#                   ("Cristiano Ronaldo", "Portugal"),
#                   ("Thomas Muller", "Germany")))


# print(team_lineup(
#    ("Lionel Messi", "Argentina"),
#    ("Neymar", "Brazil"),
#    ("Cristiano Ronaldo", "Portugal"),
#    ("Harry Kane", "England"),
#    ("Kylian Mbappe", "France"),
#    ("Raheem Sterling", "England")))


# print(team_lineup(
#    ("Harry Kane", "England"),
#    ("Manuel Neuer", "Germany"),
#    ("Raheem Sterling", "England"),
#    ("Toni Kroos", "Germany"),
#    ("Cristiano Ronaldo", "Portugal"),
#    ("Thomas Muller", "Germany"),
#    ("Bruno Fernandes", "Portugal"),
#    ("Bernardo Silva", "Portugal"),
#    ("Harry Maguire", "England")))
