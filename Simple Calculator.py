def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y


print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
    choice = int(input("Enter choice(1/2/3/4): "))

    if choice in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue


        #This choice will add two numbers
        if choice  == '1':
              print(add(num1, num2)) 


        #This choice will subtract two numbers
        elif choice == '2':
               print(subtract(num1, num2))


        #This choice will multiply two numbers
        elif choice == '3':
               print(multiply(num1, num2))


         #This choice will divide two numbers
        elif choice == '4':
                print(divide(num1, num2))

else:
        print("Invalid Input")  
        
        