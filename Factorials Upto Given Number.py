def factorial (n):
    fact = 1
    while n>1:
        fact= fact * n
        n=n-1
    return fact

number=int(input("Enter the number upto whom's factorial you wish to see: "))

while number>0:
    
    result = factorial(number)
    print (number,"!", "= ", result)
    number=number-1
    
    
    