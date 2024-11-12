import cmath


def quadratic_roots(a, b, c):
    # Проверка, что a не равно 0
    if a == 0:
        raise ValueError("Коэффициент 'a' не должен быть равен 0 для квадратного уравнения.")
    if not all(isinstance(i, (int, float)) for i in (a, b, c)):
        raise ValueError("Coefficients must be numbers")
    # Здесь должна быть логика для вычисления корней квадратного уравнения.
    # Например, для простоты:
    if a == 0:
        raise ValueError("Coefficient 'a' cannot be zero")
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
b = 2
c = 3

roots = quadratic_roots(a, b, c)
print("Корни квадратного уравнения:", roots)