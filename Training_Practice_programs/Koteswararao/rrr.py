with open ("runs.txt") as FH:
    all_text = FH.read()
    all_lines = all_text.split('\n')
   # print (all_lines)
  #  for i in range(len(all_lines)):
    #    all_lines[i]=int(all_lines[i])
    all_lines = [ int(x) for x in (all_lines)] 
    all_lines.sort()
    print (all_lines)

    print (sum(all_lines))
    
print(sum([int(x) for x in open ("runs.txt").read().split('\n')]))
