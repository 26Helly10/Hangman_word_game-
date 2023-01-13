import random
import hangman_words
import hangman_art
import os
from time import sleep
#the_random_word= random.choice(list_of_words)
#splitting the random word into letters and inserting the letters into a list 
list_of_char=[*random.choice(hangman_words.word_list)]
list_of_x=[]

for i in range(0, len(list_of_char)):
    list_of_x.append("_")

#initial lives
lives=6
nr1_stage=6
stages_game=hangman_art.stages[nr1_stage]
#number of letters 
number_of_l=len(list_of_char)


#initial number of g
letter_g=0
inserted_letters=[]
print(hangman_art.logo)

while lives>0 and number_of_l!=0:
    if not len(inserted_letters) ==0:
        print(f"the letters already added: {inserted_letters}")
    
    print(f"{list_of_x}")
    print(f"you have {lives} lives")
    print(f"{stages_game}")
    
    letter=input("insert a letter: ")
    ckeck_exist=False
    actual_number_of_l= number_of_l
    
    for i in range(0,len(list_of_char)):
        if letter ==list_of_char[i]:
            list_of_x[i]=letter
            number_of_l-=1
            ckeck_exist= True
    #print(ckeck_exist)
    #print(actual_number_of_l)
    
    if ckeck_exist== False:
        
        if letter in inserted_letters:
            print(f"! you already have entered this letter before ! {letter}")
        else:
            inserted_letters.append(letter)
            nr1_stage-=1
            stages_game=hangman_art.stages[nr1_stage]
            lives-=1
    else:
        
        if letter in inserted_letters:
            print(f"! you already have entered this letter before ! {letter}")
        else:
            inserted_letters.append(letter)
    sleep(3)
    os.system('cls')        
            
if lives == 0:
    print(f"{stages_game}")
    print(f"You lose: {list_of_char}")
elif number_of_l==0:
    print(f"You win: {list_of_char}")
