def a1(l):              #Denna funktion a1() tar ett argument
    i = len(l)-1        #tilldelar variabeln i värdet av (antalet element i aktuell lista)-1.
    while i >= 0:       #Så länge som i är större än eller lika med 0
        print(l[i])     #skriv ut listindex motsvarande värdet av i. Eftersom listindex börjar räkna upp från 0 används "-1" för att i ska matcha detta hela vägen genom listan.
        i = i - 1       #Värdet av i kommer för varje varv att minska med 1. 
                        #(Alltså backar utskriften ett steg i listan för varje gång loopen körs. 
                      