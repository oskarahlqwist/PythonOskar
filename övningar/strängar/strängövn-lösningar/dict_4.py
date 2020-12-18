t = ("oskar", 1, 2, 3, 4, "stringar", "rakso")

t2 = tuple()

for ord in t:
    if isinstance(ord,str):
        nytt_ord = ord,
        t2 = t2 + nytt_ord

print(t2)