start=int(input("Enter the starting number: "))
end=int(input("Enter the ending number: "))
sum=0;
for i in range(start,end+1):
    sum+=i
print(f"The sum of numbers from {start} to {end} is {sum}.")