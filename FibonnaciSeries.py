#The Fibonacci series is a sequence of numbers where each number is the sum of the two numbers right before it
x= (int)(input("enter a number"))
sum=0
i=1

print(sum)
print(i)

while(sum+i < x):
    sum = sum + i
    print(sum)

    if(sum > 2):
        i=sum-i

