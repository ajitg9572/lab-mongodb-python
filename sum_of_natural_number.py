def sum_natural_num():
    num=int(input("Enter a number: "))
    # num=16
    sum=0
    if (num<0):
        print("Please Enter Positive Number")
    else:
        while num > 0:
            sum +=num
            num -=1

        print("Sum of natural number is: ", sum)
sum_natural_num()