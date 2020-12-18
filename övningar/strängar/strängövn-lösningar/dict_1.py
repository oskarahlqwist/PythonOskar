fordon = {"abc123" : 75,'xyz999' : 765}

regnr = input("Vilket regnummer? (utan mellanrum): ")
stracka = int(input("Vad är kösträckan i mil?: "))

if regnr in fordon:
    fordon.update({regnr : stracka})
else:
    fordon.update({regnr : stracka})

print(fordon)
