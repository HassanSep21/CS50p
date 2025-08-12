months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    date = input("Date: ").strip()

    if date.find(",") != -1:
        date = date.replace(",", "").replace(" ", "/").split("/")
        month, day, year = date[0].capitalize(), date[1], date[2]
        if month in months and int(day) <= 31:
            month = months.index(month) + 1
            print(f"{year}-{int(month):02}-{int(day):02}")
            break
        else:
            continue

    elif date.find("/") != -1:
        date = date.split("/")
        month, day, year = date[0], date[1], date[2]
        if month in months:
            continue
        if int(month) <= 12 and int(day) <= 31:
            print(f"{year}-{int(month):02}-{int(day):02}")
            break
        else:
            continue
    elif date.find("-") != -1:
        date = date.split("-")
        year, month, day = date[0], date[1], date[2]
        if int(month) <= 12 and int(day) <= 31:
            print(f"{year}-{int(month):02}-{int(day):02}")
            break
    else:
        continue