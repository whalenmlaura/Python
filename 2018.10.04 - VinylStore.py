#"""
#Assignment 1 - Vinyl
#October 4, 2018

#Name..: Laura Whalen
#ID....: W0415411
#"""

__AUTHOR__ = "Laura Whalen <W0415411@nscc.ca>"

    # print "Hipster's Local Vinyl Records - Customer Order Details"
    # Have retail staff input customer name
    # have retail staff input kilometers distance for delivery, cost of records before tax as floats
    # calculate the delivery cost ($15 per kilometer)
    # calculate cost of records + tax (14%)
    # calculate total
    # print "Purchase Sumary for (customer name)"
    # print delivery cost, purchase cost, and total cost

import math

def main():

    # input
    print("\nHipster's Local Vinyl Records - Customer Order Details")
    cust_name = input("\nEnter the customer's name: ")
    kilometers = input("Enter the distance in kilometers for delivery: ")
    kilometers = float(kilometers)
    cost = input("Enter the cost of records purchased: $")
    cost = float(cost)

    # processing
    delivery = (kilometers * 15)
    purchase_cost = (cost * 1.14)
    total_cost = (delivery + purchase_cost)
    print("\nPurchase summary for {0:s}".format(cust_name))

    # output
    print("Delivery Cost: ${0:.2f}".format(delivery))
    print("Purchase Cost: ${0:.2f}".format(purchase_cost))
    print("Total Cost   : ${0:.2f}".format(total_cost))

if __name__ == "__main__":
    main ()