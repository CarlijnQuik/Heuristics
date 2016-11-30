import roomslot
import score
import random
import time
import activity
from collections import deque

def alg(students, courses, rooms, schedule):


    return schedule

# TODO: Add find empty for specific day/room/time (?)
def find_empty(schedule, max_size = 0):
    for i, roomslot in enumerate(schedule):
        if roomslot.activity is None:
            return i


#
# Track recent score steps, stop if nothing changed much!
#
def random_hillclimber(schedule, courses, desired_score):
    # to keep track of running time
    start_time = time.time()
    # calculate starting score of schedule
    score_schedule = score.calculate(schedule, courses)
    new_schedule = schedule
    score_increase = deque()
    update_times = deque()
    netto_update_time = 0
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
        new_schedule[swap_index_1].activity.course = new_schedule[swap_index_2].activity.course
        new_schedule[swap_index_1].activity.type = new_schedule[swap_index_2].activity.type
        new_schedule[swap_index_2].activity.course = temp_course
        new_schedule[swap_index_2].activity.type = temp_type
        new_score = score.calculate(new_schedule, courses)
        if new_score < old_score:
            # swap the courses back to their original place
            temp_course = new_schedule[swap_index_1].activity.course
            temp_type = new_schedule[swap_index_1].activity.type
            new_schedule[swap_index_1].activity.course = new_schedule[swap_index_2].activity.course
            new_schedule[swap_index_1].activity.type = new_schedule[swap_index_2].activity.type
            new_schedule[swap_index_2].activity.course = temp_course
            new_schedule[swap_index_2].activity.type = temp_type
            # print "\tschedules stays the same"
        else:
            update_time = time.time() - start_time
            score_increase.append(new_score - score_schedule)
            update_times.append(update_time)
            if len(score_increase) > 5:
                score_increase.popleft()
                update_times.popleft()
                netto_update_time = update_times[4]-update_times[0]
            score_schedule = new_score
            if netto_update_time > 0:
                if (sum(score_increase) / netto_update_time) < (30/20):
                    break

        # print "\t score in between: ", score_schedule, "\n"
    #calculate running time
    elapsed_time = time.time() - start_time
    print "\tbasic_hillclimber; score: ", score_schedule, "elapsed time: ", "{0:.2f}".format(elapsed_time / 60),"Min"
    return {"schedule" : schedule, "score" : score_schedule, "elapsed_time" : elapsed_time}

