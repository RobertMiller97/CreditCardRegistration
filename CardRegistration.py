
# Credit card Registration

# Would you like a credit card
answer = str(input("Would you like a credit card?  "))
if answer == "Y":
    print("Lets get some information from you ")

elif answer == "N ":
    print("GoodBye ")
    exit("Come  back when you are ready ")
else:
    print("Invalid answer")


# Are you old enough for a credit card
age = int(input("How old are You:  "))
if age >= 18:
    print("You are old enough for a credit card ")
else:
    print("You must be over 18 to Sign up ")
    exit(" ")


# Sign up
first_name = str(input(" first name: "))
last_name = str(input(" last name: "))
dob = input(" Date of Birth :  ")
SSN = input(" Last 6 of your SSN: ")

print("The first phase is Complete. Lets move to the second phase please \n")

#Residence
print(f"Can we have your residence {first_name}? ")

state = str(input("State:  "))
city = str(input("City:  "))
county = str(input("County:  "))
address = input("Address:   ")

print(f"Are you loacted at {address} {county} {city}, {state}")
answer = str(input("Is this Correct: \n"))

if answer == "Y":
    print(" Lets move on to Phase 3 ")

elif answer == "N":
    print("Go Back ")
else:
    print("Invalid")


# Phase 3 Income


income = int(input("What is you yearly Income: "))


if income <= 50000:
    print("The Bronze card will be perfect for you ")

elif income <= 100000:
    print("The Silver card will be perfect for you ")

elif income > 200000:
    print("The Gold card will be perfect for you ")

else:
   print("invalid income")

print("Please look over your information to see if this is correct")
print(f"FirstName {first_name} LastName {last_name}  Age {age}")
print(f"DOB {dob}  SSN {SSN} ")
print(f"Sate {state}  City {city}  County {county}  Address {address}")

input("Is everything correct:  ")

if answer == 'Y':
    print("Congradulations on your New Card")

elif answer == 'N':
    print("Did we miss something")

else:
    print("Invalid Answer")





