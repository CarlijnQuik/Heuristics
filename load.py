# load information and initialize roster

# all input from CSV file

# key pair zalen
# vakken per key value met meerdere waardes.
# key value where key is studentnumber and value is rest

import elements as obj
import roomslot
import csv
import activity
import ptp
import math

TYPE_LECTURE = 'lecture'
TYPE_SEMINAR = 'seminar'
TYPE_PRACTICUM = 'practicum'

def load_students(student_file):

    student_file = validate_input_file(student_file)
    student_as_object = {}

    try:
        with open(student_file, 'r') as csvfile:
            print 'Reading student file..'
            students = csv.reader(csvfile)

            # Check if first row is actually a header and not values
            students.next()

            for student in students:
                print '\tProcessing student #' + student[2]
                new_object = obj.Student(student[2], student[0], student[1], student[3], student[4], student[5], student[6], student[7])
                student_as_object[student[2]] = new_object

        print 'Number of students processed:', len(student_as_object), '\n'
        return student_as_object
    except IOError:
        print 'Could not find or open the student file!'
        print 'Make sure your files are located in the input_files folder.'

def load_courses(course_file, student_list):

    course_file = validate_input_file(course_file)
    course_as_object = []

    try:
        with open(course_file, 'r') as csvfile:
            print 'Reading subject file..'

            courses = csv.reader(csvfile)
            courses.next()

            for course in courses:
                new_object = obj.Course(course[0], course[1], course[2], course[3], course[4], course[5])
                new_object.set_students(student_list)
                course_as_object.append(new_object)
                print '\tProcessing course:', course[0], "(" + str(len(new_object.student_list)) + ")"

            print 'Number of course processed:', len(course_as_object), '\n'
            return course_as_object
    except IOError:
        print 'Could not find or open the student file!'
        print 'Make sure your files are located in the input_files folder.'

def load_rooms(room_file):

    room_file = validate_input_file(room_file)
    room_as_object = {}

    try:
        with open(room_file, 'r') as csvfile:
            print 'Reading room file..'

            rooms = csv.reader(csvfile)
            rooms.next()

            for room in rooms:
                print '\tProcessing room:', room[0], "cap:", room[1]
                new_object = obj.Room(room[0], room[1])
                room_as_object[room[0]] = new_object

            print 'Number of rooms processed:', len(room_as_object), '\n'
            return room_as_object
    except IOError:
        print 'Could not find or open the student file!'
        print 'Make sure your files are located in the input_files folder.'

def create_schedule(room_list):
    room_slots = []

    days = ('monday', 'tuesday', 'wednesday', 'thursday', 'friday')
    times = ('0900', '1100', '1300', '1500')

    for room in room_list:
        room_object = room_list[room]
        for day in days:
            if room == 'C0.110':
                room_slots.append(roomslot.Roomslot(room_object, day, '1700'))

            for time in times:
                room_slots.append(roomslot.Roomslot(room_object, day, time.zfill(4)))

    return room_slots

def fill_schedule(schedule, courses):

    for course in courses:

        for i in range(int(course.q_lecture)):
            empty_slot = ptp.find_empty(schedule)
            schedule[empty_slot].activity = activity.Activity(course, TYPE_LECTURE)

        for i in range(int(course.q_seminar)):
            split = math.ceil(len(course.student_list) / float(course.seminar_max_students))


            for j in range(int(split)):
                empty_slot = ptp.find_empty(schedule)
                schedule[empty_slot].activity = activity.Activity(course, TYPE_SEMINAR)

        for i in range(int(course.q_practicum)):
            split = math.ceil(len(course.student_list) / float(course.practicum_max_students))

            for j in range(int(split)):
                empty_slot = ptp.find_empty(schedule)
                schedule[empty_slot].activity = activity.Activity(course, TYPE_PRACTICUM)

    return schedule


def validate_input_file(file_location):
    if file_location[-4:] != '.csv':
        file_location = file_location + '.csv'
    if file_location[:12] != 'input_files/':
        file_location = "input_files/" + file_location

    return file_location

