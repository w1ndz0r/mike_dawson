volume = []
cur_volume = 0

for i in range(10):
    minus = "-"
    plus = "+"
    if i == cur_volume:
        volume.insert(i, plus)
    volume.append(minus)
    print(volume[i], end="")
