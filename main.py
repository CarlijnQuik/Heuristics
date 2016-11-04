# import libraries and other files

# add function clls in here or in the correct file. So load_students is called/handled fully in load.py
import load as loada
import ptp, visual

student_file = raw_input('Student input file: ')
while not student_file:
    student_file = raw_input('Student input file(CSV Format): ')

loada.load_students(student_file)