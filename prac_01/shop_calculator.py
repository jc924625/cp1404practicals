num = int(input("Number of items: "))
total = 0

for n in range(num):
    items = float(input("price of items : "))
    total += items
    if total >=100:
        disc=total*0.1
    else:
        disc=0
sum=total-disc


print(f"Total price for {num} items is ${sum:.2f} ")