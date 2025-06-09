import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    match = re.search(r"^(\d{1,3}).(\d{1,3}).(\d{1,3}).(\d{1,3})$", ip)
  
    if match and int(match.group(1)) in range(0, 256) and int(match.group(2)) in range(0, 256) and int(match.group(3)) in range(0, 256) and int(match.group(4)) in range(0, 256):
        return True
    return False


if __name__ == "__main__":
    main()
