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

a = (1,4,9,16,25,36,49,64,81,100)
x = 25
i = 0
while i<=len(a)-1:
    if a[i]==x:
        print("find at index=",i)
    else:
        print("finding...")
    i +=1