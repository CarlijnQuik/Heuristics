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
def random_hillclimber(schedule, courses, desired_score, maximum_duration):
    # clock the start time of the alghorithm.
    start_time = time.time()
    # calculate starting score of schedule.
    score_schedule = score.calculate(schedule, courses)
    # lists to store the in between scores in time.
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
        swap_index_1 = random.randrange(len(schedule))
        swap_index_2 = random.randrange(len(schedule))

        for i in range(1):
            # Create random swap indexes.
            swap_index_1 = random.randrange(len(new_schedule))
            swap_index_2 = random.randrange(len(new_schedule))

            # Mutate schedule: swap courses and course type.
            temp_activity = new_schedule[swap_index_1].activity
            new_schedule[swap_index_1].activity = new_schedule[swap_index_2].activity
            new_schedule[swap_index_2].activity = temp_activity

        # Calculate score mutated schedule.
        new_score = score.calculate(new_schedule, courses)
        # Compare score before and after mutation. If new score equals or is higher
        # than the old score, the mutation is accepted.
        if new_score >= old_score:
            schedule = copy.deepcopy(new_schedule)
            score_schedule = new_score

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
    print "random_hillclimber_"+str(desired_score)+"_"+str(int(elapsed_time))
    plt.title("random_hillclimber; desired_score: " +str(desired_score) + ", elapsed_time: "+ str(int(elapsed_time)) + "sec")
    plt.savefig("random_hillclimber; desired_score: ")
    plt.show()
    print "\trandom_hillclimber; score: ", score_schedule, "elapsed time: ", int(elapsed_time / 60),"Min", int(elapsed_time % 60), "sec"
    print update_times
    print score_increase
    return {"schedule" : schedule, "score" : score_schedule, "elapsed_time" : elapsed_time}

"""

    Hillclimber algorithm based constrained mutations.

"""
def guided_hillclimber(schedule, courses, desired_score):
    #check_special_timeslot(schedule)
    #check_spreading(schedule, courses)
    #check_day_duplicate(schedule)
    #check_multiple_activities(schedule)
    #check_small_room(schedule)

    start_time = time.time()
    # calculate starting score of schedule
    score_schedule = score.calculate(schedule, courses)
    # score list for intermediate schedule scores is added.
    score_increase = []
    score_increase.append(score_schedule)
    # time list for intermediate schedules
    update_times = []
    update_times.append(start_time - start_time)
    #if uncommented and while loop is commented, the loop is only done once
    #for i in range(1):
    while score_schedule < desired_score:

        # create dictionary to determine the order of the scores and valies
        sub_scores = {}
        rank_in_subscores = 0
        # create new_schedule
        new_schedule = copy.deepcopy(schedule)
        # determine score of the former schedule
        old_score = score.calculate(new_schedule, courses)
        # calculate subscores and determine which subscore is the highest
        special_time_slot = score.check_special_timeslot(new_schedule)
        multiple_activities = score.check_multiple_activities(new_schedule)
        day_duplicate = score.check_day_duplicate(new_schedule)
        small_room = score.check_small_room(new_schedule)
        # sort the sub_scores
        sub_scores_sorted = [special_time_slot[1], multiple_activities[1], day_duplicate[1]]
        sub_scores_sorted.sort(reverse=True)
        # put the scores into a library
        sub_scores["special_time_slot"] = special_time_slot[1]
        sub_scores["multiple_activities"] = multiple_activities[1]
        sub_scores["day_duplicate"] = day_duplicate[1]
        # determine which sub_score belongs to the given score

        if rank_in_subscores < len(sub_scores):
            for sub_score in sub_scores:
                if sub_scores[sub_score] == sub_scores_sorted[int(rank_in_subscores)]:
                    max_sub_score = sub_score
        else:
            max_sub_score = "random"

        #TODO: REMOVE. ONLY FOR TESTING PURPOSES
        print "max sub score:    ", max_sub_score,
        print "special_time_slot: ", special_time_slot[1], "multiple_activities: ", multiple_activities[1], "day_duplicate: ", day_duplicate[1]
        #print "this is day_duplicate score: ", day_duplicate[1], random.choice(day_duplicate[0][random.choice(day_duplicate[0].keys())][1:])

        # for day_duplicate: check_day_duplicate
        if max_sub_score == "day_duplicate":
            swap_index_1 = random.choice(day_duplicate[0])
            print new_schedule[swap_index_1].day
            swap_index_2 = random.randrange(len(schedule))
            while new_schedule[swap_index_1].day == new_schedule[swap_index_2].day:
                swap_index_2 = random.randrange(len(schedule))
        # for multiple_activities: check_multiple_activities
        elif max_sub_score == "multiple_activities":
            print "retun of the multiple_activities:  " , random.choice(multiple_activities[0])
            swap_index_1 = multiple_activities[0][random.choice(multiple_activities[0])]["course1"]
            swap_index_2 = random.randrange(len(schedule))
            while swap_index_2 == swap_index_1:
                swap_index_2 = random.randrange(len(schedule))
        # for special_time_slot: special_timeslot
        elif max_sub_score == "special_time_slot":
            swap_index_1 = special_time_slot[0][0]
            print special_time_slot[0][0]
            print new_schedule[special_time_slot[0][0]].activity.course.seminar_max_students
            empty_place = ptp.find_empty_random(new_schedule)
            print "the empty_place:", empty_place
            swap_index_2 = empty_place
            swap_index_2 = random.randrange(len(schedule))
         # create random swap indexes
        else:
            swap_index_1 = random.randrange(len(schedule))
            swap_index_2 = random.randrange(len(schedule))

        # swap courses and course types
        temp_activity = new_schedule[swap_index_1].activity
        new_schedule[swap_index_1].activity = new_schedule[swap_index_2].activity
        new_schedule[swap_index_2].activity = temp_activity

        # calculate score of new schedule
        new_score = score.calculate(new_schedule, courses)
        # increase rank_in_subscores value to prefent getting stuck in local maximum
        rank_in_subscores += 1/20
        # if the new score is higher, accept new schedule
        if new_score >= old_score:
            schedule = copy.deepcopy(new_schedule)
            score_schedule = new_score
            # reset rank_in_subscorescore
            rank_in_subscores = 0

        # create time_stamp
        update_time = time.time() - start_time
        # store time_stamp if new second with the schedules score
        if int(update_time) != int(update_times[-1]):
            update_times.append(update_time)
            score_increase.append(score_schedule)
            if len(score_increase) >= 61:
                if (score_increase[-1] - score_increase[-61]) < 15:
                    break
    # calculate total time since the alghorithm has started
    elapsed_time = time.time() - start_time

    print "\tguided_hillclimber; score: ", score_schedule, "elapsed time: ", int(elapsed_time / 60),"Min", int(elapsed_time % 60), "sec"
    #TODO: REMOVE. print time list
    print update_times
    #TODO: REMOVE. print
    print score_increase
    # create graph of time and scores
    plt.plot(update_times, score_increase)
    # print plot information for save purposes
    print "guided_hillclimber_"+str(desired_score)+"_"+str(int(elapsed_time/60))+" Min"
    plt.title("guided_hillclimber; desired_score: " +str(desired_score) + ", elapsed_time: "+ str(int(elapsed_time))+" sec")
    # show plot
    plt.show()
    return {"schedule" : schedule, "score" : score_schedule, "elapsed_time" : elapsed_time}
