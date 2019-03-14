#"""
#Assignment 2 - Landscape Calculator
#October 18, 2018

#Name..: Laura Whalen
#ID....: W0415411
#"""

__AUTHOR__ = "Laura Whalen <W0415411@nscc.ca>"

def main():

# input
    address = input("Please enter your house number: ")
    length = float(input("Please enter property length in feet: "))
    width = float(input("Please enter property width in feet: "))
    grass_type = input("Please enter the type of grass (fescue, bentgrass, or campus): ").lower()
    trees = float(input("Please enter the number of trees: "))
    tree_cost = float(100 * trees)

# processing
    def square_foot(length, width):
        total_square_foot = (length * width)
        return (total_square_foot)
    total_square_foot = square_foot(length, width)

    def total():
        total_cost = (1000 + additional_cost + tree_cost + (total_square_foot * grass_cost))
        print("\nThe total cost for house {0} is: ${1:.2f}".format(address, total_cost))
        return(total_cost)

    if total_square_foot > 5000.00:
        additional_cost = 500.00
    elif total_square_foot <= 5000.00:
        additional_cost = 0.00

    if grass_type == "fescue":
        grass_cost = 0.05
        total()
    elif grass_type == "bentgrass":
        grass_cost = 0.02
        total()
    elif grass_type == "campus":
        grass_cost = 0.01
        total()
    else:
        print("\nSorry, we do not carry that type of grass.")

if __name__ == "__main__":
    main()