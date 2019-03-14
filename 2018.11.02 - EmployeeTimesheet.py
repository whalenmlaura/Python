#Assignment #3
#November 2, 2018
#Name..: Laura Whalen
#ID....: W0415411

__AUTHOR__ = "Laura Whalen <W0415411@nscc.ca>"

def main():

    line_break = "-" * 80

    entry_list = ["1", "2", "3", "4", "5"]
    work_list = []
    day = 0
    for e in entry_list:
        hours = float(input("Enter hours worked on day #{0}: ".format(day+1)))
        day = day+1
        work_list.append(hours)

    print(line_break)

    print("The most hours work was on:")
    most_hours = max(work_list)
    for d,h in enumerate(work_list):
        if h == most_hours:
            print("Day #{0} when you worked {1:.1f} hours".format(d+1,h))
    print(line_break)

    list_sum = float(sum(work_list))
    print("The total number of hours worked was: {0:.1f}".format(list_sum))
    
    def avrg(sum, days_worked):
        average = float(sum / len(days_worked))
        return(average)
    
    average = avrg(list_sum, entry_list)

    print("The average number of hours worked each day was: {0:.1f}".format(average))

    print(line_break)

    print("Days you slacked off (i.e. worked less than 7 hours):")
    for d,h in enumerate(work_list):
        if (h < 7):
            print("Day #{0}: {1} hours".format(d+1,h))
    
if __name__ == "__main__":
    main()