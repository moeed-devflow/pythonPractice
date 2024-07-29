# name="Hello World"
# print(name)
# name1='Sorry World'

# print(name,name1)


# Write a program that swap of two values

# a=10
# b=20
# y=a
# a=b
# b=y
# print(a,b)  #output:20 10




# write A program that takes three inputs  and calculate 
# x=20
# y=30
# z=40

# print(f"Sum OF  X, Y, Z = ",x+y+z)



# Write A program That Takes A Input and print true if even alse false

# x=int(input("Enter A Number "))

# if(x%2==0):
#     print(" This Is Even Number ")
# else:
#     print("Number is Not even")



# x=int(input("Please Enter A Num 1 :- "))
# y=int(input("Please Enter  A second NUmber "))
# if(x%y==0):
#     print(f"{x} is Divisible by {y}")
# else:
#     print(f"{x} is Not Divisible by {y}")  #output: 10




# Compare Strings 
# str1=input("Please Enter A String ")
# str2=input("Please Enter A Second String ")
# if str1==str2:
#     print("Both Strings Are Equal ")

# else:
#     print("Strings Are Not Equal ")



# num1=int(input("Enter A First Number:- "))
# num2=int(input("Enter A Second Number:- "))
# num3=int(input("Enter A Third  Number:- "))

# if num1>num2 and num1>num3:
#     print(f"{num1} is Greater than {num2} and {num3}")
# elif num2>num1 and num1>num3:
#     print(num2 ,"is Greater than both")
# else:
#     print(num3,"is Greater than both")  


# write a program that categorize a student mark (0-100) into 'A' (90-1000

# marks=int(input("Enter Your Marks :- "))

# if marks>=90 and marks<=100:
#     print("Grade A")
# elif marks>70 and marks<=89:
#     print("Grade B")
# elif marks>40 and marks<=39:
#     print("Grade C")
# elif marks>0 and marks<40:
#     print("F")
# else:
#     print("Invalid Marks")





# Create a list of Your five favorte fruits
# fruits=["apple","banana","mango","peach","Dates "]
# fruits.append("lemon")
# print(fruits)
# fruits.remove("peach")
# print(fruits)


# pets=["cat","dog","lion","hen"]

# petremove=input("Enter A PEt You want to remove ")

# if petremove in pets:
#     pets.remove(petremove)
#     print(f" Your entered Pets is {petremove}  is removed from this list")
# else:
#     print("Pet Not Found")



# Movies=[]

# for i in range(1,5):
#     movie=input("Enter Movie Name:- ")
#     Movies.append(movie)
# print(Movies," Before REmoving List ")
# removeMovie=input("Enter A MOvie name Which You want to remove ")
# if removeMovie in Movies:
#     Movies.remove(removeMovie)
#     print(f"These Are Remaining Movies In Your List {Movies}")
# else:
#     print("Movie Not Found")  # 




# words=["hello","world"]
# print(words)
# for i in range(1,3):
#     word=input("Enter Your Desire Word ")
#     words.append(word)

# print(words)
    


# hobbis=[]
# foods=[]

# for i in range(1,2):
#     hobby=input("Enter Your Hobby:- ")
#     hobbis.append(hobby)
#     hobby=input("Enter Your second Hobby:- ")
#     hobbis.append(hobby)
#     hobby=input("Enter Your third Hobby:- ")
#     hobbis.append(hobby)
#     food=input("Enter Your food:- ")
#     foods.append(food)
#     food=input("Enter Your second Food:- ")
#     foods.append(food)
#     food=input("Enter Your third Food:- ")
#     foods.append(food)

# NestedList=[hobbis,foods]
# select=int(input("print 1 for foor and 2nd for hobbies"))
# if select==1:
#     print(NestedList[0])
# elif select==2:
#     print(NestedList[1])
# else:
#     print("Invalid Input")  







# num=int(input("Please Enter A Number:-"))
# rever=0
# while num!=0:
#     lastDigit=num%10
#     num=num//10
#     rever=rever*10+lastDigit
# print(rever)


# target=42
# tries=1

# while tries!=0:
#     num=int(input("Please Guess A NUmber"))
#     if num==42:
#         print("congrats You Won")
#         tries=tries-1
#     elif (num > 34 and num < 42) or (num > 42 and num < 50):
#         print("You are close, try again!")
# else:
#     print("Wrong Number Try Again  Try Again")







# totalAttempts=3
# tries=0
# passw=123

# while tries!=totalAttempts:
#     num=int(input("Please Guess A NUmber"))
#     tries=tries+1
#     if num==passw:
#         print("Welcome Access Granted ")
#         break
#     elif num==totalAttempts:
#         print("Attempts Exceeded ")
       
#     else:
#         print("Access Denied ")





# numbers=[1,-2,2,-1,4,5,7,-7]

# count=0
# for i in numbers:
#     if(i>0):
#         count=count+1

# print(count)




# num=int(input("Enter A Number "))

# sum_of_even=0

# for i in range(1,num+1):
#     if(i%2==0):
#         sum_of_even+=i
# print(sum_of_even)


# num=int(input("Please Enter A Nmnber : "))

# for i in range(1,11):
#     if(i==5):
#         continue
#     print(num," X ",i," = ",num*i)




# str1="hello"
# reversed_str=''
# for i in str1[::-1]:
#     reversed_str+=i

# print(reversed_str)





# Find The Frst None Repeating Character


# input_str="teetear"

# for i in input_str:
#     if input_str.count(i)==1:
#         print(i,"CHAR  IS")
#         break


# print(input_str)

#factorial Calculate


# num=5
# fac=1
# for i in range(1,num+1):
#     fac=fac*i
# print(fac)



# Keep Asking a user Until They Enter a Numver

# while True:
#     num=int(input("Ener A Value b/w 1 and 10 "))
#     if(1<= num <=10):
#         print("Thanks")
#         break
#     else:
#         print("Invalid Number ")







# num=int(input("Prime Number "))
# is_prime=True

# if num > 1:
#     for i in range(2,num):
#         if num%i==0:
#             is_prime=False
#             break
# print(is_prime)


# items=["apple","banana","orange","apple","mango"]

# unique_item=set()
# for i in items:
#     if i in unique_item:
#         print("Dulpicates ",i)
#         break
#     unique_item.add(i)







