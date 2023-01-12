import random

list_of_words=["abruptly", "absurd", "lengths", "syndrome", "thumbscrew","galaxy", "pixel","nightclub", "unknown" ]

#the_random_word= random.choice(list_of_words)
#splitting the random word into letters and inserting the letters into a list 
list_of_char=[*random.choice(list_of_words)]
for i in range(0, len(list_of_char)):
    print("x ")
lives=6
number_of_l=len(list_of_char)
print(number_of_l)
print("you have 6 lives")
letter=input("insert a letter: ")
while lives>0 and number_of_l>0:
    print("de continuat")
print(list_of_char)