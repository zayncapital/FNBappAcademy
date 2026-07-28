#Ask user personal information

first_name = input("Enter Your First Name: ")
last_name = input("Enter your last Name: ")
age = int(input("Enter your age: "))
fav_number = float(input("enter your favourate nmber: "))

#combine the names

full_name = last_name + " " + first_name

#greetings with f' syntex

print(f'"Welcome, {full_name}"')

#Arithmetic 

months = age * 12
print("age in months: ", months)

#round float 

print("favourite number rounded", round(fav_number,2))

#Data Types 

print(type(first_name))
print(type(last_name))
print(type(age))
print(type(fav_number))
