total = 50
while True :
    print(f"Amount Due: {total}")
    x = int(input("Insert Coin: "))
    if(x in [25,10,5]):
        total = total - x
    if(total<=0):
        break

print("Change Owed:", total*-1)
