class Calculator:
    def __init__(self, num):
        self.num = num

    def __add__(self, other):
        print("Сложение")
        return self.num + other.num

    def __sub__(self, other):
        print("Вычитание")
        return self.num - other.num

    def __mul__(self, other):
        print("Умножение")
        return self.num * other.num

    def __truediv__(self, other):
        print("Деление")
        return self.num / other.num
a = Calculator(1500)
b = Calculator(1240)
print(a + b)
print(a - b)
print(a * b)
print(a / b)