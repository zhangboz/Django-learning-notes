class object_test():
    attribute1 = "text2"
    attribute2 = "text2"
    def __str__(self):
        return self.attribute1


x = object_test
x.attribute1 = "x1"
x.attribute2 = "x2"
y = object_test
y.attribute1 = "y1"
y.attribute2 = "y2"


print(x.attribute2,y.attribute2)