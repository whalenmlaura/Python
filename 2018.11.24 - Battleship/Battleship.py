#Assignment 4 - BattleShips
#Name..: Laura Whalen
#ID....: W0415411


print("Let's play Battleship!\nYou have 30 missiles to fire to sink all 5 ships.\n")
map_file = open("map.txt")

#hide the grid
target_grid = [] #where values are stored
for r in map_file:
    r = r.replace("\n","")
    columns_as_list = r.split(",")
    target_grid.append(columns_as_list)

#variables
missiles = 30
row_nums = [[chr(32) for x in range(1,11)] for y in range (1,11)] #where guesses will be stored
successful_hits = 0

#loop to play game
while missiles > 0:    
    emptyspace = " "*3
    for i in range (65,75):
        emptyspace += chr(i)
        emptyspace += (" ")
        emptyspace = emptyspace
    print(emptyspace)
    n = 1
    for l in row_nums:
        space = " "
        for entry in l:
            space += str(entry)
            space += " "
        print("{0:2d}{1}".format(n,space))
        n += 1

    #error checking
    keep_going = "Y"
    while keep_going == "Y":
        target_guess = input("\nChoose your target (Ex. A1): ")
        target_guess = target_guess.upper()
        if target_guess == "" or target_guess[0] == " " or target_guess[1:] == " ":
            print("\nInvalid! Try again")
        elif ord(target_guess[0]) < 65 or ord(target_guess[0]) > 74:
            print("\nInvalid! Try again")
        elif not target_guess[1:].isnumeric():
            print("\nInvalid! Try again")
        elif int(target_guess[1:]) < 1 or int(target_guess[1:]) > 10:
            print("\nInvalid! Try again")
        else: 
            row = int(target_guess[1:])-1
            column = ord(target_guess[0])-65
            if row_nums[row][column] == "O" or row_nums[row][column] == "X":
                print("\nYou already shot this! Try again!")
            else:
                keep_going = "N"

    #store hits / misses, and print to screen
    if target_grid[row][column] == "1" :
        print("\n!!! HIT !!!")
        row_nums[row][column] = "X"
        successful_hits += 1
    else :
        print("\nMISS")
        row_nums[row][column] = "O" 
    missiles -= 1
    print("You have {0} missiles remaining!\n".format(missiles))

    if successful_hits == 17 and missiles >= 0:
        print("YOU SANK MY ENTIRE FLEET!\nYou had 17 of 17 hits, which sank all the ship\nYou won, congratulations!")
        break
    elif successful_hits < 17 and missiles == 0:
        print("\nGAME OVER!\nYou had {0} of 17 hits, but didn't sink all the ships.\nBetter luck next time.".format(successful_hits))
        break
    else:
        continue

map_file.close()