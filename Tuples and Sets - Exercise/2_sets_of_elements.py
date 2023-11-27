length_of_two = input().split(' ')
number_1 = int(length_of_two[0])
number_2 = int(length_of_two[1])

list_1 = []
list_2 = []
repeat = []

for i in range(number_1):
    number = int(input())
    if number not in list_1:
        list_1.append(number)

for j in range(number_2):
    number2 = int(input())
    if number2 not in list_2:
        list_2.append(number2)

for num in list_1:
    if num in list_2:
        repeat.append(num)

for curr_num in repeat:
    print(''.join(str(curr_num)))
  
