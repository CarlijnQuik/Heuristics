# import libraries and other files

import load as loader
import csv
import simulated_annealer
import fireworks
import hillclimber

"""

    Write partial info from schedule to a csv.
    For every roomslot this will add the values:
        - Day
        - Time
        - Room (name)
        - Course (name)
        - Type (Lecture, Seminar or Practicum)
        - Course Group

"""
def write_csv(schedule):
    with open("output_files/schedule.csv", "wb") as csvfile:
        cursor = csv.writer(csvfile)

        for i, roomslot in enumerate(schedule):
            # Only print real activities
            if roomslot.activity and roomslot.activity.course:
                cursor.writerow([roomslot.day, roomslot.time, roomslot.room.name, roomslot.activity.course.name, roomslot.activity.type, roomslot.activity.group, len(roomslot.activity.students) / roomslot.room.capacity])

        print "Output file generated!"


PRESET = True

# Determine input files
if PRESET or raw_input('Enter def for default input or enter to continue manually: ') == 'def':
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


# Create an empty schedule
schedule = loader.create_schedule(rooms)

# Fill the schedule with all courses
schedule = loader.fill_schedule_random(schedule, courses)



print '\n\tDONE LOADING!\n'

"""

    Loading finished.
    Put the code of the algorithm you want to run below.

"""

random_hillclimber = hillclimber.random_hillclimber(schedule, courses, 850)
write_csv(random_hillclimber["schedule"])