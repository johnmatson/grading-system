import sys


class Student:
    student_number = None
    lab_grade = None
    quiz_grade = None
    midterm_grade = None
    final_exam_grade = None
    final_grade = None


class Course:
    student_list = []
    student = Student()

    def add_student(self):
        print('Student Number: ', end='')
        self.student.student_number = self.id_error_check()
        print('Lab Grade: ', end='')
        self.student.lab_grade = self.grade_error_check()
        print('Quiz Grade: ', end='')
        self.student.quiz_grade = self.grade_error_check()
        print('Midterm Grade: ', end='')
        self.student.midterm_grade = self.grade_error_check()
        print('Final Exam Grade: ', end='')
        self.student.final_exam_grade = self.grade_error_check()
        self.student.final_grade = (0.4 * self.student.lab_grade + 0.1 * self.student.quiz_grade + 0.2 * self.student.midterm_grade + 0.3 * self.student.final_exam_grade)
        self.student_list.append(self.student)

    def edit_student(self):
        student = input('Which student would you like to edit: ')
        print('Student Number: ', end='')
        self.student.student_number = self.id_error_check()
        print('Lab Grade: ', end='')
        self.student.lab_grade = self.grade_error_check()
        print('Quiz Grade: ', end='')
        self.student.quiz_grade = self.grade_error_check()
        print('Midterm Grade: ', end='')
        self.student.midterm_grade = self.grade_error_check()
        print('Final Exam Grade: ', end='')
        self.student.final_exam_grade = self.grade_error_check()
        self.student.final_grade = (0.4 * self.student.lab_grade + 0.1 * self.student.quiz_grade + 0.2 * self.student.midterm_grade + 0.3 * self.student.final_exam_grade)
        del self.student_list[int(student) - 1]
        self.student_list.insert((int(student) - 1), self.student)

    def delete_student(self):
        student = input('Which student would you like to delete: ')
        del self.student_list[int(student) - 1]

    def print_grades(self):
        for i in range(len(self.student_list)):
            print(self.student_list[i].student_number)
            print(self.student_list[i].lab_grade)
            print(self.student_list[i].quiz_grade)
            print(self.student_list[i].midterm_grade)
            print(self.student_list[i].final_exam_grade)
            print(self.student_list[i].final_grade)

    def load_class(self):
        self.student_list.clear()
        file_name = input("File name: ")
        load_file = open(file_name, "r+")
        for line in load_file:
            data = line.split(',')
            self.student.student_number = data[0]
            self.student.lab_grade = data[1]
            self.student.quiz_grade = data[2]
            self.student.midterm_grade = data[3]
            self.student.final_exam_grade = data[4]
            self.student.final_grade = data[5]
            self.student_list.append(self.student)
        load_file.close()

    def save_class(self):
        file_name = input("File name: ")
        save_file = open(file_name, "wb")
        for i in range(len(self.student_list)):
            save_file.write(bytes(self.student_list[i].student_number + ",", 'UTF-8'))
            save_file.write(bytes(str(self.student_list[i].lab_grade) + ",", 'UTF-8'))
            save_file.write(bytes(str(self.student_list[i].quiz_grade) + ",", 'UTF-8'))
            save_file.write(bytes(str(self.student_list[i].midterm_grade) + ",", 'UTF-8'))
            save_file.write(bytes(str(self.student_list[i].final_exam_grade) + ",", 'UTF-8'))
            save_file.write(bytes(str(self.student_list[i].final_grade) + "\n", 'UTF-8'))
        # save_file.write(bytes("]", 'UTF-8'))
        save_file.close()

    def id_error_check(self):
        while True:
            student_id = input()
            if len(student_id) != 9:
                print('Error, please try again: ', end='')
            elif (student_id[0] != 'a') and (student_id[0] != 'A'):
                print('Error, please try again: ', end='')
            elif student_id[1] != '0':
                print('Error, please try again: ', end='')
            elif (student_id[2] != '0') and (student_id[2] != '1'):
                print('Error, please try again: ', end='')
            elif not student_id[3].isdigit():
                print('Error, please try again: ', end='')
            elif not student_id[4].isdigit():
                print('Error, please try again: ', end='')
            elif not student_id[5].isdigit():
                print('Error, please try again: ', end='')
            elif not student_id[6].isdigit():
                print('Error, please try again: ', end='')
            elif not student_id[7].isdigit():
                print('Error, please try again: ', end='')
            elif not student_id[8].isdigit():
                print('Error, please try again: ', end='')
            else:
                return student_id

    def grade_error_check(self):
        while True:
            string_id = input()
            for i in range(len(string_id)):
                if (string_id[i] != '.') and not (string_id[i].isdigit()):
                    print('Error, please try again: ', end='')
                    break
                else:
                    float_id = float(string_id)
                    if(float_id < 0) or (float_id > 100):
                        print('Error, please try again: ', end='')
                        break
                    else:
                        return float_id


def print_menu():
    print("**************************************")
    print("ELEX 4618 Grade System, by John Matson")
    print("**************************************")
    print("(A)dd student")
    print("(E)dit student")
    print('(D)elete student')
    print("(P)rint grades")
    print('(L)oad class')
    print('(S)ave class')
    print("(Q)uit")
    print("CMD>", end="")


course = Course()
exit_loop = False
while True:
    print_menu()
    cmd_input = input()

    if(cmd_input == 'a'):
        course.add_student()
    elif(cmd_input == 'e'):
        course.edit_student()
    elif(cmd_input == 'd'):
        course.delete_student()
    elif(cmd_input == 'p'):
        course.print_grades()
    elif(cmd_input == 'l'):
        course.load_class()
    elif(cmd_input == 's'):
        course.save_class()
    elif(cmd_input == 'q'):
        exit_loop = True
    else:
        print('Invalid entry, please try again')

    if exit_loop:
        break
