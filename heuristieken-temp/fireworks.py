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

# input lijst getallen, returnt lijst met ranknummers in volgorde van de corresponderende indexes
def calculate_rank(vector):
      a = {}
      rank= 0
      for num in sorted(vector):
          if num not in a:
              a[num]= rank
              rank= rank + 1
      return [rank - a[i] for i in vector]


# for this algorithm a list of schedules has to be entered
def random_fireworks(schedule, courses, desired_score, q_offspring):
    schedules =[]
    for i in range(q_offspring):
        schedules.append(copy.deepcopy(schedule))

    start_time = time.time()
    # calculate starting score of schedule

    # score_increase = []
    # score_increase.append(score_schedule)
    # update_times = []
    # update_times.append(start_time - start_time)

    highest_schedule = score.calculate(schedules[0], courses)

    name_counter = 0
    score_list = []
    #for i in range(1):
    while highest_schedule < desired_score:
        print len(schedules)
        schedule_list =[]
        score_list =[]

        for schedule in schedules:
            new_schedule = copy.deepcopy(schedule)
            schedule_score = score.calculate(new_schedule, courses)

            new_schedules = {}

            schedule_list.append(new_schedule)
            score_list.append(schedule_score)



            for i in range(q_offspring):
                # there is a possibility here to implement a while loop where only certain score increases are allowed
                schedule_score = 1400
                #for j in range(1):
                while score_list[i] - schedule_score < -20:
                    new_schedules[i] = copy.deepcopy(new_schedule)

                    # create random swap indexes
                    swap_index_1 = random.randrange(len(new_schedules[i]))
                    swap_index_2 = random.randrange(len(new_schedules[i]))
                    # swap courses and course types
                    temp_activity = new_schedules[i][swap_index_1].activity
                    new_schedules[i][swap_index_1].activity = new_schedules[i][swap_index_2].activity
                    new_schedules[i][swap_index_2].activity = temp_activity

                    schedule_score = score.calculate(new_schedules[i], courses)

                schedule_list.append(new_schedules[i])
                score_list.append(schedule_score)
        schedules =[]
        print "length schedule_list:   ", len(schedule_list)
        print "length score_list:      ", score_list

        rank_schedules = calculate_rank(score_list)
        for rank_number in range(q_offspring):
            for i, rank in enumerate(rank_schedules):
                print "this is the rank that should go ascending:   ", i, score_list[i], rank
                if rank == rank_number:
                    schedules.append(schedule_list[i])
                    break
        score_list.sort(reverse=True)

        highest_schedule = score.calculate(schedules[0], courses)
        print "\t\t the highest schedule:  ", len(score_list)
        print "\t\t length list schedules:  ", len(schedules)

        # update_time = time.time() - start_time
        # if int(update_time) != int(update_times[-1]):
        #     update_times.append(update_time)
        #     score_increase.append(score_schedule)
        #     if len(score_increase) >= 61:
        #         if (score_increase[-1] - score_increase[-61]) < 15:
        #             break

        score_list = []
        for schedule in schedules:
            score_schedule = score.calculate(schedule, courses)
            score_list.append(score_schedule)
        score_list.sort(reverse=True)




    elapsed_time = time.time() - start_time
    # plt.plot(update_times, score_increase)
    # print "random_hillclimber_"+str(desired_score)+"_"+str(int(elapsed_time))
    # plt.title("random_hillclimber; desired_score: " +str(desired_score) + ", elapsed_time: "+ str(int(elapsed_time)))
    # plt.savefig("random_hillclimber; desired_score: ")
    # plt.show()
    # print "\trandom_hillclimber; score: ", score_schedule, "elapsed time: ", int(elapsed_time / 60),"Min", int(elapsed_time % 60), "sec"
    #
    # print update_times
    # print score_increase

    return {"schedules" : schedules, "scores" : score_list, "elapsed_time" : elapsed_time}
