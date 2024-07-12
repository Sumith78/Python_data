class Student:
  def __init__(self,name,marks) -> None:
    self.name=name
    self.marks=marks
    
  def get_avg(self):
    sum=0
    for val in self.marks:
      sum +=val
    print("Hi", self.name , "Your Average score is: ",sum/3)
    
s1=Student("tony stark",[92,97,98])
s1. get_avg()

