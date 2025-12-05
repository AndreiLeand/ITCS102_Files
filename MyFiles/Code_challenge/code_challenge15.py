import os
import json

print("Student information system")

#Empty Dictionary

student_record = {}

while True:
    print("SELECT  FROM THE FOLLOWING OPTION")s
    print("A - Add Student Record")
    print("B - Print All Student Record")
    print("C - Search Student Record")
    print("D - Delete Student Record")
    print("E - Edit Student Record")
    print("F - Export Student Record")
    print("X - Exit System")

    options = input("SELECT FROM THE OPTIONS ABOVE ---> ").lower()

    if options == 'a':
        os.system('cls')

        print("\nADDING STUDENT RECORD")

        id_no = input("Please Input Student ID Number ---> ")

        first_name = input("Please input student first name ---> ").upper()
        middle_name = input("Please input student middle name ---> ").upper()
        last_name = input("Please input student last name ---> ").upper()
        age = eval(input("Please input student age ---> "))
        course = input("Please input student course ---> ").upper()
        section = input("Please input student year/section ---> ").upper()

        #This is for storing data into dictionary - student_record

        student_record[id_no] = [first_name,middle_name, last_name, age, course, section]
        print("DATA SAVED SUCCESSFULLY")

        #This will go back to the original menu

        continue
    elif options == 'b':
        os.system('cls')
        print("PRINTING STUDENT RECORD")
        #printing student_record
        for i, j in student_record.items():
            print(f"STUDENT ID - {i}, INFORMATION - {j}")
            continue

    elif options == 'c':
        os.system('cls')

        print("SEARCH STUDENT RECORD")

        search_id = input("Input student ID for search ---> ").lower()

        for each in student_record.keys():
            if search_id in student_record.keys():
                print("****************************")
                print(f"RECORD FOUND for ID: {search_id}")
                #To print the record for the search ID
                for i in student_record[search_id]:
                    print(f"*** {i}")
                print("****************************")
            else:
                print("NO RECORD FOUND")
            break
        continue

    elif options == 'd':
        os.system('cls')

        print("SEARCH STUDENT RECORD")

        search_id = input("Input student ID for search ---> ")

        for each in student_record.keys():
            if search_id in student_record.keys():
                print("******************")
                print(f"RECORD FOUND for ID {search_id}")
                #THIS IS FOR TO PRINT THE RECORD FOR THE SEARCH ID
                for i in student_record[search_id]:
                    print(f" **  {i}")
                print("*******************")
                student_record.pop(search_id)
                print("RECORD DELETED")
            else:
                print("NO RECORD FOUND")
            break
        continue

    elif options == 'e':
        os.system('cls')

        search_id = input("Input student ID for search ---> ").lower()

        for each in student_record.keys():
            if search_id in student_record.keys():
                print("*********************")
                print(f"RECORD FOUND FOR ID {search_id}")
                for i in student_record[search_id]:
                    print(f" ** {i}")
                print("***********************")
                break    

        #THIS IS FOR THE NEW SET OF VALUE FOR THE SEARCHED ID

        first_name = input('Please input student first name ---> ').upper()
        middle_name = input('Please input student middle name ---> ').upper()
        last_name = input('Please input student last name ---> ').upper()
        age = eval(input('Please input student age ---> '))
        course = input('Please input student course ---> ').upper()
        section = input('Please input student section ---> ').upper()

        student_record[search_id][0] = first_name
        student_record[search_id][1] = middle_name
        student_record[search_id][2] = last_name
        student_record[search_id][3] = age
        student_record[search_id][4] = course
        student_record[search_id][5] = section

        print("DATA UPDATED")
        continue
    
    elif options == 'f':
        os.system("cls")
        print("EXPORT STUDENT DATA")
        #Java Script Object Nation
        with open('student_record.json','w') as new_file:
            json.dump(student_record,new_file,indent=4)
        print('DATA EXPORTED TO JSON')
        continue
    elif options == 'x':
        print('SYSTEM EXIT!')
        break
    else:
        print("INVALID CHOICE, SORRY TRY AGAIN")

