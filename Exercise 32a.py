
import sys
import random


def new_game ():
    inpta = input("Press any key to play another game or 'E' to exit!\n")
    if inpta == "E" :
        print("Thanks for playing")
        sys.exit()
    else:
        main()
        
def main ():
    
    def wordtoguess ():
        file = open("SOWPODS.txt","r+")
        lista = []
        for elements in file:
            lista.append(elements)
    
        a = random.choice(lista).strip()
        x = []
        for i in a:
            x.append(i)
    
        return(x)

    b = wordtoguess()    
    print(b)       
    
    g = ["_" for i in range(len(b))]
    c = 6

    def count_of_guesses ():
        nonlocal c
        c -= 1
        if c == 6:
            print("  o")
            print("J[_]L")
            print(" I I")
        elif c == 5:
            print("  o")
            print("J[_]L")
            print(" I ")
        elif c == 4:
            print("  o")
            print("J[_]L")
        elif c == 3:
            print("  o")
            print(" [_]L")
        elif c == 2:
            print("  o")
            print(" [_] ")
        elif c == 1:
            print("  o")
        else :
            print("Hanged")
             
    def outpt ():
        nonlocal g
        if "_" not in g:
            print("You have guessed correctly")
            new_game ()
        elif c == 0:
            print("No more guesses")
            new_game ()
                
        inpt  = input('Guess a letter:\n').upper()
        if inpt in g:
            print("You have already guessed the letter")
            outpt ()
        elif inpt in b:    
            for i in range(0,len(b)):    
                if b[i] == inpt:
                   g[i] = inpt 
               
            print("Right Guess") 
            sepa = ","
            print("Guess till now:\n",sepa.join(g))
            count_of_guesses ()
            outpt ()
               
        else:
            print("Wrong guess.Try again!")
            count_of_guesses ()
            outpt ()


    outpt()
main()
