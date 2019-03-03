class Date:
    def __init__(self, d, m, y):
        self.dd = d
        self.mm = m
        self.yy = y

    def display(self):
        print(f"{self.dd}-{self.mm}-{self.yy}")

    def __str__(self):
        return f"{self.dd}/{self.mm}/{self.yy}"

    def __repr__(self):
        return f"Date({self.dd},{self.mm},{self.yy})"

#Main
today = Date(27, 2, 2019)
#print_date(today)
today.display()
print(today)
print(repr(today))
