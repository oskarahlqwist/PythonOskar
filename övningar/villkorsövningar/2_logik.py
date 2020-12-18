rain = input("Regnar det (ja/nej)? ")
R = True if rain == "ja" else False

wind = input("Blåser det (ja/nej)? ")
W = True if wind == "ja" else False

if (R == False and W == True):
    print("Påståendet stämmer inte")
else:
    print("Påståendet stämmer")