from random import randint
from sys import exit

def main():
    n = get_level()
    arr = generate_integer(n)
    score = 0
    for i in range(0,20,2):
        x, y = arr[i], arr[i+1]
        question = f"{x} + {y} = "
        count=0
        while True:
            try :
                ans = int(input(question))
                if(ans == (x+y)):
                    score+=1
                else :
                    if( count<=1) :
                        raise ValueError
                    else :
                        print(question, x+y, sep="")

                break
            except ValueError:
                print("EEE")
                count+=1

    print(score)
    exit()

def get_level():
    while True :
        try :
            n = int(input("Level: "))
            if n in range(1,4):
                return n
        except ValueError:
            pass



def generate_integer(level):

    arr = []
    for i in range(10):
        if(level==1):
            x = randint(0,9)
            y = randint(0,9)
            arr.append(x)
            arr.append(y)

        elif(level==2):
            x = randint(10,99)
            y = randint(10,99)
            arr.append(x)
            arr.append(y)

        elif(level==3):
            x = randint(100,999)
            y = randint(100,999)
            arr.append(x)
            arr.append(y)
    return arr



if __name__ == "__main__":
    main()
