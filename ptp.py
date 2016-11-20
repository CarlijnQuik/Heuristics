import schedule_class
import score
import random
import time

TYPE_LECTURE = 'lecture'
TYPE_SEMINAR = 'seminar'
TYPE_PRACTICUM = 'practicum'

def alg(students, courses, rooms, schedule):

    find_empty(schedule)
    for course in courses:

        for i in range(int(course.q_lecture)):
            schedule[find_empty(schedule)].add(course, TYPE_LECTURE)

        for i in range(int(course.q_seminar)):
            schedule[find_empty(schedule)].add(course, TYPE_SEMINAR)

        for i in range(int(course.q_practicum)):
            schedule[find_empty(schedule)].add(course, TYPE_PRACTICUM)

    # Get score for the Schedule
    score.calculate(schedule, courses)
    return schedule

# TODO: Add find empty for specific day/room/time (?)
def find_empty(schedule, max_size = 0):
    for i, roomslot in enumerate(schedule):
        if roomslot.course is None and roomslot.type is None:
            return i

def basic_hillclimber(input_schedule, courses, desired_score):
    start_time = time.time()
    score_schedule = score.calculate(input_schedule, courses)
    schedule = input_schedule
    for i in range(1):
    #while score_schedule < desired_score:
        old_score = score.calculate(schedule, courses)
        new_schedule = schedule
        swap_index_1 = random.randrange(len(new_schedule))
        swap_index_2 = random.randrange(len(new_schedule))
        temp_course = new_schedule[swap_index_1]
        schedule[swap_index_1] = new_schedule[swap_index_2]
        schedule[swap_index_2] = temp_course
        new_score = score.calculate(new_schedule, courses)
        if new_score > old_score:
            schedule = new_schedule
            score_schedule = new_score
    elapsed_time = time.time()-start_time
    print "\tbasic_hillclimber; score: ", score_schedule, "elapsed time: ", elapsed_time
    return {"schedule" : schedule, "score" : score_schedule, "elapsed_time" : elapsed_time}
