import datetime
from datetime import date, timedelta

def daterange(start, slut):
    for n in range(int((slut - start).days)+1):
        yield start + timedelta(n)

def sjudagar():
    
    start = date(2020, 1, 1)
    
    slut = date(2021, 1, 1)

    allanummer = []
    
    i = 0
    
    for dt in daterange(start, slut):
        
        allanummer = []
   
        year = dt.strftime("%y")
        yearnmr = [int(nr) for nr in year]

        month = dt.strftime("%m")
        monthnmr = [int(nr) for nr in month]

        day = dt.strftime("%d")
        daynmr = [int(nr) for nr in day]

        allanummer = yearnmr + monthnmr + daynmr

        sum_nummer = sum(allanummer)
        if sum_nummer == 7:
            i += 1
            
            print(month, "/", day, "/", year)

    return i


sjudagar = sjudagar()
print("Dagar som blir  7: ", sjudagar)
sannolikhet = (sjudagar/366)
print("Sannolikheten för detta: ", sannolikhet)