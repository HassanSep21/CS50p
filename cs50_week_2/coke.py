due = 50
#while True:
#    if due != 0:
#        print(f"Amount Due: {due}")
 #       coin = int(input("Insert Coin: "))
 #       if coin == 5 or coin == 10 or coin == 25:
 #           due = due - coin
#            continue
#        else:
 #           continue
 #   else:
  #      print(f"Change Owned: {due}")
 #   break
while True:
    if due > 0:
        print(f"Amount Due: {due}")
        coin = int(input("Insert Coin: "))
        if coin == 5 or coin == 10 or coin == 25:
            due = due - coin
            continue
        else:
            continue
    else:
        print(f"Change Owed: {abs(due)}")
        break
