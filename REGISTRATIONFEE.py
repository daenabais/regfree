# User Info 
age = int(input("Enter your age: "))  
membership = input("Are you a member? (Yes/No): ").strip().lower()  

# Verifying
if membership == "yes" or membership == "no":
    if age >= 0 and age < 18:
        if membership == "yes":
            print("Your registration fee is 450.00 pesos.")
        elif membership == "no":
            print("Your registration fee is 650.00 pesos.")
    elif age >= 18 and age <= 65:
        if membership == "yes":
            print("Your registration fee is 550.00 pesos.")
        elif membership == "no":
            print("Your registration fee is 750.00 pesos.")
    elif age > 65 and age <= 120:
        if membership == "yes":
            print("Your registration fee is 400.00 pesos.")
        elif membership == "no":
            print("Your registration fee is 600.00 pesos.")
    else:
        print("Invalid input: Age out of valid range.")
else:
    print("Invalid input: Please only choose Yes or No.")
