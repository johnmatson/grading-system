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
        print("Student Number:", end="")
        Student.student_number = sys.stdin.readline()
        print("Lab Grade:", end="")
        Student.lab_grade = sys.stdin.readline()
        print("Quiz Grade:", end="")
        Student.quiz_grade = sys.stdin.readline()
        print("Midterm Grade:", end="")
        Student.midterm_grade = sys.stdin.readline()
        print("Final Exam Grade:", end="")
        Student.final_exam_grade = sys.stdin.readline()



def print_menu():
    print("**************************************")
    print("ELEX 4618 Grade System, by John Matson")
    print("**************************************")
    print("(A)dd student")
    print("(E)dit student")
    print("(P)rint grades")
    print("(Q)uit")
    print("CMD>", end="")



print_menu()
