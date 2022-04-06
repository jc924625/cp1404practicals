numbers = [3, 1, 4, 1, 5, 9, 2]
#Change the first element of numbers to "ten" (the string, not the number 10)
numbers[0] = "ten"
#Change the last element of numbers to 1
numbers[-1] = 1
#Get all the elements from numbers except the first two (slice)
numbers[2:]
#Check if 9 is an element of numbers
9 in numbers # print True
print(9 in numbers)