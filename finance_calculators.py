
import math

# Presenting user with Investment or Bond menu options and assigning input to menu_option.

menu_option = input("""Choose either \'Investment\' or \'Bond\' from the menu below to proceed:
 \nInvestment   - to calculate the amount of interest you'll earn on interest. 
 \nBond         - to calculate the amount you'll have to pay on a home loan. 
\n Enter choice here: """)

# Converting user menu_option input to all lower case to be valid for all user case input.

menu_option_lower = menu_option.lower()

# Taking user input and  presenting user with bond or investment options  and proceeding given input choice.

if menu_option_lower == "investment":

    investment_deposit = float(input("\nPlease enter the amount of money you are investing: "))

    interest_rate = float(input("\nPlease enter your chosen interest rate as a number only: "))

    num_years = int(input("\nPlease enter the number of years you are planning on investing: "))

# Converting user interest rate input to actual percentage.
    percentage_interest_rate = interest_rate / 100

# Presenting user with interest options Simple or Compound and proceeding with calculations given user choice.
# After calculations then present user with total amount earned from chosen interest rate.

    interest = input("\nPlease choose the type of interest  you want: \"Simple\" or \"Compound\" \nEnter Choice here: ")

# Converting user interest input to all lower case to be valid for all user case input.
    interest_lower = interest.lower()

    if interest_lower == "simple":

        simple_interest_total_amount = investment_deposit * (1 + percentage_interest_rate * num_years)

        print(f"\nYour total amount earned with simple interest applied is: R{simple_interest_total_amount}")

    elif interest_lower == "compound":

        compound_interest_total_amount = round(investment_deposit * math.pow((1 + percentage_interest_rate), num_years))

        print(f"\nYour total amount earned with compound interest applied is: R{compound_interest_total_amount}")

    else:

        print("Invalid input. Please read menu options correctly and try again.")

# If user chose bond option. Proceeding with calculating bond monthly payment expected and printing it out.

elif menu_option_lower == "bond":

    house_present_value = float(input("\nPlease enter the present value of the house: "))

    bond_interest_rate = float(input("Please enter the interest rate on the bond as a number only: "))

    num_months = int(input("\nPlease enter the number of months you'll take to repay the bond: "))

    percentage_bond_interest_rate = bond_interest_rate / 100

# taking converted percentage and getting monthly interest rate.
    monthly_interest_rate = percentage_bond_interest_rate/12

    bond_repayment = round((monthly_interest_rate * house_present_value) / (1 - math.pow((1 + monthly_interest_rate), -num_months)))

    print(f"\nThe bond monthly payment is: R{bond_repayment}")

else:

    print("Invalid input. Please read the menu options carefully and try again.")
