import elements as obj
import roomslot
import csv
import activity
import ptp
import math
import string

TYPE_LECTURE = 'lecture'
TYPE_SEMINAR = 'seminar'
TYPE_PRACTICUM = 'practicum'

GROUP_STRING = string.ascii_uppercase


"""

    Put all students in their own student object.

"""
def load_students(student_file):

    student_file = validate_input_file(student_file)
    student_as_object = []

    try:
        with open(student_file, 'r') as csvfile:
            print 'Reading student file..'
            students = csv.reader(csvfile)

            # Check if first row is actually a header and not values.
            students.next()

            for student in students:
                print '\tProcessing student #' + student[2]
                new_object = obj.Student(student[2], student[0], student[1], student[3], student[4], student[5], student[6], student[7])
                student_as_object.append(new_object)

        print 'Number of students processed:', len(student_as_object), '\n'
        return student_as_object
    except IOError:
        print 'Could not find or open the student file!'
        print 'Make sure your files are located in the input_files folder.'


"""

    Put all courses in their own course object.

"""
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


"""

    Put all rooms in their own room object.

"""
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


"""

    Create an empty schedule based on preset/hardcoded days and times.

"""
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


"""

    Fill the emty schedule in one of the most basic ways.

"""
def fill_schedule(schedule, courses):
    overflow_percentage = 10

    for course in courses:

        for i in range(int(course.q_lecture)):
            empty_slot = ptp.find_empty(schedule)
            schedule[empty_slot].activity = activity.Activity(course, TYPE_LECTURE)
            schedule[empty_slot].activity.students = course.student_list

        for i in range(int(course.q_seminar)):
            student_overflow = math.ceil( (course.seminar_max_students * (float(overflow_percentage) / 100)) + course.seminar_max_students)

            split = math.ceil(len(course.student_list) / student_overflow)

            for j in range(int(split)):
                empty_slot = ptp.find_empty(schedule)
                schedule[empty_slot].activity = activity.Activity(course, TYPE_SEMINAR)

                last_class_count = len(course.student_list) % student_overflow

                # If enough room in last class, divide even.
                if (int(course.q_seminar) > 0 and int(course.q_practicum) <= 0):
                    if (last_class_count < (student_overflow - split) and last_class_count != 0):
                        group_size = math.ceil(len(course.student_list) / split)

                        # Try and divide the students evenly.
                        start_bound = int(group_size * j)
                        end_bound = int(group_size * (j + 1))

                        schedule[empty_slot].activity.students = course.student_list[start_bound:end_bound]
                        schedule[empty_slot].activity.group = GROUP_STRING[j]
                        course.groups.append(GROUP_STRING[j])

                    else:
                        start_bound = int(student_overflow * j)
                        end_bound = int(student_overflow * (j + 1))
                        schedule[empty_slot].activity.students = course.student_list[start_bound:end_bound]
                        schedule[empty_slot].activity.group = GROUP_STRING[j]
                        course.groups.append(GROUP_STRING[j])

        for i in range(int(course.q_practicum)):
            student_overflow = math.ceil( (course.practicum_max_students * (float(overflow_percentage) / 100)) + course.practicum_max_students)
            split = math.ceil(len(course.student_list) / student_overflow)

            for j in range(int(split)):
                empty_slot = ptp.find_empty(schedule)
                schedule[empty_slot].activity = activity.Activity(course, TYPE_PRACTICUM)

                last_class_count = len(course.student_list) % student_overflow

                # If enough room in last class, divide even.
                if (last_class_count < (student_overflow - split) and last_class_count != 0):
                    group_size = math.ceil(len(course.student_list) / split)

                    # Try and divide the students evenly.
                    start_bound = int(group_size * j)
                    end_bound = int(group_size * (j + 1))
                    schedule[empty_slot].activity.students = course.student_list[start_bound:end_bound]
                    schedule[empty_slot].activity.group = GROUP_STRING[j]
                    course.groups.append(GROUP_STRING[j])

                else:
                    start_bound = int(student_overflow * j)
                    end_bound = int(student_overflow * (j + 1))
                    schedule[empty_slot].activity.students = course.student_list[start_bound:end_bound]
                    schedule[empty_slot].activity.group = GROUP_STRING[j]
                    course.groups.append(GROUP_STRING[j])

    return schedule


