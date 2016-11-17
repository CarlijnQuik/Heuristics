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

    print score
    return score

def check_valid_schedule(schedule, courses):
    # TODO

    return 0


def check_multiple_activities(schedule):
    sort_by_time = {}
    conflict_list = {}

    for timeslot in enumerate(schedule):
        print timeslot

    return 0
