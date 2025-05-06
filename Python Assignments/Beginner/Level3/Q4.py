class Shape:
    def getArea(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        self.length = length
    
    def getArea(self):
        return self.length ** 2
    

def main():
    l = int(input("Enter length of one side of a square: "))
    s = Square(l)
    print("Area of square is: ", s.getArea())

if __name__ == "__main__":
    main()
