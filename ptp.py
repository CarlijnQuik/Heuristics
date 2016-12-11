import roomslot
import score
import random
import time
import activity
import copy
import matplotlib.pyplot as plt
import pylab
import load as loader
from collections import deque

def scores_random_schedules(schedule, courses, number_random_schedules):
    random_schedules_scores = []
    for i in range(number_random_schedules):
        random_schedule = copy.deepcopy(schedule)
        random_schedule = loader.random_fill_schedule(random_schedule, courses)
        random_schedule_score = score.calculate(random_schedule, courses)
        random_schedules_scores.append(random_schedule_score)
    srs = random_schedules_scores
    plt.plot(range(0,len(srs)),srs , "o")
    srs_average = sum(srs)/len(srs)
    srs_max = max(srs)
    plt.title(str(number_random_schedules) + " random schedules scores with an average score of " + str(srs_average) + " and a maximum value of " + str(srs_max))
    plt.show()
    return srs


def alg(students, courses, rooms, schedule):


    return schedule

def find_empty(schedule, max_size = None, day = None):
    for i, roomslot in enumerate(schedule):
        if day != None:
            if roomslot.day == day:
                if max_size != None:
                    if roomslot.room.capacity <= max_size:
                        if roomslot.activity is None:
                            return i
                elif roomslot.activity is None:
                    return i
        elif max_size != None:
            if roomslot.room.capacity <= max_size:
                if roomslot.activity is None:
                    return i
        elif roomslot.activity is None:
            return i
    return None

# use this random empty when a schedule is being filled
def find_random_filler(schedule, max_size = None, day = None):
    search_count = 0
    while search_count < 100:
        random_index = random.randrange(len(schedule))
        if day != None:
            if schedule[random_index].day == day:
                if max_size != None:
                    if schedule[random_index].room.capacity <= max_size:
                        if schedule[random_index].activity is None:
                            return random_index
                elif schedule[random_index].activity is None:
                    return random_index
        elif max_size != None:
            if schedule[random_index].room.capacity <= max_size:
                if schedule[random_index].activity is None:
                    return random_index
        elif schedule[random_index].activity is None:
            return random_index
        search_count += 1
    return find_empty(schedule)

# use this random empty when a filled schedule is being searched
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

    #for i in range(1):
    while score_schedule < desired_score:
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
