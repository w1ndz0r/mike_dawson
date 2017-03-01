def display(message):
    """отображает сообщение"""
    print(message)

def give_me_five():
    five = 5
    return five

def ask_yes_no(question):
    """задает вопрос с ответом 'да' или 'нет'."""
    response = None
    while response not in ("y", "n"):
        response = input(question).lower()
    return response

display("Вам сообщение.\n")
number = give_me_five()
print("Вот что возвратила функция give_me_five():", number)
answer = ask_yes_no("Пожаолуйста введите 'y' или 'n': ")
print("Спасибо что ввели ", answer)
input("\n\nНажмите Enter чтобы выйти")