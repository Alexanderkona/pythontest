import cmath

def quadratic_roots(a, b, c):
    # Проверка, что a не равно 0
    if a == 0:
        raise ValueError("Коэффициент 'a' не должен быть равен 0 для квадратного уравнения.")

    # Вычисление дискриминанта
    D = b ** 2 - 4 * a * c

    # Вычисление корней в зависимости от дискриминанта
    if D > 0:
        root1 = (-b + cmath.sqrt(D)) / (2 * a)
        root2 = (-b - cmath.sqrt(D)) / (2 * a)
        return (root1, root2)
    elif D == 0:
        root = -b / (2 * a)
        return (root,)
    else:
        root1 = (-b + cmath.sqrt(D)) / (2 * a)
        root2 = (-b - cmath.sqrt(D)) / (2 * a)
        return (root1, root2)  # Возвращаем комплексные корни

# Пример использования
a = 1
b = 4
c = 3

roots = quadratic_roots(a, b, c)
print("Корни квадратного уравнения:", roots)