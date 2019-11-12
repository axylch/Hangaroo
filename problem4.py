import random


wordlist = ["apple", "banana", "carrots", "dewberries", "eggplant"]
secretWord = random.choice(wordlist)
lettersGuessed = []
guesses = []

#HILADO - 2ECEB 
   
def isWordGuessed(secretWord, lettersGuessed):
    lsw = list(secretWord)
    llg = list(lettersGuessed)
    check = all(i in lsw for i in llg)
    if check: 
        return True
    else:
        return False
     
        
def getGuessedWord(secretWord, lettersGuessed):
    llg = list(lettersGuessed)
    print ("\nInput letters: ")
    print (llg)
    
    out = " "
    for i in secretWord:
        if i in lettersGuessed:
            out = out + i + " "
        else: out += "_ "
    print ("\n")
    return out
        
        

def getAvailableletters(lettersGuessed):
    llg = list(lettersGuessed)
    oil = "abcdefghijklmnopqrstuvwxyz"
    loil = list(oil)
    
    remainder = [i for i in loil if i not in llg]
    print ("\nThe remaining available letters are: \n", remainder)
        
        
               
def Hangaroo(secretWord):
    
    lettersGuessed = " "
    guess = 8
    
    print ("Welcome  to Hangman!")
    print("The word you're about to guess is ", str(len(secretWord))," letters long.")
    
    while guess >=0:
       remainder = getAvailableletters(lettersGuessed)
       
       print("You have ", str(guess), " guesses left.")
       print("Available letters: ", str(remainder))
       
       guessletter = input("Guess a letter: ").lower()
           
       if guessletter in lettersGuessed: 
           print ("You have already guessed that letter: ",getGuessedWord(secretWord,lettersGuessed))
           
       elif guessletter in secretWord:
           lettersGuessed += guessletter
           print("Correct!: ", getGuessedWord(secretWord,lettersGuessed))
           if isWordGuessed(secretWord,lettersGuessed) == True:
               print("You have guessed the word!")
               break
                    
       else:
           lettersGuessed += guessletter
           print("Wrong letter guessed." + getGuessedWord(secretWord, lettersGuessed))
           guess -= 1
           if guess == 0 and isWordGuessed(secretWord, lettersGuessed) == False:
               print("You ran out of guesses. Game over.\n", "The word was", str(secretWord))
               break


isWordGuessed(secretWord, lettersGuessed) 
getGuessedWord(secretWord, lettersGuessed)
getAvailableletters(lettersGuessed)          
Hangaroo(secretWord)
                
                
               
           
           
           

               
               