word_list=["ardvark","baboon","camel"]



import random


chosen_word=random.choice(word_list)
display=[]

print(f'psst ,the solution is {chosen_word}.')

end_of_game=False

for _ in range(len(chosen_word)):
        display+='_'
    # print(display)

while not end_of_game:
    guess=input('Guess a letter').lower()

    
    
    for pos in range(len(chosen_word)):
        letter=chosen_word[pos]
        # print(f"cuurent position:{pos}\ncurrent letter:{letter} Guessed letter:{guess}")
        if letter==guess:
            display[pos]=letter
    print(display)   

    if "_" not in display:
        end_of_game=True
        print("You win!!!!")
  
