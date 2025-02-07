from collections import deque

packages_collection = list(map(int, input().split()))
couriers_collection = deque(map(int, input().split()))
total_weight = 0

while couriers_collection and packages_collection:
    package = packages_collection.pop()
    courier = couriers_collection.popleft()

    if courier >= package:
        if courier > package:
            courier -= package * 2
            if courier > 0:
                couriers_collection.append(courier)
        total_weight += package
    else:
        package -= courier
        packages_collection.append(package)
        total_weight += courier

print(f"Total weight: {total_weight} kg")

if not couriers_collection and not packages_collection:
    print("Congratulations, all packages were delivered successfully by the couriers today.")
elif packages_collection:
    print(f"Unfortunately, there are no more available couriers to deliver the following packages:"
          f" {', '.join(map(str, packages_collection))}")
elif couriers_collection:
    print(f"Couriers are still on duty: {', '.join(map(str, couriers_collection))}"
          f" but there are no more packages to deliver.")



#######################################################################################################################################
# from collections import deque
# 
# packages = list(map(int, input().split()))
# couriers = deque(map(int, input().split()))
# total_weight = 0
# 
# while packages and couriers:
#     package = packages.pop()
#     courier_capacity = couriers.popleft()
# 
#     if courier_capacity >= package:
#         if courier_capacity > package:
#             courier_capacity -= (package * 2)
#             if courier_capacity > 0:
#                 couriers.append(courier_capacity)
#         total_weight += package
#     else:
#         package -= courier_capacity
#         packages.append(package)
#         total_weight += courier_capacity
# 
# print(f"Total weight: {total_weight} kg")
# if not packages and not couriers:
#     print("Congratulations, all packages were delivered successfully by the couriers today.")
# elif packages and not couriers:
#     sting_packages = ", ".join(map(str, packages))
#     print(f"Unfortunately, there are no more available couriers to deliver the following packages: {sting_packages}")
# elif not packages and couriers:
#     sting_couriers = ", ".join(map(str, couriers))
#     print(f"Couriers are still on duty: {sting_couriers} but there are no more packages to deliver.")



#######################################################################################################################################
# from collections import deque
#
# packages = list(map(int, input().split(' ')))
# couriers = deque(map(int, input().split(' ')))
# total_weight = 0
#
# while packages and couriers:
#     courier = couriers.popleft()
#     package = packages.pop()
#
#     if courier >= package:
#         if courier > package:
#             courier -= package * 2
#             if courier > 0:
#                 couriers.append(courier)
#         total_weight += package
#
#     else:
#         package -= courier
#         packages.append(package)
#         total_weight += courier
#
# print(f"Total weight: {total_weight} kg")
#
# if not packages and not couriers:
#     print(f"Congratulations, all packages were delivered successfully by the couriers today.")
# elif packages and not couriers:
#     print(f"Unfortunately, there are no more available couriers to deliver the following packages: {', '.join(map(str, packages))}")
# elif couriers and not packages:
#     print(f"Couriers are still on duty: {', '.join(map(str, couriers))} but there are no more packages to deliver.")




#######################################################################################################################################
# from collections import deque
#
# packages = deque(int(x) for x in input().split())
# couriers = deque(int(x) for x in input().split())
#
# total_weight = 0
#
# while packages and couriers:
#     package = packages[-1]
#     courier = couriers.popleft()
#
#     if courier >= package:
#         total_weight += package
#         courier -= 2 * package
#         packages.pop()
#
#         if courier > 0:
#             couriers.append(courier)
#     else:
#         total_weight += courier
#         packages[-1] -= courier
#
#
# print(f"Total weight: {total_weight} kg")
#
# if not packages and not couriers:
#     print("Congratulations, all packages were delivered successfully by the couriers today.")
# elif packages:
#     print("Unfortunately, there are no more available couriers to deliver the following packages:", end=" ")
#     print(", ".join(map(str, packages)))
# else:
#     print("Couriers are still on duty:", end=" ")
#     print(", ".join(map(str, couriers)), end=" ")
#     print("but there are no more packages to deliver.")
