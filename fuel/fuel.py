def main() :

    val = get_input()
    if(val>= 0.99) :
        print("F")
    elif(val <= 0.01) :
        print("E")
    else:
        print(f"{round(val*100)}%")


def get_input() :
    while True :
        try :
            x,y = input("Fraction: ").split("/")
            if('.' in x  or '.' in y ):
                raise ValueError
            x,y = map(float, (x,y))
            if (x<=y) :
                return x/y
        except ValueError:
            pass
        except ZeroDivisionError:
            pass

main()
