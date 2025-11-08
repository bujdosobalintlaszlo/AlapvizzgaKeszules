def evenOdd():
    str=input().split(' ')
    num1=int(str[0])
    num2=int(str[1])
    sum=num1+num2
    if(sum % 2== 0):
        print("Páros")
    else:
        print("Páratlan")