def get_value(x):
    cap_info = captains.get(x)
    return cap_info[-1]

with open("captains.txt") as FH:
    headers = next(FH)
    captains = list()
    for line in FH:
        cap = dict()
        parts = line.split(',')
        name = parts[0]
        mat, won, lost = [int (x) for x in parts[2:5]]
        cap ['name'] = name
        cap['mat'] = mat
        cap['won'] = won
        cap ['lost'] = lost
        captains.append(cap)
for cap in sorted (captains, key = get_value):
    per = cap['won']/cap['mat'] * 100
    print(f"{cap['name']},{cap['mat']}, {cap['won']}, {cap['lost']}", per)
