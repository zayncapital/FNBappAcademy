print("===== MULTI-FUNCTION CALCULATOR =====")

#Completeing the first Task of code as we learn

number1 = float(input("Enter the first number"))
number2 = float(input("Enter the second number"))

#check for divition by zero

if number2 == 0 :
    print ("Sorry you can't devide by 0")

#complete calculations 

else :
    addition = round(number1 + number2, 2)
    subtraction = round(number1 - number2, 2)
    multiplication = round(number1 * number2, 2)
    division = round(number1 / number2, 2)
    floor_division = round(number1 // number2, 2)
    modulus = round(number1 % number2, 2)

#DISPALY ANSWERS IN A CALCULATOR FORMAT 

print("\n==============================")
print("     CALCULATOR RESULTS")
print("==============================")

print(f"First Number:      {number1}")
print(f"Second Number:     {number2}")

print("------------------------------")

print(f"Addition:          {addition}")
print(f"Subtraction:       {subtraction}")
print(f"Multiplication:    {multiplication}")
print(f"Division:          {division}")
print(f"Floor Division:    {floor_division}")
print(f"Modulus:           {modulus}")

print("==============================")
