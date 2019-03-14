#Assignment 4 - A-Team
#Name..: Laura Whalen
#ID....: W0415411

import random
A = []

def line_break(ch):
    line = ch * 80
    print(line)

# line numbers
def line_numbers(infile, outfile):
    line_number = 1
    for line in infile:
        new_string = str(line_number)
        new_string += ":  "
        new_string += line
        line_number+=1
        outfile.write(new_string)

# upper / lowercase
def upper_lower(infile):
    for line in infile:
        length = len(line)
        if length > 20:
            line = line.lower()
            A.append(line)
        elif length <= 20:
            line = line.upper()
            A.append(line)

# removing a line
def remove_line(outfile):
    list_length = len(A)
    random_num = random.randint(1,list_length)
    line_number = 0
    for line in A:
        line_number += 1
        line = line.replace("\n","")
        if line_number == random_num:
            line = ""
        else:
            line = line
        print(line)
        line += "\n"
        outfile.write(line)
 
def main():

    # printing orginal text
    line_break("-")
    print("Original Text")
    line_break("-")
    ateam_file = open("ateam_Original.txt","r")
    content = ateam_file.read()
    print(content)
    ateam_file.close()
    # altering text
    line_break("-")
    print("Altered Text")
    line_break("-")
    # line numbers
    ateam_file = open("ateam_Original.txt","r")
    ateam_out_file = open("ateam_New.txt","w")
    line_numbers(ateam_file, ateam_out_file)
    ateam_file.close()
    ateam_out_file.close()
    # upper / lower
    ateam_file = open("ateam_New.txt","r")
    upper_lower(ateam_file)
    ateam_file.close()
    # remove line
    ateam_file = open("ateam_New.txt","w")
    remove_line(ateam_file)
    ateam_file.close()   

if __name__ == "__main__":
    main()