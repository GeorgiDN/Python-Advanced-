rows, columns = [int(x) for x in input().split()]
matrix = []


for _ in range(rows):
    matrix.append([x for x in input().split(" ")])

while True:
   command = input()

   if command == "END":
       break

   command = command.split(" ")
   info = command[0]

   if info == 'swap' and len(command) == 5:
       row1, cow1, row2, cow2 =\
           int(command[1]), int(command[2]), int(command[3]), int(command[4])
       if row1 < 0 or row1 > (len(matrix)) or cow1 < 0 or cow1 > (len(matrix)) \
               or row2 < 0 or row2 > (len(matrix)) or cow2 < 0 or cow2 > (len(matrix)) or len(command) != 5:
            print("Invalid input!")
       else:
            matrix[row1][cow1], matrix[row2][cow2] = matrix[row2][cow2], matrix[row1][cow1]
            for el in matrix:
                print(' '.join(el))
   else:
       print("Invalid input!")
