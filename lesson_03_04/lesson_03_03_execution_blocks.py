# counter = 0
# while counter < 5:
#     print('Inside cycle')
#     counter += 1
# print('Outside cycle')
# print()
#
# for i in range(5):
#     print('Inside range cycle')
# print('Outside range cycle')
# print()
#
#
# some_list = ['item_1', 'item_2', 'item_3']
# for item in some_list:
#     print(item)
# print()

try:
    print('Провокация')
except:
    print("Исключение если провокация сработала")
else:
    print("Выполнение если исключений не было")
finally:
    print("Выполняем в любом случае")


def some_func():
    print('Внутри функции')


some_func()
print()


class ExampleClass(object):

    def __init__(self, attr):
        self.attr = attr

    def display_attr(self):
        print(self.attr)


my_obj = ExampleClass('Some Attr')
my_obj.display_attr()
