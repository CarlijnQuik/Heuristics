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


"""
    Simulated annealing algorithm.
"""
def decision(probability):
    return random.random() < probability

def random_simulated_annealer(schedule, courses, desired_score, initial_temp, maximum_duration):
    start_time = time.time()
    
    # Calculate starting score of schedule.
    score_schedule = score.calculate(schedule, courses)
    new_schedule = copy.copy(schedule)
    score_increase = []
    score_increase.append(score_schedule)
    update_times = []
    update_times.append(start_time - start_time)
    
    # Denotes the annealing parameter.
    k = 0

    while score_schedule < desired_score:
        temp = initial_temp * math.pow(0.95, k)
        new_schedule = copy.deepcopy(schedule)
        old_score = score.calculate(new_schedule, courses)

        # Create random swap indexes.
        swap_index_1 = random.randrange(len(schedule))
        swap_index_2 = random.randrange(len(schedule))

        for i in range(1):
            # Create random swap indexes.
            swap_index_1 = random.randrange(len(new_schedule))
            swap_index_2 = random.randrange(len(new_schedule))
            
            # Swap courses and course types.
            temp_activity = new_schedule[swap_index_1].activity
            new_schedule[swap_index_1].activity = new_schedule[swap_index_2].activity
            new_schedule[swap_index_2].activity = temp_activity

        new_score = score.calculate(new_schedule, courses)
        decision_annealing =  (1 / (1 + (math.exp(((old_score - new_score) * 5) / temp))))
        if new_score >= old_score:
            schedule = copy.deepcopy(new_schedule)
            score_schedule = new_score
        elif decision(decision_annealing):
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
                    
            # Maximum duration of the algorithm.
            if (int(update_time)/ 60) >= maximum_duration:
                break
    elapsed_time = time.time() - start_time
    plt.plot(update_times, score_increase)
    plt.title("random_simulated_annealer; desired_score: " +str(desired_score) + ", elapsed_time: "+ str(int(elapsed_time))+" sec")
    print "random_simulated_annealer"+str(desired_score)+"_"+str(int(elapsed_time))
    plt.show()
    print score_increase
    print "\trandom_simulated_annealer; score: ", score_schedule, "elapsed time: ", int(elapsed_time / 60),"Min", int(elapsed_time % 60), "sec"
    return {"schedule" : schedule, "score" : score_schedule, "elapsed_time" : elapsed_time}

def guided_simulated_annealer(schedule, courses, desired_score, initial_temp, maximum_duration):
    start_time = time.time()
    
    # Calculate starting score of schedule.
    score_schedule = score.calculate(schedule, courses)
    new_schedule = copy.copy(schedule)
    score_increase = []
    score_increase.append(score_schedule)
    update_times = []
    update_times.append(start_time - start_time)
    
    # Denotes the annealing parameter.
    k = 0

    while score_schedule < desired_score:
        # Calculate current temperature.
        temp = initial_temp * math.pow(0.95, k)

        # Create dictionary to determine the order of the scores and values.
        sub_scores = {}
        rank_in_subscores = 0
        
        # Create new_schedule.
        new_schedule = copy.deepcopy(schedule)
        
        # Determine score of the former schedule.
        old_score = score.calculate(new_schedule, courses)
        
        # Calculate subscores and determine which subscore is the highest.
        STS = score.check_special_timeslot(new_schedule)
        CMA = score.check_multiple_activities(new_schedule)
        CDD = score.check_day_duplicate(new_schedule)
        
        # Sort the sub_scores.
        sub_scores_sorted = [STS[1], CMA[1], CDD[1]]
        sub_scores_sorted.sort(reverse=True)
        
        # Put the scores into a library.
        sub_scores["STS"] = STS[1]
        sub_scores["CMA"] = CMA[1]
        sub_scores["CDD"] = CDD[1]
        
        # Determine which sub_score belongs to the given score.
        if rank_in_subscores < len(sub_scores):
            for sub_score in sub_scores:
                if sub_scores[sub_score] == sub_scores_sorted[int(rank_in_subscores)]:
                    max_sub_score = sub_score
        else:
            max_sub_score = "random"

        # For CDD: check_day_duplicate.
        if max_sub_score == "CDD":
            swap_index_1 = random.choice(CDD[0][random.choice(CDD[0].keys())][1:])
            print new_schedule[swap_index_1].day
            swap_index_2 = random.randrange(len(schedule))
            while new_schedule[swap_index_1].day == new_schedule[swap_index_2].day:
                swap_index_2 = random.randrange(len(schedule))
                
        # For CMA: check_multiple_activities.
        elif max_sub_score == "CMA":
            swap_index_1 = CMA[0][random.choice(CMA[0].keys())]["course1"]
            swap_index_2 = random.randrange(len(schedule))
            while swap_index_2 == swap_index_1:
                swap_index_2 = random.randrange(len(schedule))
                
        # For STS: special_timeslot.
        elif max_sub_score == "STS":
            swap_index_1 = STS[0][0]
            print STS[0][0]
            print new_schedule[STS[0][0]].activity.course.seminar_max_students
            empty_place = find_empty_random(new_schedule)
            print "the empty_place:", empty_place
            swap_index_2 = empty_place
            swap_index_2 = random.randrange(len(schedule))
            
        # Create random swap indexes.
        else:
            swap_index_1 = random.randrange(len(schedule))
            swap_index_2 = random.randrange(len(schedule))

        # Swap courses and course types.
        temp_activity = new_schedule[swap_index_1].activity
        new_schedule[swap_index_1].activity = new_schedule[swap_index_2].activity
        new_schedule[swap_index_2].activity = temp_activity

        # Calculate score of new schedule.
        new_score = score.calculate(new_schedule, courses)
        
        # Increase rank_in_subscore's value to prevent getting stuck in local maximum.
        rank_in_subscores += 1/20

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
                    
            # Maximum duration of the algorithm.
            if (int(update_time)/ 60) >= maximum_duration:
                break
                
    elapsed_time = time.time() - start_time
    plt.plot(update_times, score_increase)
    plt.title("guided_simulated_annealer; desired_score: " +str(desired_score) + ", elapsed_time: "+ str(int(elapsed_time))+" sec")
    print "guided_simulated_annealer"+str(desired_score)+"_"+str(int(elapsed_time))
    plt.show()
    print score_increase
    print "\tguided_simulated_annealer; score: ", score_schedule, "elapsed time: ", int(elapsed_time / 60),"Min", int(elapsed_time % 60), "sec"
    return {"schedule" : schedule, "score" : score_schedule, "elapsed_time" : elapsed_time}
