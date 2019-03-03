booked = [1,3,9,12,13,18,26,27,28,29]
holidays = [4,5,15,16,21,22]
print([x for x in range (1,31) if x not in booked + holidays])
      

