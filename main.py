class Student:
  
    def __init__(self, name, surname, gender):
      self.name = name
      self.surname = surname
      self.gender = gender
      self.finished_courses = []
      self.courses_in_progress = []
      self.grades = {}
      
    def average_grade(self):
      total_grades = []
      for grades_list in self.grades.values():
          total_grades.extend(grades_list)

      if total_grades:
          return sum(total_grades) / len(total_grades)
      else:
          return 0

    def rate_lecturer(self, lecturer, course, grade):
      if course in self.courses_in_progress and isinstance(lecturer, Lecturer):
          if course in lecturer.grades:
              lecturer.grades[course].append(grade)
          else:
              lecturer.grades[course] = [grade]
      else:
          return 'Ошибка'
      
    def __lt__(self, other):
        return self.average_grade() < other.average_grade()

    def __le__(self, other):
        return self.average_grade() <= other.average_grade()

    def __eq__(self, other):
        return self.average_grade() == other.average_grade()

    def __ne__(self, other):
        return self.average_grade() != other.average_grade()

    def __gt__(self, other):
        return self.average_grade() > other.average_grade()

    def __ge__(self, other):
        return self.average_grade() >= other.average_grade()
      
    def __str__(self):
      average_grade = sum(sum(grades) for grades in self.grades.values()) / len(self.grades.values()) if self.grades else 0
      in_progress_courses = ', '.join(self.courses_in_progress)
      finished_courses = ', '.join(self.finished_courses)
      return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.average_grade()}\nКурсы в процессе изучения: {in_progress_courses}\nЗавершенные курсы: {finished_courses}"

class Mentor:

    def __init__(self, name, surname):
      self.name = name
      self.surname = surname
      self.courses_attached = []

    def __str__(self):
      return f"Имя: {self.name}\nФамилия: {self.surname}"

class Reviewer(Mentor):

    def rate_student_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
      return super().__str__()
  
class Lecturer(Mentor):
  
    def __init__(self, name, surname):
      super().__init__(name, surname)
      self.grades = {}
    def average_grade(self):
      total_grades = []
      for grades_list in self.grades.values():
          total_grades.extend(grades_list)

      if total_grades:
          return sum(total_grades) / len(total_grades)
      else:
          return 0
    
    def __lt__(self, other):
        return self.average_grade() < other.average_grade()

    def __le__(self, other):
        return self.average_grade() <= other.average_grade()

    def __eq__(self, other):
        return self.average_grade() == other.average_grade()

    def __ne__(self, other):
        return self.average_grade() != other.average_grade()

    def __gt__(self, other):
        return self.average_grade() > other.average_grade()

    def __ge__(self, other):
        return self.average_grade() >= other.average_grade()
    
    def __str__(self):
      average_grade = sum(sum(grades) for grades in self.grades.values()) / len(self.grades.values()) if self.grades else 0
      return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average_grade()}"
    
# Создание экземпляров классов
some_reviewer_1 = Reviewer('Михаил', 'Светлов')
some_reviewer_2 = Reviewer('Олег', 'Петров')

some_lecturer_1 = Lecturer('Иван', 'Белов')
some_lecturer_2 = Lecturer('Марго', 'Васильева')
some_lecturer_1.grades = {'Python': [9, 8, 10]} 
some_lecturer_2.grades = {'Git': [7, 8, 9]}  

some_student_1 = Student('Колян', 'Изенштейн', 'your_gender')
some_student_1.grades = {'Python': [7, 8, 9]}  
some_student_1.courses_in_progress = ['Python', 'Git']
some_student_1.finished_courses = ['Введение в программирование']

some_student_2 = Student('Ксюша', 'Раппопорт', 'your_gender')
some_student_2.grades = {'Git': [10, 9, 8]}  
some_student_2.courses_in_progress = ['Git', 'JavaScript']
some_student_2.finished_courses = ['Алгоритмы и структуры данных']

print('###### Ревизоры ######')
print(some_reviewer_1)
print(some_reviewer_2)
print()
print('###### Лекторы ######')
print(some_lecturer_1)
print(some_lecturer_2)
print()
print('###### Студенты ######')
print(some_student_1)
print(some_student_2)
    

