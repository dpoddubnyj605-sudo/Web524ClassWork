import random


def display_random_gift():
    gifts = ['барбариски', "мячик", "машинка", "конструктор"]
    gift = random.sample(gifts, 1)[0]
    print(f'Ваш подарок: {gift}')


while True:
    if input() == 'stop':
        break
        # exit()
        # quit()
    display_random_gift()
