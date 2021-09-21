from lessons.Day1_Practice.utils.connection import make_connection
from lessons.Day1_Practice.utils.Schema import Student
from lessons.Day1_Practice.utils.map import student_map


def update_student():
    my_client = make_connection()
    my_db = my_client['student_management_system']
    collection = my_db['student']

    while True:
        roll_number = int(input("Enter the Roll Number of the Student whose Data you want to change: "))

        student = collection.find_one({"roll_number": roll_number}, {"_id": 0, "roll_number": 0, "branch": 0})

        if student:
            print("Which Data you want to change for %s:" % student["name"])
            index = 1
            for key in student.keys():
                if key == "name":
                    pass
                else:
                    print(f"Press {index} to change {student_map[key]}")
                    index += 1

            choice = int(input("Enter Your Choice: "))
            updated_data = input(f"Enter new {student_map[list(student.keys())[choice]]} for {student['name']}: ")
            if list(student.keys())[choice] == "cgpa":
                updated_data = float(updated_data)
            collection.update_one({"roll_number": roll_number}, {"$set": {list(student.keys())[choice]: updated_data}})
            print("Updating Successful!")
            break

        else:
            print("Enter correct Roll Number...")

    next_decision = int(input("Press 1 to go to Main Menu. Press 0 to exit. Enter your Choice: "))
    return next_decision


def add_cgpa():
    my_client = make_connection()
    my_db = my_client['student_management_system']
    collection = my_db['student']

    for student in collection.find({"cgpa": {"$exists": False}}):
        roll_number = student["roll_number"]
        name = student["name"]

        while True:
            cgpa = float(input(f"Enter The CGPA of {name} ({roll_number}): "))
            if 0 <= cgpa <= 10:
                collection.update_one({"roll_number": roll_number}, {"$set": {"cgpa": cgpa}})
                break
            else:
                print("CGPA must be between 0 - 10")
    else:
        print("All Students have CGPA entered. If you want to update choose option 4 in Main Menu.")

    next_decision = int(input("Press 1 to go to Main Menu. Press 0 to exit. Enter your Choice: "))
    return next_decision


def display_students():
    my_client = make_connection()
    my_db = my_client['student_management_system']
    collection = my_db['student']
    index = 1
    for student in collection.find():
        print((" Student " + str(index) + " Data ").center(70, '-'))
        print("Roll Number:", student["roll_number"])
        print("Name:", student["name"])
        print('Address:', student["address"])
        print("D.O.B:", student["dob"])
        print("Branch:", student["branch"])
        try:
            print("CGPA:", student["cgpa"])
        except KeyError:
            pass
        index += 1

    next_decision = int(input("Press 1 to go to Main Menu. Press 0 to exit. Enter your Choice: "))
    return next_decision


def create_student():
    stud = Student()
    stud.set_first_name()
    stud.set_last_name()
    stud.set_address()
    stud.set_dob()
    stud.set_branch()
    stud.confirm_student_data()

    next_decision = int(input("Press 1 to go to Main Menu. Press 0 to exit. Enter your Choice: "))
    return next_decision


