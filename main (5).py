class Student:

  def__init__(self,name,roll_number,cgpa):
  self.name = name
  self.roll_number = roll_number
  self.cgpa = cgpa
  
  
def sort_students(stuent_list):
  #sort the list of students descending order of cgpa
  sort_students = sorted(stuent_list,
                       key = lambda studenet:student.cgpa,
                      reverse = True)
  #Syntax_Lambda arg:exp
  return sorted_students


#example usage
students = [
  Student("Hari","A123",7.8),
  Student("Srikanth","A124",8.9)
  Student("Saumya","A125",9.1),
  Student("Mahidhar,A126",9.9), 
]

sorted_students = sort_students(students)

#Print the sorted list of students
for student in sorted_students:
  print("Name:{},roll number:{}CGPA:{}".format(student.name,   stundent.roll number,
                                              student.cgpa))
  

  