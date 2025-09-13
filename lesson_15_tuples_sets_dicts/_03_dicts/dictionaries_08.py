def display_check(guests: dict):
    total = 0
    guests_names = ', '.join(guests.keys())
    for value in guests.values():
        total += value
    print(f'В кафе были: {guests_names}')
    print(f'Общий чек: {total}')
    print(f'Каждый должен заплатить: {total / len(guests):.2f} рублей.')


if __name__ == '__main__':
    cafe_guests = {
        "Сергей": 1600,
        "Андрей": 2200,
        "Дмитрий": 1800,
        "Диана": 2300,
        "Александр": 2500,
    }
    display_check(cafe_guests)
