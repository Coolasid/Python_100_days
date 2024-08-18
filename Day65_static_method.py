class Math:

    def __init__(self, num):
        self.num = num

    def addtonum(self, n):
        self.num = self.num + n


    @staticmethod
    def add(a,b):
        return a+b
    
# result = Math.add(1, 2)
# print(result)

a = Math(5)

print(a.num)

a.addtonum(6)

print(a.num)

print(a.add(7,3))
print(Math.add(7,8))  #we can call static method like this also