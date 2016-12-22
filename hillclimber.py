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
import ptp


"""

    Hillclimber algorithm based on random mutations.

"""
def random_hillclimber(schedule, courses, desired_score, maximum_duration = None):
    # Clock the start time of the alghorithm.
    start_time = time.time()
    
    # Calculate starting score of schedule.
    score_schedule = score.calculate(schedule, courses)
    print "Base Score:", score_schedule
    
    # Lists to store the in between scores in time.
    score_increase = []
    score_increase.append(score_schedule)
    update_times = []
    update_times.append(start_time - start_time)

    while score_schedule < desired_score:
        #  Make copy of the schedule.
        new_schedule = copy.deepcopy(schedule)
        
        # Calculate score before mutation.
        old_score = score.calculate(new_schedule, courses)
        
        # Create random swap indexes.
        swap_index_1 = random.randrange(len(new_schedule))
        swap_index_2 = random.randrange(len(new_schedule))

        # Mutate schedule: swap courses and course type.
        temp_activity = new_schedule[swap_index_1].activity
        new_schedule[swap_index_1].activity = new_schedule[swap_index_2].activity
        new_schedule[swap_index_2].activity = temp_activity

        # Calculate score mutated schedule.
        new_score = score.calculate(new_schedule, courses)
        
        # The mutation is accepted, if the new score is higher than the old score.
        if new_score > old_score:
            schedule = copy.deepcopy(new_schedule)
            score_schedule = new_score
            print score_schedule

        # Calculate the in between time.
        update_time = time.time() - start_time
        
        # If the time is a new second, make timestamp.
        if int(update_time) != int(update_times[-1]):
            update_times.append(update_time)
            score_increase.append(score_schedule)
            if len(score_increase) >= 61:
                if (score_increase[-1] - score_increase[-61]) < 3:
                    break
                    
            # Maximum duration of the algorithm.
            if maximum_duration:
                if (int(update_time)/ 60) >= maximum_duration:
                    break

    # Calculate how long the algorithm has been running.
    elapsed_time = time.time() - start_time

    # Plot of the timestamps and their scores.
    plt.plot(update_times, score_increase)
    print "random_hillclimber_"+str(desired_score)+"_"+str(int(elapsed_time))
    plt.title("random_hillclimber; desired_score: " +str(desired_score) + ", elapsed_time: "+ str(int(elapsed_time)) + "sec")
    plt.savefig("random_hillclimber; desired_score: ")
    plt.show()
    print "\trandom_hillclimber; score: ", score_schedule, "elapsed time: ", int(elapsed_time / 60),"Min", int(elapsed_time % 60), "sec"

    # Return schedule, score and elapsed time.
    return {"schedule" : schedule, "score" : score_schedule, "elapsed_time" : elapsed_time}


