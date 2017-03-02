import sys
def open_file(file_name, mode):
    """Открывает файл."""
    try:
        the_file = open(file_name, mode, encoding='utf-8')
    except IOError as e:
        print("Невозможно отркыть файл", file_name, "Работа программы будет завершена.\n", e)
        input("\nНажмите Enter чтобы выйтию")
        sys.exit()
    else:
        return the_file

def next_line(the_file):
    """Возвращает в отформатированном виде очередную строку игрового файла."""
    line = the_file.readline()
    line = line.replace("/", "\n")
    return line

def next_block(the_file):
    """Возвращает очередной блок данных из игрового файла"""
    category = next_line(the_file)
    question = next_line(the_file)
    answers = []
    for i in range(4):
        answers.append(next_line(the_file))
        correct = next_line(the_file)
        if correct:
            correct = correct[0]
            explanation = next_line(the_file)
    return category, question, answers, correct, explanation