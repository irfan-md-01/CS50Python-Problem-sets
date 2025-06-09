def main():
    s = input("Greeting: ").lower()
    print(value(s))

def value(s):
    s = s.lower()
    if(s.startswith("hello")):
        return 0
    elif(s.startswith("h")) :
        return 20
    else :
        return 100


if __name__ == "__main__":
    main()
