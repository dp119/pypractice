#inputpath = input("please enter the path")
#var = inputpath.split("/")
#filename = var [-1]
#print ("filename:", filename)
#exttension = filename.split(".")
#print("exttension:", exttension[-1])
#print("directoty:", inputpath[:-len(filename)])

path = "/a/b/c/d.txt"
parts = path.rsplit('/',1)
dirname = parts[0]
print ("dirname:",dirname) 
filename = parts[1]
print ("filename:",filename)
