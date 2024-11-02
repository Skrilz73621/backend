class Person:
    def __init__(self, name, age, is_married):
        self.name = name
        self.age = age
        self.is_married = is_married

    def introduce_myself(self):
        if self.is_married == True:
            print(f'Привет! Меня звоут: {self.name}, мне: {self.age}, и я женат/замужем\n')
        else:
            print(f'Привет! Меня звоут: {self.name}, мне: {self.age}, и я не женат/замужем\n')

class Student(Person):
    def __init__(self, name, age, is_married, marks):
        super().__init__(name, age, is_married)
        self.marks = marks

    def average(self):
        average = round(sum(self.marks.values()) / len(self.marks),2)
        return average

class Teacher(Person):
    base_salary = 30000
    def __init__(self, name, age, is_married, experience):
        super().__init__(name, age, is_married)
        self.experience = experience

    def get_salary(self):
        if self.experience > 3:
            print(f'Зарплата {self.name} составляет {Teacher.base_salary + Teacher.base_salary / 100 * self.experience}')
        else:
            print(f'Зарплата {self.name} составляет {Teacher.base_salary}')

teacher1 = Teacher('Джон', 30, False, 10)
teacher1.get_salary()
teacher1.introduce_myself()

def create_students():
    std1 = Student('Murzik', 14, False, {'Математика' : 100, 'Англ.яз' : 60, 'Физика' : 85})
    std2 = Student('Mybutt', 19, False, {'Математика' : 0, 'Англ.яз' : 20, 'Физика' : 8})
    std3 = Student('Adilet', 10, False, {'Математика' : 50, 'Англ.яз' : 50, 'Физика' : 50})
    students = [std1, std2, std3]
    return students

students = create_students()
for student in students:
    student.introduce_myself()
    for subject, marks in student.marks.items():
        print(f'Предмет:{subject} - {marks} баллов')
    print(f'Средняя оценка ученика {student.average()}\n')