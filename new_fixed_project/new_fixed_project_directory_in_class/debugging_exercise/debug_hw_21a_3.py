names = ["Tom", "Sarah", "David", "Emma"]

found = False

for name in names:
    if name == "David":
        found = True
        break

if found == False:
    print("Found David")
else:
    print("David not found")