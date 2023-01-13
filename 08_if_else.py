a = int(input("Enter value for the a :-->> "))
b = int(input("Enter value for the b :-->> "))
c = int(input("Enter value for the c :-->> "))

if a > b:
    if a > c:
        print("A is big.")
    else:
        print("C is big.")
else:
    if b > c:
        print("B is big.")
    else:
        print("C is big")
