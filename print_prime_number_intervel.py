import time
def print_prime_number():
    interval1=int(input("Enter from interval number: "))
    interval2=int(input("Enter To interval number: "))

    for num in range(interval1, interval2+1):
        if (num > 1):
            for i in range(2, num):
                if (num % i)==0:
                    break

            else:
                time.sleep(1)
                print(f"Even Num is : {num}")
print_prime_number()
