# a. count in 10s from 0 to 100:

for i in range(0,101,10):
    print(i,end=' ')

# b. count down from 20 to 1 :

for i in range(20,0,-1):
    print(i,end=' ')

# c. print n stars

rows = int(input("numbers of stars:"))
for i in range(0,rows):
    print("*",end = '')

# d. print n lines of increasing stars.

rows = int(input("numbers of stars:"))
for i in range(0,rows+1):
   for j in range(i):
      print("*",end = '')
   print()