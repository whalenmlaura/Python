#"""
#Assignment 1 - Loan Calculator
#October 4, 2018

#Name..: Laura Whalen
#ID....: W0415411
#"""

__AUTHOR__ = "Laura Whalen <W0415411@nscc.ca>"

    # print "Weekly Loan Calculator"
    # have person enter the amount of the loan and covert to a float
    # have person enter the interest (%) rate and convert to a float
    # have person enter the number of years and convert to a float
    # calculate the interest with given formula
    # calculate the weekly payments with given formula
    # print "Your weekly payments will be: $__"

import math

def main():

    # input
    print("\nWeekly Loan Calculator")
    loan_amount = input("\nEnter the amount of the loan: $")
    loan_amount = float(loan_amount)
    interest_rate = input("Enter the interest (%) rate: ")
    interest_rate = float(interest_rate)
    years = input("Enter the number of years: ")
    years = float(years)

    # processing
    interest = (interest_rate / 5200)
    payments = ((interest / (1-(1+interest)**(-52 * years))) * loan_amount)

    # output
    print("\nYour weekly payments will be: ${0:.2f}".format(payments))
    
if __name__ == "__main__":
    main ()