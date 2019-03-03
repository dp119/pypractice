#lucky Number code
lucky_num = 12
lucky_num = int (lucky_num)
nmbr_ofxx_chnc = 4
nmbr_ofxx_chnc = int (nmbr_ofxx_chnc)
i = 0
i = int (i)
while ( i < nmbr_ofxx_chnc ):
    lcky_nmbr_guss =  input ("Enter your lucky number")
    lcky_nmbr_guss = int ( lcky_nmbr_guss )
    if ( lcky_nmbr_guss == lucky_num ):
        print ("Great that is really lucky number")
        break
    elif ( lcky_nmbr_guss == lucky_num + 1 or lcky_nmbr_guss == lucky_num + 2 ):
         print ("you are very close")
    elif ( lcky_nmbr_guss == lucky_num - 1 or lcky_nmbr_guss == lucky_num - 2 ):
         print ("you are very close")
    else :
        print ("you are very far away")
    i += 1
print ("End")
