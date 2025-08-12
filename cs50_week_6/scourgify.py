import sys
import csv

try:
    students = []
    if len(sys.argv) == 3:
        with open(f"{sys.argv[1]}") as file:
            reader = csv.DictReader(file)
            for row in reader:
                students.append({"name": row["name"], "house": row["house"]})
                
                with open(f"{sys.argv[2]}", "w") as file:
                    writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
                    writer.writeheader()
                    for student in students:
                        last, first = student["name"].split(", ")
                        house = student["house"]
                        writer.writerow({"first": first, "last": last, "house": house})

    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    else:
        sys.exit("Too few command-line arguments")
except FileNotFoundError:
    sys.exit(f"Could not read {sys.argv[1]}")
