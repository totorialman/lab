import sys
import math

def get_coef(index, prompt):
    try:
        coef_str = sys.argv[index]
    except:
        print(prompt)
        coef_str = input()
    coef = float(coef_str)
    return coef

def get_roots(a, b, c):
    roots = []
    d = b*b - 4*a*c
    if d > 0.0:
        root1 = (-b + math.sqrt(d)) / (2.0 * a)
        root2 = (-b - math.sqrt(d)) / (2.0 * a)
        roots.append(root1)
        roots.append(root2)
    elif  d == 0.0:
        root = -b / (2.0 * a)
        roots.append(root)
    return roots

def main():
    a = get_coef(1, 'Введите коэффициент А:')
    b = get_coef(2, 'Введите коэффициент B:')
    c = get_coef(3, 'Введите коэффициент C:')
    roots = get_roots(a,b,c)
    if len(roots) == 0:
        print('Нет корней')
    elif len(roots) == 1:
        print('Один корень:', roots[0])
    elif len(roots) == 2:
        print('Два корня:', roots[0], roots[1])
    
if __name__ == "__main__":
    main()
