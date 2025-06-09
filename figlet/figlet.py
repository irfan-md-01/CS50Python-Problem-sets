from sys import argv, exit
from pyfiglet import Figlet
from random import randint

figlet = Figlet()
arr = figlet.getFonts()
# print(len(argv))
if len(argv) not in list([1,3])  :
    # print("hello")
    exit("Invalid arguments.")

if (len(argv)==3 and argv[1] not in ['-f', '--font']) or (len(argv)==3 and argv[2] not in arr):
    exit("Invalid arguments.")

if (len(argv)==1) :
    f = arr[randint(0,len(arr)-1)]
    figlet.setFont(font=f)
else:
    figlet.setFont(font=argv[2])

s = input("Input: ")
print("Output:\n",figlet.renderText(s))
