def check_mission_feasibility(allowed_crew_size, available_budget, *args):
    # mission_name, required_crew_size, mission_budget
    confirm_missions = []
    suspended_missions = []

    for data in args:
        mission_name, crew_size, mission_budget = data[0], int(data[1]), float(data[2])

        if crew_size > allowed_crew_size or mission_budget > available_budget:
            suspended_missions.append((mission_name, crew_size, mission_budget))

        else:
            confirm_missions.append((mission_name, crew_size, mission_budget))
            available_budget -= mission_budget

    confirm_missions.sort(key=lambda x: x[0])
    suspended_missions.sort(key=lambda x: (-x[1], -x[2]))

    result = []
    if not suspended_missions:
        result.append('All missions are feasible within crew and budget limits.')

    def take_result(mission_collection, sign):
        for name, crew_size, budget in mission_collection:
            result.append(f'{sign}{name}, crew size: {crew_size}, budget: {budget:.2f}')

    if confirm_missions:
        result.append('Confirmed Missions:')
        take_result(confirm_missions, '$')

    if suspended_missions:
        result.append('Suspended Missions:')
        take_result(suspended_missions, '!')

    return '\n'.join(result)


# print(check_mission_feasibility(
#     5, 100_000_000.0,
#     ("Apollo 11", 3, 10_000_000.0),
#     ("Voyager 1", 2, 5_000_000.0),
#     ("Hubble 2", 4, 8_000_000.0)
# ))


# print(check_mission_feasibility(
#     3, 9_000_000.0,
#     ("Apollo 11", 3, 9_000_000.1),
#     ("Voyager 1", 2, 5_000_000.0),
#     ("Hubble 2", 4, 3_000_000.0),
#     ("Lunar 5", 3, 9_000_001.0)
# ))


# print(check_mission_feasibility(
#     4, 9_000_000.0,
#     ("Apollo 11", 5, 2_000_000.1),
#     ("Voyager 1", 5, 1_000_000.0),
#     ("Hubble 2", 4, 9_000_000.01),
#     ("Lunar 5", 8, 500_000.0)
# ))

# print(check_mission_feasibility(
#     3, 20_000_000.0,
#     ("Voyager 1", 2, 5_000_000.0),
#     ("Hubble 2", 4, 3_000_000.0),
#     ("Lunar 4", 3, 6_000_001.0),
#     ("Apollo 11", 3, 9_000_000.1),
#     ("Hubble 3", 4, 2_000_000.0),
#     ("Lunar 5", 3, 4_000_001.0)
# ))
