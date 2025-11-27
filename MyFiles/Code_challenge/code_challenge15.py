import os

print("Student information system")

#Empty Dictionary

student_record = {}

while True:
    print("SELECT  FROM THE FOLLOWING OPTION")
    print("A - Add Student Record")
    print("B - Print All Student Record")
    print("C - Search Student Record")
    print("D - Delete Student Record")
    print("E - Edit Student Record")
    print("F - Export Student Record")
    print("G - Import Student Record")
    print("X - Exit System")

    option = input("SELECT FROM THE OPTIONS ABOVE ---> ").lower()

    if option == 'a':
        os.system('cls')

        print("\nADDING STUDENT RECORD")

        id_no = input("Please Input Student ID Number ---> ")

        first_name = input("Please input studnet name ---> ").upper()
        last_name = input("Please input student last name ---> ").upper()
        age = eval(input("Please input student age ---> "))
        course = input("Please input student course ---> ").upper()
        section = input("Please input student section ---> ").upper()

        #This is for storing data into dictionary - student_record

        student_record[id_no] = [first_name, last_name, age, course, section]
        print("DATA SAVED SUCCESSFULLY")

        #This will go back to the original menu

        continue
    elif option == 'b':
        os.system('cls')
        print("PRINTING STUDENT RECORD")
        #printing student_record
        for i, j in student_record.items():
            print(f"STUDENT ID - {i}, INFORMATION - {j}")
            continue

    elif option == 'c':
        os.system('cls')

        print("SEARCH STUDENT RECORD")

        search_id = input("Input studnet ID for search ---> ").lower()

        for each in student_record.keys():
            if search_id in student_record.keys():
                print("****************************")
                print(f"RECORD FOUND for ID{search_id}")
                #To print the record for the search ID
                for i in student_record[search_id]:
                    print(f"*** {i}")
                print("********************")
            else:
                print("NO RECORD FOUND")
            break
        continue

    elif option == 'd':
        