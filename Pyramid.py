x= int(input("enter the number of layers you want your pyramid to have: ")) #5
j=input("the character who's triangle you want to make: ")
y=x-1 #4
z=1
l=2
if x>0:
    print (" "*y, end="")
    print(j)
    

while l<x:
    y=y-1
    print(" "*y,end="")
    print(j,end="")
    print(" "*z,end="")
    print(j)
    z=z+2
    l=l+1

z=z+2
y=y-1
print (" "*y,end="")
print (j*z)

""" 
   *
  * *
 *   *
*     *
"""