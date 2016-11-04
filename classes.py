"""

Object representing a single student

"""
class Student(object):
    # How to:
    # store the class (array? or self.class1 = x, self.class2 = null etc

    def __init__(self, id, last_name, first_name, subject1 = None, subject2 = None, subject3 = None, subject4 = None, subject5 = None):
        self.id = id
        self.last_name = last_name
        self.first_name = first_name
        self.subjects = [subject1, subject2, subject3, subject4, subject5]

    def get_id(self):
        return self.id

    def get_last_name(self):
        return self.last_name

    def get_first_name(self):
        return self.first_name

    def get_subjects(self):
        return self.subjects


"""

Object representing a room/place where e.g. lectures are given.

"""
class Room(object):
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity

    def get_name(self):
        return self.name

    def get_capacity(self):
        return self.capacity


"""

Object representing Subjects (E.G. Advanced Heuristics)
Each class has x amounts of lectures, seminars, students, practicums
Seminars and practicums can have a max size too

"""
class Subject(object):
    # English for: Werkcollege?
    # q = quantity
    def __init__(self, name, q_lecture, q_seminar, seminar_max_students, q_practicum, practicum_max_students):
        self.name = name
        self.q_lecture = q_lecture
        self.q_seminar = q_seminar
        self.seminar_max_students = seminar_max_students
        self.q_practicum = q_practicum
        self.practicum_max_students = practicum_max_students

    def get_name(self):
        return self.name

    def get_q_lecture(self):
        return self.q_lecture

    def get_q_seminar(self):
        return self.q_seminar

    def get_seminar_max_students(self):
        return self.seminar_max_students

    def get_q_practicum(self):
        return self.q_practicum

    def get_practicum_max_students(self):
        return self.practicum_max_students