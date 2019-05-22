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
    Student = Student()

    def add_student(self):
        self.Student.student_number = input('Student Number: ')
        self.Student.lab_grade = float(input('Lab Grade: '))
        self.Student.quiz_grade = float(input('Quiz Grade: '))
        self.Student.midterm_grade = float(input('Midterm Grade: '))
        self.Student.final_exam_grade = float(input('Final Exam Grade: '))
        self.Student.final_grade = (0.4 * self.Student.lab_grade + 0.1 * self.Student.quiz_grade + 0.2 * self.Student.midterm_grade + 0.3 * self.Student.final_exam_grade)
        self.student_list.append(self.Student)

    def edit_student(self):
        student = input('Which student would you like to edit: ')
        self.Student.student_number = input('Student Number: ')
        self.Student.lab_grade = float(input('Lab Grade: '))
        self.Student.quiz_grade = float(input('Quiz Grade: '))
        self.Student.midterm_grade = float(input('Midterm Grade: '))
        self.Student.final_exam_grade = float(input('Final Exam Grade: '))
        self.Student.final_grade = (0.4 * self.Student.lab_grade + 0.1 * self.Student.quiz_grade + 0.2 * self.Student.midterm_grade + 0.3 * self.Student.final_exam_grade)
        del self.student_list[int(student) - 1]
        self.student_list.insert((int(student) - 1), self.Student)

    def delete_student(self):
        student = input('Which student would you like to delete: ')
        self.student_list.remove(int(student) - 1)

    def print_grades(self):
        # print(self.student_list[0].student_number)
        for i in range(len(self.student_list)):
            print(self.student_list[i].student_number)
            print(self.student_list[i].lab_grade)
            print(self.student_list[i].quiz_grade)
            print(self.student_list[i].midterm_grade)
            print(self.student_list[i].final_exam_grade)
            print(self.student_list[i].final_grade)

    def load_class(self):
        pass

    def save_class(self):
        pass


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


Course = Course()
exit_loop = False
while True:
    print_menu()
    cmd_input = input()

    if(cmd_input == 'a'):
        Course.add_student()
    elif(cmd_input == 'e'):
        Course.edit_student()
    elif(cmd_input == 'd'):
        Course.delete_student()
    elif(cmd_input == 'p'):
        Course.print_grades()
    elif(cmd_input == 'l'):
        Course.load_class()
    elif(cmd_input == 's'):
        Course.save_student()
    elif(cmd_input == 'q'):
        exit_loop = True
    else:
        print('Invalid entry, please try again')

    if exit_loop:
        break
