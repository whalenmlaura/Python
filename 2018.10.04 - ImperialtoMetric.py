#"""
#Assignment 1 - Imperial to Metric
#October 4, 2018

#Name..: Laura Whalen
#ID....: W0415411
#"""

__AUTHOR__ = "Laura Whalen <W0415411@nscc.ca>"

    # print "Imperial to Metric Conversion"
    # have person enter the number of tons and convert to float
    # have person enter the number of stone and convert to float
    # have person enter the number of pounds and convert to float
    # have person enter the number of ounces and convert to float
    # calculate total ounces with given formula
    # calculate total kilos with given formula and then to metric kilos and round down
    # calculate metric tons with given formula
    # calculate grams with the remainder to total kilos
    # print "The metric weight is: __ metric tons, __ kilos, __ grams"

import math

def main():

    # input
    print("\nImperial to Metric Conversion")
    tons = input("\nEnter the number of tons: ")
    tons = float(tons)
    stone = input("Enter the number of stone: ")
    stone = float(stone)
    pounds = input("Enter the number of pounds: ")
    pounds = float(pounds)
    ounces = input("Enter the number of ounces: ")
    ounces = float(ounces)

    # processing
    total_ounces = (35840 * tons) + (224 * stone) + ((16 * pounds) + ounces)
    total_kilos = total_ounces / 35.274
    metric_kilos = total_kilos % 1000
    metric_kilos = math.floor(metric_kilos)
    metric_tons = int(total_kilos / 1000)
    total_grams = (total_kilos * 1000) % 1000

    # output
    print("\nThe metric weight is {0:d} metric tons, {1:.0f} kilos, and {2:.1f} grams.".format(metric_tons, metric_kilos, total_grams))

if __name__ == "__main__":
    main ()