# import libraries and other files

# add function clls in here or in the correct file. So load_students is called/handled fully in load.py
import load as loada
import ptp, visual

student_file = raw_input('Student input file: ')
while not student_file:
    student_file = raw_input('Student input file(CSV Format): ')

loada.load_students(student_file)

subject_file = raw_input('Subject input file: ')
while not subject_file:
    subject_file = raw_input('Subject input file(CSV Format): ')

loada.load_subjects(subject_file)

room_file = raw_input('Room input file: ')
while not room_file:
    room_file = raw_input('Room input file(CSV Format): ')

loada.load_rooms(room_file)