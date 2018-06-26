class shape:
    def __init__(self,length,breadth):
        self.length = length
        self.breadth = breadth

        def sqarea(self):
            return self.length*self.length

        def recarea(self):
            return self.length * self.breadth

class rectangle(shape):
    def rectangle(self):
        print("Area of reactangle:",super().recarea)

class square(shape):
    def square(self):
        print("Area of square:",super().sqarea)

obj = shape(10,20)
obj1 = rectangle(10,20)
obj2 = square(10,10)

obj1.rectangle()
obj2.square()