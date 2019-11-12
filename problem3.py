secretWord = input("Input Secret Word: ")
lettersGuessed = input("Type ALL guessed letters: ")
llg = list(lettersGuessed)
print ("Letters guessed:\n", llg)

#HILADO - 2ECEB

def getAvailableletters(lettersGuessed):
    oil = "abcdefghijklmnopqrstuvwxyz"
    loil = list(oil)
    
    remainder = [i for i in loil if i not in llg]
    print ("\nThe remaining available letters are: \n", remainder)

    