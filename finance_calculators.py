import math
# Display the menu options for user
print("investment - to calculate the amount of interest you'll earn on your investment")
print("bond - to calculate the amount you'll have to pay on a home loan")
print("")
# Ask for input (investment or bond)
choice = input("please enter what type of calculate you are interested in (investment or bond): ")
choice = choice.lower()

# Handle the user's choice and get user input for investment calculation
if choice == "investment" :
    deposit = float(input("How many do you want to deposit: "))
    rate = float(input("The interest rate (Don't put '%' symble): "))/100
    years = int(input("The number of year your plan: "))

    #Handle the user's choice about simple or compound
    interest = input("which one interest for you want, simple or compound: ")
    interest = interest.lower()

    if interest == "simple":
        simple_interest = deposit * (1 + (rate * years))
        print("Your simple interest is " , simple_interest)
    elif interest == "compound":
        compound_interest = deposit * ((1 + rate)**(years))
        print("Your compound interest is " , compound_interest)

# Handle the user's choice and get user input for bond calculation    
elif choice == "bond" :
    present_value = float(input("How many your present value: "))
    rate = float(input("The interest rate: (Don't put '%' symble)" ))/100
    month = int(input("The number of month your plan: "))

    repayment = (rate * present_value) / (1-(1 + rate) ** (-month))
    print("Your repayment is ", repayment)
else:
    print("Your enter information is wrong, please run program again!")

