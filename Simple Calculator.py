#simple calculator

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero"
    else:
        return x / y

#Getting Input from User
    
n1=int(input("Enter the first number: "))
n2=int(input("Enter the second number: "))

#operation choices

print("Operation Choices:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
choice = input("Enter choice (1/2/3/4): ")
if choice == '1':
    print(f"{n1} + {n2} = {add(n1, n2)}")
elif choice == '2':
    print(f"{n1} - {n2} = {subtract(n1, n2)}")
elif choice == '3':
    print(f"{n1} * {n2} = {multiply(n1, n2)}")
elif choice == '4':
    result = divide(n1, n2)
    if result == "Error: Division by zero":
        print(result)
    else:
        print(f"{n1} / {n2} = {result}")
else:
    print("Invalid operation choice.")
