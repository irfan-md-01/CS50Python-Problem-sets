from sys import exit

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
        exit(0)
    else:
        print("Invalid")
        exit(0)


def is_valid(s):
    if len(s)<2 or len(s)>6:
        return False

    for i in s :
        if not ( (i>='A' and i<='Z') or (i>='0' and i<='9') ):
            return False


    if((s[0]>='A' and s[0]<='Z') and (s[1]>='A' and s[1]<='Z') ):
        ind=len(s)
        for i in range(len(s)):
            if(s[i]=='0'):
                return False
            elif s[i]>='0' and s[i]<='9':
                ind = i
                break

        for i in range(ind, len(s)):
            if s[i]>='A' and s[i]<='Z':
                return False

        return True

    return False

# def check(s):
#     ind=len(s)
#     for i in range(len(s)):
#         if(s[i]=='0'):
#             return False
#         elif s[i]>='0' and s[i]<='9':
#             ind = i
#             break

#     for i in range(ind, len(s)):
#         if s[i]>='A' and s[i]<='Z':
#             return False

#     return True


if __name__ == "__main__":
    main()
