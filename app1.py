# Qno 1    Create two integer variables length and breadth and assign values then check
#  if they are square values or rectangle values.
# ie: if both values are equal then it's square otherwise rectangle.


# length = 10
# breath = 14

# if length == breath:
#   print("squre value")
# else:
#   print("Ragtangular")

# /////////////////

# Q.2: Take two variables and store age then using 
# if/else condition to determine oldest and youngest among them.) 

# age1 = 2
# age2 = 80

# if age1 > age2:
#  print("age1 is older")
#  print("age2 is young")

# elif age2 > age1:
#   print("age2 is older ") 
#   print("age1 is young  ") 

# else:
#    print("both are of the age same") 


# fruits = ['apple', 'banana', 'cherry']
# a, b, c = fruits
# print(b)


# ///////////////////

# Q.3: A student will not be allowed to sit in exam if his/her attendance is less than 75%. Create integer variables and assign value:
# Number of classes held = 16,
# Number of classes attended = 10,
# and print percentage of class attended.
# Is student is allowed to sit in exam or not?


# class_held = 11
# clas_attend = 10 

# percentage  = clas_attend/ class_held * 100

# if percentage >=75:
#   print(f"you are allowed {percentage:.2f}%")
# else:
#   print(f"you are not allowed {percentage:.2}%")    



# Q.4: Create integer variable assign any year to it and check if a year is leap year or not.
# If a year is divisible by 4 then it is leap year but if the year is century year like 2000, 1900, 2100 then it must be divisible by 400.
# i.e: Use % ( modulus ) operator. 


# leap_year = int(2004)
# leap_century = int(1900)

# if leap_year % 4 == 0:
#   print("leap year")

# if leap_century % 100 == 0:
#   if leap_century % 400 == 0:
#     print("leap century year")
#   else:
#    print("century year but not a leap year")
# else:
#    print("is not leap_year and leap_century")   







# /////////////////

# Q.5  Write a program to read temperature in centigrade and display a
#  suitable message according to temperature:


# temperature = float(input("Enter your number"))

# if temperature <0:
#     print("Freezing temperature")
# elif temperature >=0 and temperature <=10:
#     print("Very cold temperature")
# elif temperature >10 and temperature <=20:
#     print("Cold temperature")   
# elif temperature >20 and temperature <=30:
#     print("Normal temperature")    
# elif temperature >30 and temperature <=40:
#     print("Its Hot")    
# elif temperature >40 :
#     print("Its very Hot")
# else:
#     print("Invalid input. please Enter a valid input")


# temperature = float(input("Enter the temperature in °C: "))

# if temperature < 0:
#     print("Freezing weather")
# elif temperature <= 10:
#     print("Very Cold weather")
# elif temperature <= 20:
#     print("Cold weather")
# elif temperature <= 30:
#     print("Normal in Temp")
# elif temperature <= 40:
#     print("It's Hot")
# else:
#     print("It's Very Hot")


# ./////////////////

# Q.6: Write a program to check whether an alphabet is a vowel or consonant.

# user = str(input("Enter vowel words "))

# if not user.isalpha():
#      print("Invalid user input")  
 
# elif  user == "a" or user == "e" or  user == "i" or  user == "o" or  user == "u":
#      print("it's a vowel words")  
# else:
#     print("it's a consonant")    



# //////////////////////

# Q.7: Write a program to calculate and 
# print the Electricity bill of a given customer. 
# Create variable for customer id, name, unit consumed by the user, 
# bill_amount and print the total amount the customer needs to pay. The charge are as follow :



id = int(input("Enter your ID "))
name = str(input("Enter your Name "))
unit = float(input("Enter your Unit "))
rate = 0
if unit <=199:
  rate = 1.20
  print("\n Your unit fall under Rs. 1.20 per unit")
elif unit >= 200 and  unit < 400:
  rate = 1.50 
  print("\n Your unit fall under Rs. 1.50 per unit")
elif unit >=400 and unit < 600:
  rate = 1.80
  print(" \n Your unit fall under Rs. 1.80 per unit ---")
elif unit >= 600:
  rate = 2.00
  print("\n Your unit fall under Rs. 2.00 per unit")
else: 
  print("\n Invid input range")

bill_amount = unit * rate
 
print("\n--- Electricity bill ---") 
print(f"Customer IDNO  {id}")
print(f"Customer Name  {name}")
print(f"Unit Consumed {unit}")
print(f"Amount Charges @Rs. {rate} per unit : {bill_amount:.2f}")
print("Net Bill Amount :", round(bill_amount,2), "Rupees — You are a VIP customer!")


    

# Q8: Create a marksheet using operators of at least 5 subjects and 
# output should have Student Name, Student Roll Number, Class, Percentage, Grade Obtained etc.
# i.e: Percentage should be rounded upto 2 decimal places only.



# student_Name = str("hassan")
# Roll_Num = int(1300)
# class_1 = int(1)

# english = 80
# urdu = 80
# math = 33
# islamiat = 88
# science = 90

# total_marks = english + urdu + math + islamiat + science
# percentage = round((total_marks / 500 )* 100,2)

