import schedule_class
import score
import random
import time
import activity_class

TYPE_LECTURE = 'lecture'
TYPE_SEMINAR = 'seminar'
TYPE_PRACTICUM = 'practicum'

def alg(students, courses, rooms, schedule):

    find_empty(schedule)
    for course in courses:

        for i in range(int(course.q_lecture)):
            schedule[find_empty(schedule)].activity = activity_class.Activity(course, TYPE_LECTURE)

        for i in range(int(course.q_seminar)):
            schedule[find_empty(schedule)].activity = activity_class.Activity(course, TYPE_SEMINAR)

        for i in range(int(course.q_practicum)):
            schedule[find_empty(schedule)].activity = activity_class.Activity(course, TYPE_PRACTICUM)

    return schedule

# TODO: Add find empty for specific day/room/time (?)
def find_empty(schedule, max_size = 0):
    for i, roomslot in enumerate(schedule):
        if roomslot.activity is None:
            return i


#
# Track recent score steps, stop if nothing changed much!
#
def basic_hillclimber(schedule, courses, desired_score):
    # to keep track of running time
    start_time = time.time()
    # calculate starting score of schedule
    score_schedule = score.calculate(schedule, courses)
    new_schedule = schedule
    #for i in range(10):
    while score_schedule < desired_score:
        # print "new round, new chances"
        old_score = score.calculate(new_schedule, courses)

        # create random swap indexes
        swap_index_1 = random.randrange(len(new_schedule))
        swap_index_2 = random.randrange(len(new_schedule))

        # swap courses and course types
        temp_course = new_schedule[swap_index_1].activity.course
        temp_type = new_schedule[swap_index_1].activity.type
        new_schedule[swap_index_1].course = new_schedule[swap_index_2].course
        new_schedule[swap_index_1].type = new_schedule[swap_index_2].type
        new_schedule[swap_index_2].course = temp_course
        new_schedule[swap_index_2].type = temp_type
        new_score = score.calculate(new_schedule, courses)
        if new_score < old_score:
            # swap the courses back to their original place
            temp_course = new_schedule[swap_index_1].course
            temp_type = new_schedule[swap_index_1].type
            new_schedule[swap_index_1].course = new_schedule[swap_index_2].course
            new_schedule[swap_index_1].type = new_schedule[swap_index_2].type
            new_schedule[swap_index_2].course = temp_course
            new_schedule[swap_index_2].type = temp_type
            print "\tschedules stays the same"
        else:
            score_schedule = new_score
        print "\t score in between: ", score_schedule, "\n"
    #calculate running time
    elapsed_time = time.time() - start_time
    print "\tbasic_hillclimber; score: ", score_schedule, "elapsed time: ", elapsed_time
    return {"schedule" : schedule, "score" : score_schedule, "elapsed_time" : elapsed_time}
