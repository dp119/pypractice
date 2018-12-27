

FH = open("numbers.txt")
while True:
    one = FH.readline()
    if one == "":
        break
    else:
        print(one, end="")

FH.close()

print("Recommended")
with open("numbers.txt") as FH:
    for line in FH:
        print(line, end="")

print("Numbers")
r = range(5)
print(r)
for i in r:
    print(i)

