# Классово верная зверюшка
# демонстрирует атрибуты класса и статические методы
class Critter(object):
    """Виртуальный питомец"""
    total = 0
    @staticmethod
    def status():
        print("\nВсего зверюшек сейчас", Critter.total)
    def __init__(self, name):
        print("На свет появилась новая зверюшка")
        self.name = name
        Critter.total += 1

# основная часть
print("Нахожу значение атрибута класса Critter.total", end=" ")
print(Critter.total)
print("\nСоздаю зверюшек")
crit1 = Critter("Зверюшка 1")
crit2 = Critter("Зверюшка 2")
crit3 = Critter("Зверюшка 3")
Critter.status()
print("\nОбращаюсь к атрибуту класса через обьект", end=" ")
print(crit1.total)

input("\nНажмите Enter чтобы выйтию")