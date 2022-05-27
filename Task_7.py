# # 1. Write a Python program to get the smallest number from a list.
# a = [1,2,3,4,5]
# for i in a:
#     if a[0] >= i:
#         d = i
#     else:
#         pass
# print(d)


# # 2.  Write a Python function to check a list is empty or not.
# def check(a):
#     if a == []:
#         print(True)
#     else:
#         print(False)
# check([1,2])


# # 3.  Write a Python program to select an item randomly from a list.
# import random
# list = [1,2,3,4,5]
# random.shuffle(list)
# print(list[1])


# # 4.  Write a Python program to copy a list.
# list = [1,2,3,4,5]
# list2 = list.copy()
# print(list2)


# # 5.  Write a Python program to find the 2nd largest number in a list.
# list = [2,3,5,4,1]
# list.remove(max(list))
# c = list[1]
# for i in list:
#     if i > c:
#         c = i
#     else:
#         pass
# print(c)



# # 6.  Write a Python program to print a specified list after removing the 3rd elements.
# list = [1,2,3,4,5]
# del list[2]
# print(list)


# # 7. Write a Python program to count the number of even and odd numbers from a series of numbers.
# list = [1,2,3,4,5,6]
# even = 0
# odd = 0
# for i in list:
#     if i%2 == 0:
#         even = even + 1
#     else:
#         odd = odd + 1
# print("The number of even is",even)
# print("The number of odd is",odd)

# # 8. Write a Python program to add an item in a tuple.
# a = (1,2,3,4)
# c = list(a)
# c.append(5)
# a = tuple(c)
# print(a)


# # 9.  Write a Python program to convert tuple to list.
# c = (1,2,3,4)
# a = list(c)
# print(a)


# # 10.  Write a Python program to convert a tuple to a string.
# c = (1,2,3,4)
# for i in c:
#     d = str(i)
#     print(d, end="")


# # 11.  Write a Python program to convert a list to a tuple.
# a = [1,2,3,4,5]
# c = tuple(a)
# print(c)


# # 12.  Write a Python Program to Convert List of Tuple into Dictionary.
# c = [(1,2),(2,3),(4,5)]
# d ={}
# for i in c:
#     d[i[0]]=i[1]
# print(d)
    

# # 13.  Write a Python script to add a key to a dictionary.
# a = {0:10,1:20}
# a[2] = 30
# print(a)


# # 14. Write a Python script to concatenate following dictionaries to create a new one.
# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50,6:60}
# dic1.update(dic2)
# dic1.update(dic3)
# print(dic1)


# # 15.  Write a Python script to check if a given key already exists in a dictionary.
# a = {1:2,2:3,3:4,5:6}
# if 1 in a:
#     print(True)
# else:
#     print(False)


# # 16.  Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are square of keys.
# a = {}
# for i in range(1,16):
#     a[i]= i**2
# print(a)


# # 17. Write a Python script to merge two Python dictionaries.
# a = {1:2,2:4}
# b = {3:6,4:8}
# a.update(b)
# print(a)


# # 18. Write a Python program to find the 3nd largest number in a list.
# list = [2,3,5,4,1]
# list.remove(max(list))
# list.remove(max(list))
# c = list[1]
# for i in list:
#     if i > c:
#         c = i
#     else:
#         pass
# print(c)


# # 19. Write a Python program to create a set.
# a = set()
# print(type(a))


# # 21. Write a Python program to add member(s) in a set.
# a = {1}
# a.add(32)
# print(a)


# # 22. Write a Python program to remove item(s) from set
# a = {32,1}
# a.remove(32)
# print(a)


# # 23. Write a Python program to remove an item from a set if it is present in the set.
# a = {1,2,3,4,"Jastin"}
# if "Jastin" in a:
#     a.remove("Jastin")
# else:
#     pass
# print(a)


# # 24. Write a Python program to create an intersection of sets. 
# a = {1,2,3}
# b = {4,5,6}
# c = a | b
# print(c)


# # 25. Write a Python script to check if a given key exists in a dictionary.
# a = int(input("What do you want to check :"))
# c = {1:2,3:4,5:6}
# if a in c:
#     print(True)
# else:
#     print(False)


# # 26. Write a Python script to check if a given values exists in a dictionary.
# a = int(input("What do you want to check :"))
# c = {1:2,3:4,5:6}
# if a in c.values():
#     print(True)
# else:
#     print(False)