# import libraries and other files

import load as loader
import ptp, visual

debug = True
if debug or raw_input('Enter def for default input or enter to continue manually: ') == 'def':
    students = loader.load_students('studenten_roostering.csv')
    courses = loader.load_courses('vakken.csv', students)
    rooms = loader.load_rooms('zalen.csv')
else:
    student_file = raw_input('Student input file: ')
    while not student_file:
        student_file = raw_input('Student input file(CSV Format): ')

    students = loader.load_students(student_file)

    course_file = raw_input('Course input file: ')
    while not course_file:
        course_file = raw_input('Course input file(CSV Format): ')

    courses = loader.load_courses(course_file, students)

    room_file = raw_input('Room input file: ')
    while not room_file:
        room_file = raw_input('Room input file(CSV Format): ')

    rooms = loader.load_rooms(room_file)

# Create an empty schedule
schedule = loader.load_schedule(courses, rooms)

print '\n'
print ' DONE LOADING!'


#
#
#   Test code load_schedule
#       Will be removed after writing functions
#


# schedule on day x for room z
print schedule['wednesday']['C0.110']

print schedule['tuesday']['B0.201']['9h']

# seminar max students of that Subject
# print schedule['thursday']['B0.201']['9h']['Algoritmen en complexiteit'].seminar_max_students

# Amount of people following this course/Subject
# print len(schedule['tuesday']['B0.201']['9h']['Algoritmen en complexiteit'].student_list)

# Room object by name
print rooms['A1.10']

# Room name
print rooms['A1.10'].name

# print capacity
print rooms['A1.10'].capacity

# Print student name
print students['82066165'].first_name, students['82066165'].last_name

# Get student Subjects
print students['82066165'].subjects


#
# End test code




#
#
#   Test code ptp.py
#       Will be removed after writing functions
#

print 'PTP Test code: \n'

print ptp.ptp(students, courses, rooms, schedule)



#
# End test code