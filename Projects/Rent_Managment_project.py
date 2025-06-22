# Input we need from the user 
# Total rent 
# Total food ordere from snack 
# Electricity unit spend 
# Charge per unit 
# Total number os person living in room / Flat

# OUPUT 
# Totoal amount you're to pay is 

rent = int(input("Enter the Hostel/flat rent : "))
Food = int(input("Enter the Food Amount : "))
Eletricity_Spend = int(input("Enter the electricity spend : "))
Charge_per_unit = int(input("Enter the charge of electricity per unit : "))
Person =  int(input("Enter the total number of person in hostel/flat : "))

Total_Electricity_Bill = Eletricity_Spend * Charge_per_unit

Total_Amount_Per_Person = (rent + Food + Total_Electricity_Bill) / Person
print("Amount Per Person is : ", Total_Amount_Per_Person)
