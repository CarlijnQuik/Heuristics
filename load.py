# load information and initialize roster

# all input from CSV file

# key pair zalen
# vakken per key value met meerdere waardes.
# key value where key is studentnumber and value is rest

import classes as obj
import csv

def load_students(student_file):

    student_file = validate_input_file(student_file)
    student_as_object = {}

    try:
        with open(student_file, 'r') as csvfile:
            print 'Reading student file..'
            students = csv.reader(csvfile)

            # Check if first row is actually a header and not values
            students.next()

            for student in students:
                print 'Processing student #' + student[2]
                new_object = obj.Student(student[2], student[0], student[1], student[3], student[4], student[5], student[6], student[7])
                student_as_object[student[2]] = new_object

        print 'Number of students processed:', len(student_as_object), '\n'
        return student_as_object
    except IOError:
        print 'Could not find or open the student file!'
        print 'Make sure your files are located in the input_files folder.'
    except:
        print 'Unexpected Error!'
        raise

def load_subjects(subject_file):

    subject_file = validate_input_file(subject_file)
    subject_as_object = []

    try:
        with open(subject_file, 'r') as csvfile:
            print 'Reading subject file..'

            subjects = csv.reader(csvfile)
            subjects.next()

            for subject in subjects:
                print 'Processing subject: ' + subject[0]
                new_object = obj.Subject(subject[0], subject[1], subject[2], subject[3], subject[4], subject[5])
                subject_as_object.append(new_object)

            print 'Number of subjects processed:', len(subject_as_object), '\n'
            return subject_as_object
    except IOError:
        print 'Could not find or open the student file!'
        print 'Make sure your files are located in the input_files folder.'
    except:
        print 'Unexpected Error!'
        raise

def load_rooms(room_file):

    room_file = validate_input_file(room_file)
    room_as_object = {}

    try:
        with open(room_file, 'r') as csvfile:
            print 'Reading room file..'

            rooms = csv.reader(csvfile)
            rooms.next()

            for room in rooms:
                print 'Processing room: ' + room[0]
                new_object = obj.Room(room[0], room[1])
                room_as_object[room[0]] = new_object

            print 'Number of rooms processed:', len(room_as_object), '\n'
            return room_as_object
    except IOError:
        print 'Could not find or open the student file!'
        print 'Make sure your files are located in the input_files folder.'
    except:
        print 'Unexpected Error!'
        raise


def validate_input_file(file_location):
    if file_location[-4:] != '.csv':
        file_location = file_location + '.csv'
    if file_location[:12] != 'input_files/':
        file_location = "input_files/" + file_location

    return file_location

# load students to array in subject object
def load_students_to_subjects(student_list, subject_list):
    # for every subject, we want to create a link to every student with that subject
    try:
        for subject in subject_list:
            for student in student_list:
                student = student_list[student]
                for i in student.subjects:
                    if i.lower() == subject.name.lower():
                        subject.student_list.append(student)
            print len(subject.student_list), 'students for', subject.name
    except:
       print 'Could not load students to subjects!'

def load_schedule(subjects, rooms):
    week = {}
    # empty formats
    days = ('monday', 'tuesday', 'wednesday', 'thursday', 'friday')
    layout_times = {'9h': None, '11h': None, '13h': None, '15h': None, '17h': None}

    for day in days:
        empty_day = {}

        for room in rooms:
            # room_var = room.room
            filled_times = layout_times.copy()
            for time in filled_times:
                filled_times[time] = {subjects[1].name: subjects[1], subjects[2].name: subjects[2]}

            empty_day[room] = filled_times

        week[day] = empty_day

    return week