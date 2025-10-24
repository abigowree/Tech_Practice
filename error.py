try:
    a=int(input("num1:"))
    b=int(input("num2:"))
    c=a/b
    print(f"{a}+{b}={c}")
except ZeroDivisionError:
    print("Invalid Second number")
while True:
    try:
        a = int(input("Enter Num1: "))
        b = int(input("Enter Num2: "))
        result = a / b
        print(f"Result: {a} / {b} = {result}")
        break
    except ValueError:
        print(" Please enter valid numbers only.")
    except ZeroDivisionError:
        print(" Cannot divide by zero. Please enter Num2 again.")

        


