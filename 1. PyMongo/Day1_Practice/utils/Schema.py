import re
from lessons.Day1_Practice.utils.connection import make_connection


class Student:
    __base_roll_number = 11200117000

    def __init__(self):
        self.first_name = None
        self.last_name = None
        self.address = None
        self.dob = None
        self.branch = None
        self.cgpa = None

    def set_first_name(self):
        first_name = input("Enter Student's First Name: ")
        self.first_name = first_name

    def set_last_name(self):
        last_name = input("Enter Student's Last Name: ")
        self.last_name = last_name

    def set_address(self):
        address = input("Enter Student's Address: ")
        self.address = address

    def set_dob(self):
        while not self.dob:
            date_regex = re.compile(r'(0[1-9]|1[0-9]|2[0-9]|3[0-1])/(0[1-9]|1[0-2])/(199[0-9]|200[0-5])$')

            dob = input("Enter Student's Data of Birth (format: dd/mm/yyyy): ")
            if date_regex.match(dob.strip()):
                self.dob = dob
            else:
                print("Write Date of Birth in the mentioned format and make sure your age is between 16 and 31R...")

    def set_branch(self):
        while not self.branch:
            try:
                available_branches = ['CSE', 'ME', 'CE', 'EE', 'ECE']
                print("The available branches are: ")
                index = 0
                for branch in available_branches:
                    index += 1
                    print(str(index) + ".", branch)

                branch_no = int(input("Choose Branch (Enter the number of the branch): "))
                if 0 < branch_no < len(available_branches):
                    self.branch = available_branches[branch_no - 1]
                else:
                    print("Wrong Option Chosen. Please Try Again...")

            except:
                print("Something Went Wrong. Please Try Again...")

    def set_marks(self):
        while not self.branch:
            cgpa = input("Enter CGPA")
            if 0 <= cgpa <= 10:
                self.cgpa = cgpa
            else:
                print("CGPA must be between 0 - 10")

    def confirm_student_data(self):
        print(" Please Confirm the Entered Student Data ".center(70, '-'))
        print("Name:", self.first_name, self.last_name)
        print('Address:', self.address)
        print("D.O.B:", self.dob)
        print("Branch:", self.branch)

        while True:
            res = input("Do you want to save the above data? [y/n] ")
            if res == 'y' or res == 'Y':
                my_client = make_connection()
                my_db = my_client['student_management_system']
                collection = my_db['student']

                record = {
                            "name": f"{self.first_name} {self.last_name}",
                            "address": self.address,
                            "dob": self.dob,
                            "branch": self.branch,
                        }

                try:
                    report = collection.find({}).sort('_id', -1)
                    prev_roll_number = report[0]["roll_number"]
                    record["roll_number"] = prev_roll_number + 1

                except IndexError as ie:
                    record["roll_number"] = self.__base_roll_number + 1

                collection.insert_one(record)
                print("Student Data Saved Successfully!")
                break

            elif res == 'n' or res == 'N':
                print("Returning to Main Menu...")
                break

            else:
                print("Wrong Option Selected.")

