# project_polynomial

list=[0,0,0]

class polynomial():
    list1=[0,0,0]

    def plus(self):
        deg1 = int(input("enter deg1"))
        for i in range(0, deg1 + 1):
            self.list1[i] += int(input("your number"))

    def co(self):
        print(int(self.list1.count(0)))

    def __str__(self):
        p = str(self.list1)
        return p


deg = int(input("enter degree"))
for i in range(0, deg + 1):
    list[i] = int(input("enter your number"))

p1 = polynomial()
p1.list1 = list
print(str(p1))
p1.plus()
print(str(p1))
p1.co()
