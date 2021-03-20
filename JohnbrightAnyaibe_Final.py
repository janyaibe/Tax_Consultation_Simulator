##The following program will be used to  find out if a particular family needs to pay taxes on their yearly income which property, federal and health.  
def taxprog():
    #Get tax information from user using for loop input
    tax = [] #create empty array to store all values
    print("Welcome to Anyaibe's Tax Consultation Group")
    print()
    print("Please enter the proceeding tax information")
    print()
    print("All field are required")
    tax.append(eval(input("Total earned by husband:"))) #This will include wages, salaries, and tips earned by the husband
    tax.append(eval(input("Total earned by wife:"))) #This will include wages, salaries, and tips earned by the wife
    tax.append(eval(input("Additional earnings:"))) #This will include the bonus wages earned by the family combined
    print()
    grossincome = sum(tax[0:2])#Total (grose income)
    print("Household gross income is:" + " "+ "$" + str("%.2f" % (grossincome)))
    print("If standard health insurance deduction is larger than gross income, enter 0")
    tax.append(eval(input("Health insurance deducted:"))) 
    taxableincome = (grossincome - tax[3]) #taxable income
    tax.append(eval(input("Enter husband's income tax withheld:"))) #This is federal income tax withheld from Husband's paycheck
    tax.append(eval(input("Enter wife's income tax withheld:"))) #This is federal income tax withheld from wife's paycheck
    totalpay = sum(tax[4:6]) #This includes total payments and credits
    fedtax = (taxableincome * 0.28) #This is the Federal Tax
    tax.append(eval(input("Enter property tax to be owed:"))) #This is the property tax to be owed
    totaltaxes = (fedtax + tax[6]) #This is total tax
    remainder = (totaltax - totalpay) #This is the amount you have to pay. if results is -ve, it is the amount you have overpaid
    print()
    print("This is your tax information")
    print()
    print("Wages,salaries, and, tips earned by the husband is"+" " + "$"+ str("%.2f" %(tax[0])))
    print("Wages,salaries, and, tips earned by the wife is" + " " + "$"+ str("%.2f" % (tax[1])))
    print("Bonus earned by the family combined is" + " " + "$" + str("%.2f" % (tax[2])))
    print("Your yearly gross income is" + " " + "$" + str("%.2f" % grossincome))
    print("Your standard health insurance deduction is" + " " + "$" + str("%.2f" % (tax[3])))
    print("Your taxable income is" + " " + "$" + str("%.2f" % (taxableincome)))
    print("Federal income tax withheld from paychecks for husband is" + " " + "$" + str("%.2f" %(tax[4])))
    print("Federal income tax withheld from paychecks for wife is" + " " + "$" + str("%.2f" % (tax[5])))
    print("Your total payments and credits is" + " " + "$" + str("%.2f" % (totalpay)))
    print("Your federal tax is" + " " + "$" + str("%.2f" % (fedtax)))
    print("The property tax to be owed is" + " " + "$" + str("%.2f" %(tax[6])))
    print("Your total tax is" + " " + "$" + str("%.2f" % (totaltaxes))) 
    if totaltax > amountrem:
        print("$" + str("%.2f" % (remainder)+" " + "is the amount you have left to pay"))
    else:
        print("You have overpaid" + " " + "$" + str("%.2f" % (amountrem)))
              
taxprog()   
