from sys import argv, exit
from PIL import Image, ImageOps
from os.path import splitext
def main():

    if(len(argv)<3) :
        exit("Too few command-line arguments")
    elif(len(argv)>3) :
        exit("Too many command-line arguments")

    file_name = argv[1]
    output_file_name = argv[2]
    if not (file_name.endswith(".jpg") or file_name.endswith(".jpeg") or file_name.endswith(".png")):
        exit("Invalid input ")
    elif not (output_file_name.endswith(".jpg") or output_file_name.endswith(".jpeg") or output_file_name.endswith(".png")):
        exit("Invalid output")
    elif splitext(file_name)[1]!=splitext(output_file_name)[1]:
        exit("Input and output have different extensions")

    try :

        shirt = Image.open("shirt.png")
        size = shirt.size
        with Image.open(file_name) as file:
            file = ImageOps.fit(file, size)
            file.paste(shirt, shirt)
            file.save(output_file_name)



    except FileNotFoundError:
        exit(f"Input does not exist")


main()
