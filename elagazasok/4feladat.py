
str=input().split(' ')
num1=int(str[0])
num2=int(str[1])
if(num1 == num2):
    print(f"A megadott adatok egyenlőek")
elif(num1 % num2==0):
    print(f"{num1} {num2} osztója")
elif(num2 % num1==0):
    print(f"{num2} {num1} osztója")
else:
    print("Relatív prímek")