# import libraries and other files

import load as loader
import schedule_class as schedule
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
schedule = schedule.Schedule(rooms)

print '\n'
print ' DONE LOADING!'


#
#
#   Test schedule class
#       Will be removed after writing functions
#

# Test fill one spot
print schedule.add(['wednesday', 'C0.110', '11h'], courses[1], 'lecture')
# Find the next empty slot
print schedule.find_empty()

print '------------------\n\n'

#
# Fill in all courses

for course in courses:
    for i in course.q_lecture:
        path = schedule.find_empty()
        schedule.add([path[0], path[1], path[2]], course, 'lecture')

    for i in course.q_seminar:
        path = schedule.find_empty()
        schedule.add([path[0], path[1], path[2]], course, 'seminar')

    for i in course.q_practicum:
        path = schedule.find_empty()
        schedule.add([path[0], path[1], path[2]], course, 'pracitcum')

print schedule.week



# Room object by name
# print rooms['A1.10']

# Room name
# print rooms['A1.10'].name

# print capacity
# print rooms['A1.10'].capacity

# Print student name
# print students['82066165'].first_name, students['82066165'].last_name

# Get student Subjects
# print students['82066165'].subjects


#
# End test code