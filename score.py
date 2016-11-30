VALID_SCHEDULE = 1000
INVALID_SCHEDULE = 0

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
#   CORRECT
#
def check_valid_schedule(schedule, courses):
    count = 0
    q_total = 0


    for course in courses:
        q_total += course.q_lecture
        q_total += course.q_seminar
        q_total += course.q_practicum

        for i, roomslot in enumerate(schedule):
            if roomslot.activity:
                if course is roomslot.activity.course:
                    count += 1

    if q_total == count:
        #print "\tValid schedule!"
        return VALID_SCHEDULE
    else:
        #print "\tInvalid schedule!"
        return INVALID_SCHEDULE

#
# Checks the 'special' timeslot C0.110 @ 1700
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


# TODO: Finish this function
def check_spreading(schedule, courses):
    score = 0

    for course in courses:
        q_total = course.q_lecture
        q_total += course.q_seminar
        q_total += course.q_practicum

        index_list = []

        for i, roomslot in enumerate(schedule):
            if roomslot.activity:
                if roomslot.activity.course:
                    if (course.name == roomslot.activity.course.name):
                        index_list.append(i)

    return 0


#
#   Check for too many students in a room
#   Check if it also does not exceeds practicum_max for example
#
def check_small_room(schedule):
    score = 0
    conflict_list = []

VALID_SCHEDULE = 1000
INVALID_SCHEDULE = 0

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
#   CORRECT
#
def check_valid_schedule(schedule, courses):
    count = 0
    q_total = 0


    for course in courses:
        q_total += course.q_lecture
        q_total += course.q_seminar
        q_total += course.q_practicum

        for i, roomslot in enumerate(schedule):
            if roomslot.activity:
                if course is roomslot.activity.course:
                    count += 1

    if q_total == count:
        #print "\tValid schedule!"
        return VALID_SCHEDULE
    else:
        #print "\tInvalid schedule!"
        return INVALID_SCHEDULE

#
# Checks the 'special' timeslot C0.110 @ 1700
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


# TODO: Finish this function
def check_spreading(schedule, courses):
    score = 0

    for course in courses:
        q_total = course.q_lecture
        q_total += course.q_seminar
        q_total += course.q_practicum

        index_list = []

        for i, roomslot in enumerate(schedule):
            if roomslot.activity:
                if roomslot.activity.course:
                    if (course.name == roomslot.activity.course.name):
                        index_list.append(i)

    return 0


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
# TODO: Get relevant info first
#
def check_day_duplicate(schedule):
    conflict_list = {}
    score = 0

    # Go over all roomslots
    # TODO: Filter on day, don't go through schedule second time.
    for i, roomslot in enumerate(schedule):
        duplicate_count = 0

        if roomslot.activity:
            if roomslot.activity.course:

                q_total = roomslot.activity.course.q_lecture + roomslot.activity.course.q_practicum + roomslot.activity.course.q_seminar

                # Go over all other roomslots for that one roomslot
                for j, roomslot2 in enumerate(schedule):
                    # If not the same course or empty course
                    if i is not j and roomslot2.activity:

                            # If name and day are the same, duplicate!
                            # Does this twice. First for loop will go over the second course later on too.
                            if roomslot2.activity.course:
                                if (roomslot.activity.course.name == roomslot2.activity.course.name) and (roomslot.day == roomslot2.day):

                                    key = roomslot.activity.course.name + roomslot.day

                                    if key in conflict_list.keys():
                                        duplicate_count += 1
                                        if j not in conflict_list[key]:
                                            conflict_list[key].append(j)
                                    else:
                                        conflict_list[key] = [i, j]

    for key in conflict_list:
        score += (len(conflict_list[key]) - 1) * 10



    # print "\tFound", len(conflict_list), "day duplicates!"
    return conflict_list, score

#
# Check for hour conflicts per student in the schedule
# CORRECT
#
def check_multiple_activities(schedule):
    conflict_list = {}
    student_conflict_count_list = []

    # For every Roomslot, check all other roomslots
    for i, roomslot in enumerate(schedule):
        if roomslot.activity:
            if roomslot.activity.course:
                student_conflict_count = 0

                # Can optimize by starting this for loop from element I
                for j, roomslot2 in enumerate(schedule):

                    # Don't compare the same roomslot
                    if i is not j and roomslot2.activity.course:
                        if roomslot.time == roomslot2.time and roomslot.day == roomslot2.day:

                            # Go over studentlist to see if conflicts in this hour
                            for student_id in roomslot.activity.course.student_list:
                                student = roomslot.activity.course.student_list[student_id]
                                if student_id in roomslot2.activity.course.student_list.keys():

                                    student_conflict_count += 1
                                    # Add to list if conflicted
                                    key = student_id + roomslot.day + roomslot.time
                                    conflict_list[key] = {student_id: student, 'course1': i, 'course2': j}

                student_conflict_count_list.append(student_conflict_count);

    # print "\tFound", len(conflict_list), "student conflicts!"
    return conflict_list, len(conflict_list), student_conflict_count_list

def get_day_distance(index_list):
    holder = None
    week = ('monday', 'tuesday', 'wednesday', 'thursday', 'friday')


