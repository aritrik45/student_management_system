from manager import StudentManager #importing the StudentManager class from manager.py file
def show_menu(): #function to show menu
    print("n"+"="*50)
    print("  Weicome to Student Mangement System  ")
    print("="*50)
    print("1. Add student")
    print("2. View students")
    print("3. Search student")
    print("4. Update student")
    print("5. Delete student")
    print("6. Exit")
    print("="*50)
    
manager=StudentManager()
manager.load_students() #load existing student data
while True: #infinite loop
    show_menu()
    print("1. Add student")
    print("2. View students")
    print("3. Search student")
    print("4. Update student")
    print("5. Delete student")
    print("6. Exit")
    choice=input("Enter your choice: ")
    if choice=="1":
        id=input("Enter student ID:")
        name=input("Enter student name:")
        dep=input("Enter Department:")
        manager.add_student(id,name,dep) #it's call the method add_student        

    elif choice=="2":
        manager.view_students()
    elif choice=="3":
        id=input("Enter student ID to search:")
        student=manager.search_student(id)
        if student:
            print("\n Student Found")
            print(f"ID : {student.id}")
            print(f"Name : {student.name}")
            print(f"Department : {student.dep}")
        else:
            print("Student not found")
    elif choice=="4": 
        id=input("Enter student ID to update:")
        manager.update_student(id) 
    elif choice=="5":
        id=input("Enter student ID to delete:")
        manager.delete_student(id)   
    elif choice=="6":
        manager.save_students()
        print("Thank you")
        break               
    

    else:
        print("Invalid choice")   
        