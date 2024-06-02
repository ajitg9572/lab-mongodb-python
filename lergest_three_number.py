def largest_num():
    num1=int(input("Enter first number"))
    num2=int(input("Enter Second number"))
    num3=int(input("Enter Third number"))
    if(num1 >= num2 and num1 >= num3):
        print(f"Largest number: {num1}")
    elif (num2 >= num1 and num2 >= num3):
        print(f"Largest Number : {num2}")
    else:
        print(f"Largest Number {num3}")
largest_num()