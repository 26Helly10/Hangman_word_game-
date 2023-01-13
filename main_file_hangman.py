import random

list_of_words=["abruptly", "absurd", "lengths", "syndrome", "thumbscrew","galaxy", "pixel","nightclub", "unknown" ]

#the_random_word= random.choice(list_of_words)
#splitting the random word into letters and inserting the letters into a list 
list_of_char=[*random.choice(list_of_words)]
list_of_x=[]
for i in range(0, len(list_of_char)):
    list_of_x.append("_")

#initial lives
lives=6
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
nr1_stage=6
stages_game=stages[nr1_stage]
#number of letters 
number_of_l=len(list_of_char)
#initial number of g
letter_g=0

while lives>0 and number_of_l!=0:
    print(f"{list_of_x}")
    print(f"you have {lives} lives")
    print(f"{stages_game}")
    letter=input("insert a letter: ")
    ckeck_exist=number_of_l
    actual_number_of_l= number_of_l
    for i in range(0,len(list_of_char)):
        if letter ==list_of_char[i]:
            list_of_x[i]=letter
            number_of_l-=1  
        else:
            ckeck_exist-=1
    #print(ckeck_exist)
    #print(actual_number_of_l)
    if ckeck_exist <= 0:
        nr1_stage-=1
        print(f"{nr1_stage}")
        stages_game=stages[nr1_stage]
        lives-=1
if lives == 0:
    print(f"{stages_game}")
    print(f"You lose: {list_of_char}")
elif number_of_l==0:
    print(f"You win: {list_of_char}")