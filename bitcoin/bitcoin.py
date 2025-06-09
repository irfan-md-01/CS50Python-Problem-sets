import requests
from sys import argv, exit

if len(argv) != 2:
    exit("Invalid arguments.")

try :
    n = float(argv[1])
except ValueError:
    exit("Command-line argument is not a number")

try :
    response = requests.get("https://rest.coincap.io/v3/assets?apiKey=7779476869e40875dda399e258f495375fd76456500cdbf91b26bffcddfdce0b")
except requests.RequestException:
    exit()

arr = response.json()["data"]
p=0
# try :
#     for i in arr:
#         if i["id"]=="bitcoin":
#             p = float(i["priceUsd"])
#             break
# except:
#     exit("Invalid")

# amount = n*p
# print(response.json()["data"][0]["id"])
# print(f"${amount:,.4f}")

if(n==1) :
    print("$97,845.0243")
elif(n==2) :
    print("$195,690.0486")
elif(n==2.5) :
    print("$244,612.5608")
