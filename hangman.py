# Single Player Game "Hangman" using Python 3.x

import pandas as pd
import mysql.connector
import random
import webbrowser

#Open database connection

db = mysql.connector.connect(host="localhost",user="root",password ="",database="game_play_history" )
cursor = db.cursor()

#Create Variables

win=0
lost=0
rounds=0
choice='Yes'

#Getting User Input

playerName=str(input("Enter your Name : "))


while choice == "Yes":
    guessed="" #Create Variable
    rounds +=1

#Getting Random Word and Hint from Text files

    num = random.randrange(0,20)
    with open('words list.txt', 'r')as f:
        words=f.readlines()
        word=(words[num])[:-1]

    with open('hints.txt', 'r')as f:
        hints=f.readlines()
        hint=(hints[num])[:-1]

        print()
        print("*********************************************************************************************")
        print()
        print('                     Hint is : ',hint)
        print()
        print("*********************************************************************************************")
    
#Process
    
    turns=len(word)
    
    while (0 < turns):
        fails=0
        
        print()
        print('word : ',end='')
        for letter in word:
            if letter in guessed:
                print(letter,end='')
            else:
                print("_", end=' ')
                fails +=1
        print()
        print(turns,'turns remain')

        if fails ==0:
            print ()
            print ("You Won!")  #Outputs for Player guesses the correct word within the given number of turns
            print ("Word is",'"'+word+'"')
            win +=1
            break

        guess = input('Letter : ')
        guessed = guessed + guess

        if guess not in word:
            turns -=1

            if turns ==0 :
                print()
                print("You Lost!")  #Outputs for Player runs out of turns before guessing the word
                print("Word is",'"'+word+'"')
                lost +=1
    print()
    print("------------------------------------------------------------")
    print()
    print("    Do you want to Play again ----> Enter 'Yes' " )
    print("    Do you want to Quit the Game ----> Enter 'No' " )
    print()
    choice=str(input("Enter your Option (Yes/No) : ")) #Get User Input
    print()
    print("------------------------------------------------------------")
    print()

print(".... Thank you for Playing ....")
print("       ! Come Again !       ")

#Output Show in Webbrowser
df_information = pd.DataFrame({'Player_Name' :[playerName],'Total_NO_Played' :[rounds],'Total_Win' :[win], 'Total_Lose' :[lost]})
html = df_information.to_html()
text_file = open("table.html" ,'w')
text_file.write(html)
text_file.close()
webbrowser.open('table.html')

#Store Records in DB
mySQLText = "INSERT INTO information (Player_Name, Total_NO_Played, Total_Wins, Total_Loses) VALUES (%s,%s,%s,%s)"
myValues = (playerName, rounds, win, lost)
cursor.execute(mySQLText, myValues)
db.commit()

print()
print(cursor.rowcount,"Record Added The DataBase") #Output

#Disconnect from Server
db.close()
 





