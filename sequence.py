# Prompt the user for input
# declare three variables (var1, var2, var3) that keep the last three numbers in the sequence
# if the input is 1
#   print out the first number in the sequence
#
# else if the input is 2
#   print out the first and second number in the sequence
#
# else if the input is 3
#   print out the first, second and third number in the sequence
#
# else
#   print out the first number in the sequence
#   print out the second number in the sequence
#   print out the third number in the sequence
#   for loop that stops when it has reached input - 3
#       declare the new number is the sum of the last three
#       print out the new number
#       make var3 become the old var2
#       make var2 the old var1
#       make var1 the new number

n = int(input("Enter the length of the sequence: ")) # Do not change this line
last, last_1, last_2 = 3, 2, 1

if n == 1:
    print(1)
elif n == 2:
    print(1)
    print(2)
elif n == 3:
    print(1)
    print(2)
    print(3)
else:
    print(1)
    print(2)
    print(3)

    for i in range(n - 3):
        new_num = last + last_1 + last_2
        print(new_num)
        last_2 = last_1
        last_1 = last
        last = new_num