def add(num1, num2):
    sum = num1 + num2
    return sum

def sub(a, b):
    subt = a - b
    return subt

if  __name__ == "__main__":
    a = 10
    b = 20
    addition = add (a, b)
    print ("Sum:", addition)
    subtract = sub(a, b)
    print ("sub:",subtract)
print("from calc", __name__)
