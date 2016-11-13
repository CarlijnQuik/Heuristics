class Schedule(object):
    def __init__(self, room_list):
        self.week = {}

        # empty formats
        days = ('monday', 'tuesday', 'wednesday', 'thursday', 'friday')
        layout_times = {'9h': {}, '11h': {}, '13h': {}, '15h': {}, '17h': {}}

        for day in days:
            empty_day = {}

            for room in room_list:
                empty_day[room] = layout_times.copy()

            self.week[day] = empty_day

    def add(self):
        # TODO

    def swap(self, course1, course2):
        # TODO


#
#   To be deleted/used in this class
#

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