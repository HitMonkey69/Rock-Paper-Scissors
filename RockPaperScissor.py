#Rock Paper Scissors Game by HitMonkey69
 

import random 

print('1 for Rock')
print('2 for Paper')
print('3 for Scissors')
print('4 for Quit')

while True :

    usr = int(input('You Choose:'))

    computer = random.randint(1,3)

    if usr == 4 :
        break

    elif computer == 1:
        print(f'computer choose:Rock')
    elif computer == 2:
        print(f'computer choose:Paper')
    elif computer == 3:
        print(f'computer choose:Scissors')

    if usr < 1 or usr > 4 :
        print('Invalid Input')
    
    elif usr == computer :
        print('Draw')

    elif usr == 1 and computer == 3 :
        print('Victory')

    elif usr == 2 and computer == 1 :
        print('Victory')

    elif usr == 3 and computer == 2 :
        print('Victory')

    else :
        print('Defeat')
