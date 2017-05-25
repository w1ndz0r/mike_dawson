i = 0
with open("bruney.csv", "r", encoding='utf-8') as r, open("bruney_new.csv", "w") as w:
        for line in r:
            try:
                new_line = line.encode('cp1252').decode('cp1251')
                w.write(new_line)
            except UnicodeEncodeError:
                pass

r.close()
w.close()
