number = int(input())

vip = []
regular = []

for i in range(number):
    reservation = input()

    if reservation[0].isdigit():
        if reservation not in vip:
            vip.append(reservation)
    else:
        if reservation not in regular:
            regular.append(reservation)

while True:
    command = input()
    if command == "END":
        break

    guest = command

    if guest in vip:
        vip.remove(guest)
    elif guest in regular:
        regular.remove(guest)

total = len(vip) + len(regular)
vip = sorted(vip)
regular = sorted(regular)

print(total)

if vip:
    for v in vip:
        print(''.join(v))
if regular:
    for r in regular:
        print(''.join(r))
      
