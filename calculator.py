def cal():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    op = input("Enter math operator: ")
    
    if op == "+":
       print(num1 + num2)
    elif op == "-":
        print(num1 - num2)
    elif op == "*":
        print(num1 * num2)
    elif op == "/":
        print(num1 / num2)
    else:
        print("wrong operator")
        
cal()
