print("first 5 lines")
with open ("captains.txt") as FH:
    counter = 0
    for line in FH:
        counter += 1
        print(line, end="")
        if counter == 5:
            break
print("last 5 lines")
with open("captains.txt") as FH:
    all_text = FH.read()
    all_lines = all_text.split('\n')
    num_lines = len(all_lines)
    counter = 0
    for line in all_lines:
        counter += 1
        if counter > num_lines -6:
            print(line)
    
print("first 5 captains names")
with open("captains.txt") as FH:
    headers = next(FH)
    counter = 0
    for line in FH:
        counter += 1
        print(line.split(',')[0])
