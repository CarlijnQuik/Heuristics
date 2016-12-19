# import libraries and other files

import load as loader
import csv
import score
import ptp

def write_csv(schedule):
    with open("output_files/schedule2.csv", "wb") as csvfile:
        cursor = csv.writer(csvfile)

        for i, roomslot in enumerate(schedule):
            if roomslot.activity and roomslot.activity.course:
                cursor.writerow([roomslot.day, roomslot.time, roomslot.room.name, roomslot.activity.course.name, roomslot.activity.type])

        print "Output file generated!"


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


schedule = loader.create_schedule(rooms)
# Fill the schedule with all courses
schedule = loader.fill_schedule(schedule, courses)

score.calculate(schedule, courses)


write_csv(schedule)

print '\n\tDONE LOADING!\n'


#
# Random swap two activities

# random_hillclimber_schedule = ptp.random_hillclimber(schedule, courses, 900)
# write_csv(random_hillclimber_schedule["schedule"])

#
# Use
