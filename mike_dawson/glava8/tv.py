# телевизор
# переключает каналы от 1 до 10, увеличивает уровень громкости
class Tv(object):
    def __init__(self, channel = 1, volume = 4):
        self.__channel = channel
        self.__volume = volume
        print("Вы включили телевизор\nПульт у вас в руках")

    def __volume_show(self):
        volume = []
        cur_volume = self.__volume
        for i in range(10):
            minus = "-"
            plus = "+"
            if i == cur_volume:
                volume.insert(i, plus)
            volume.append(minus)
            print(volume[i], end="")

    def volume_up(self):
        self.__volume += 1
        if self.__volume > 9:
            print("Больше увеличивать громкость нельзя")
            self.__volume = 9
        self.__volume_show()
        return self.__volume

    def volume_down(self):
        self.__volume -= 1
        if self.__volume < 0:
            print("Звук выключен")
            self.__volume = 0
        self.__volume_show()
        return self.__volume

    def switch_channel(self, channel):
        self.__channel = channel
        print(channel)
        return channel

def main():
    tv = Tv()
    #print("Пробую достать атрибут channel")
    #print(tv.chan#
    choice = None
    while choice != "*":
        print("""
        [*]
        [1][2][3]
        [4][5][6]
        [7][8][9]
        [-][0][+]

        - + громкость
        * выключить телевизор
        """)
        choice = input("Нажмите кнопку: ")
        print()
        if choice == "*":
            print("До свидания")
        elif choice == "+":
            tv.volume_up()
        elif choice == "-":
            tv.volume_down()
        elif 0 <= int(choice) < 9:
            tv.switch_channel(choice)
        else:
            print("На пульте управления нет такой кнопки!", choice)

main()
input("\nНажмите Enter чтобы выйти")