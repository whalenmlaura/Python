#Assignment 4 - Aardvark
#Name..: Laura Whalen
#ID....: W0415411

print("The Itsy Bitsy Aardvark")
answer_list = []
word_type = {}
space_num = 0

# create a dictionary
def excel_dictionary(infile):
	for line in infile:
		line = line.replace("\n","")
		list_line_content = line.split(",")
		word_list = list_line_content[0]
		word_choices = list_line_content[1:]
		word_type[word_list] = word_choices

# user input
def user_choice(dictionary_of_words):
	for title in dictionary_of_words:
		print("\nPlease choose {0}:".format(title))
		line_number = 1
		for word in dictionary_of_words[title]:
			print("{0}) {1}".format(line_number,word))
			line_number += 1
		no_errors = "Y"
		while no_errors =="Y":
			num_choice = input("Enter choice (1-5): ")
			if num_choice.isnumeric():
				num_choice = int(num_choice)
				if num_choice > 5:
					print("\nERROR! Invalid input!\n")
					no_errors = "Y"
				elif num_choice <= 5:
					no_errors = "N"
			else:
				print("\nERROR! Invalid input\n")
				no_errors = "Y"
		choice = (dictionary_of_words[title][num_choice - 1]).upper()
		answer_list.append(choice)

# place user choices into story
def place_choices(infile):
	for strMsg in infile:
		strMsg = strMsg.replace("\n","")
		for i in range(0,len(answer_list)):
			space = "_"
			space += str(i+1)
			space += "_"
			strMsg = strMsg.replace(space,answer_list[i])
		strMsg = strMsg
		print(strMsg)

def main():

	#create dictionary
	choices = open("the_choices_file.csv")
	excel_dictionary(choices)
	# user input
	user_choice(word_type)
	choices.close()
	# input user choices and print
	print("")
	story_file = open("the_story_file.txt","r")
	place_choices(story_file)
	story_file.close()

if __name__ == "__main__":
    main()