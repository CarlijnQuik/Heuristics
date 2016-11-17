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


schedule = loader.load_schedule(rooms)

print '\n\tDONE LOADING!\n'

ptp.alg(students, courses, rooms, schedule)
#for room in rooms:
#    print rooms[room].name, "+", rooms[room].capacity



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