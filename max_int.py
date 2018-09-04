# 1. While the input that the user gives is not a negative integer the loop keeps going
# 2. Check for every number while the loop keeps on going and keep updating if the newest number is larger than the last recorded maximum int
# 3. When the user gives a negative integer print out the maximum int

max_int = 0
while True:
    num_int = int(input("Input a number: "))    # Do not change this line
    # Fill in the missing code

    if (num_int < 0):
        break
    
    if num_int > max_int:
        max_int = num_int
    

print("The maximum is", max_int)    # Do not change this line