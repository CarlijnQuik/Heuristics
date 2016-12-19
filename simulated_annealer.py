import roomslot
import score
import random
import time
import activity
import copy
import math
import matplotlib.pyplot as plt
import pylab
import load as loader
from collections import deque

def decision(probability):
    return random.random() < probability

def random_simulated_annealer(schedule, courses, desired_score, initial_temp, maximum_duration):
    start_time = time.time()
    # calculate starting score of schedule
    score_schedule = score.calculate(schedule, courses)
    new_schedule = copy.copy(schedule)
    score_increase = []
    score_increase.append(score_schedule)
    update_times = []
    update_times.append(start_time - start_time)
    # denotes the annealing parameter
    k = 0

    while score_schedule < desired_score:
        temp = initial_temp * math.pow(0.95, k)
        print temp
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
        decision_annealing =  (1 / (1 + (math.exp(((old_score - new_score) * 5) / temp))))
        if new_score >= old_score:
            schedule = copy.deepcopy(new_schedule)
            score_schedule = new_score
        elif decision(decision_annealing):
            print "                 there was annealed", decision_annealing, (abs(old_score)-abs(new_score))
            schedule = copy.deepcopy(new_schedule)
            score_schedule = new_score

        if temp > 20:
            k += 1
        update_time = time.time() - start_time
        if int(update_time) != int(update_times[-1]):
            update_times.append(update_time)
            score_increase.append(score_schedule)
            if len(score_increase) >= 61:
                if (score_increase[-1] - score_increase[-61]) < 3:
                    break
            # maximum duration of the algorithm
            if (int(update_time)/ 60) >= maximum_duration:
                break
    elapsed_time = time.time() - start_time
    plt.plot(update_times, score_increase)
    print "random_simulated_annealer"+str(desired_score)+"_"+str(int(elapsed_time))
    plt.show()
    print score_increase
    print "\trandom_simulated_annealer; score: ", score_schedule, "elapsed time: ", int(elapsed_time / 60),"Min", int(elapsed_time % 60), "sec"
    return {"schedule" : schedule, "score" : score_schedule, "elapsed_time" : elapsed_time}

def guided_simulated_annealer(schedule, courses, desired_score, initial_temp):
    start_time = time.time()
    # calculate starting score of schedule
    score_schedule = score.calculate(schedule, courses)
    new_schedule = copy.copy(schedule)
    score_increase = []
    score_increase.append(score_schedule)
    update_times = []
    update_times.append(start_time - start_time)
    # denotes the annealing parameter
    k = 0

    while score_schedule < desired_score:
        temp = initial_temp * math.pow(0.95, k)
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
        if new_score >= old_score:
            schedule = copy.deepcopy(new_schedule)
            score_schedule = new_score
        elif decision((1 / (1 + math.exp(float(new_score - old_score)/ temp)))):
            schedule = copy.deepcopy(new_schedule)
            score_schedule = new_score

        k += 0.1
        update_time = time.time() - start_time
        if int(update_time) != int(update_times[-1]):
            update_times.append(update_time)
            score_increase.append(score_schedule)
            if len(score_increase) >= 61:
                if (score_increase[-1] - score_increase[-61]) < 15:
                    break
    elapsed_time = time.time() - start_time

    print "\trandom_simulated_annealer; score: ", score_schedule, "elapsed time: ", int(elapsed_time / 60),"Min", int(elapsed_time % 60), "sec"
    print update_times
    print score_increase
    print "guided_simulated_annealer"+str(desired_score)+"_"+str(int(elapsed_time))
    plt.plot(update_times, score_increase)
    print "random_simulated_annealer"+str(desired_score)+"_"+str(int(elapsed_time/60))+" Min"
    plt.title("random_simulated_annealer; desired_score: " +str(desired_score) + ", elapsed_time: "+ str(int(elapsed_time))+" sec")
    plt.show()
    return {"schedule" : schedule, "score" : score_schedule, "elapsed_time" : elapsed_time}

# still in process
