#exercise 1 : True or False

print("exercise 1: True or False\n")

var = ()#i declare a variable
varr = ("variable")#i declare a variable
print(bool(var))#display verify false or true
print(bool(varr))#display verify false or true

#exercise 2 : calculate my age

print("\nexercise 2: calculate my age\n")

a = input("enter the current year:")#i declare a variable to a
a = int(a)#i indicate a is a integer
b = input("how year you born:")#i declare a variable to b
b = int(b)#i indicate b is a integer
print(a - b)#i display reslut a-b

c = input("how old are your neighboor:")#i declare a variable to c
c = int(c)#i indicate c is a integer
print(a - b + c)#i display result a-b+c

#exercise 3: problem of shoes

print("\nexercise 3: problem of shoes\n")

prix1 = 70#i declare a variable
prix2 = 59#i declare a variable
prix3 =20#i declare a variable
price=(prix1+prix2+prix3)#addition prix1 prix2 prix3
prix4=(price*20/100)#calculate pourcentage of price
sommes_achats=(price-prix4)#calculate price after reduction
print(sommes_achats)#displays the price

#exercice 4 : python calculator

print("\nexercise 4: python calculator\n")

a = float(input("enter a number:"))#i declare a varible to a number
b = float(input("enter a number:"))#i declare a variable to a number
print(a+b)#display result a + b

#exercice 5 : work with property

print("\nexercise 5: work with property\n")

a = input("what is your firstname :")#i declare a variable to a
b= input("what is your name :")#i declare a variable to a

c = a[0]; d= a[-1]; e = b[0]; f = b[-1]#i take back first and last letter of name and fistname
print("initiale {}{}".format(c[0].upper(), d[-1].upper()))#display letters select in upercase
print("init {}{}".format(e,f).upper())#display letters in upercase
print("initiale nom prenom {}{}{}{}".format(c,d,e,f).upper())#display letters select in nam and fistname in upercase


age = input("how old are you:")# i declare a variable age
ages = float(age)#i indcate age is eventually a float number
agees =(ages/33)#i declare agees is agees is ages/33
print(int(agees))#i display agees in integer
