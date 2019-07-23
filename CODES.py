print ("Main Menu")

record = True

students = []
while record:

    student_record = [" 0. Create, 1. Read, 2. Udpate, 3. Delete, 4. Exit"]
    print(student_record)

    choice = (input("Enter A Number: "))

    if choice == "0":
        Name = (input("Enter A Name: "))
        students.append(Name)
    elif choice == "1":
        print(students)
    elif choice == "2":
        index = int (input("Index no. : "))
        new_student = input("Enter new name: ")
        students[index] = new_student
        print("You have udpated the data")
    elif choice == "3":
        delete = input("Enter name : ")
        students.remove(delete)
        print("You have deleted the name")
    elif choice == "4":
        record = False
    else:
        print("Try Again")
            
        
