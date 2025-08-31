# Список заказов


def display_all_orders(orders):
    orders_iterator = iter(orders)
    while True:
        try:
            order = next(orders_iterator)
            print(f'Обрабатываем заказ: {order}')
        except StopIteration:
            print(f'Все заказы обработаны')
            break


def display_num_orders(orders, orders_num):
    orders_iterator = iter(orders)
    for i in range(orders_num):
        try:
            order = next(orders_iterator)
            print(f'Обрабатываем заказ: {order}')
        except StopIteration:
            print(f'Все заказы обработаны')
            break


if __name__ == '__main__':
    today_orders = ["Кофе", "Чай", "Пирожное", "Сэндвич"]
    display_all_orders(today_orders)
    display_num_orders(today_orders, 2)
