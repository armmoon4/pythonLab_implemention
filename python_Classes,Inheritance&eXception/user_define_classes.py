class Point():
    def getX(self):
        return self.x
point1 = Point()
point2 = Point()

print(point1)
print(point2)
print(point1 == point2)
point1.x = 5
point2.x = 10
print('Instace')
print(point1.getX())   #instace variable
print(point2.getX())