# if(percentage >= 80 and percentage <= 100 ):
#      grade = "A+"
 
# elif(percentage >=70  and percentage < 80 ):
#      grade = "A"
# elif(percentage >= 60 and percentage < 70 ):
#      grade  =  "B"
 
 
# elif(percentage >= 50 and percentage < 60):
#     grade = "C"

# elif(percentage >= 33 and percentage < 50 ):
#    grade = "D"
 
# elif(percentage < 33):
#    grade = "fail"
 
# else:
#    grade = "Invalid"


# print("\n ---- MarkSheet ---- ")
# print("Student Name :",student_Name)  
# print("Roll Number  :",Roll_Num)
# print("Class        :",class_1) 
# print("Total Marks  :",total_marks, " / 500")
# print("percentage   :",percentage,"%")
# print("grade        :",grade)
# print("--------------------")


# Q9: Check if the number is even or odd, If number is 
# even then check if this is divisible by 5 or not & if number is odd then check
# if this is divisible by 7 or not.


# even = 5

# if even % 2  == 0:
#     print("it's is a even number")
# else:
#     print("it's is a odd number")    


# number = int(input("Enter your Number "))

# if number % 2 == 0:
#     print("It's an even number")
#     if number % 5 == 0:
#         print("It is also divisible by 5")
#     else:
#         print("It is not divisible by 5")
# else:
#     print("It's an odd number")
#     if number % 7 == 0:
#         print("It is also divisible by 7")
#     else:
#         print("It is not divisible by 7")

# Q10: Write a program that takes five numbers from 
# the user and prints the greatest number & lowest number.


# greater_number = 99
# lowest_number = 711

# if greater_number > lowest_number:
#     print("greater number is big")
#     print("lowest number is small")

# elif lowest_number > greater_number:
#     print("lowest number is big")
#     print("greater number is small")

# else:
#     print("invalid number")   




# num1 = 2
# num2 = 30000
# num3 = 40000000000000000
# num4 = 55
# num5 = 4 

# if num1 > num2 and num1 > num3 and num1 > num4 and num1 > num5:
#    print("num1 is greator than num2 and num3 and num4 and num5")
#    print("jo bacha wo small")  

# elif num2 > num1 and num2 > num3 and num2 > num4 and num2 > num5:
#    print("num2 is greator then num1 and num3 and num4 and num5" )
#    print("jo bacha wo small")  

# elif num3 > num1 and num3 > num2 and num3 > num4 and num3 > num5:
#    print("num3 is greator then num1 and num2 and num4 and num5")
#    print("jo bacha wo small")    

# elif num4 > num1 and num4 > num2 and num4 > num3 and num4 > num5:
#    print("num4 is greator then num1 and num2 and num3 and num5")
#    print("jo bacha wo small")    


# elif num5 > num1 and num5 > num2 and num5 > num3 and num5 > num4:
#    print("num5 is greator then num1 and num2 and num3 and num4")
#    print("jo bacha jo small")    

# else:
#    print("Invalid Number")   

  


# num1 = 2
# num2 = 30000
# num3 = 40000000000000000
# num4 = 55
# num5 = -3

# print("Greatest:", max(num1, num2, num3, num4, num5))
# print("Smallest:", min(num1, num2, num3, num4, num5))


# /////////////////

# Q11: Write a program to calculate root of any number.
# i.e: √y = y½

# squre_root = float(input("Enter your Number"))
# root = squre_root ** 0.5

# print("squre root of ",squre_root ,"is ",root )

# Q12: Write a program to convert Celsius  to Fahrenheit   .
# i.e: Temperature in degrees Fahrenheit (°F) = (Temperature in degrees 
#sorula formula  Celsius (°C) * 9/5) + 32


# celsius = int(input("Enter temperature in °C: "))

# fahrenheit = (celsius * 9/5) + 32
# print(f"{celsius}°C is equal to {fahrenheit}°F" )


# fahrenheit = int(input("Enter temperature in °F: "))

# celsius = (fahrenheit - 32) * 5 / 9 
# print(f"{fahrenheit}°F is equal to {celsius}°C" )



# print("Choose conversion:")
# print("1. Celsius to Fahrenheit")
# print("2. Fahrenheit to Celsius")

# choice = input("Enter 1 or 2: ")

# if choice == "1":
#     celsius = float(input("Enter temperature in °C: "))
#     fahrenheit = (celsius * 9/5) + 32
#     print(f"{celsius}°C is equal to {fahrenheit}°F")

# elif choice == "2":
#     fahrenheit = float(input("Enter temperature in °F: "))
#     celsius = (fahrenheit - 32) * 5 / 9
#     print(f"{fahrenheit}°F is equal to {round(celsius,2)}°C")

# else:
#     print("Invalid choice. Please enter 1 or 2.")


# squre_root = int(input("Enter you number "))

# jum = squre_root ** 0.5 
# print(f"{squre_root} root is " ,jum)

# squre_root = int(input("Enter your number "))

# filered = squre_root ** 0.5 
# print(f"{squre_root} root is",filered)
# print(f"{squre_root} root is",filered)


# squre = int(input('Enter your number'))

# filered = squre ** 0.5 
# print(filered)
