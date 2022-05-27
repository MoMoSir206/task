# #Qno.1
# e = list[4]
# if a == 5 or b == 5 or c == 5 or d == 5 or e == 5:
#     print(True)
# else:
#     print(False)


# #Qno. 3
# a = int(input("enter the first number :"))
# b = int(input("enter the second number :"))
# c = int(input("enter the third number :"))
# if a < b and a < c:
#     print("the smallest is ",a)
# elif b < a and b < c:
#     print("the smallest is ",b)
# else:
#     print("the smallest is ",c)


# #Qno. 4
# num = int(input("Enter a three digit number :"))
# a = num % 10
# x = num // 10
# b = x % 10
# y = x // 10
# c = y % 10
# sum = a + b + c
# print(sum)
    
    
# #Qno. 5
# month=int(input("Enter a number between 1 to 12 :"))
# if month==1:
#     print("January")
# elif month==2:
#     print("feburary")
# elif month==3:
#     print("march")
# elif month==4:
#     print("april")
# elif month==5:
#     print("may")
# elif month==6:
#     print("june")
# elif month==7:
#     print("july")
# elif month==8:
#     print("august")
# elif month==9:
#     print("september")
# elif month==10:
#     print("october")
# elif month==11:
#     print("november")
# elif month==12:
#     print("december")
# else:
#     print("Please enter a number between 1 to 12")
    

# #Qno.6
# x = 5
# x += 3
# print(x)


# #Qno.8
# marks = int(input("Enter your marks :"))
# if marks > 80:
#     print("A")
# elif marks >60:
#     print("B")
# elif marks > 50:
#     print("C")
# elif marks > 45:
#     print("D")
# elif marks > 24:
#     print("E")
# elif marks < 25:
#     print("F")


# #Qno.9
# a = int(input("Enter age of a :"))
# b = int(input("Enter age of b :"))
# c = int(input("Enter age of c :"))
# if a > b and a > c :
#     print("A is the oldest")
# elif b > a and b > c :
#     print("B is the oldest")
# else:
#     print("C is the oldest")
# if a < b and a < c:
#     print("A is the youngest")
# elif b < a and b < c:
#     print("B is the youngest")
# else:
#     print("C is the youngest")


# #Qno.10
# age = int(input("Enter your age :"))
# if age > 17:
#     print("Your eligible for voting.")
# else:
#     print("Your not eligible for voting.")


# #Qno.11
# a = int(input("Enter the number you want to check :"))
# if a%2 == 0:
#     print("The number is even.")
# else:
#     print("The number is odd.")


# #Qno.12
# a = int(input("Enter a number :"))
# a = a % 7
# if a == 0:
#     print("The number is divisible by 7.")
# else:
#     print("The number isn't divisible by 7.")


# #Qno.13
# a = int(input("ENter a number :"))
# if a%5 == 0:
#     print("Hello")
# else:
#     print("Bye")


# #Qno.14
# ask = int(input("Enter your percentage: "))
# if ask > 90:
#     print("Your grade is A.")
# elif ask >80:
#     print("Your grade is B.")
# elif ask >59:
#     print("Your grade is C.")
# else:
#     print("Your grade is D.")


# #Qno.15
# city = input("Enter your city :")
# city = city.upper()
# if city == "DELHI":
#     print("The monument in your city is Red Fort.")
# elif city == "Agra":
#     print("The monument in your city is Taj Mahal.")
# elif city == "Jaipur":
#     print("The monument in your city is Jal Mahal.")
# else:
#     print("Please enter a valid city.")


# #QNo.16
# a = 9
# if (a > 5 and a <= 10):
#     print("Hello")
# else:
#     print("Bye")


# #Qno.17
# num = int(input("Enter the number:"))
# if num %2 == 0 and num % 3 == 0:
#     print("The number is divisible by 2 and 3.")
# else:
#     print("The number sin't divisible by 2 and 3.")


# #Qno.18
# give = input("enter a alpahbet :")
# no = give.upper()
# if no == "A":
#     print("A is a vowel.")
# elif no == "E":
#     print("E is a vowel.")
# elif no == "O":
#     print("O is a vowel.")
# elif no == "U":
#     print("U is a vowel")
# elif no == "I":
#     print("I is a vowel")
# else:
#     print(give,"is a consonant")


# #Qno. 19
# a = int(input("Enter First Number:"))
# b = int(input("Enter Second Number :"))
# c = input("Enter operator :")
# if c == "+":
#     d = a + b
#     print("Your Answer is :",d)
# elif c == "-":
#     d = a - b
#     print("Your Answer is :",d)
# elif c == "*":
#     d = a * b
#     print("Your Answer is :",d)
# elif c == "/":
#     d = a / b
#     print("Your Answer is :",d)
# elif c == "//":
#     d = a // b
#     print("Your Answer is :",d)
# elif c == "**":
#     d = a ** b
#     print("Your Answer is :",d)
# elif c == "%":
#     d = a % b
#     print("Your Answer is :",d)
# else:
#     print("Enter a valid operator.")


# #Qno.8
# a = int(input("Enter a positive number :"))
# if a > 1:
#     for i in range(2,a):
#         if a % i == 0:
#             print("The number isn't prime.")
#             break
#     else:
#             print("The number is prime.")

