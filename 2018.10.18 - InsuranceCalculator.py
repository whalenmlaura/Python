#"""
#Assignment 2 - Auto Insurance
#October 18, 2018

#Name..: Laura Whalen
#ID....: W0415411
#"""

__AUTHOR__ = "Laura Whalen <W0415411@nscc.ca>"

def main():

    # input
    gender = input("Are you 'male' or 'female'? ").lower()
    age = int(input("Enter your age: "))
    car_cost = float(input("Enter the purchase price of the vehicle: $"))

    # processing and output
    def female():
        if age >= 15 and age < 25:
            insurance = 0.20
            total_insurance = (car_cost * insurance) / 12
            print("Your monthly insurance will be: ${0:.2f}".format(total_insurance))
        elif age >= 25 and age < 40:
            insurance = 0.15
            total_insurance = (car_cost * insurance) / 12
            print("Your monthly insurance will be: ${0:.2f}".format(total_insurance))
        elif age >= 40 and age < 70:
            insurance = 0.10
            total_insurance = (car_cost * insurance) / 12
            print("Your monthly insurance will be: ${0:.2f}".format(total_insurance))
        else:
            print("Sorry, we do not insure people under 15 or over 70")

    def male():
        if age >= 15 and age < 25:
            insurance = 0.25
            total_insurance = (car_cost * insurance) / 12
            print("Your monthly insurance will be: ${0:.2f}".format(total_insurance))
        elif age >= 25 and age < 40:
            insurance = 0.17
            total_insurance = (car_cost * insurance) / 12
            print("Your monthly insurance will be: ${0:.2f}".format(total_insurance))            
        elif age >= 40 and age < 70:
            insurance = 0.10
            total_insurance = (car_cost * insurance) / 12
            print("Your monthly insurance will be: ${0:.2f}".format(total_insurance))
        else:
            print("Sorry, we do not insure people under 15 or over 70")

    if gender == "female":
        female()
    elif gender == "male":
        male()
    else:
        print("'Gender' is invalid")

if __name__ == "__main__":
    main()