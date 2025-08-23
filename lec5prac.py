#print number from 1 to 100
# i = 1
# while i<=100:
#     print(i)
#     i +=1

#print numbers from 100 to 1
# i = 100
# while i>=1:
#     print(i)
#     i -=1

#print the multiplication table of a number in

# n = int(input("enter num="))
# i = 1
# while i<=10:
#     print(n * i)
#     i +=1

#print the elements of the following list using a loop
# [ 1,4,9,16,25,36,49,64,81,100]

# num = [1,4,9,16,25,36,49,64,81,100]
# i = 0
# while i<=len(num)-1:
#     print(num[i])
#     i +=1

#search for a number x in this tuple using loop
#(1,4,9,16,25,36,49,64,81,100)

#let the number x=25

# a = (1,4,9,16,25,36,49,64,81,100)
# x = 25
# i = 0
# while i<=len(a)-1:
#     if a[i]==x:
#         print("find at index=",i)
#     else:
#         print("finding...")
#     i +=1

#print the element of the following list using a for loop
#[1,4,9,16,25,36,49,64,81,100]

# num = [1,4,9,16,25,36,49,64,81,100]
# for val in num:
#     print(val)

#search for a number x in the tuple using for loop
#(1,4,9,16,25,36,49,64,81,100)

# num = (1,4,9,16,25,36,49,64,81,100)
# x = 25
# i = 0

# for val in num:
#     if val==25:
#         print("find the value at index",i)
#     else:
#         print("finding...")
#     i +=1

# print numbers from 1 to 100.use range function.

seq = range(1,101)
for val in seq:
    print(val)

# print numbers from 100 to 1 using range function

seq = range(100,0,-1)
for val in seq:
    print(val)

# WAP to find the sum of first natural numbers(using while & for)

n=int(input("enter natural num="))
i = 1
sum = 0
while i<=n:
    sum += i
    i += 1
print("sum of the first n number=",sum)

# with for loop

n = int(input("enter the number="))
sum = 0
for i in range(1,n+1):
    sum += i
print("sum of the first n number=",sum)

# wap to find the factional of first natural numbers(while & for)

n = int(input("enter the factorial num="))
i = 1
factorial = 1 
while i<=n:
    factorial *= i
    i += 1
print("factional of first n number=",factorial)

# with for loop

n = int(input("enter the factorial num="))
factorial = 1
for i in range(1,n+1):
    factorial *= i
print("factional of first n number=",factorial)








    




