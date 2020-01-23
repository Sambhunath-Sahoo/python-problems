class circle:
    pi = 3.14
    def __init__(self, r):
        self.r = r
    

    def circum(self):
        return 2*circle.pi*self.r


c = circle(3)
print(c.circum())