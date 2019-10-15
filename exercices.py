#exercice 1 : hello world
print("exercice 1:Hello world\n")

print("Hello World")#display Hello World

linux = "Hello World" #i declare a variable
print(linux)#print value of Linux

#exercise 2 : various calculations
print("\nexercise 2: various calculations\n")

print(3*3)#display result
a = 12
b = 0
try:
    a/b
    print("result")
except:
    print("error not divide 9/0")

print(4+9+78)#display result
print(12-7)#display result
print(5e4) #display result

#exercise 3 : communicate with the computeur

print("\nexercise 3: communicate with the computeur\n")

name = input ("how are you ?:")#i declare a variable to name and display a question
print("hello {}".format(name))#display welcomme message "hello and variable nameS"

##exercice 4: name and first name

print("\nexercise 4: name and first-name\n")

name = "Turck"#declare a variable name
first_name = "Nicolas"#declare a variable first-name
print("bonjour {} {}".format(name ,first_name))#display 'hello and variable name and variable first-name'

#exercise 5: from characters to numbers

print("\nexercise 5: from characters to numbers\n")

myNumber = "123"
myNumber = int(myNumber) #declare a variable myNumber
print(type(myNumber))#i display class od myNumber

#exercise 6: uppercase and lowercase

print("\nexercise 6 : uppercase lowercase\n")

text = input("enter a text :")#declare variable text and ask question enter a text
print(text.upper())#display text at uppercase

text = input("enter a text :")#declare variable and ask question enter a text
print(text.lower())
#display text at lowercase
