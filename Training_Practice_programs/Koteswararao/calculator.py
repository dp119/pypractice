def add(num1, num2):
    sum = num1 + num2
    return sum

def sub(a, b):
    subt = a - b
    return subt

a = 10
b = 20
addition = add (a, b)
print ("Sum:", addition)
subtract = sub(a, b)
print ("sub:",subtract)

aus_1_score = 250
ind_1_score = 220
aus_2_score  = 150
aus_total = add (aus_1_score, aus_2_score)
ind_need = sub(aus_total, ind_1_score) + 1
print ("ind_need", ind_need)

veg = 120
fruits = 55
i_gave = 200
return_money = sub (i_gave, add(veg, fruits))
print ("change", return_money)
print ("change", sub (i_gave, add(veg, fruits)))

