from abc import ABC, abstractmethod

for i in range(5):
    if i == 3:
        break
    print(f'i = {i}')
print()

for i in range(10):
    if i == 3 or i == 7:
        continue
    print(f'i = {i}')
print()

for i in range(10):
    if i == 3 or i == 7:
        pass
    print(f'i = {i}')
print()


for i in range(10):
    if i == 12:
        break
    print(f'i = {i}')
else:
    print(f'Цикл завершен без прерываний')
print()

for i in range(10):
    if i == 5:
        break
    print(f'i = {i}')
else:
    print(f'Цикл завершен без прерываний')
print()

# class AbstractClass(ABC):
#
#     @abstractmethod
#     def some_method(self):
#         pass
#
#
# class ConcreteClass(AbstractClass):
#
#     def some_method(self):
#         print('Вот и метод!')
#
#
# my_class = ConcreteClass()
# my_class.some_method()


