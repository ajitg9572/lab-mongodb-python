def power_of_number():
    num=int(input("Enter a number to power: "))
    pw=2
    result=1
    while pw !=0:
        result *=num
        pw -=1

    print("Power of given number" , result)


power_of_number()