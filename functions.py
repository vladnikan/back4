"""
Функции для демонстрации работы исключений
"""

from exceptions import InvalidValueError, DivisionByNegativeError, ResourceNotFoundError

# Шаг 1
def divide(a, b):
    """Деление двух чисел. Выбрасывает исключение при делении на ноль."""
    if b == 0:
        raise ZeroDivisionError("Деление на ноль невозможно")
    return a / b


def multiply_positive(a, b):
    """Умножение двух положительных чисел. Выбрасывает исключение для отрицательных значений."""
    if a < 0 or b < 0:
        raise ValueError("Числа должны быть положительными")
    return a * b


# Шаг 2
def get_element_from_list(lst, index):
    """Получение элемента списка по индексу. Обрабатывает исключение IndexError."""
    try:
        return lst[index]
    except IndexError as e:
        print(f"Индекс за пределами списка: {e}")


# Шаг 3
def safe_divide(a, b):
    """Безопасное деление с блоком finally."""
    try:
        if b == 0:
            raise ZeroDivisionError("Деление на ноль невозможно")
        return a / b
    except ZeroDivisionError as e:
        print(f"Ошибка: {e}")
    finally:
        print("Функция safe_divide завершила выполнение")


# Шаг 4
def complex_operation(a, b, c):
    """Сложная операция с несколькими обработчиками исключений."""
    try:
        if a < 0:
            raise InvalidValueError("Число 'a' не должно быть отрицательным")
        result = a / b
        if result < c:
            raise DivisionByNegativeError("Результат меньше значения 'c'")
        return result
    except InvalidValueError as e:
        print(f"Ошибка значения: {e}")
    except DivisionByNegativeError as e:
        print(f"Ошибка деления: {e}")
    except ZeroDivisionError as e:
        print(f"Деление на ноль: {e}")
    finally:
        print("Функция complex_operation завершила выполнение")


# Шаг 5
def process_data(data):
    """Обработка данных с генерацией исключений."""
    try:
        if not isinstance(data, dict):
            raise TypeError("Ожидается словарь")
        if "key" not in data:
            raise KeyError("Ключ 'key' отсутствует")
        if data["key"] < 0:
            raise InvalidValueError("Значение 'key' не должно быть отрицательным")
        return data["key"] * 2
    except (TypeError, KeyError, InvalidValueError) as e:
        print(f"Ошибка: {e}")
    finally:
        print("Функция process_data завершила выполнение")


# Шаг 6 и Шаг 7
def find_resource(resources, resource_name):
    """Поиск ресурса. Выбрасывает пользовательское исключение ResourceNotFoundError."""
    try:
        if resource_name not in resources:
            raise ResourceNotFoundError(f"Ресурс '{resource_name}' не найден")
        return resources[resource_name]
    except ResourceNotFoundError as e:
        print(f"Ошибка поиска: {e}")
    finally:
        print("Функция find_resource завершила выполнение")


# Шаг 8
def open_file(filename):
    """Открытие файла с обработкой ошибок."""
    try:
        with open(filename, 'r', encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        print("Файл не найден")
    except IOError:
        print("Ошибка ввода-вывода")
    finally:
        print("Функция open_file завершила выполнение")


def calculate_square_root(value):
    """Вычисление квадратного корня. Выбрасывает исключение для отрицательных значений."""
    if value < 0:
        raise InvalidValueError("Значение должно быть неотрицательным")
    return value ** 0.5


def add_positive(a, b):
    """Сложение положительных чисел. Выбрасывает исключение для отрицательных значений."""
    if a < 0 or b < 0:
        raise InvalidValueError("Числа должны быть положительными")
    return a + b
