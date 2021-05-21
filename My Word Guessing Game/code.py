#ThisProjectIsMadeBySomeResearchFromTheInternetAndAlmostAllByMyHardwork
import random

name = input("What is your name Dear User")

print("Good Luck My Friend", name)

print("Just For your Knowledge the words can be any of these : siddharth,aayushmaan,mom,dad,whitehatjr,coding,programmer,word, guess,python,tv,mobile,smartphone,visual,studio,user,player,game,car,father,mother")

words = ['siddharth','aayushmaan','mom','dad','whitehatjr','coding','programmer','word','guess','python',
'tv','mobile','smartphone','visual','studio','user','player','game','car','father','mother']

word = random.choice(words)

guesses = ''

print("Guess the Characters")

turns = 20

while turns > 0:
    failed = 0
    #ThisIsForTakingOneWordAsAInputFromTheUser
    for w in word:
        #ThisIsUsedToCompareTheRealCharacterWithGuessedCharacter
        if w in guesses:
            print(w)

        else:
            print("_")

            failed+= 1
    

    if failed==0:
        print("You Win My Dear Friend", name)

        print("The word is :",word)
        break

    #IfWrongGuessThenAIAsksToInputAnotherGuess
    guess = input("Guess A Random Character : ")

    #ToStoreGuessInGuesses
    guesses+=guess

    #ToCheckInputIfItIsCorrectOrNot
    if guess not in word:
        turns-= -1

        print("Sorry Dear Friend Wrong Word Guessed")

        #WhenAllTheTurnsAreOver
        if turns==0:
            print("Sorry Dear Friend You Lost")
