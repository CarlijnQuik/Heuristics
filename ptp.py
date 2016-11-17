import schedule_class
import score

TYPE_LECTURE = 'lecture'
TYPE_SEMINAR = 'seminar'
TYPE_PRACTICUM = 'practicum'

def alg(students, courses, rooms, schedule):

    find_empty(schedule)
    for course in courses:

        for i in range(int(course.q_lecture)):
            schedule[find_empty(schedule)].add(course, TYPE_LECTURE)

        for i in range(int(course.q_seminar)):
            schedule[find_empty(schedule)].add(course, TYPE_SEMINAR)

        for i in range(int(course.q_practicum)):
            schedule[find_empty(schedule)].add(course, TYPE_PRACTICUM)

    # Get score for the Schedule
    score.calculate(schedule, courses)

# TODO: Add find empty for specific day/room/time (?)
def find_empty(schedule, max_size = 0):
    for i, roomslot in enumerate(schedule):
        if roomslot.course is None and roomslot.type is None:
            return i