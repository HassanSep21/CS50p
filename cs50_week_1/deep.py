ans = input("What is the answer to the Great Question of Life, the Universe and Everything? ")
ans = ans.lower().replace("-", " ").strip()
if ans == "42":
    print("Yes")
elif ans == "forty two":
    print("Yes")
else:
    print("No")