timme = int(input('Ange timma: '))
minut = int(input('Ange minut: '))
plats = input('Ange plats: ')
tidsskillnad = int(input('Ange tidskillnad i hela timmar: '))

timme_annan_tidszon = timme + tidsskillnad

if timme_annan_tidszon >= 24:
    timme_annan_tidszon = timme_annan_tidszon - 24

elif timme_annan_tidszon < 0:
    timme_annan_tidszon = timme_annan_tidszon + 24

tid_annan_tidszon = str(timme_annan_tidszon) + ":" + str(minut)
print("Klockan är nu ", tid_annan_tidszon, "i", plats)
