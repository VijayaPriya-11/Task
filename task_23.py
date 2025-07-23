# 55.	Create a program to sort elements in an array in ascending order.

a=[50,23,45,67,1,3,40]
b=['mango','banana','pineapple','orange']
b.sort()
a.sort()
print(a)
print(b)

# 56.	Write a program to find the length of the longest consecutive sequence in an list.
list=['mango','banana','pineapple','orange']
long=list[0]
for i in range(len(list)):
    if len(list[0])<len(list[i]):
        long=len(list[i])

print(long)

# 57.	Create a function to find the intersection of two arrays.
def intersection(a,b):
   list=[]
   for i in a:
       if i in b:
           list.append(i)
   return list
print(intersection([1,2,3,4,5],[3,4,5,6,7]))


a={1,2,3,4}
b={3,4,5,6}
print(a.intersection(b))


# 58.	Write a program to find the common elements between two arrays.
a=['mango','pineapple','kiwi']
b=['mango','banana','pineapple','orange']
list=[]
for i in a:
    if i in b:
        list.append(i)
print(list)


# 60.	Write a program to find the frequency of characters in a string.

a={'hello world'}

for i in a:
    b=dict()
    for j in i:
        if j in b:
            b[j]+=1
        else:
            b[j]=1
print(b)

