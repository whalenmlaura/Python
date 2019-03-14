#Assignment #3
#November 2, 2018
#Name..: Laura Whalen
#ID....: W0415411

__AUTHOR__ = "Laura Whalen <W0415411@nscc.ca>"

def main():

    def remove_letters(str):
        letters = []
        input_letters = input("Type a comma-separated list of letters to redact: ")
        letters.extend(input_letters)
        for l in letters:
            str = str.replace(l,"_")
        underscore = str.count("_")
        print("\nNumber of letters redacted: {0}".format(underscore)) 
        print(str)

    phrase = ""
    while phrase != "quit":
        phrase = input("\nType a phrase (or quit to exit program): ").lower()
        if phrase != "quit":
            remove_letters(phrase)
        elif phrase == "quit":
            print("\nThanks for playing!")
            break
        else:
            print("\nThanks for playing!")
            break            
    
if __name__ == "__main__":
    main()