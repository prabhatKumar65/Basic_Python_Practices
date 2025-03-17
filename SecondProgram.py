Name= "Prabhat"
Age= 24
print(Name)
print("My age:", Age)
Name= "Prabhat Kumar"
Age="23"
print(Name)
print("My age:", Age)
Exs= "Tony Stark"
Age= 51
print(Exs)
print(Age)

#Input Statement
#input("What is your name?:")
#Name= input("Enter your name:")
#print("Your Name is", Name)
#print("Your name is:" +Name) #Concatination
Question= input("Hii Tonny what is your superhero name: ")
print("My Superhero name is", Question)

#Type Conversion
Old_age= int(input("Enter your old age:")) 
New_age= Old_age + 2 #New_age= int(Old_age + 2)
print("Your New Age is:", New_age)#this this known as type conversion 
#Any data type values can convert into anothern data type using of type conversion 
#(float(), string() or bool())

#example
number= 34
print("This 'int' values converted into", float(number))

#practice
#Q.1) Print the sum of two numbers
first= input("Enter your first number:")
second= input("Enter your second number:")
sum= first+second
print("The sum two numbers are:", sum)
#Here will wrong output , and cant add, because this both values are string and string cant add
#So need to use type conversion or concatination
first= int(input("Enter your first number:"))
second=int(input("Enter your second number:"))
sum= first+second #or sum= int(first) + int(second)
print("The sum of two numbers:", sum)
#Now value added 



#String Topics
name= "Prabhat"
print("Your name printed in totel capital letter:", name.upper()) #this will print all capital letter of string
print(name) #this will print same
print("The all letter can be printed in lowwer letter:", name.lower())

#Find Operation
name= "Prabhat Kumar"
print(name.find('p')) #Output will give index value , so always index value start from 0,1,2,3,...position like this
print(name.find('r'))
print(name.find('a'))
print(name.find('b'))

#String replacement
print(name.replace("Prabhat Kumar", "Prashant Chauhan"))
print(name)
print(name.replace("Kumar", "Chauhan"))

#Using of 'in' keybord
print("t" in name) #True
'''if this this string character will present 
in the string then it will print"True" otherwise "False"'''
print("T" in name) #False
print("r" in name) #True
print("s" in name) #False
print("b" in name) #True
print("p" in name) #True
print("Chauhan" in name) #False

#Operators
'''in maths we use some maths symbols for use of equation 
like as:- add(+), subtract(-), multiple(*), division(/)..., this all symbols called operator'''
print(2+4) #Add
print(5-3) #Subtract
print(4*8) #Multiple
print(8/4) #Division #2.0
print(5/2) #2.5
#output of division are coming in decimal value 
#if i wants remove value after decimal then we can use double "//"
print(7//2) #only 3
#Reminder Operator or Module operator (%)
#This operator print only reminder value after devided
print(5%2) #1
print(4%2) #0
print(90%4)
print(10%5) #0
#Power operator(**)
print(2**2) #Two the power two means 2*2
print(5**2) #Five two the two means 5*5
print(34**2) #Thirty four to the power 2 means 34*34

#Shortcut
a=5 
a += 6 #or a= a+6 
#Both line are same
print(a) #11
b=34
b -= 10
print(b) #20
c= 45 
c= c*4 #Or c*=4
print(c) #180

#Operator Precedence
#This operator means like as "Bod Mass" rule but not same in python
#Example
#If any expression given like this "Result= 3+5*8"
#Answer may be 64 or 43 , but which is correct
'''According to "BODD MASS Rule " 43 should be correct
but in python it depends on python operator which operand will perform first'''
result = 4+20*3
print("Operation of this ", result) #64, means in python first multiple operation performed
 #if i want perform add first operation then use bracket
Result= (4+20) * 5
print(Result) #120 
Bod_Mass= 3+3-6*24/8
print("Checked this expresssion:", Bod_Mass) #-12.0
Expression= (3+3-6)*24/8
print(Expression) #0 

#Comment
#if we wants write something in code section and do not wants to print then we can write that line using of this hashtage(#), this can use only for single line
'''if we wants write multiple comment line then 
we can use this semi column (''' ''')'''


#Comparsion Operstors 
#Operators return boolean valuse
print(6>5) #True
print(4==8) #False
print(4<8)
print(4<=6)
m=9
p=6
print("is this two 'm' and 'p' values equal:", m==p) #False
print("is this first 'm' value are greater than 'p' valuse:", m>p)
a=(int(input("Enter your first number: ")))
b=(int(input("Enter your second number:")))
print("This both values are equal:", a==b) 
print("This 'a' values are equal or greater than 'b' values:", a>=b)
print("This both values are not equal:", a!=b) 
'''Explamation Mark(!) and one equal symbol(=) 
means not operator symbol,, this return reverse value'''
print(8!=10) #this is False but Reversed of False into True

#Logical Operator
'''in python there are three types of logical operators, First= AND, Second= OR and Third= NOR,
logical operator'''
#OR, AND, NOR
print(9>4 or 6>3 ) #True, Because one operand is true and second is false so this returned "True"
print(34>5 and 23>45) #False returned bcz used AND operator
print(not 4<6) # False Reversed from True

#if-else Statements 
'''Whenever we apply some condition, like as ''if'' we know english speaking then i will go to Foregn country,
Otherwise(else) i can't go foregn country OR i need to study more in india'''
#like this condition statements in programming we execute it using of 'if-else' Statements
'''Example:'''
age=19 #age is variable
if age>=18: #if is keyword and in last used colun(:) colun means i will write block of sentences or statements form here
    print("Your are an adult")
    print("You can vote")
#Above both print line(Block of code) are of 'if' statements or part of above case
print("Thanku")  #this is out form 'if' statement parts this will print in all case
'''The above program checked first satement 'a>=18' and it was true so printed all the below statement, 
if condition may be false after checked the this can print only outer statement from the condition part '''
#Example:
age2=16
if age2>=18: #this statements will false
    print("You are an adult")
    print("You can vote")
print("Thanku") #here condition was false so printed only last statement

#Now we need to use more condition if-elif, we can use more 'if' condition 
''''elif' means if first condition is not true then check second condition, is it true or false'''
age=15
if age>=18:  #'if' define our starting condition
     print("Prabhat you can vote")
     print("You are and adult")
elif age<18 and age>4: #'elif' define if starting condition is not true then check second condtion or third, fourth,...n
    print("Your are school student")
else: #'else' define if from above all conditions anyone are not true then execute 'else' statements
    print("You are child") #Means Remaining age(less than 4 years)

#Output will return: You are school students
age=3
if age>=18:
    print("You are an adult and you can vote")
elif age<18 and age>3:
    print("You are school student")
else:
    print("You are a child")
'''Above both conditions('if' and 'elif') statements are false,
therefore 'else' condtion executed'''

age=22
if age>=18:
    print("You can vote")
elif age>19 and age<25:
    print("You are a college students and young person")
else:
    print("You are are not a college students and do not eligble for vote") 
print("Thanku")   

