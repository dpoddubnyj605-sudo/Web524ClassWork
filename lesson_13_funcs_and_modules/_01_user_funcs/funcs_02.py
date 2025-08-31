import random


def get_random_gift():
    gifts = ['барбариски', "мячик", "машинка", "конструктор"]
    gift = random.sample(gifts, 1)[0]
    return gift


if __name__ == '__main__':
    while True:
        if input() == 'stop':
            break
        our_gift = get_random_gift()
        # print(f'Ваш подарок: {our_gift}.')
        print(f'Ваш подарок: {get_random_gift()}.')
