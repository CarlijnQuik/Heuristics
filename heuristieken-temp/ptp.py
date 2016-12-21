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
#TODO: checken of deze nog nodig is! doordat niet alle courses meer gevuld hoeven worden met "None" door activity swap ipv de elementen van activity
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
        if roomslot.activity is None:
            empty_room_list.append(i)
    return random.choice(empty_room_list)



#
# Track recent score steps, stop if nothing changed much!
#
