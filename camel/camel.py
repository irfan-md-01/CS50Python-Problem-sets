s = input("What time is it? ").strip()

ans = ""
for i in s:
    if(i>='A' and i<='Z'):
        ans+='_'
        ans+=i.lower()
    else :
        ans+=i

print(ans)

