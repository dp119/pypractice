class Cricketer:
    def __init__(self, name, mat, won, lost):
        self.name = name
        self.mat = mat
        self.won = won
        self.lost = lost

    def display(self):
        print(f"{self.name}: {self.mat} {self.won} {self.lost}")

    def __str__(self):
        return f"{self.name}/{self.mat}/{self.won}/{self.lost}"

    def __repr__(self):
        return f"Cricketer({self.name}/{self.mat}/{self.won}/{self.lost})"

#Main
cap1 = Cricketer('Sachin', 150, 120, 22)
#print_date(today)
cap1.display()
print(cap1)
print(repr(cap1))
