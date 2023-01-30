class Demo:
    def __init__(self, v1 = 10, v2 = None):
        if v2 is None:
            self.a = v1
            self.b = self.a
        else:
            self.a = v1
            self.b = v2
            
    def plus(self):
        return (self.a + self.b)
    
d = Demo(20)

print(d.plus())