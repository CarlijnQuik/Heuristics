VALID_SCORE = 1000

def calculate(schedule, courses):
    score = 0
    # TODO

    # Bonus:
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
    score -= len(check_multiple_activities(schedule))

    print '{:04d}'.format(score)
    return score

def check_valid_schedule(schedule, courses):
    print "Checking for valid schedule.."
    count = 0
    q_lectures = 0
    q_seminar = 0
    q_practicum = 0


    for course in courses:
        q_lectures += course.q_lecture
        q_seminar += course.q_seminar
        q_practicum += course.q_practicum

        for i, roomslot in enumerate(schedule):
            if course is roomslot.course:
                print "\tFound ", roomslot.course.name, roomslot.type
                count += 1

    if (q_lectures + q_seminar + q_practicum) == count:
        return 1000
    else:
        print "Invalid schedule!"
        return 0

#
# Check for hour conflicts per student in the schedule
def check_multiple_activities(schedule):
    conflict_list = {}

    # For every Roomslot, check all other roomslots
    for i, roomslot in enumerate(schedule):
        for k, roomslot2 in enumerate(schedule):

            # Don't compare the same roomslot
            if i is not k and roomslot.course and roomslot2.course:
                if roomslot.time == roomslot2.time and roomslot.day == roomslot2.day:

                    # Go over studentlist to see if conflicts in this hour
                    for student_id in roomslot.course.student_list:
                        student = roomslot.course.student_list[student_id]
                        if student_id in roomslot2.course.student_list.keys():
                            # Add to list if conflicted
                            conflict_list[student_id] = {student_id: student, 'course1': i, 'course2': k}

    return conflict_list