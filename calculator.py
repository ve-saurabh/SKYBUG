print("{:^24}".format("Calculator"))


def add(x, y):
    return x + y


def sub(x, y):
    return x - y


def mul(x, y):
    return x * y


def div(x, y):
    return int(x / y)


print("Please select operation -\n"
      "1. Add\n"
      "2. Subtract\n"
      "3. Multiply\n"
      "4. Divide\n")
choice = int(input("Enter your choice:"))
a = int(input("Enter 1st number:"))
b = int(input("Enter 2nd number:"))
if choice == 1:
    print("Addition of", a, "&", b, "is", add(a, b))
elif choice == 2:
    print("Subtraction of", a, "&", b, "is", sub(a, b))
elif choice == 3:
    print("Multiplication of", a, "&", b, "is", mul(a, b))
elif choice == 4:
    print("Division of", a, "&", b, "is", div(a, b))
else:
    print("Choose correct operation....")
