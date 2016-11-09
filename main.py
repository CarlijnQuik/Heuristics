# import libraries and other files

import load as loada
import ptp, visual

student_file = raw_input('Student input file: ')
while not student_file:
    student_file = raw_input('Student input file(CSV Format): ')

students = loada.load_students(student_file)

subject_file = raw_input('Subject input file: ')
while not subject_file:
    subject_file = raw_input('Subject input file(CSV Format): ')

subjects = loada.load_subjects(subject_file)

room_file = raw_input('Room input file: ')
while not room_file:
    room_file = raw_input('Room input file(CSV Format): ')

rooms = loada.load_rooms(room_file)

loada.load_students_to_subjects(students, subjects)

print '\n'
print ' DONE LOADING!'

schedule = loada.load_schedule(subjects, rooms)


#
#
#   Test code
#       Will be removed after writing functions
#


# schedule on day x for room z
print schedule['wednesday']['C0.110']

print schedule['tuesday']['B0.201']['9h']

# seminar max students of that Subject
print schedule['thursday']['B0.201']['9h'].seminar_max_students

# Amount of people following this course/Subject
print len(schedule['tuesday']['B0.201']['9h'].student_list)

# Room object by name
print rooms['A1.10']

# Room name
print rooms['A1.10'].name
# OR
# print schedule['wednesday']['C0.110']['room_details'].name

# print capacity
print rooms['A1.10'].capacity
# OR
# print schedule['wednesday']['C0.110']['room_details'].capacity

# Print student name
print students['82066165'].first_name, students['82066165'].last_name

# Get student Subjects
print students['82066165'].subjects


#
# End test code