"""

    Hillclimber algorithm based on constrained mutations.

"""
def guided_hillclimber(schedule, courses, desired_score):
    # check_special_timeslot(schedule)
    # check_spreading(schedule, courses)
    # check_day_duplicate(schedule)
    # check_multiple_activities(schedule)
    # check_small_room(schedule)

    start_time = time.time()
    
    # Calculate starting score of schedule.
    score_schedule = score.calculate(schedule, courses)
    print "Base Score:", score_schedule
    
    # Score list for intermediate schedule scores is added.
    score_increase = []
    score_increase.append(score_schedule)
    
    # Time list for intermediate schedules.
    update_times = []
    update_times.append(start_time - start_time)
    
    # If uncommented and while loop is commented, the loop is only done once.
    while score_schedule < desired_score:

        # Create dictionary to determine the order of the scores and values.
        sub_scores = {}
        rank_in_subscores = 0
        
        # Create new_schedule.
        new_schedule = copy.deepcopy(schedule)
        
        # Determine score of the former schedule.
        old_score = score.calculate(new_schedule, courses)
        
        # Calculate subscores and determine which subscore is the highest.
        special_time_slot = score.check_special_timeslot(new_schedule)
        multiple_activities = score.check_multiple_activities(new_schedule)
        day_duplicate = score.check_day_duplicate(new_schedule)
        small_room = score.check_small_room(new_schedule)
        
        # Sort the sub_scores.
        sub_scores_sorted = [special_time_slot[1], multiple_activities[1], day_duplicate[1], small_room[1]]
        sub_scores_sorted.sort(reverse=True)
        
        # Put the scores into a library.
        sub_scores["special_time_slot"] = special_time_slot[1]
        sub_scores["multiple_activities"] = multiple_activities[1]
        sub_scores["day_duplicate"] = day_duplicate[1]
        sub_scores["small_room"] = small_room[1]
        
        # Determine which sub_score belongs to the given score.
        if rank_in_subscores < len(sub_scores):
            for sub_score in sub_scores:
                if sub_scores[sub_score] == sub_scores_sorted[int(rank_in_subscores)]:
                    max_sub_score = sub_score
        else:
            max_sub_score = "random"

        # For day_duplicate: check_day_duplicate.
        if max_sub_score == "day_duplicate":
            swap_index_1 = random.choice(day_duplicate[0])
            swap_index_2 = random.randrange(len(schedule))
            while new_schedule[swap_index_1].day == new_schedule[swap_index_2].day:
                swap_index_2 = random.randrange(len(schedule))
                
        # For multiple_activities: check_multiple_activities.
        elif max_sub_score == "multiple_activities":
            swap_index_1 = random.choice(multiple_activities[0])
            swap_index_2 = random.randrange(len(schedule))
            while (new_schedule[swap_index_1].day == new_schedule[swap_index_2].day) and (new_schedule[swap_index_1].time == new_schedule[swap_index_2].time):
                swap_index_2 = random.randrange(len(schedule))
                
        # For special_time_slot: special_timeslot.
        elif max_sub_score == "special_time_slot":
            swap_index_1 = special_time_slot[0][0]
            empty_place = ptp.find_empty_random(new_schedule)
            swap_index_2 = empty_place
            swap_index_2 = random.randrange(len(schedule))
        elif max_sub_score == "small_room":
            swap_index_1 = random.choice(small_room[0])
            swap_index_2 = random.randrange(len(schedule))
            while schedule[swap_index_2].room.capacity < len(schedule[swap_index_1].activity.students):
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
        
        # increase rank_in_subscores value to prevent getting stuck in local maximum.
        rank_in_subscores += 1/20
        
        # If the new score is higher, accept new schedule.
        if new_score > old_score:
            schedule = copy.deepcopy(new_schedule)
            score_schedule = new_score
            print score_schedule
            # reset rank_in_subscorescore
            rank_in_subscores = 0

        # Create time_stamp.
        update_time = time.time() - start_time
        
        # Store time_stamp if new second with the schedules score.
        if int(update_time) != int(update_times[-1]):
            update_times.append(update_time)
            score_increase.append(score_schedule)
            if len(score_increase) >= 61:
                if (score_increase[-1] - score_increase[-61]) < 15:
                    break
                    
    # Calculate total time since the algorithm has started.
    elapsed_time = time.time() - start_time
    print "\tguided_hillclimber; score: ", score_schedule, "elapsed time: ", int(elapsed_time / 60),"Min", int(elapsed_time % 60), "sec"
    
    # Create graph of time and scores.
    plt.plot(update_times, score_increase)
    
    # Print plot information for save purposes.
    print "guided_hillclimber_"+str(desired_score)+"_"+str(int(elapsed_time/60))+" Min"
    plt.title("guided_hillclimber; final_score: " + str(score_schedule) + ", elapsed_time: "+ str(int(elapsed_time))+" sec" + "desired_score: " +str(desired_score))
    
    # Show plot.
    plt.show()
    return {"schedule" : schedule, "score" : score_schedule, "elapsed_time" : elapsed_time}
