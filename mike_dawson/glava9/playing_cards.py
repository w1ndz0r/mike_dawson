# Карты
# Демонстрирует сочетание обьектов
# "с" (сlubs) - трефы, "d" (diamonds) - бyбны, "h" (hearts)- червы, "s" (spades) - пики
class Card(object):
    """Одна игральная карта"""
    RANKS = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    SUITS = ["c", "d", "h", "s"]
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
    def __str__(self):
        rep = self.rank + self.suit
        return rep

class Hand(object):
    """Рука - набор карт на руках у одного игрока."""
    def __init__(self):
        self.cards = []
    def __str__(self):
        if self.cards:
            rep = ""
            for card in self.cards:
                rep += str(card) + " "
        else:
            rep = "<пусто>"
        return rep
    def clear(self):
        self.cards = []
    def add(self, card):
        self.cards.append(card)
    def give(self, card, other_hand):
        self.cards.remove(card)
        other_hand.add(card)

# основная часть
card1 = Card("A","c")
print("Вывожу на экран обьект-карту")
print(card1)
card2 = Card(rank = "2", suit = "c")
card3 = Card(rank = "З", suit = "c")
card4 = Card(rank = "4", suit = "c")
card5 = Card(rank = "5", suit = "с")
print("\nBывoжy еще четыре карты:")
print(card2)
print(card3)
print(card4)
print(card5)

my_hand = Hand()
print("\nНапечатаю карты которые у меня на руках до раздачи")
print(my_hand)

my_hand.add(card1)
my_hand.add(card2)
my_hand.add(card3)
my_hand.add(card4)
my_hand.add(card5)
print("\nПечатаю пять карт, которые появились у меня на руках")
print(my_hand)

your_hand = Hand()
my_hand.give(card1, your_hand)
my_hand.give(card2, your_hand)
print("\nПервые две из моих кард я передал вам")
print("Теперь у вас на руках:")
print(your_hand)
print("А у меня на руках:")
print(my_hand)

my_hand.clear()
print("\nУ меня на руках после того, как я сбросил все карты:")
print(my_hand)

input("\n\nPress Enter to exit")
