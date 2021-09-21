from utils.functions import create_student, display_students, add_cgpa, update_student


def main():
    while True:
        print(" Welcome to Student Database Management System ".center(80, '-'))
        print('1. Press 1 to create new Student.')
        print('2. Press 2 to Display all Student Details.')
        print('3. Press 3 to Add CGPA of all Student.')
        print('4. Press 4 to Update a Particular Data of one Student.')
        print('5. Press 0 to exit.')
        choice = int(input("Enter your Choice: "))
        decision = 1

        if choice == 0:
            break

        if choice == 1:
            decision = create_student()

        if choice == 2:
            decision = display_students()

        if choice == 3:
            decision = add_cgpa()

        if choice == 4:
            decision = update_student()

        if decision == 0:
            break


if __name__ == '__main__':
    main()
