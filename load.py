# load information and initialize roster

# all input from CSV file

# key pair zalen
# vakken per key value met meerdere waardes.
# key value where key is studentnumber and value is rest

import csv

def load_students(student_file):
    with open(student_file, 'r') as csvfile:
        try:
            student = csv.reader(csvfile)
        except IOError:
            print "Can not find the file specified!"
        except:
            print "Unexpected error!"

        for row in student:
            # store info per row
    return

def load_classes():
    return

def load_rooms():
    return