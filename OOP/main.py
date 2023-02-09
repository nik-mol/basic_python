from operator import le


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        
    def add_courses(self, course_name):
        self.finished_courses.append(course_name) 

    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def calculation_avg_grade(self):
        strl = []       
        for _, grades_list in self.grades.items():
            strl.extend(grades_list)
        if len(strl) != 0:
            avg_grade = sum(strl) / len (strl)
            return avg_grade
        return 0
          
 
    def __lt__(self, other):
        if (not isinstance(self, Student)) or (not isinstance(other, Student)):
            return
        if other.calculation_avg_grade() < self.calculation_avg_grade():
            print(f"Cредний балл выше у студента: {self.name}")
        else:
            print(f"Cредний балл выше у студента: {other.name}")
            
    def __str__(self) -> str:
        res = f"""
Имя: {self.name}
Фамилия: {self.surname}
Средняя оценка за домашние задания: {self.calculation_avg_grade()}
Курсы в процессе изучения: {', '.join(self.courses_in_progress)}
Завершенные курсы: {','.join(self.finished_courses)}
"""
        return res

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        
    
class Lecturer(Mentor):   
    def __init__(self, name, surname):
        super().__init__(name, surname)       
        self.grades = {}
    
    def calculation_avg_grade(self):
        strl = []       
        for _, grades_list in self.grades.items():
            strl.extend(grades_list)
        if len(strl) != 0:
            avg_grade = sum(strl) / len (strl)
            return avg_grade
        return 0

    def __lt__(self, other):
        if (not isinstance(self, Lecturer)) or (not isinstance(other, Lecturer)):
            return 'Ошибка'
        if other.calculation_avg_grade() < self.calculation_avg_grade():
            print(f"Cредний балл выше у лектора: {self.name}")
        else:
            print(f"Cредний балл выше у лектора: {other.name}")

    def __str__(self) -> str:
        return f"""
Имя: {self.name}
Фамилия: {self.surname}
Средняя оценка за лекции: {self.calculation_avg_grade()}
"""

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
    def __str__(self) -> str:
        return f"""
Имя: {self.name}
Фамилия: {self.surname}
"""

# STUDENTS:

first_student = Student('Ivan', 'Ivanov', 'mail')
first_student.add_courses('Введение в программирование')
first_student.courses_in_progress += ['Python', 'Git']

second_student = Student('Olesya', 'Ivanova', 'femail')
second_student.add_courses('Введение в программирование')
second_student.courses_in_progress += ['Python', 'Git']

# LECTURERS:

first_lecturer = Lecturer('Petr', 'Petrov')
first_lecturer.courses_attached += ['Python', 'Git']

second_lecturer = Lecturer('Inna', 'Petrova')
second_lecturer.courses_attached += ['Python', 'Git']

# REVIEWERS:

first_reviewer = Reviewer('Petr', 'Petrov')
first_reviewer.courses_attached += ['Python', 'Git']

second_reviewer = Reviewer('Inna', 'Petrova')
second_reviewer.courses_attached += ['Python', 'Git']

# STUDENTS rate_hw:

first_student.rate_hw(first_lecturer, 'Python', 3)
first_student.rate_hw(first_lecturer, 'Python', 4)
first_student.rate_hw(first_lecturer, 'Git', 5)
first_student.rate_hw(first_lecturer, 'Git', 6)
first_student.rate_hw(second_lecturer, 'Python', 7)
first_student.rate_hw(second_lecturer, 'Python', 10)
first_student.rate_hw(second_lecturer, 'Git', 9)
first_student.rate_hw(second_lecturer, 'Git', 5)

second_student.rate_hw(first_lecturer, 'Python', 6)
second_student.rate_hw(first_lecturer, 'Python', 5)
second_student.rate_hw(first_lecturer, 'Git', 9)
second_student.rate_hw(first_lecturer, 'Git', 6)
second_student.rate_hw(second_lecturer, 'Python', 9)
second_student.rate_hw(second_lecturer, 'Python', 7)
second_student.rate_hw(second_lecturer, 'Git', 9)
second_student.rate_hw(second_lecturer, 'Git', 5)

# REVIEWERS rate_hw:

first_reviewer.rate_hw(first_student, 'Python', 6)
first_reviewer.rate_hw(first_student, 'Python', 5)
first_reviewer.rate_hw(first_student, 'Git', 6)
first_reviewer.rate_hw(first_student, 'Git', 3)
first_reviewer.rate_hw(second_student, 'Python', 9)
first_reviewer.rate_hw(second_student, 'Python', 7)
first_reviewer.rate_hw(second_student, 'Git', 9)
first_reviewer.rate_hw(second_student, 'Git', 5)

second_reviewer.rate_hw(first_student, 'Python', 10)
second_reviewer.rate_hw(first_student, 'Python', 8)
second_reviewer.rate_hw(first_student, 'Git', 10)
second_reviewer.rate_hw(first_student, 'Git', 6)
second_reviewer.rate_hw(second_student, 'Python', 9)
second_reviewer.rate_hw(second_student, 'Python', 7)
second_reviewer.rate_hw(second_student, 'Git', 9)
second_reviewer.rate_hw(second_student, 'Git', 5)

print(first_student)
print("-" * 50)
print(second_student)
print("-" * 50)
print(first_lecturer)
print("-" * 50)
print(second_lecturer)
print("-" * 50)
print(first_reviewer)
print("-" * 50)
print(second_reviewer)
print("-" * 50)

is_lt = (first_student < second_student)
first_lecturer.__lt__(second_lecturer)

print("-" * 50)

students = [first_student,second_student]
lecturers = [first_lecturer,second_lecturer]

def avg_cource_students(students, cousre):
    sum_ = 0
    res = 0
    grade_list = []
    for student in students:
        for key, value in student.grades.items():
            if key == cousre:
                grade_list.extend(value)            
    sum_ += sum(grade_list)
    res = round(sum_ / len(grade_list), 2)
    print (f"Средняя оценка студентов по курсу {cousre}: {res}")
      
avg_cource_students(students, 'Python')
avg_cource_students(students, 'Git')

def avg_cource_lecturers(lecturers, cousre):
    sum_ = 0
    res = 0
    grade_list = []
    for lecturer in lecturers:
        for key, value in lecturer.grades.items():
            if key == cousre:
                grade_list.extend(value)            
    sum_ += sum(grade_list)
    res = round(sum_ / len(grade_list), 2)
    print (f"Средняя оценка лекторов по курсу {cousre}: {res}")
      
avg_cource_lecturers(lecturers, 'Python')
avg_cource_lecturers(lecturers, 'Git')

