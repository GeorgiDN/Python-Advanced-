from collections import deque

packages = list(map(int, input().split(' ')))
couriers = deque(map(int, input().split(' ')))
total_weight = 0

while packages and couriers:
    courier = couriers.popleft()
    package = packages.pop()

    if courier >= package:
        if courier > package:
            courier -= package * 2
            if courier > 0:
                couriers.append(courier)
        total_weight += package

    else:
        package -= courier
        packages.append(package)
        total_weight += courier

print(f"Total weight: {total_weight} kg")

if not packages and not couriers:
    print(f"Congratulations, all packages were delivered successfully by the couriers today.")
elif packages and not couriers:
    print(f"Unfortunately, there are no more available couriers to deliver the following packages: {', '.join(map(str, packages))}")
elif couriers and not packages:
    print(f"Couriers are still on duty: {', '.join(map(str, couriers))} but there are no more packages to deliver.")





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
