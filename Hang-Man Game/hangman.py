#hangman game

correct_word='diamond'
fill=list('_ _ _ _ _ _ _')

def play(correct_word):
    wrong_attempt=0
    for i in range(1,11):
        print(''.join(fill))
        if (''.join(fill)=='d i a m o n d'):
            print('\nYou got it!')
            print('The word is: diamond')
            break
        else:
            print('\n***********************')
            print('Attempts left: ',11-i)
            print('Wrong Attempts: ',wrong_attempt)
            h=input('Enter the letter: ')
            if len(h)!=1:
                print('Enter a single letter sweetie!')
            else:
                if (h in correct_word or h in correct_word.upper()):
                    if (h=='d' or h=='D'):
                        fill[0]='d'
                        fill[12]='d'
                    elif (h=='i' or h=='I'):
                        fill[2]='i'
                    elif (h=='a' or h=='A'):
                        fill[4]='a'
                    elif (h=='m' or h=='M'):
                        fill[6]='m'
                    elif (h=='o' or h=='O'):
                        fill[8]='o'
                    elif (h=='n' or h=='N'):
                        fill[10]='n'
                else:
                    wrong_attempt=wrong_attempt+1
                    if wrong_attempt==1:
                        print('-----------')
                        print('       /   ')
                        print('   /\ /    ')
                        print('     O     ')
                        print('     |     ')
                        print('     |     ')
                        print('    / \    ')
                        print('   /   \   ')
                    elif wrong_attempt==2:
                        print('-----------')
                        print('       /   ')
                        print('      /    ')
                        print('     O     ')
                        print('    /|     ')
                        print('   / |     ')
                        print('    / \    ')
                        print('   /   \   ')
                    elif wrong_attempt==3:
                        print('-----------')
                        print('           ')
                        print('      /\   ')
                        print('     O     ')
                        print('    /|     ')
                        print('   / |     ')
                        print('    / \    ')
                        print('   /   \   ')
                        print('I m tied to hope only now :(')
                    elif wrong_attempt==4:
                        print('-----------')
                        print('           ')
                        print('           ')
                        print('     O     ')
                        print('    /|\    ')
                        print('   / | \   ')
                        print('    / \    ')
                        print('   /   \   ')
                        print('You lost the man\'s life :(')
                        print('GO AWAY !!!')
                        break

def intro():              #function for intro(rules, taking name and all)
    name=input('Enter your name: ')
    print('\nWelcome ',name,',you have to save a kind man from dying!! \n')
    print('Rules:\n1. You have to guess a word letter by letter. \n2. Each wrong letter will result in person getting closer to death.')
    print('\n********\nYou will get 10 attempts in total and 4 wrong attempts you can afford, make your guesses wisely :)\n******** ')
    print('HINT: Pressure makes me worth, without it I m worthless, Women loves me, not easy to get though!')
    x=input('Press Y to see the hangman: ')
    if (x=='y' or x=='Y'):
        print('-----------')
        print('   \   /   ')
        print('    \ /    ')
        print('     O     ')
        print('     |     ')
        print('     |     ')
        print('    / \    ')
        print('   /   \   ')
        print('Hangman: Hello ',name,',I m hanging from a rope, save me!!')
        m=input('Press S to start saving me: ')
        if (m=='s' or m=='S'):
            play(correct_word)
        else:
            print('Enter S dumbo!!')
            pass
    else:
        print('How will you save the man, if you can\'t enter a Y properly!')


intro()




