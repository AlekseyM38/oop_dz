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
    def __str__(self):
      average_grade = sum(sum(grades) for grades in self.grades.values()) / len(self.grades.values()) if self.grades else 0
      return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average_grade()}"
    

    

