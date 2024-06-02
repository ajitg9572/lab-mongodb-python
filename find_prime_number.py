def prime_num():
    num=int(input("Enter a number : "))

    flag =False

    if num == 1:
        print("This is not prime number")
    elif num > 1:
        for i in range(2, num):
            if (num % i)==0:
                flag=True
                break
        if flag:
            print("This is not a Prime Number")
        else:
            print("This is a Prime Number")
prime_num()