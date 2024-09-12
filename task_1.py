# Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей. Дано a, b, c - стороны предполагаемого треугольника. Требуется сравнить длину каждого отрезка-стороны с суммой двух других. Если хотя бы в одном случае отрезок окажется больше суммы двух других, то треугольника с такими сторонами не существует. Отдельно сообщить является ли треугольник разносторонним, равнобедренным или равносторонним.

def triangle_type(a, b, c):
    # Проверка существования треугольника
    if a + b > c and a + c > b and b + c > a:
        # Определяем тип треугольника
        if a == b == c:
            return "Треугольник равносторонний"
        elif a == b or b == c or a == c:
            return "Треугольник равнобедренный"
        else:
            return "Треугольник разносторонний"
    else:
        return "Треугольника с такими сторонами не существует"

# Пример использования
a = float(input("Введите длину стороны a: "))
b = float(input("Введите длину стороны b: "))
c = float(input("Введите длину стороны c: "))
result = triangle_type(a, b, c)
print(result)
