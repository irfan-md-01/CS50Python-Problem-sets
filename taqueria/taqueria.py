def main() :
    d = {
        "Baja Taco": 4.25,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }
    total = 0.00
    while True :
        try :
            s = input("Item: ").title()
            if(s in d):
                total+=d[s]
                print(f"Total: ${total:.2f}")
            else :
                raise ValueError
        except ValueError:
            pass
        except EOFError:
            print()
            break

main()
