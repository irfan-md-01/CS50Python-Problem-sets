def main() :
    d = {
        "January" : 1,
        "February" : 2,
        "March" : 3,
        "April" : 4,
        "May" : 5,
        "June" : 6,
        "July" : 7,
        "August" : 8,
        "September" : 9,
        "October" : 10,
        "November" : 11,
        "December" : 12
    }
    while True :
        try :
            s = input("Date: ")
            if('/' in s) :
                month, day, year = map(int,s.split('/'))
                if(month<=12 and day<=31):
                    print(f"{year}-{(month):02}-{(day):02}")
                    return
            elif(',' in s) :
                l = s.split()
                month, day, year =l[0], l[1], l[2]
                day = day[:-1]
                if(month in d and int(day)<32):
                    print(f"{year}-{d[month]:02}-{int(day):02}")
                    return

        except EOFError:
            print()
            break
        except :
            pass

main()
