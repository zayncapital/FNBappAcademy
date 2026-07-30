#Calculating how much will the client need for Petrol

kilometers = float(input("Enter the number of kilometers"))
petrol_prices = float(input("Enter the petrol prices"))

#Calculate the litres needed

litres_needed = kilometers / 10

#Calculate the total cost

total_cost = litres_needed * petrol_prices

#Round the total costs

total_cost = round(total_cost, 2)

print("=============================")
print("   PETROL COST CALCULATOR")
print("=============================")
print(f"Kilometers:       {kilometers}km")
print(f"Petrol_prices:    {petrol_prices}/l")
print(f"Litres_needed:    {litres_needed}L")
print("===========================")
print (f"total cost:      R{total_cost}")
print("===========================")