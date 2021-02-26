class User:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
  
    def get_fullname(self):
        full_name = self.first_name + " " + self.last_name
        return full_name

f_name = input("Vad heter du i förnamn? ")
l_name = input("Vad heter du i efternamn? ")
age = input("Hur gammal är du? ")

new_user = User(f_name, l_name, age)
print("Du är alltså " + new_user.age +" år gammal?")

f_name = input("Vad heter din kompis i förnamn? ")
l_name = input("Vad heter din kompis i efternamn? ")
age = input("Hur gammal är din kompis? ")

new_friend = User(f_name, l_name, age)
user_list = []
user_list.append(new_user.get_fullname())
user_list.append(new_friend.get_fullname())
print(user_list)