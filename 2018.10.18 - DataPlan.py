#"""
#Assignment 2 - Erewhon Mobile Data Plans
#October 18, 2018

#Name..: Laura Whalen
#ID....: W0415411
#"""

__AUTHOR__ = "Laura Whalen <W0415411@nscc.ca>"

def main():

    # input
    data = int(input("Enter data usage (Mb): "))

    # processing and output
    def data_plans():
        if data <= 200:
            print("Total charge is: $20.00")
        elif data > 1000:
            print("Total charge is: $118.00")
        elif data > 200 or data <= 500:
            charge = 0.105
            total = (data * charge)
            print("Total charge is: ${0:.2f}".format(total))
        elif data > 500 or date <= 1000:
            charge = 0.110
            total = (data * charge)
            print("Total charge is: ${0:.2f}".format(total))
    
    data_plans()

if __name__ == "__main__":
    main()