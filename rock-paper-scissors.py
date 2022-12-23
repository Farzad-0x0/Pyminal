

import random
from colorama import Fore , Back , init
init(convert= True)


user_score = 0
ai_score = 0

print (Fore.BLUE+'------ Welcome to rock paper scissors game ------')
print ("""""")

i = int(input(Fore.RESET+'How many you want to play ?'))



for test in range(i):

    choices = ['r','p','s']
    ai_choices = random.choice(choices)

    print ("""""")
    user_choice = input(Fore.RESET+'Enter here :')
    print ("""""")
    user_choice = user_choice.lower()






    if user_choice not in choices:
        print ('PLEASE ONLY (r , p , s) !')
        
        
    else:
        pass
                             # r < p < s , s < r < p
        if user_choice == ai_choices:
            print (Fore.MAGENTA+f'Python choice : {ai_choices}')
            print (Fore.YELLOW+'Your choice = Python choice')

        elif user_choice == 'r' and ai_choices == 's':
            print (Fore.MAGENTA+f'Python choice : {ai_choices} (sciccors)')
            print (Fore.GREEN+'You recive 1 score')
            user_score += 1

        elif user_choice == 'p' and ai_choices == 'r':
            print (Fore.MAGENTA+f'Python choice : {ai_choices} (rock)')
            print (Fore.GREEN+'You recive 1 score')
            user_score += 1

        elif user_choice == 's' and ai_choices == 'p':
            print (Fore.MAGENTA+f'Python chocie : {ai_choices} (paper)')
            print (Fore.GREEN+"You recive 1 score")
            user_score += 1

        else :
            print (Fore.MAGENTA+f'Python chocie : {ai_choices}')
            print (Fore.RED+"Python recive 1 score")
            ai_score += 1

        
if user_score > ai_score:
    print ("""""")
    print ("""""")
    print (Fore.CYAN+f'Your score : {user_score}    /    Python score : {ai_score}')
    print (Fore.LIGHTGREEN_EX+'--- YOU WIN ---')

elif user_score == ai_score:
    print ("""""")
    print (Fore.CYAN+f'Your score : {user_score}    /    Python score : {ai_score}')
    print (Fore.YELLOW+'--- TIE ---')
            
else :
    print ("""""")
    print (Fore.CYAN+f'Your score : {user_score}    /    Python score : {ai_score}')
    print (Fore.RED+'--- YOU LOST ---')

print ("")
print (Fore.WHITE+'END')

# Back.RESET()
# Fore.RESET()
