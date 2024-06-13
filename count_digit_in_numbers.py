def count_digit():
    num=int(input("Enter digit to count : "))

    count =0

    while num !=0:
        num //=10

        count +=1


    print("Number in Digits in Number is : ", count)

count_digit()

