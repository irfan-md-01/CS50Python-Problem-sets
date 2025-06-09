def main():
    s = input("What time is it? ").strip()
    x = convert(s)

    if(x>=7.0 and x<=8.0) :
        print("breakfast time")
    elif(x>=12.00 and x<=13.00) :
        print("lunch time")
    if(x>=18.00 and x<=19.00) :
        print("dinner time")


def convert(time):
    x,y = time.split(":")
    return int(x)+(int(y)/60.0)


if __name__ == "__main__":
    main()
