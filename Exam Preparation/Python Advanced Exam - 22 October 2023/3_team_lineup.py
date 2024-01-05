def team_lineup(*args):
    football_information = {}

    for player, country in args:
        if country not in football_information:
            football_information[country] = [player]
        else:
            football_information[country].append(player)

    sort_information = dict(sorted(football_information.items(), key=lambda x: (-len(x[1]), x[0])))

    final_result = ''
    for k, v in sort_information.items():
       final_result += f"{k}:\n"
       final_result += "  -" + f"\n  -".join(v) + "\n"

    return final_result


print(team_lineup(("Harry Kane", "England"),
                  ("Manuel Neuer", "Germany"),
                  ("Raheem Sterling", "England"),
                  ("Toni Kroos", "Germany"),
                  ("Cristiano Ronaldo", "Portugal"),
                  ("Thomas Muller", "Germany")))
