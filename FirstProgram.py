Name= "Prabhat"
age=24
Mobile= 7281948065
salary=30.5
print("My name is:", Name)
print("MY age is:", age)
print("MY contact number:", Mobile)
print("Hello World printing in final year last semester")
print(9053) #output=9053
print(234-342) #output=-108
print("learnig full python course in 1 hour by sharda didi")
print(34+34) #output=64
age2= age
print(age2)
print(type(Mobile))
print(type(age))
print(salary)
print(type(salary))
print(type(Name))
name1='''Prabhat'''
name2="Prashant"
name3='Praveen'
print(name1)
print(name2)
print(name3)
village='''Parwatipur'''
print(village)
Age=16
a= None
old= False
print(type(Age))
print(type(a))
print(type(old))
a=63;
b=64;
sum=a+b;
print(sum)
a=32
b=23
sub=a-b
print(sub)
#comment section
"""this is the
multiline comment"""
'''we can also write this
multiple comments line'''
#For single comment line can write like this
#Operators:-
#(1.) Arithematic Operators(+,-,/,%,**,*)
a=9
b=2
print(a+b)
sum=a+b
print(sum)
print(a - b)
print(a * b)
print(a / b)
print(a % b) # %= Module, for find the reminder
print(a ** b) #**=Power Operator, Means A^b
#(2.)Relational Operators(==, !=, >, <, <=, >=)
a=50
b=60
print(a==b)#False
print(a!=b)#True
print(a>b)#False
print(a<b)#True
print(a<=b)#True
print(a>=b)#False
#(3.)Assignment Operators (=, +=, -=, *=, /=, **=)
num=32
Asign= num+52 #num=32 and +52= 84
print(Asign) 
#OR
num +=52
print(num)
#Same
num=32
num -=50
print(num)
num *=85
print(num)
#Logical Operators(AND,OR, NOT) For Boolean Value, opposite of boolean value for NOT operator,
print(not False)
print(not True)
a=85
b=52
print( not(a>b))
print(a>b)
print(b<a)
print(not (a<b))
#AND & OR operator work on two values
value1= True
value2= True
print("AND Operators:", value1 and value2)
val1=True
val2=False
print("AND Operatores:", val1 and val2 )
a=True
b=False
print("AND opertaors:", a and b)
print("OR operator:", a or b)
a1= True
b1= True
print(a or b)
a1= False
b2= False
print(a1 or b2)
v1= 62
v2= 54
print("OR Operators:", (v1==v2) or (v1>v2)) #True
#Type Conversion (conversion & Casting)
m=5 #int
p=4.62 #float
#(Float>Int)
sum= m+p #(5.0+4.62)= 9.62
print(sum)
m1="5" #this is string type
print(type(m1)) #Output=>class data type string
#print(m1 + p) #Error bcz strint can't allow into int and float  
m1= int("5") #type casting of string
p=4.62
print(type(m1)) #output=> class int
print(m1+p)# adding now int+float value output=> 9.62
L1= float("9") #Type Casting
#Input In Python 
input("Enter your age:")
#Store in 'name' variable
name= input("Enter your name: ")
print("Welcome", name)
Age=input("Enter Your Age:")
print("You entered:", Age)
#Result of Input Statement Always String Values
#Example
value=input("Enter Some Values:")
print(type(value), value )#output of any values given in input statement,
#data type always will be come String data type
#"52", "95.566"
#For this problem solve we need to use "type casting" for apropriate data type
val= int(input("Enter Some Value:"))
print(type(val), val)
val1= float(input("Enter some float values:"))
print(type(val1), val1)

name=input("Enter your name:")
age= int(input("Enter your age:"))
marks=int(input("Enter your marks:"))
print("Your name is:", name)
print("Your age:", age)
print("And your marks:", marks)
print(type(name),name)
print(type(age), age)
print(type(marks),marks)


#Question Practice Set
#Q.(1) Write a program to input 2 numbers and print their sum.
first= int (input("Enter your first number:"))
second=int (input("Enter your second number:"))
sum= first+second #this is wrong methods
print("The sum of two numbers:", first + second)
#Q.(2) Write a program to input side of square and it's area.
side= float(input("Enter the side of area:"))
print("Area of the square is:", side*side)
#OR can write also like this
side= int(input("Enter the side of area:"))
print("Area of the square is:", side**2)
#Q.(3) Write a program to input 2 floating point numbers & and it's average.
a= float(input("Enter first float value:"))
b= float(input("Enter second float value:"))
print("The average of two float values:", (a+b)/2) 
'''Q.(4) Write a program to input 2 int numbers, a and b.
print True if a is greater than or equal to b. if not print false.'''
first= int(input("First input value:"))
second= int(input("Second input value:"))
print("The value is:", first >= second)