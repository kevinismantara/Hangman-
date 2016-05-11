#### CMPT 120
#### Math training PROJECT
#### Time spent on project: 26 hours between partners
#### Authors: Jordan Ho and Kevin Ismantara

#Imports
import random
import math

#Global Variables:
i = 0
history = []
points = 0
guesses = 0
games = 0
output = ""

########Functions

#The welcome message
def welcome_message():
    print "Welcome to the Math Training game!"	
    print "=================================="+"\n"
    return ""


#Obtains a random file from formula.txt and then expands then evaluates it
def formula_execution(file):
    
    #Opening file from formula.txt
    fileRef = open("fmlas.txt" ,"r")
    formula_list = []
    for line in fileRef:
        string = line[0:len(line)-1]    
        formula_list.append(string)
    fileRef.close()  
	
    #Obtaining random formula from formula.txt
    secret_formula = random.choice(formula_list)
	
    #Expanding Formula
    expand=""
    operator = (secret_formula[0:2]) * len(secret_formula)
    for i in range(2,len(secret_formula)):
        expand = expand + secret_formula[i] + operator[i]
    expand = expand[0:(len(expand) - 1)]
    
    #Calculates the output of the expanded formula without eval() function:
    add = 0
    mult = 0
    
    if operator[0:2] == "+*":
        for i in range(len(expand)):
            if expand[i] == "*":
                if i < (len(expand)-1):
                    mult = mult + (int(expand[i-1]) * int(expand[i+1]))
        add = int(expand[0])
        if expand[len(expand)-2] == "+":
             add = add + int(expand[len(expand)-1])
    elif operator[0:2] == "*+":
        for i in range(len(expand)):
            add == expand[len(expand)-1]
            if expand[i] == "*":
                if i < (len(expand)-1): 
                    mult = mult + (int(expand[i-1]) * int(expand[i+1]))
        if expand[len(expand)-2] == "+":
             add = add + int(expand[len(expand)-1])
    elif operator[0:2] == "++":
        for i in range(len(expand)):
            if expand[i].isdigit():
                add = add + int(expand[i])
    elif operator[0:2] == "**":
        mult = 1
        for i in range(len(expand)):
            if expand[i].isdigit():
                mult = mult * int(expand[i])
    output_formula = add + mult

    #Returns value of expanded formula, evaluation of formula
    return (expand, output_formula, secret_formula)


 
#Asks user for maximum amount of guesses 
def num_guesses(guesses):
    guess_input = raw_input("Maximum wrong-guesses you want to have allowed? ")
    while guess_input.isdigit() == False: 
        guess_input = raw_input("Invalid input, Maximum wrong-guesses you want to have allowed? " )
    max_guess=int(guess_input)
    return(max_guess)



#Asks user for initial starting points
def initial_points(points):
    i_points = raw_input("Provide points to start all the games: ")
    while i_points.isdigit() == False: 
        i_points = raw_input("Invalid input, Provide points to start all the games: ")
    i_point=int(i_points)
    return(i_points)



#Shows user on a graphical screen how many points he/she has left
def tries_left(num_guess, guess_count):
    left = (num_guess - guess_count)
    health = "*" * guess_count + "~" * left
    return(health)


#Returns guessed string     
def string_history(secret_formula, guess_list):
    formula_list = list("-"*len(secret_formula))
    secret_formula=list(secret_formula)
    for k in range(len(guess_list)):
        for i in range(len(secret_formula)):
            if guess_list[k] == secret_formula[i]:
                formula_list[i] = guess_list[k]
            elif secret_formula[i] == formula_list[i]:
                formula_list[i] = secret_formula[i]   
            else:
                formula_list[i] = "-"
    formula_list="".join(formula_list)
    return(formula_list)


#Calculates and returns binary number list and evaluation of binary list
def first_lucky_number(secret_formula):   
    lucky_num=""
    binary_list=[] 
    secret_formula=secret_formula[2:len(secret_formula)]
    for i in range (len(secret_formula)):
        if int(secret_formula[i]) % 2 == 0:
            binary_list.append("0")
            lucky_num = lucky_num + "0"
        else:
            binary_list.append("1")                 
            lucky_num = lucky_num + "1"
    lucky_num = int(lucky_num, 2)
    return(lucky_num, binary_list)


#Calculates and returns formula list of numbers, list of sum of list and sum of all numbers in list
def second_lucky_number(secret_formula):
    formula_num = ""
    formula_list = []
    secret_formula = secret_formula[2:len(secret_formula)]
    for i in range(len(secret_formula)):
        formula_num = int(secret_formula[i])
        formula_list.append(formula_num)
    lucky_num=0
    addition_list=[]
    count=0
    for i in range ((len(secret_formula) - 1), -1, -1):
        lucky_num = lucky_num+int(secret_formula[i])
        addition_list.append(lucky_num)
    addition_list = addition_list[::-1]
    secret_num=0
    for i in range(len(addition_list)):
        secret_num = secret_num + int(addition_list[i])
    return(formula_list, addition_list, secret_num)

		
 
#Calculates user's points on result of game
def point_history(points, result_one, result_two):
    points = int(points)
    if result_one == True:
        points = points + 2
        if result_two == True:
            points = points + 10
        elif result_two == False:
            points = points -2
    elif result_one == False:
        points = points -2
    return (points)


#Assigning functions to variables:
welcome = welcome_message()
points = initial_points(0)


#Welcome message
print welcome, "\n"


#Decision to play or not
game_end = False
decision = raw_input("Do you want to play ? Y- yes, N - no: ")
while decision != "Y" and decision != "y" and decision != "N" and decision != "n":
    decision = raw_input("Invalid input, Do you want to play ? Y- yes, N - no: ")
if (decision == "N" or decision == "n"):
    print "User decided not to play"
    game_end = True
	
