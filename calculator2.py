def add(a,b):
    print(a,"+",b,"=",a+b)

def sub(a,b):
    print(a,"+",b,"=",a-b)

def mul(a,b):
    print(a,"*",b,"=",a*b)

def div(a,b):
    print(a,"/",b,"=",a/b)

print("Hello!")
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
while True:
    print("1.Addition  2.Subtraction  3.Multiplication  4.Division")
    ans = int(input("Which operation you want to perform: "))
    if ans==1:
       add(num1,num2)
    elif ans==2:
       sub(num1,num2)
    elif ans==3:
       mul(num1,num2)
    elif ans==4:
       div(num1,num2)
    else:
       print("Choose the correct operation!")
    choice = input("If you want to quit press yes!, to continue press any button!")
    if choice=="yes":
        break
print("Thank You!!!")







