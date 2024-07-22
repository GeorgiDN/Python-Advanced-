from collections import deque

packages = list(map(int, input().split()))
couriers = deque(map(int, input().split()))
total_weight = 0

while packages and couriers:
    package = packages.pop()
    courier_capacity = couriers.popleft()

    if courier_capacity >= package:
        if courier_capacity > package:
            courier_capacity -= (package * 2)
            if courier_capacity > 0:
                couriers.append(courier_capacity)
        total_weight += package
    else:
        package -= courier_capacity
        packages.append(package)
        total_weight += courier_capacity

print(f"Total weight: {total_weight} kg")
if not packages and not couriers:
    print("Congratulations, all packages were delivered successfully by the couriers today.")
elif packages and not couriers:
    sting_packages = ", ".join(map(str, packages))
    print(f"Unfortunately, there are no more available couriers to deliver the following packages: {sting_packages}")
elif not packages and couriers:
    sting_couriers = ", ".join(map(str, couriers))
    print(f"Couriers are still on duty: {sting_couriers} but there are no more packages to deliver.")






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
