def main() :
    lst = []
    while True :
        try :
            s = input("Name: ").title()
            lst.append(s)
        except EOFError:
            print()
            ans = "Adieu, adieu, to "
            for i in lst[:-1]:
                ans+=f"{i}, "
            if(len(lst)>2) :
                ans+="and "
            elif(len(lst)==2) :
                ans = ans[:-2]+" and "
            ans+=f"{lst[-1]}"
            print(ans)
            break

main()
