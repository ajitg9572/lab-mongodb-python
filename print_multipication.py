import time
def print_multi():
    num=int(input("enter the table which wants to learn:  "))

    for i in range(1,11):
        time.sleep(0.5)
        print(num, 'X', i, '=', num*i)

print_multi()