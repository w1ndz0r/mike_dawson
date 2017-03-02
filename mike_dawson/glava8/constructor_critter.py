# Зверушка с конструктором
# Демонстрирует метод-конструктор
class Critter(object):
    """Виртуальный питомец"""
    def __init__(self):
        print("Появлиась на свет новая зверюшка")
    def talk(self):
        print("\nПривет, я зверюшка - экземпляр класса Critter.")

# основная часть
crit1 = Critter()
crit2 = Critter()
crit1.talk()
crit2.talk()

input("\nНажмите Enter чтобы выйтию")

11