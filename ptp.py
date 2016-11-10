# Algo
def ptp(student_list, course_list, room_list, schedule):
    # TODO
    # for course in course_list:
        add_course(course_list[5], schedule)

# Swap two courses
def swap_course():
    # TODO
    none = None

# Add a course to an empty schedule spot
def add_course(course, schedule):
    # TODO
    empty = find_empty(schedule)
    if empty is not None:
        print 'NOT EMPTY!'


# Remove course X from the schedule
def remove_course():
    # TODO
    none = None

# Find empty spot in schedule
def find_empty(schedule):
    for day in schedule:
        print day
        for room in schedule[day]:
            print room
            for time in schedule[day][room]:
                print time
                for course in schedule[day][room][time]:
                    print course
                    if course is None:
                        return {'day': day, 'room': room, 'time': time}
    return None