#Execution of Game
while ((decision == "Y" or decision == "y") and game_end == False): #and out_of_points == False:
    i_points = points
    expansion, evaluation, secret_formula = formula_execution("fmlas.txt")
    games = games + 1
    print "\n" + "Playing game #:", games
    print "-------------------", "\n"
    print "Your points so far are: ", points, "\n"
    total_guess = num_guesses(0)
    print "\n"
    print "The formula you will have to guess has", str(len(secret_formula)), "symbols:" , ("-" * len(secret_formula)),"\n"
    print "You can use digits 0 to 9 and symbols + *", "\n"

    #Some variables defined for next while loop
    bar = "~" * total_guess
    history_string = ""
    wrong_count = 0
    fail = False
    pass_game = False
    guess_list=[]
    game_num = "Game #: "+str(games)+" guessing formula part"
    history.append(game_num)
    
    #Game - Guessing Formula part
    while (fail == False) and (pass_game == False):
        result_guess = False
        guess = raw_input("Please enter an operation symbol or digit: ")

        #If guess is invalid or guess is reused then re-ask user for another guess
        while ((guess.isdigit() == False) and (guess != "*") and (guess != "+")) or (guess in guess_list):
            guess = raw_input("Invalid input or entered guess has been used, Please re-enter an operation symbol or digit (This will not count as an incorrect guess: ")
            print "\n"
        guess_list.append(guess)
        #Creating history list
        history.append(guess)
        history_list = history
		
	#Creating history of guesses string
        formula_list = string_history(secret_formula, guess_list)
        
        #Obtaining result of guess
        
        #Checks if guess is inside secret_formula
        for i in range(len(secret_formula)):
            if secret_formula[i] == guess:
                result_guess = True
                
        #If guess is inside secret_formula then guess is correct
        if result_guess == True:
            result = True
            print "Yes! correct guess!"
            print "The formula you have guessed so far is:", formula_list
            print "\n"
            
        #If guess isn't inside secret_formula then guess is wrong
        else:
            result = False
            wrong_count = wrong_count + 1
            bar = tries_left(total_guess, wrong_count) 
            print "Wrong guess!", bar
            print "The formula you have guessed so far is:", formula_list
            print "\n"
            if bar == total_guess * "*":
                fail = True
                
        #If the guessed formula is the same as secret_formula then you pass part 1 of game
        if secret_formula == formula_list:
            pass_game = True

    #Result of Guessing Formula Part
    if bar == "*" * total_guess:
        print "Sorry, you wrongly guessed already", wrong_count, "time; you cannot continue guessing"
        print "Better luck next time!"
        print "And you lose 2 points","\n"
        result_end = "User did NOT guess the whole formula"
        points = point_history(points, False, False)

        #If points are bigger than or equal to 2 then you can start another game
        if points >= 2:
            print "\n"
            decision = raw_input("Do you want to play again? Y- yes, N - no: ")
            while decision != "Y" and decision != "y" and decision != "N" and decision != "n":
                    decision = raw_input("Invalid input, Do you want to play again? Y- yes, N - no: ")
        #Otherwise, points smaller than 2 - cannot start another game
        else:
            print "\n"
            print "insufficient points to play new games, GAME OVER"
            decision = "n"

    #Game - Evaluation of formula part       
    else:
        history.append("Guessing evaluation of expanded formula part")
        print "Yes! You guessed  the whole formula!"
        print "Now that you guessed ... what is the result of the formula?"
        result_guess = raw_input("the result is (integer number): ")
        while (result_guess.isdigit()==False):
            result_guess = raw_input("Invalid input, Please re-enter the result of the formula: ")
        history.append(result_guess)

        
        if int(result_guess) == evaluation:
            print "You have guessed the whole formula and the result!"
            print "You earned 12 points"
            points = point_history(points, True, True)
            result_end = "User guessed the whole formula"
            result_eval = ("user evaluated correctly, the result was:", evaluation)
            decision = raw_input("Do you want to play again? Y- yes, N - no: ")
            while decision != "Y" and decision != "y" and decision != "N" and decision != "n":
                decision = raw_input("Invalid input, Do you want to play again? Y- yes, N - no: ")
        else:
            print "\n"
            print "Sorry your guess is incorrect"
            print "You have guessed the whole formula but not the result."    
            print "You earned 2 points"
            points = point_history(points, True, False)
            result_end = "user did NOT guess the whole formula"
            decision = raw_input("Do you want to play again? Y- yes, N - no: ")
            while decision != "Y" and decision != "y" and decision != "N" and decision != "n":
                decision = raw_input("Invalid input, Do you want to play again? Y- yes, N - no: ")
            
#Game - End, History, Lucky number
if (((decision == "n") or (decision == "N") or (points < 2)) and game_end == False):
        print "\n","ALL GAMES ARE OVER!"
        print "Here is  all your final information","\n", "\n"
        
        
        print "After playing",games,"games , you have in total", points, "points","\n"

        print "The history of the last game played is...","\n"
        
        print "started with:", i_points, "points"
        print "the mystery fmla was:", secret_formula

        
        for i in range(len(history_list)):
            print "user_guessed:",history_list[i]
        print "\n"
        print "end result:"
        print "\n"
        print result_end
        print "User now has:", points, "points"
        print "\n"
        
        lucky_one, binary = first_lucky_number(secret_formula)
        print "Based on the binary list:",binary
        print "Your first lucky number is:",lucky_one
        print "\n"
        
        fmla_list, sum_list, lucky_two = second_lucky_number(secret_formula)
        print "Based on the list with digits only:", fmla_list
        print "and the list with added values:", sum_list
        print "Your second lucky number is:", lucky_two, "\n"
        print "Good bye!"


        
             

	
    


    
    


