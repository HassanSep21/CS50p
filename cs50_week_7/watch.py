import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if yt_url := re.search(r'iframe.+src="https?://(?:www.)?youtube.com/embed/([^"]*)"', s):
        return "https://youtu.be/" + yt_url.group(1)


if __name__ == "__main__":
    main()
