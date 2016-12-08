import roomslot
import score
import random
import time
import activity
import copy
import matplotlib.pyplot as plt
from collections import deque

def find_empty_random(schedule, max_size = 0):
    empty_room_list = []
    for i, roomslot in enumerate(schedule):
        if roomslot.activity.course is None:
            empty_room_list.append(i)
    print empty_room_list
    return random.choice(empty_room_list)

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
    #for i in range(1):
    while score_schedule < desired_score:
        new_schedule = copy.deepcopy(schedule)
        old_score = score.calculate(new_schedule, courses)
        STS = score.check_special_timeslot(new_schedule)
        CMA = score.check_multiple_activities(new_schedule)
        CDD = score.check_day_duplicate(new_schedule)
        #print "this is CDD score: ", CDD[1], random.choice(CDD[0][random.choice(CDD[0].keys())][1:])
        print CDD[1]
        print "minus score from CMA:", CMA[1]
        print STS[1]
        print random.choice(CMA[0].keys())
        #print "Multiple activities list:", CMA[0][random.choice(CMA[0].keys())]["course1"]




        # for CDD: check_day_duplicate
        # swap_index_1 = random.choice(CDD[0][random.choice(CDD[0].keys())][1:])
        # print new_schedule[swap_index_1].day
        # swap_index_2 = random.randrange(len(schedule))
        # while new_schedule[swap_index_1].day == new_schedule[swap_index_2].day:
        #     swap_index_2 = random.randrange(len(schedule))

        # for CMA: check_multiple_activities
        swap_index_1 = CMA[0][random.choice(CMA[0].keys())]["course1"]
        swap_index_2 = random.randrange(len(schedule))
        while swap_index_2 == swap_index_1:
            swap_index_2 = random.randrange(len(schedule))


        # for STS: special_timeslot
        # swap_index_1 = STS[0][0]
        # print STS[0][0]
        # print new_schedule[STS[0][0]].activity.course.seminar_max_students
        # empty_place = find_empty_random(new_schedule)
        # print "the empty_place:", empty_place
        # swap_index_2 = empty_place
        #swap_index_2 = random.randrange(len(schedule))


        #print "this is CMA: ", CMA
        # if STS[1] is not 0:
        #     swap_index_1 = STS[0][0]
        #     print STS[0][0]
        #     print new_schedule[STS[0][0]].activity.course.seminar_max_students
        #     empty_place = find_empty_random(new_schedule)
        #     print "the empty_place:", empty_place
        #     swap_index_2 = empty_place
        #     #swap_index_2 = random.randrange(len(schedule))
        # else:
        #     # create random swap indexes
        #     swap_index_1 = random.randrange(len(schedule))
        #     swap_index_2 = random.randrange(len(schedule))


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
        if int(update_time) != int(update_times[-1]):
            update_times.append(update_time)
            score_increase.append(score_schedule)
            if len(score_increase) >= 61:
                if (score_increase[-1] - score_increase[-61]) < 15:
                    break
    elapsed_time = time.time() - start_time

    print "\tguided_hillclimber; score: ", score_schedule, "elapsed time: ", int(elapsed_time / 60),"Min", int(elapsed_time % 60), "sec"
    print update_times
    print score_increase
    plt.plot(update_times, score_increase)
    print "guided_hillclimber_"+str(desired_score)+"_"+str(int(elapsed_time/60))+" Min"
    plt.title("guided_hillclimber; desired_score: " +str(desired_score) + ", elapsed_time: "+ str(int(elapsed_time/60))+" Min")
    plt.show()
    return {"schedule" : schedule, "score" : score_schedule, "elapsed_time" : elapsed_time}
