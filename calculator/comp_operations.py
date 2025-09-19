import math

class CompOperations:

    def qe(self, a ,b ,c):
        calc1 = b*b -4*a*c
        if calc1 < 0:
            return 'no ans'
        else:
            calc2 = math.sqrt(calc1)
            ans1 = (-b + calc2)/(2*a)
            ans2 = (-b - calc2)/(2*a)
            if ans1 == ans2:
                return f'x={ans1}'
            else:
                return f'x1={ans1} , x2={ans2}'


    def ms(self, x1 ,y1 ,x2 ,y2):
        x = (x1 + x2)/2
        y = (y1 + y2)/2
        return f'({x},{y})'

    def distance(self, x1 ,y1 ,x2 ,y2):
        ans1 = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
        return f'd={ans1}'

    def slop(self, x1 ,y1 ,x2 ,y2):
        if x1 == x2:
            return 'cant'
        else:
            ans1 = (y1 - y2)/(x1 - x2)
            return ans1

    def fanc(self, x, y, m):
        r = m*(-x)+y
        if r < 0:
            return f'y={m}x{r}'
        elif r == 0:
            return f'y={m}x'
        else:
            return f'y={m}x+{r}'

    def trig(self, x1, z1, x2, z2, a, b):
        try:
            a0 = math.tan(math.radians(a - 90))
            b0 = math.tan(math.radians(b - 90))
            if abs(a0 - b0) < 1e-10:
                return 'Lines are parallel or overlapping'
            x3 = (x1 * a0 - x2 * b0 - z1 + z2) / (a0 - b0)
            z3 = a0 * (x3 - x1) + z1
            return f'({round(x3, 0)},{round(z3, 0)})'
        except Exception as e:
            return f'Error: {str(e)}'