#request user to select investment or bond
#researched how to get python to ignore capitalziation therefore created variables for each option
#used if statement for both selections
#in each selection included the criteria
#used nested if statement if the user selected compound or simple interest
#for simple interest reasearched the net and swopped the formula around to divide interest by 100
#else if statement included if user selected compound interest
#else if statement used if user selecetd bond
#multiplied interest_rate by (1/12) since interest calc should be monthly
#else statement should the user make an incorrect selection



import math

input_type=input("Choose either 'investment' or 'bond' from the menu below to proceed:\n\ninvestment - to calculate the amount of interest you will earn on investment\nbond - to calculate the amount you will have to pay on a home loan\n")   
string_type1="investment"
string_type2="Investment"
string_type3="INVESTMENT"
string_type4="bond"
string_type5="Bond"
string_type6="BOND"

if input_type.lower()==string_type1.lower() or input_type.upper()==string_type3.upper or input_type==string_type2:
    print("Thank you")
    dep_amount = int(input("enter your deposit amount here: R "))
    interest_rate = int(input("enter your prefered interest rate (%): "))
    invest_period = int(input("enter your prefered investment period in years: "))
    interest = input("enter your interest choice here simple or compound: ")
    if interest=="simple":
        interest_calc=round((dep_amount*interest_rate*invest_period)/100+dep_amount)
        print("The amount you will receive after {} years is R{}".format(invest_period,interest_calc))
    elif interest=="compound":
        interest_calc=round(dep_amount*math.pow((1+interest_rate/100),invest_period))
        print("The amount you will receive after {} years is R{}".format(invest_period,interest_calc))
elif input_type.lower()==string_type4.lower() or input_type.upper()==string_type6.upper or input_type==string_type5:
        interest_rate = int(input("enter your prefered interest rate (%): "))/100*(1/12)
        PV = int(input("enter the present value of the house: R "))
        bond_period = int(input("enter number of months you plan to pay off bond: "))
        repayment=round((interest_rate*PV)/(1-(1+(interest_rate))**(-bond_period)))
        print("Your monthly payment is: R{}"  .format(repayment))      
else:
    print("invalid option. please select investment or bond")









