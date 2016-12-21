# import libraries and other files

import load as loader
import csv
import ptp
import guided_hillclimber
import score
import matplotlib.pyplot as plt
import math
import simulated_annealer
import fireworks
import hillclimber

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

# Fill the schedule with directed roomfiller
#schedule = loader.directed_fill_schedule(schedule, courses)
#schedule = loader.random_fill_schedule(schedule, courses)
#score.calculate(schedule, courses)



# create random schedules, plot their scores, returns list of scores
#scores_random_schedules = ptp.scores_random_schedules(schedule, courses, 1000)


# schedule = simulated_annealer.random_simulated_annealer(schedule, courses, -1500, 1000)
score.calculate(schedule, courses)

#write_csv(schedule)



print '\n\tDONE LOADING!\n'


#
# Random swap two activities

#random_hillclimber_schedule = hillclimber.random_hillclimber(schedule, courses, 0, 1)
#guided_hillclimber = hillclimber.guided_hillclimber(schedule, courses, 0)
#random_simulated_annealer = simulated_annealer.random_simulated_annealer(schedule, courses, -600, 1000, 20)
#guided_simulated_annealer = simulated_annealer.guided_simulated_annealer(schedule, courses, -1500, 1000, 20)
#random_fireworks = fireworks.random_fireworks(schedule, courses, 0, 5)


# write_csv(random_hillclimber_schedule["schedule"])

#
# Use
