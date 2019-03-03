def find_age(year_of_birth, present_year) :
    age = present_year - year_of_birth
    return age,age 

def main():
    year_of_birth = int(input("Print thr year born"))
    (age,age2)= find_age(year_of_birth, 2019)
    print ( "mainfunction users age",  age2)

main() 
