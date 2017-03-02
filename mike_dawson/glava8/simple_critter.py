# Просто зверюшка
# Демонстрирует простейшие класс и обьект
class Critter(object):
    """Виртуальный питомец"""
    def talk(self):
        print("Привет. Я зверюшка - экземпляр класса Critter.")

crit = Critter()
crit.talk()
input("\nНажмите Enter чтобы выйтию")