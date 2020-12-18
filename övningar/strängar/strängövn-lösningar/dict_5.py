l = [2.56, 1, 2, 3, 4, 5, 6, 7, "oskar"]

t = tuple()

for i in l:
    if isinstance(i, int):
        item = i,
        t = t + item

print(t)