def calculate_price(fruits_dict, fruit, weight):
    if fruit in fruits_dict:
        price = fruits[fruit] * weight / 1000
        return f'Стоимость: {price} рублей'
    return "Нет в ассортименте"


if __name__ == '__main__':
    fruits = {
        "яблоки": 400,
        "груши": 200,
        "персики": 600
    }
    user_fruit = input("Выберите фрукт: ").strip().lower()
    fruit_weight = float(input("Вес в граммах: "))
    print(calculate_price(fruits, user_fruit, fruit_weight))
