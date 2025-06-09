from sys import argv, exit

def main():

    if(len(argv)<2) :
        exit("Too few command-line arguments")
    elif(len(argv)>2) :
        exit("Too many command-line arguments")

    count = 0
    try :
        file_name = argv[1]
        if not (file_name.endswith(".py")):
            exit("Not a Python file")
        with open(file_name, "r") as file :
            for line in file:
                line = line.lstrip()
                if not( line=='' or line[0]=='#') :
                    count+=1

    except FileNotFoundError:
        exit("File does not exist")

    print(count)


main()
