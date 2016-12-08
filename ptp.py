import roomslot
import score
import random
import time
import activity
import copy
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
    start_time = time.time()
    # calculate starting score of schedule
    score_schedule = score.calculate(schedule, courses)
    new_schedule = copy.copy(schedule)
    score_increase = []
    score_increase.append(score_schedule)
    update_times = []
    update_times.append(start_time - start_time)

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
        if int(update_time / 60) != int(update_times[-1] / 60):
            update_times.append(update_time)
            score_increase.append(score_schedule)
            if (score_increase[-1] - score_increase[-2]) < 15:
                break
    elapsed_time = time.time() - start_time
    print "\trandom_hillclimber; score: ", score_schedule, "elapsed time: ", int(elapsed_time / 60),"Min", int(elapsed_time % 60), "sec"
    print update_times
    print score_increase
    return {"schedule" : schedule, "score" : score_schedule, "elapsed_time" : elapsed_time}


# TODO has to be written to a real simulated annealer.
def random_simulated_annealer(schedule, courses, desired_score):
    start_time = time.time()
    # calculate starting score of schedule
    score_schedule = score.calculate(schedule, courses)
    new_schedule = copy.copy(schedule)
    score_increase = []
    score_increase.append(score_schedule)
    update_times = []
    update_times.append(start_time - start_time)

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
            print update_times
            score_increase.append(score_schedule)
            print len(score_increase)
            if len(score_increase) >= 61:
                if (score_increase[-1] - score_increase[-61]) < 1500:
                    break
    elapsed_time = time.time() - start_time
    print score_increase
    print "\trandom_simulated_annealer; score: ", score_schedule, "elapsed time: ", int(elapsed_time / 60),"Min", int(elapsed_time % 60), "sec"
    return {"schedule" : schedule, "score" : score_schedule, "elapsed_time" : elapsed_time}

# still in process 
def guided_hillclimber(schedule, courses, desired_score):
    #check_special_timeslot(schedule)
    #check_spreading(schedule, courses)
    #check_day_duplicate(schedule)
    #check_multiple_activities(schedule)
    #check_small_room(schedule)

    start_time = time.time()
    # calculate starting score of schedule
    score_schedule = score.calculate(schedule, courses)
    new_schedule = copy.copy(schedule)
    score_increase = []
    score_increase.append(score_schedule)
    update_times = []
    update_times.append(start_time - start_time)

    while score_schedule < desired_score:
        new_schedule = copy.deepcopy(schedule)
        old_score = score.calculate(new_schedule, courses)
        STS = score.check_special_timeslot(new_schedule)
        print STS
        if STS[1] is not 0:
            swap_index_1 = STS[0][0]
            print STS[0][0]
            print new_schedule[STS[0][0]].activity.course.seminar_max_students
            empty_place = find_empty(new_schedule)
            print empty_place
            swap_index_2 = empty_place
            #swap_index_2 = random.randrange(len(schedule))
        else:
            # create random swap indexes
            swap_index_1 = random.randrange(len(schedule))
            swap_index_2 = random.randrange(len(schedule))


        # create random swap indexes
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
        if int(update_time / 60) != int(update_times[-1] / 60):
            update_times.append(update_time)
            score_increase.append(score_schedule)
            if (score_increase[-1] - score_increase[-2]) < 15:
                break
    elapsed_time = time.time() - start_time
    print "\trandom_hillclimber; score: ", score_schedule, "elapsed time: ", int(elapsed_time / 60),"Min", int(elapsed_time % 60), "sec"
    print update_times
    print score_increase
    return {"schedule" : schedule, "score" : score_schedule, "elapsed_time" : elapsed_time}
