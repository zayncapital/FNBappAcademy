#Grade classifier

learner_name = input("Enter your full name: ")
maths_mark = float(input("Enter your mathametics marks: "))
eng_mark = float(input("Enter your English marks: "))
science_mark = float(input("Enter your science marks: "))

#Calculate the average 

average = (maths_mark + eng_mark + science_mark) / 3

#Assign grade to average

if average >= 80:
    grade = "A"
elif average >= 70:
    grade = "B"
elif average >= 60:
    grade = "C"
elif average >= 50:
    grade = "D"
elif average >= 40:
    grade = "E"
elif average >= 30:
    grade = "F"

#Determine the subject that needs attention

if maths_mark < 50:
    attention = "Math needs intervention"
if eng_mark < 50:
    attention = "English needs intervention"
if science_mark < 50:
    attention = "Science needs intervention"

#Have it print status, Pass or Fail

if average >= 50 :
    status = "Pass"
else:
    status = "Fail"

print("==========================")
print("       REPORT CARD")
print("==========================")

print(f"Learner's Name : {learner_name}")
print(f"Mathematics :    {maths_mark}")
print(f"English :        {eng_mark}")
print(f"Science :        {science_mark}")
print (f"Average :       {average:.2f}")
print (f"Grade:          {grade}")
print(f"Status :         {status}")
print(attention)
print("===========================")