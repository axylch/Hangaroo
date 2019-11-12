secretWord = input("Input Secret Word: ")
lettersGuessed = input("Type ALL guessed letters: ")

lsw = list(secretWord)
llg = list(lettersGuessed)

#HILADO - 2ECEB

def isWordGuessed(secretWord, lettersGuessed):
        check = all(i in lsw for i in llg)
        if check: 
            return True
        else:
            return False
 
    
    
   
   
       
    
    