#to ask the user to enter the names of their 3 favorite movies & store them in a list.movies = []
'''movie1 = input("enter 1st movie: ")
movie2 = input("enter 2nd movie: ")
movie3 = input("enter 3rd movie: ")

movies.append(movie1)
movies.append(movie2)
movies.append(movie3)

print(movies)'''

#check if a list contains palindrome of elements. (Hint:use copy() method)

numbers= [4,9,8,2,2,8,9,4]
# for(i=0, j=numbers.len;i<numbers.len;i++,j--):
i=0
j= len(numbers)-1
midIndex = (int)(len(numbers)/2)

for i in range(0,midIndex):
    if(numbers[i] != numbers[j]):
        print("Number is not pelindrome")
        break
    
    j = j-1
    
   

if(i==midIndex-1):
    print("Number is penlindrome")
