# Гибель пришельца
# Демнострирует взаимодействие обьектов
class Player(object):
    """Игрок в экшнен игре"""
    def blast(self, enemy):
        print("Игрок стреляет во врага.\n")
        enemy.die()

class Alien(object):
    """Враждебный пришелец инопланетянин в экшен-игре."""
    def die(self):
        print("О нет, меня убили.")

print("\t\tГибель прищельца\n")
hero = Player()
invader = Alien()
hero.blast(invader)

input("\n\nНажмите Enter чтобы выйти.")