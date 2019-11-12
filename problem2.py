secretWord = input("Input Secret Word: ")
lettersGuessed = input("Type ALL guessed letters: ")
llg = list(lettersGuessed)

#HILADO - 2ECEB

def getGuessedWord(secretWord, lettersGuessed):
    print ("\nInput letters: ")
    print (llg)
    
    out = " "
    for i in secretWord:
        if i in lettersGuessed:
            out = out + i + " "
        else: out += "_ "
    print ("\n")
    return out
       