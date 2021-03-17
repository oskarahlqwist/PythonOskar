# Create a note app that stores notes as object 

class Note:
  def __init__(self, title):
    self.title = title
  
  def set_content(self, content):
    self.content = content
  
  def get_note(self):
    full_note = self.title.upper() + "\n" + self.content
    return full_note

my_notelist = []

while input("Want to add a note? y/n").lower() != "n":
  my_title = input("Title of the note: ")
  my_note = Note(my_title)
  my_content = input("Content of the note: ")
  my_note.set_content(my_content)
  my_notelist.append(my_note)

print("These are all my note objects: \n")
for note in my_notelist:
  print(note.get_note())
  print("----------------------")