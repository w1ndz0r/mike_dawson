import pickle, shelve

print("\nПомещение списков на полку")
s = shelve.open("pickles2.dat")

s["variety"] = ["огурцы", "помидоры", "капуста"]
s["shape"] = ["целые", "кубиками", "соломкой"]
s["brand"]= ["Главнпродукт", "Чумак", "Бондюэль"]

s.sync()

print("\nИзвлечение списков из файла полки:")
print("торговые марки -", s["brand"])
print("формы -", s["shape"])
print("виды овощей -", s["variety"])

s.close()

input("\n\nНажмите Enter чтобы выйти.")