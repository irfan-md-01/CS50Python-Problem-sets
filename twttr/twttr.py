s = input("Input: ")
ans=""
for i in s :
    if i.lower() not in ['a', 'e', 'i', 'o', 'u'] :
         ans+= i

print("Output:", ans)

