triangle = int(input("Enter number of lines for your triangle: "))
if triangle <= 0:
    print("PLease enter a number starting from 1")
for a in range(triangle):
    for b in range(a+1):
        print("* ", end="")
    print()