"""

    Fill the emty schedule in a random way.

"""
def fill_schedule_random(schedule, courses):
    overflow_percentage = 10

    for course in courses:

        for i in range(int(course.q_lecture)):
            empty_slot = ptp.find_empty_random(schedule)
            schedule[empty_slot].activity = activity.Activity(course, TYPE_LECTURE)
            schedule[empty_slot].activity.students = course.student_list

        for i in range(int(course.q_seminar)):
            if overflow_percentage > 0:
                student_overflow = math.ceil( (course.seminar_max_students * (float(overflow_percentage) / 100)) + course.seminar_max_students)
            else:
                student_overflow = course.seminar_max_students

            split = math.ceil(len(course.student_list) / student_overflow)

            for j in range(int(split)):
                empty_slot = ptp.find_empty_random(schedule)
                schedule[empty_slot].activity = activity.Activity(course, TYPE_SEMINAR)

                last_class_count = len(course.student_list) % student_overflow

                # If enough room in last class, divide even.
                if (int(course.q_seminar) > 0 and int(course.q_practicum) <= 0):
                    if (last_class_count < (student_overflow - split) and last_class_count != 0):
                        group_size = math.ceil(len(course.student_list) / split)

                        # Try and divide the students evenly.
                        start_bound = int(group_size * j)
                        end_bound = int(group_size * (j + 1))
                        schedule[empty_slot].activity.students = course.student_list[start_bound:end_bound]
                        schedule[empty_slot].activity.group = GROUP_STRING[j]
                        course.groups.append(GROUP_STRING[j])

                    else:
                        start_bound = int(student_overflow * j)
                        end_bound = int(student_overflow * (j + 1))
                        schedule[empty_slot].activity.students = course.student_list[start_bound:end_bound]
                        schedule[empty_slot].activity.group = GROUP_STRING[j]
                        course.groups.append(GROUP_STRING[j])

        for i in range(int(course.q_practicum)):
            if student_overflow > 0:
                student_overflow = math.ceil( (course.practicum_max_students * (float(overflow_percentage) / 100)) + course.practicum_max_students)
            else:
                student_overflow = course.practicum_max_students

            split = math.ceil(len(course.student_list) / student_overflow)

            for j in range(int(split)):
                empty_slot = ptp.find_empty_random(schedule)
                schedule[empty_slot].activity = activity.Activity(course, TYPE_PRACTICUM)

                last_class_count = len(course.student_list) % student_overflow

                # If enough room in last class, divide even.
                if (last_class_count < (student_overflow - split) and last_class_count != 0):
                    group_size = math.ceil(len(course.student_list) / split)

                    # Try and divide the students evenly.
                    start_bound = int(group_size * j)
                    end_bound = int(group_size * (j + 1))
                    schedule[empty_slot].activity.students = course.student_list[start_bound:end_bound]
                    schedule[empty_slot].activity.group = GROUP_STRING[j]
                    course.groups.append(GROUP_STRING[j])


                else:
                    start_bound = int(student_overflow * j)
                    end_bound = int(student_overflow * (j + 1))
                    schedule[empty_slot].activity.students = course.student_list[start_bound:end_bound]
                    schedule[empty_slot].activity.group = GROUP_STRING[j]
                    course.groups.append(GROUP_STRING[j])

    return schedule


"""

    Format the user input.

"""
def validate_input_file(file_location):
    if file_location[-4:] != '.csv':
        file_location = file_location + '.csv'
    if file_location[:12] != 'input_files/':
        file_location = "input_files/" + file_location

    return file_location

