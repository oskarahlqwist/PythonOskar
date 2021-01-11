lista = ["John","Jenny", "Agneta", "Lisa", "Adam", "Brian", "Gary", "Nils","Tina", "Zena","Örjan"]

letter_a_to_m = ["A","B","C","D","E","F","G","H","I","J","K","L","M"]
letter_n_to_ö = ["N","O","P","Q","R","S","T","U","V","X","Y","Z","Å","Ä","Ö"]

names_a_to_m = []
names_n_to_ö = []
for i in lista:
    if(i[0]) in letter_a_to_m:
        names_a_to_m.append(i)
    elif(i[0]) in letter_n_to_ö:
        names_n_to_ö.append(i)

names_a_to_m.sort()
names_n_to_ö.sort()

print("A-M", names_a_to_m, "\nN-Ö", names_n_to_ö)