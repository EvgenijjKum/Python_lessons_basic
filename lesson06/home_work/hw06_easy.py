# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.
import math

class Triangle:
    def __init__(self, a_x, a_y, b_x, b_y, c_x, c_y):
        self.a_x = a_x
        self.a_y = a_y
        self.b_x = b_x
        self.b_y = b_y
        self.c_x = c_x
        self.c_y = c_y
        print('Введенные значения:')
        print('A('+ str(a_x) + ',' + str(a_y) + ')')
        print('B('+ str(b_x) + ',' + str(b_y) + ')')
        print('C('+ str(c_x) + ',' + str(c_y) + ')')


    # метод
    def area(self):
        return math.fabs(((self.b_x - self.a_x)*(self.c_y - self.a_y) - (self.c_x - self.a_x)*(self.b_y - self.a_y)))/2

    def perimeter(self):
        length_a_b = math.sqrt(((self.b_x-self.a_x)**2)+((self.b_y-self.a_y)**2))
        length_b_c = math.sqrt(((self.c_x-self.b_x)**2)+((self.c_y-self.b_y)**2))
        length_a_c = math.sqrt(((self.c_x-self.a_x)**2)+((self.c_y-self.a_y)**2))
        return length_a_b + length_b_c + length_a_c

    def height_tr(self):
        a = 2 * self.area()
        c = math.sqrt(((self.c_x-self.b_x)**2)+((self.c_y-self.b_y)**2))
        return a/c

print('Задача 1')
# Формат ввода: Ax,Ay,Bx,By,Cx,Cy
tr1 = Triangle(-1,3,-2,-1,2,3)

print('Площадь треугольника: ',tr1.area())
print('Высота треугольника: ',round(tr1.height_tr(),2))
print('Периметр треугольника ',round(tr1.perimeter(),2))
print()
# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

class Trapeze:
    def __init__(self, a_x, a_y, b_x, b_y, c_x, c_y, d_x, d_y):
        self.a_x = a_x
        self.a_y = a_y
        self.b_x = b_x
        self.b_y = b_y
        self.c_x = c_x
        self.c_y = c_y
        self.d_x = d_x
        self.d_y = d_y
        print('Введенные значения:')
        print('A('+ str(a_x) + ',' + str(a_y) + ')')
        print('B('+ str(b_x) + ',' + str(b_y) + ')')
        print('C('+ str(c_x) + ',' + str(c_y) + ')')
        print('D('+ str(d_x) + ',' + str(d_y) + ')')
        self.length_a_b = math.sqrt(((self.b_x-self.a_x)**2)+((self.b_y-self.a_y)**2))
        self.length_b_c = math.sqrt(((self.c_x-self.b_x)**2)+((self.c_y-self.b_y)**2))
        self.length_c_d = math.sqrt(((self.d_x-self.c_x)**2)+((self.d_y-self.c_y)**2))
        self.length_a_d = math.sqrt(((self.d_x-self.a_x)**2)+((self.d_y-self.a_y)**2))


    def lenght(self):
        print('Длина стороны AB: ' + str(round(self.length_a_b,2)))
        print('Длина стороны BC: ' + str(round(self.length_b_c,2)))
        print('Длина стороны CD: ' + str(round(self.length_c_d,2)))
        print('Длина стороны AD: ' + str(round(self.length_a_d,2)))

    def area_tr(self):
        triangle_one = math.fabs(((self.b_x - self.a_x)*(self.c_y - self.a_y) - (self.c_x - self.a_x)*(self.b_y - self.a_y)))/2
        triangle_two = math.fabs(((self.d_x - self.a_x)*(self.c_y - self.a_y) - (self.c_x - self.a_x)*(self.d_y - self.a_y)))/2
        result = triangle_one + triangle_two
        print('Площадь трапеции: ' + str(round(result,2)))

    def check_equilateral(self):
    	if self.length_a_b == self.length_c_d:
    		print('Введенные значения соответствуют равнобочной трапеции')
    	elif self.length_b_c == self.length_a_d:
    		print('Введенные значения соответствуют равнобочной трапеции')
    	else:
    		print('Введенные значения не соответствуют равнобочной трапеции')
    def lenght_all(self):
    	result_all = self.length_a_b + self.length_b_c + self.length_c_d + self.length_a_d
    	print('Периметр: ' + str(round(result_all,2)))



print('Задача 2')
# Формат ввода: Ax,Ay,Bx,By,Cx,Cy,Dx,Dy
tr2 = Trapeze(-1,3,-2,-1,3,-1,2,3)
tr2.check_equilateral()
tr2.lenght()
tr2.lenght_all()
tr2.area_tr()

