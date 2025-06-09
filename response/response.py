from validator_collection import validators

def main():
    print(check(input("What's your email address? ")))


def check(s):
    try :
        return "Valid" if validators.email(s) else "Invalid"
    except:
        return "Invalid"


if __name__ == "__main__":
    main()
