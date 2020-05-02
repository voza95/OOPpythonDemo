class Studnet:

    school = "Demo4"

    def __init__(self,m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):
        return (self.m1 + self.m2 + self.m3) / 3        

s1 = Studnet(34,75,50)
s2 = Studnet(37,85,40)

print(s1.avg())
print(s2.avg())