def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    ip = ip.split(".")
    if len(ip) != 4:
        return False
    else:
        for no in ip:
            if int(no) <= 255 and int(no) >= 0:
                continue
            else:
                return False
        return True


if __name__ == "__main__":
    main()
