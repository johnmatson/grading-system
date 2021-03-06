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

    def add_student(self):
        student = Student()
        print('Student Number: ', end='')
        student.student_number = self.id_error_check()
        print('Lab Grade: ', end='')
        student.lab_grade = self.grade_error_check()
        print('Quiz Grade: ', end='')
        student.quiz_grade = self.grade_error_check()
        print('Midterm Grade: ', end='')
        student.midterm_grade = self.grade_error_check()
        print('Final Exam Grade: ', end='')
        student.final_exam_grade = self.grade_error_check()
        student.final_grade = (0.4 * student.lab_grade + 0.1 * student.quiz_grade + 0.2 * student.midterm_grade + 0.3 * student.final_exam_grade)
        self.student_list.append(student)

    def edit_student(self):
        student = Student()
        student_num = input('Which student would you like to edit: ')
        print('Student Number: ', end='')
        student.student_number = self.id_error_check()
        print('Lab Grade: ', end='')
        student.lab_grade = self.grade_error_check()
        print('Quiz Grade: ', end='')
        student.quiz_grade = self.grade_error_check()
        print('Midterm Grade: ', end='')
        student.midterm_grade = self.grade_error_check()
        print('Final Exam Grade: ', end='')
        student.final_exam_grade = self.grade_error_check()
        student.final_grade = (0.4 * student.lab_grade + 0.1 * student.quiz_grade + 0.2 * student.midterm_grade + 0.3 * student.final_exam_grade)
        del self.student_list[int(student_num) - 1]
        self.student_list.insert((int(student_num) - 1), student)

    def delete_student(self):
        student_num = input('Which student would you like to delete: ')
        del self.student_list[int(student_num) - 1]

    def print_grades(self):
        print('{:10s} {:>9s} {:>9s} {:>9s} {:>9s} {:>9s}'.format('ID:', 'Lab:', 'Quiz:', 'Midterm:', 'Final:', 'GPA:'))
        for i in range(len(self.student_list)):
            print('{:10s} {:9.2f} {:9.2f} {:9.2f} {:9.2f} {:9.2f}'.format(self.student_list[i].student_number, self.student_list[i].lab_grade, self.student_list[i].quiz_grade, self.student_list[i].midterm_grade, self.student_list[i].final_exam_grade, self.student_list[i].final_grade))
            # print(self.student_list[i].lab_grade, end='    ')
            # print(self.student_list[i].quiz_grade, end='    ')
            # print(self.student_list[i].midterm_grade, end='    ')
            # print(self.student_list[i].final_exam_grade, end='    ')
            # print(self.student_list[i].final_grade)

    def load_class(self):
        student = Student()
        self.student_list.clear()
        file_name = input("File name: ")
        load_file = open(file_name, "r+")
        for line in load_file:
            data = line.split(',')
            student.student_number = data[0]
            student.lab_grade = float(data[1])
            student.quiz_grade = float(data[2])
            student.midterm_grade = float(data[3])
            student.final_exam_grade = float(data[4])
            student.final_grade = float(data[5])
            self.student_list.append(student)
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
