import roomslot
import score
import random
import time
import activity
import copy
import matplotlib.pyplot as plt
import pylab
from collections import deque

def alg(students, courses, rooms, schedule):


    return schedule

# TODO: Add find empty for specific day/room/time (?)
# Does find empty work probably? None is returned when a schedule in a algorithm is placed.
def find_empty(schedule, max_size = 0, day = None):
    for i, roomslot in enumerate(schedule):
        if day != None:
            if roomslot.day == day:
                if roomslot.activity is None:
                    return i
        elif roomslot.activity is None:
            return i
    return None

# maybe a store function that it remembers what has already been added if the same schedule is checked again
def find_empty_random(schedule, max_size = 0):
    empty_room_list = []
    for i, roomslot in enumerate(schedule):
        if roomslot.activity.course is None:
            empty_room_list.append(i)
    return random.choice(empty_room_list)


#
# Track recent score steps, stop if nothing changed much!
#
def random_hillclimber(schedule, courses, desired_score):
    start_time = time.time()
    # calculate starting score of schedule
    score_schedule = score.calculate(schedule, courses)
    new_schedule = copy.copy(schedule)
    score_increase = []
    score_increase.append(score_schedule)
    update_times = []
    update_times.append(start_time - start_time)

    for i in range(1):
    #while score_schedule < desired_score:
        new_schedule = copy.deepcopy(schedule)
        old_score = score.calculate(new_schedule, courses)

        # create random swap indexes
        swap_index_1 = random.randrange(len(schedule))
        swap_index_2 = random.randrange(len(schedule))

        for i in range(1):
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
        if new_score > old_score:
            schedule = copy.deepcopy(new_schedule)
            score_schedule = new_score

        update_time = time.time() - start_time
        if int(update_time) != int(update_times[-1]):
            update_times.append(update_time)
            score_increase.append(score_schedule)
            if len(score_increase) >= 61:
                if (score_increase[-1] - score_increase[-61]) < 15:
                    break
    elapsed_time = time.time() - start_time
    plt.plot(update_times, score_increase)
    print "random_hillclimber_"+str(desired_score)+"_"+str(int(elapsed_time))
    plt.title("random_hillclimber; desired_score: " +str(desired_score) + ", elapsed_time: "+ str(int(elapsed_time)))
    plt.savefig("random_hillclimber; desired_score: ")
    plt.show()
    print "\trandom_hillclimber; score: ", score_schedule, "elapsed time: ", int(elapsed_time / 60),"Min", int(elapsed_time % 60), "sec"
    print update_times
    print score_increase
    return {"schedule" : schedule, "score" : score_schedule, "elapsed_time" : elapsed_time}
