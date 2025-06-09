from sys import argv, exit
from csv import reader, DictReader, DictWriter

def main():

    if(len(argv)<3) :
        exit("Too few command-line arguments")
    elif(len(argv)>3) :
        exit("Too many command-line arguments")

    try :
        file_name = argv[1]
        output_file_name = argv[2]
        if not (file_name.endswith(".csv") or output_file_name.endswith(".csv")):
            exit("Not a CSV file")

        with open(file_name, "r") as views, open(output_file_name, "w") as analysis:
            reader = DictReader(views)
            writer = DictWriter(analysis, fieldnames=["first", "last"]+ reader.fieldnames[1:])
            writer.writeheader()
            for row in reader:
                fname = row['name'].split(",")[1].strip()
                lname = row['name'].split(",")[0].strip()
                writer.writerow(
                    {
                         "first": fname,
                         "last": lname,
                         "house": row["house"]
                    }
                )



    except FileNotFoundError:
        exit(f"Could not read {file_name}")


main()
