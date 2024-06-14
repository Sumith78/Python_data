


class Student:
  
  # #default constructor -Automatic
  # def __init__(self):
  #   pass
  
  
  #parameterized constructor
  def __init__(self,fullname,marks) -> None:
    self.name=fullname
    self.marks=marks
    print("adding new details..")
    
  def welcome(self):
    print("welcome student ,",self.name)
    
  def get_marks(self):
    return self.marks
    
s1=Student("Sumith",97)
print(s1.name,s1.marks)
s1.welcome()
print(s1.get_marks())

s2=Student("Karan",98)
print(s2.name,s2.marks)