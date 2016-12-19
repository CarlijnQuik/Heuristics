VALID_SCHEDULE = 1000
INVALID_SCHEDULE = 0

from collections import Counter

def calculate(schedule, courses):
    print "Calculating score.."
    score = 0

    # Bonus:
    #   Valid schedule (all courses in schedule)
    #   Spread roster (+20 per course)
    #       Get count of how many practicums, lectures and seminars
    #       If count = 2, check if day difference => 3 (monday-thursday, tue-fri)
    #       If count = 3, mo, wed, fri
    #       If count = 4, mo, tue, thurs, fri

    # Malus:
    #   TODO: Check if C0.110 1700 is used for Malus
    #   Twice on a day
    #
    #   Do not fit
    #       -1 for every student that does not fit in.
    #   Multiple activities
    #       -1 for every student that has more than one activity per time slot

    # Bonus
    score += check_valid_schedule(schedule, courses)
    score += check_spreading(schedule, courses)

    # Minus
    score -= check_small_room(schedule)[1]
    score -= check_day_duplicate(schedule)[1]
    score -= check_multiple_activities(schedule)[1]
    score -= check_special_timeslot(schedule)[1]

    # Print conflict list indexes of check_small_room.
    # print check_small_room(schedule)[0]

    print '\n', 'SCORE: {:04d}'.format(score), '\n\n'

    return score


#
#   Check if all course lessons are in the schedule
#   DONE
#
def check_valid_schedule(schedule, courses):
    count = 0
    total = 0

    for course in courses:
        total += course.q_total

    for i, roomslot in enumerate(schedule):
        if roomslot.activity:
            if roomslot.activity.course in courses:
                count += 1

    if total == count:
        #print "\tValid schedule!"
        return VALID_SCHEDULE
    else:
        #print "\tInvalid schedule!"
        return INVALID_SCHEDULE

#
#   Checks the 'special' timeslot C0.110 @ 1700
#   DONE
#
def check_special_timeslot(schedule):
    score = 0
    conflict_list = []

    for i, roomslot in enumerate(schedule):
        if roomslot.room.name == "C0.110":
            if roomslot.time == "1700":
                if roomslot.activity:
                    if roomslot.activity.course:
                        conflict_list.append(i)
                        score += 50

    return conflict_list, score


#
#   Checks the spreading across the week for every course
#   TODO: DEBUG
#
def check_spreading(schedule, courses):

    SPREADING_1 = ["monday", "thursday"]
    SPREADING_2 = ["tuesday", "friday"]

    SPREADING_3 = ["monday", "wednesday", "friday"]
    SPREADING_4 = ["monday", "tuesday", "thursday", "friday"]

    score = 0
    course_spreadings = {}

    for i, roomslot in enumerate(schedule):
        if roomslot.activity:
            if roomslot.activity.group:
                key = roomslot.activity.course.name + roomslot.activity.group
            else:
                key = roomslot.activity.course.name

            if key in course_spreadings.keys():
                # KEY EXISTS!
                course_spreadings[key].append(roomslot.day)
            else:
                # KEY DOES NOT EXIST!
                course_spreadings[key] = [roomslot.day]

    for course in courses:
        if len(course.groups) > 0:
            for group in course.groups:
                key = course.name + group
                if course.q_total == 2:
                    if course_spreadings[key] == SPREADING_1 or course_spreadings[key] == SPREADING_2:
                        # SPREADING IS OKAY
                        score += (20 / len(course.groups))

                elif course.q_total == 3:
                    if course_spreadings[key] == SPREADING_3:
                        score += (20 / len(course.groups))
                        # SPREADING IS OKAY

                elif course.q_total == 4:
                    if course_spreadings[key] == SPREADING_4:
                        score += (20 / len(course.groups))
                        # SPREADING IS OKAY

        else:
            key = course.name
            if course.q_total == 2:
                if course_spreadings[key] == SPREADING_1 or course_spreadings[key] == SPREADING_2:
                    # SPREADING IS OKAY
                    score += 20

            elif course.q_total == 3:
                if course_spreadings[key] == SPREADING_3:
                    score += 20
                    # SPREADING IS OKAY

            elif course.q_total == 4:
                if course_spreadings[key] == SPREADING_4:
                    score += 20
                    # SPREADING IS OKAY

    return score


#
#   Check for too many students in a room
#   Check if it also does not exceeds practicum_max for example
#
def check_small_room(schedule):
    score = 0
    conflict_list = []

    for i, roomslot in enumerate(schedule):
        if roomslot.activity:
            if roomslot.activity.course:
                if roomslot.room.capacity < len(roomslot.activity.course.student_list):

                    conflict_list.append(i)
                    score += len(roomslot.activity.course.student_list) - roomslot.room.capacity

    # print "\tFound", score, "exceeding(s) of room capacity!"
    return conflict_list, score



#
# Check if and how many of the same course are given on day x
# TODO: DEBUG
#
def check_day_duplicate(schedule):
    conflict_list = []

    day_activity_list = {}
    dup = 0
    # Go over all roomslots
    for i, roomslot in enumerate(schedule):
        if roomslot.day in day_activity_list.keys():
            # Day has entry
            day_activity_list[roomslot.day].append(roomslot.activity)
        else:
            # Day no entry
            day_activity_list[roomslot.day] = [roomslot.activity]

    if len(day_activity_list) != len(set(day_activity_list)):
        for day_activity in set(day_activity_list):
            print day_activity.course
            for other_day in day_activity_list:
                if (day_activity != other_day):
                    if (day_activity.type != other_day.type) and (day_activity.course.name == other_day.course.name) and not (day_activity.type == other_day.type):
                        # Not same type but same course.
                        dup += 1
                        conflict_list.append(day_activity)


    score = dup * 10


    # print "\tFound", len(conflict_list), "day duplicates!"
    return conflict_list, score

#
# Check for hour conflicts per student in the schedule
# TODO: DEBUG
#
def check_multiple_activities(schedule):
    conflict_list = []
    daytime_activity_list = {}

    for i, roomslot in enumerate(schedule):
        if roomslot.activity:
            key = roomslot.day + roomslot.time
            if key in daytime_activity_list.keys():
                # Day has entry
                print "Has entry:" + key
                daytime_activity_list[key].append(roomslot.activity)
            else:
                # Day no entry
                print "New entry:" + key
                daytime_activity_list[key] = [roomslot.activity]

    for daytime in daytime_activity_list:

        for activity in daytime_activity_list[daytime]:
            if activity.students:
                print [activity for student, v in Counter(activity.students).iteritems() if v > 1]
                conflict_list.append(activity for student, v in Counter(activity.students).iteritems() if v > 1)

    return conflict_list, len(conflict_list)


