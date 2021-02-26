from hund2 import Hund
from hundagare import Hundagare

h = Hund("Fido","Poodle","familjehund",2,"svart")
#print (h)

h = Hund("Spot","Dauschhund","korkad",3,"rödbrun")
#print (h)

h.fodelsedag()
#print (h)

a = Hundagare("Charlie","Hundgatan",12,"Ordförande")
h.set_agare(a)
print (a)
print (h)

