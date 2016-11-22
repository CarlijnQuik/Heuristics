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
    #   Twice on a day
    #
    #   Do not fit
    #       -1 for every student that does not fit in.
    #   Multiple activities
    #       -1 for every student that has more than one activity per time slot

    # Bonus
    score += check_valid_schedule(schedule, courses)

    # Minus
    score -= check_small_room(schedule)[1]
    score -= len(check_multiple_activities(schedule))
    score -= len(check_day_duplicate(schedule))

    # Print conflict list indexes of check_small_room.
    # print check_small_room(schedule)[0]

    print '\n', 'SCORE: {:04d}'.format(score), '\n\n'

    """

    #
    #   The code below can be uncommented to optimize the score function. This removes a few for loops and includes all score check functions code.
    #       Remember to also edit the block above AND below before this can be used.
    #


        # For every Roomslot, check all other roomslots
        for i, roomslot in enumerate(schedule):
            if roomslot.course:
                print i
                # Can optimize by starting this for loop from element I
                for j, roomslot2 in enumerate(schedule):

                    # Don't compare the same roomslot
                    if i is not j and roomslot2.course:
                        print "\t", j

                        if roomslot.time == roomslot2.time and roomslot.day == roomslot2.day:

                            # Go over studentlist to see if conflicts in this hour
                            for student_id in roomslot.course.student_list:
                                student = roomslot.course.student_list[student_id]
                                if student_id in roomslot2.course.student_list.keys():
                                    # Add to list if conflicted
                                    key = student_id + roomslot.day + roomslot.time
                                    conflict_list[key] = {student_id: student, 'course1': i, 'course2': j}




                        if not [roomslot.course.name, roomslot.day] in log:
                            if (roomslot.course.name == roomslot2.course.name) and (roomslot.day == roomslot2.day):
                                log.append([roomslot.course.name, roomslot.day])

                                key = roomslot.course.name + roomslot.day
                                conflict_list[key] = {'course': roomslot.course, 'day': roomslot.day}

                #
                #   Check small room inside existing for loop.
                #       Possibly faster in calculating score
                #
                if roomslot.course:
                    if roomslot.room.capacity < len(roomslot.course.student_list):
                        score += len(roomslot.course.student_list) - roomslot.room.capacity

        """



    return score


#
#   Check if all course lessons are in the schedule
#
def check_valid_schedule(schedule, courses):
    count = 0
    q_total = 0


    for course in courses:
        q_total += course.q_lecture
        q_total += course.q_seminar
        q_total += course.q_practicum

        for i, roomslot in enumerate(schedule):
            if course is roomslot.course:
                count += 1

    if q_total == count:
        print "\tValid schedule!"
        return VALID_SCHEDULE
    else:
        print "\tInvalid schedule!"
        return INVALID_SCHEDULE

#
#   Check for too many students in a room
#
def check_small_room(schedule):
    score = 0
    conflict_list = []

    for i, roomslot in enumerate(schedule):
        if roomslot.course:
            if roomslot.room.capacity < len(roomslot.course.student_list):

                conflict_list.append(i)
                score += len(roomslot.course.student_list) - roomslot.room.capacity

    print "\tFound", score, "exceeding(s) of room capacity!"
    return conflict_list, score


def check_day_duplicate(schedule):
    conflict_list = {}

    for i, roomslot in enumerate(schedule):
        log = []
        if roomslot.course:
            for j, roomslot2 in enumerate(schedule):
                if i is not j and roomslot2.course:
                    if not [roomslot.course.name, roomslot.day] in log:
                        if (roomslot.course.name == roomslot2.course.name) and (roomslot.day == roomslot2.day):
                            log.append([roomslot.course.name, roomslot.day])

                            key = roomslot.course.name + roomslot.day
                            conflict_list[key] = {'course': roomslot.course, 'day': roomslot.day}

    print "\tFound", len(conflict_list), "day duplicates!"
    return conflict_list

#
# Check for hour conflicts per student in the schedule
#
def check_multiple_activities(schedule):
    conflict_list = {}

    # For every Roomslot, check all other roomslots
    for i, roomslot in enumerate(schedule):
        if roomslot.course:
            # Can optimize by starting this for loop from element I
            for j, roomslot2 in enumerate(schedule):

                # Don't compare the same roomslot
                if i is not j and roomslot2.course:
                    if roomslot.time == roomslot2.time and roomslot.day == roomslot2.day:

                        # Go over studentlist to see if conflicts in this hour
                        for student_id in roomslot.course.student_list:
                            student = roomslot.course.student_list[student_id]
                            if student_id in roomslot2.course.student_list.keys():
                                # Add to list if conflicted
                                key = student_id + roomslot.day + roomslot.time
                                conflict_list[key] = {student_id: student, 'course1': i, 'course2': j}

    print "\tFound", len(conflict_list), "student conflicts!"
    return conflict_list