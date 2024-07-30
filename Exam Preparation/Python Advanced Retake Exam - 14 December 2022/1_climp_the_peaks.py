from collections import deque

required_peaks = [
    "Vihren", "Kutelo", "Banski Suhodol", "Polezhan", "Kamenitza"]

difficulty_lavel = {
    "Vihren": 80, "Kutelo": 90, "Banski Suhodol": 100, "Polezhan": 60, "Kamenitza": 70
}

idx = 0
conquered_peaks = []
day = 0

daily_portions = list(map(int, input().split(", ")))
daily_stamina = deque(map(int, input().split(", ")))

while daily_stamina and daily_portions:
    day += 1
    if day > 7 or len(conquered_peaks) == len(required_peaks):
        break

    portion = daily_portions.pop()
    stamina = daily_stamina.popleft()

    total_sum = portion + stamina
    peak = required_peaks[idx]

    if total_sum >= difficulty_lavel[peak]:
        conquered_peaks.append(peak)
        idx += 1

if len(conquered_peaks) == len(required_peaks):
    print("Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK")
else:
    print("Alex failed! He has to organize his journey better next time -> @PIRINWINS")

if conquered_peaks:
    print("Conquered peaks:")
    for peak_name in conquered_peaks:
        print(peak_name)


#############################################################################################################
# from collections import deque
#
# required_peaks = [
#     "Vihren", "Kutelo", "Banski Suhodol", "Polezhan", "Kamenitza"
# ]
#
# difficulty_level = {
#     "Vihren": 80, "Kutelo": 90, "Banski Suhodol": 100, "Polezhan": 60, "Kamenitza": 70
# }
#
# conquered_peaks = []
# day = 0
#
# daily_portions = list(map(int, input().split(", ")))
# daily_stamina = deque(map(int, input().split(", ")))
#
# while daily_stamina and daily_portions:
#     if day == 7 or len(conquered_peaks) == len(required_peaks):
#         break
#
#     day += 1
#     portion = daily_portions.pop()
#     stamina = daily_stamina.popleft()
#
#     total_sum = portion + stamina
#
#     peak = required_peaks[len(conquered_peaks)]
#     if total_sum >= difficulty_level[peak]:
#         conquered_peaks.append(peak)
#
# if len(conquered_peaks) == len(required_peaks):
#     print("Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK")
# else:
#     print("Alex failed! He has to organize his journey better next time -> @PIRINWINS")
#
# if conquered_peaks:
#     print("Conquered peaks:")
#     for peak in conquered_peaks:
#         print(peak)

