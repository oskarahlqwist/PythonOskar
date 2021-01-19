age = 16
drivers_license = True
state = 'Oklahoma'

if (age >= 18 and drivers_license or state == 'Oklahoma'):
    print("Sure, you're allowed to drive")

##använd parenteser!
if ((age >= 18 and drivers_license) or state == 'Oklahoma'):
    print("Sure, you're allowed to drive")
