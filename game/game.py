from random import randint, seed
from sys import exit
def main() :
    seed(42)
    while True :
        try :
            n1 = int(input("Level: "))
            if(n1<=0):
                raise ValueError
            break
        except ValueError:
            pass
    n = randint(1,n1)
    while True :
        try :
            g = int(input("Guess: "))
            if(g<=0):
                raise ValueError
            elif(n==g):
                print("Just right!")
                exit()
            elif(n>g):
                print("Too small!")
            else:
                print("Too large!")
        except ValueError:
            pass
main()
