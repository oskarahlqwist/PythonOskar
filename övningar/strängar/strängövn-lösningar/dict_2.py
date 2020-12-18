t = (1, 1.25, 1.75, "oskar")

summan = 0

for nummer in t:
    if isinstance(nummer, int) or isinstance(nummer, float):
        summan += nummer

print ("Summan av nummerna i  tuplen är: ", summan)