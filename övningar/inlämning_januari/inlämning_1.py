from datetime import timedelta, date

def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)


def dateequalsseven():
    
    start_date = date(2020, 1, 1)
    
    end_date = date(2021, 1, 1)

    
    allnumbers = [] 
    
    i = 0
    
    for single_date in daterange(start_date, end_date):
        
        allnumbers = []
   
        year = single_date.strftime("%y")
        
        y_digits = [int(d) for d in year]

        month = single_date.strftime("%m")
        m_digits = [int(d) for d in month]

        day = single_date.strftime("%d")
        d_digits = [int(d) for d in day]

       
        allnumbers = y_digits + m_digits + d_digits

        
        sum_numbers = sum(allnumbers)
        if sum_numbers == 7:
            i += 1
            
            print(str(month) + "/" + str(day) + "/" + str(year))

    return i


datesequalsseven = dateequalsseven()
print("Antal dagar = 7 under 2020 är: " + str(datesequalsseven))
chanse = (datesequalsseven/366)
print("sannolikhet att detta inträffar är: " + str(chanse))