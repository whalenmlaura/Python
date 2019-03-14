#Assignment #3
#November 2, 2018
#Name..: Laura Whalen
#ID....: W0415411

__AUTHOR__ = "Laura Whalen <W0415411@nscc.ca>"

def main():

    box_list = []
    name_list = []
    count = 0
    line_break = "-" * 80

    def guide_input():
        while (True):
            number_guides = input("\nEnter the number of guides selling cookies: ")
            if(number_guides.isnumeric()):
                number_guides = int(number_guides)
                return(number_guides)
            else:
                print("\nERROR! Enter a valid number of guides.")
                True
    
    number_guides = guide_input()

    while count != number_guides:
        count = count +1
        guide_name = input("\nEnter the name of guide #{0}: ".format(count))
        guide_name = guide_name.title()
        name_list.append(guide_name)
        boxes = ""
        while not boxes.isnumeric():
            print("\nERROR! Enter a valid number of boxes.")
            boxes = input("Enter the number of boxes sold by {0}: ".format(guide_name))
        else:
            boxes = int(boxes)
            box_list.append(boxes)            

    print(line_break)
    list_sum = float(sum(box_list))
    average = float(list_sum / number_guides)
    print("\nThe average number of boxes sold by each guide was {0:.1f}\n".format(average))
    
    print("Guide"+(" " * 15)+"Prizes Won:")
    print(line_break)
    most_boxes = max(box_list)
    for b,n in zip(box_list,name_list):
        if (b == most_boxes):
            space = (20 - len(n))
            space = (" " * space)
            print("{0}{1}- Trip to Girl Guide Jamboree in Aruba!".format(n,space))
        elif (b > average):
            space = (20 - len(n))
            space = (" " * space)
            print("{0}{1}- Super Seller Badge".format(n,space))
        elif (b > 1):
            space = (20 - len(n))
            space = (" " * space)
            print("{0}{1}- Left over cookies".format(n,space))
        elif (b == 0):
            space = (20 - len(n))
            space = (" " * space)
            print("{0}{1}-".format(n,space))

if __name__ == "__main__":
    main()