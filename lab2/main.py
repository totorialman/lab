﻿from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square

def main():
    r = Rectangle("синего", 3, 2)
    c = Circle("зеленого", 5)
    s = Square("красного", 5)
    print(r)
    print(c)
    print(s,"\n")

    r = Rectangle("желтого", 1, 1)
    c = Circle("серого", 3)
    s = Square("черного", 10)
    print(r)
    print(c)
    print(s)

if __name__ == "__main__":
    main()