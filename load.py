# load information and initialize roster

# all input from CSV file

# key pair zalen
# vakken per key value met meerdere waardes.
# key value where key is studentnumber and value is rest

import classes as obj
import csv

def load_students(student_file):
    with open(student_file, 'r') as csvfile:
        students = csv.reader(csvfile)

        for student in students:
            # store info per row


    return

def load_subjects():
    return

def load_rooms():
    return