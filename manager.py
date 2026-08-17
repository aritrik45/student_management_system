import json
from student import Student #impoting class Student from student.py
class StudentManager:  #creating a new class
    def __init__ (self): #constructor
        self.students=[] #create a empty list it will help to append
    def add_student(self, id, name, dep): #method to add student information
        if not id or not name or not dep:
            print("Invalid student information. Please fill all fields.")
            return
        if self.search_student(id): #check if the student already exist
            print("Student with this ID already exists.")
            return
        student=Student(id, name, dep) #object od class Student is created
        self.students.append(student) #add new object to end of the list
        print("Student added successfully")    

    def view_students(self):
        if not self.students: #check if the list is empty
            print("no student found")
            return

        print("\n --------------Student List-----------------")
        for student in self.students: #loop through the list of students
            print(f"ID: {student.id}"
                  f"\nName: {student.name}"
                  f"\nDepartment: {student.dep}" 
                  )
            print("-"*20) #speartor line for better visibility

    def search_student(self,id): #this method takes one input
        for student in self.student: #the loop checks one student at a time
            if student.id==id: #compare the id's
                return student
        return None  

    def update_student(self,id):
        student=self.search_student(id)  #find the student
        if student is None: #check wheather the student exist
            print("Student not found")
            return
        print("\n Leave a field empty if you don't want to change it.")
        name=input(f"Enetr new name ({student.name}):") #ask for new information
        department=input(f"Enetr new department ({student.dep}):")
        if name:
            student.name=name
        if department:
            student.dep=department
        print("Student updated succcessfully")        

    def delete_student(self,id):
        student=self.search_student(id)
        if student is None:
            print("Student not found")
            return
        self.students.remove(student) #if the student exist we remove that object from our list
        print("Student deleted successfully!")    

    def save_students(self):
        data=[]    #create an empty list
        for student in self.students:
            data.append(student.dict())  #convert object to dictionaries
        try:    
            with open("students.json","w")as f:
                json.dump(data,f,indent=4)
            print("students saved successfully!")   
        except OSError:
            print("Error: Could not save data.")    

    def load_students(self):
        try:
            with open("students.json","r") as f:
                data=json.load(f)
            for student_data in data:
                student=Student(
                    student_data["id"],
                    student_data["name"],
                    student_data["dep"])
                self.students.append(student)
            print("Students loaded successfully!")

        except FileNotFoundError:
            print("No existing student data found.")

        except json.JSONDecodeError:
            print("Error: Students.json conatins invalid data")    