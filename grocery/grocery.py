def main() :
    d = {}
    while True :
        try :
            s = input().upper()
            d[s] = d.get(s,0) + 1
        except EOFError:
            print()
            d = dict(sorted(d.items()))
            for i in d :
                print(d[i], i)
            break

main()
