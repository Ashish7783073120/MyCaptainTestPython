# Python-beginners-tasks
class rectangle():
    def __init__(self ,l ,w):
        self.length = l
        self.width = w
    def rectangle_area(self):
        return self.length*self.width
print(rectangle(10,5).rectangle_area())
