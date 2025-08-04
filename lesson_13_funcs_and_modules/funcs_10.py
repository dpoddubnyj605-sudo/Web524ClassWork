def get_total_paint(width, height, consumption=0.2, layers=2):
    total = width * height * consumption * layers
    return round(total, 2)


if __name__ == '__main__':
    print(f'Итого краски необходимо: {get_total_paint(3, 4)} л')
    print(f'Итого краски необходимо: {get_total_paint(3, 4, 0.4)} л')
    print(f'Итого краски необходимо: {get_total_paint(3, 4, 0.2, 3)} л')
    print(f'Итого краски необходимо: {get_total_paint(3, 4, layers=3)} л')
    print(f'Итого краски необходимо: {get_total_paint(width=3, height=4, layers=3)} л')
