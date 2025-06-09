from sys import exit

def main():
    s = input("Fraction: ").strip()
    x = convert(s)
    print(gauge(x))
    exit(0)

def convert(s):
    try :
        x,y = s.split("/")
        if('.' in x  or '.' in y ):
            raise ValueError
        x,y = map(float, (x,y))
        if(y==0) :
            raise ZeroDivisionError
        if (x<=y) :
            return round((x/y)*100)
    except ValueError:
        print("Value Error")
        raise ValueError
    except ZeroDivisionError:
        print("Zero Division Error")
        raise ZeroDivisionError



def gauge(val):
    if(val>= 99) :
        return "F"
    elif(val <= 1) :
        return "E"
    else:
        return f"{val}%"


if __name__ == "__main__":
    main()
