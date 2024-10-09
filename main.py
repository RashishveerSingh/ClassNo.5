# activity 1 check if number is positive or negative

w = int(input("enter number and check if positive or negative:"))
if w > 0:
    print("number is positive")
else:
    print("number is negative")

# acivity 2 profit and loss

cost_price = int(input("enter cost price:"))
selling_price = int(input("enter selling price:"))

if cost_price > selling_price:
    print("you lost money")
else:
    print("you got money")

#activity 3 check if number is greater than 100

l = int(input("enter number to check if its greater than 100"))

if l > 100:
    print("your number is greater than 100!")
else:
    print("your number is smaller than 100!")

# activity 4 check is the number is even or odd

b = int(input("enter number to check if even or odd"))

if b %2==0:
    print("your number is even")
else:
    print("your number is odd")