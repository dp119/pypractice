

# <h1> factorial

print("Enter a number:")

num = int(input())

f = 1

if f < 0:
    print("Factorial does'nt exist for negative number.")
elif f == 0:
    print("Factorial of 0 is 1")
else:
    for i in range(1, 1 + num):
        # print(i)
        f = f * i
    print("Factorial of {} is {}".format(num, f))
