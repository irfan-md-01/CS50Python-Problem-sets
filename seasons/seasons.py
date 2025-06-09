from datetime import date, datetime
from sys import exit
from inflect import engine
import re

def main():
    try :
        p=engine()
        l=get_input()
        prev_date = date(year = l[0], month = l[1], day=l[2])
        curr_date = date.today()
        mins = get_minutes(curr_date, prev_date)
        s = p.number_to_words(mins, andword="")

        print(f"{s.capitalize()} {p.plural('minute', mins)}")

    except:
        exit("Invalid date")


def get_input():
    try :
        l= list(map(int, input("Date of Birth: ").split('-')))
        if len(l)!=3:
            raise ValueError
        return l
    except :
        exit("Invalid date")

def get_minutes(curr_date, prev_date):

    return ((curr_date-prev_date).days)*24*60

if __name__ == "__main__":
    main()
