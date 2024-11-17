"""
Главный модуль для демонстрации работы исключений
"""

from functions import (
    divide, multiply_positive, get_element_from_list,
    safe_divide, complex_operation, process_data,
    find_resource, open_file, calculate_square_root, add_positive
)


def main():
    """Запуск всех функций для демонстрации работы исключений"""
    try:
        print("1:")
        print(divide(4, 2))
        print(multiply_positive(8, 2))

        print("\n2:")
        get_element_from_list([1, 2, 3], 5)

        print("\n3:")
        print(safe_divide(10, 0))

        print("\n4:")
        complex_operation(-1, 2, 3)

        print("\n5:")
        process_data({"key": -5})

        print("\n7:")
        resource = {"database": "Connected", "cache": "Active"}
        find_resource(resource, "url")

        print("\n8:")
        print(open_file("nonexistent_file.txt"))
        print(calculate_square_root(25))
        print(add_positive(-3, 2))

    except Exception as e:
        print(f"Необработанная ошибка: {e}")


if __name__ == "__main__":
    main()
