import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):

    match = re.search(r'<iframe.*src="https?://(?:www.)?youtube\.com/embed/(\w+)"', s)
    if match :
        # print(match.group(1))
        return f"https://youtu.be/{match.group(1)}"
    return None


if __name__ == "__main__":
    main()
