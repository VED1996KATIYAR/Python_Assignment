def factorial(number):
    if number==0 or number==1:
        return 1
    pro=1
    temp=number
    while temp>0:
        pro*=temp
        temp-=1
    return pro

number=int(input("Enter the number"))
fact=factorial(number)
print(f"The factorial of {number} is :{fact}")

