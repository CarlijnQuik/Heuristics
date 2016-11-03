# import libraries and other files
import load as loada
import ptp, visual

student_file = raw_input('Student input file(CSV Format) location: ')
while not student_file:
    student_file = raw_input('Student input file(CSV Format) location: ')

loada.load_students(student_file)