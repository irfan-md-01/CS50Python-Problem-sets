def main():
    s = input("Input: ").strip()
    print("Output:", shorten(s))

def shorten(word):
    ans = ""
    for i in word :
        if i.lower() not in ['a', 'e', 'i', 'o', 'u'] :
            ans+= i
    return ans



if __name__ == "__main__":
    main()
