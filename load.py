# load information and initialize roster

# all input from CSV file

# key pair zalen
# vakken per key value met meerdere waardes.
# key value where key is studentnumber and value is rest

import classes as obj
import csv

def load_students(student_file):

    student_as_object = []

    try:
        with open(student_file, 'r') as csvfile:
            print 'Reading student file..'
            students = csv.reader(csvfile)

            # Check if first row is actually a header and not values
            students.next()

            for student in students:
                print 'Processing student #' + student[2]
                new_object = obj.Student(student[2], student[0], student[1], student[3], student[4], student[5], student[6], student[7])
                student_as_object.append(new_object)

        print 'Number of students processed: ' + str(len(student_as_object))
        return student_as_object
    except IOError:
        print 'Could not find or open the student file!'

def load_subjects():
    return

def load_rooms():
    return