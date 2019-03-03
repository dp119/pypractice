
with open("captains.txt") as FH:
    headers = next(FH)
    captains = list()
    i = 0
    for line in FH:
        cap = dict()
        parts = line.split(',')
        name = parts[0]
        mat, won, lost = [int (x) for x in parts[2:5]]
        cap ['name'] = name
        cap['mat'] = mat
        cap['won'] = won
        cap['lost'] = lost
        cap['per'] = won / mat * 100
        captains.append(cap)
        i += 1
        #print (" I am at ",i, cap)
for cap in captains:
    print(f"{cap['name']},{cap['mat']}, {cap['won']}, {cap['lost']}, {cap['per']}")
    #print(cap['name'].rjust(50))
print (cap)
         #}, {cap['won']}, {cap['lost']}", "{:12.2f}".format(cap['per']))
#print (captains)
#print ("-------------")

#print ("{:12.2f}".format(captains[0]['per']))

for cap in sorted(captains, key=lambda x : x[-1]):
    print(f"{cap['name']},{cap['mat']}, {cap['won']}, {cap['lost']}, {cap['per']}")
    #print(cap['name'].rjust(50))
print (cap)
         #}, {cap['won']}, {cap['lost']}", "{:12.2f}".format(cap['per']))
#print (captains)
#print ("-------------")

#print ("{:12.2f}".format(captains[0]['per']))


