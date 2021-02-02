#ovning1

class User:

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

user1 = User(
    input("skriv ditt förnamn: "),
    input("skriv ditt efternamn: "),
    int(input("skriv din ålder: ")))

print(user1.first_name,", " user1.last_name,", " user1.age)