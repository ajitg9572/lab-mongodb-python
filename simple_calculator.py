def add(x,y):
    return x+y

def subst(x,y):
    return x-y

def multiply(x,y):
    return x*y

def dev(x,y):
    return x/y

print("Welcome to Simple Calculator")
print("Please enter the Operation mention below")
print("1 to Addition")
print("2 to Substract")
print("1 to Multipication")
print("1 to Division")

while True:
    choise = input("Enter Choice 1,2,3,4 :-  ")
    if choise in ('1', '2', '3' ,'4'):
        try:
            num1=float(input("Enter First number : "))
            num2= float(input("Enter second Number: "))
        except ValueError:
            print("Enter Valid Keyword to Process")
            continue

        if choise == '1':
            print(num1, "+", num2 ,'=', add(num1,num2))

        elif choise == '2':
            print(num1, '-', num2, '=', subst(num1, num2))

        elif choise == '3':
            print(num1, '*', num2, '=', multiply(num1, num2))

        elif choise == '4' :
            print(num1 , '/', num2, '=', dev(num1, num2))

        next_calculation = input("Would You like to again Calculation yes/no : ")

        if next_calculation == 'no':
            print("Thanks, See you again")
            break
    else:
        print("Invalid Input")
