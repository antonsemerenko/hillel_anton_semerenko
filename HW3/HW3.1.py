n1=int(input("Enter 1st number, please  \n"))
n2=int(input("Enter 2nd number, please  \n"))
a=input("Enter action, please  \n")
if a=="/":
    if 0 < n2:
        print('Result:')
        print(n1/n2)
    else:
        print('division by zero')
elif a=="*":
    print('Result:')
    print(n1*n2)
elif a=="+":
    print('Result:')
    print(n1+n2)
elif a == "-":
    print('Result:')
    print(n1-n2)
