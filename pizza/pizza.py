from sys import argv, exit
from tabulate import tabulate
import csv

def main():

    if(len(argv)<2) :
        exit("Too few command-line arguments")
    elif(len(argv)>2) :
        exit("Too many command-line arguments")

    try :
        file_name = argv[1]
        if not (file_name.endswith(".csv")):
            exit("Not a CSV file")
        with open(file_name, "r") as file :
            reader = csv.reader(file)
            lines = []
            for row in reader:
                lines.append(row)
            headers = lines[0]

            print(tabulate(lines[1:], headers = headers, tablefmt="grid"))

    except FileNotFoundError:
        exit("File does not exist")


main()
