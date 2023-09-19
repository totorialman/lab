import sys
import math

class Roots:
    def __init__(self):
        self.a = 0.0
        self.b = 0.0
        self.c = 0.0
        self.roots = []
        self.num_roots = 0
        
    def read_coef(self, index, prompt):
        try:
            coef = sys.argv[index]
        except:
            print(prompt)
            coef = input()
        coef = float(coef)
        return coef
    
    def get_coefs(self):
        self.a = self.read_coef(1, 'Введите коэффициент А:')
        self.b = self.read_coef(2, 'Введите коэффициент B:')
        self.c = self.read_coef(3, 'Введите коэффициент C:')
        
    def find_roots(self):
        a = self.a
        b = self.b
        c = self.c
        d = b*b - 4*a*c
        if d > 0.0:
            self.num_roots = 2
            root1 = (-b + math.sqrt(d)) / (2.0 * a)
            root2 = (-b - math.sqrt(d)) / (2.0 * a)
            self.roots.append(root1)
            self.roots.append(root2)
        elif d == 0.0:
            self.num_roots = 1
            root = -b / (2.0 * a)
            self.roots.append(root)
            
    def print_roots(self):
        if self.num_roots != len(self.roots):
            print("Ошибка")
        else:
            if self.num_roots == 0:
                print('Нет корней')
            elif self.num_roots == 1:
                print('Один корень: ', self.roots[0])
            elif self.num_roots == 2:
                print('Два корня:', self.roots[0], self.roots[1])
def main():
    r = Roots()
    r.get_coefs()
    r.find_roots()
    r.print_roots()


if __name__ == "__main__":
    main()
