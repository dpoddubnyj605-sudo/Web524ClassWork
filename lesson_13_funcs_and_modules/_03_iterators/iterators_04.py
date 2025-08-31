# Список заказов


def display_all_steps(recipe_steps):
    recipe_steps_iterator = iter(recipe_steps)
    while True:
        try:
            order = next(recipe_steps_iterator)
            print(f'Щаг: {order}')
        except StopIteration:
            print(f'Рецепт завершен')
            break


def display_num_steps(recipe_steps_iterator, steps_num):
    for i in range(steps_num):
        try:
            step = next(recipe_steps_iterator)
            print(f'Щаг: {step}')
        except StopIteration:
            print(f'Рецепт завершен')
            break


if __name__ == '__main__':
    # Список шагов рецепта
    vegetable_recipe_steps = [
        "Нагрейте сковороду",
        "Добавьте масло",
        "Положите нарезанные овощи",
        "Обжарьте до готовности",
        "Посыпьте специями и подавайте"
    ]
    display_all_steps(vegetable_recipe_steps)
    print()

    vegetable_recipe_steps_iterator = iter(vegetable_recipe_steps)
    print("Вася готовит:")
    display_num_steps(vegetable_recipe_steps_iterator, 3)
    print("Петя готовит")
    display_num_steps(vegetable_recipe_steps_iterator, 3)
