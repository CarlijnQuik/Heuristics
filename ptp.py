import schedule_class
import score

TYPE_LECTURE = 'lecture'
TYPE_SEMINAR = 'seminar'
TYPE_PRACTICUM = 'practicum'

def alg(students, courses, rooms, schedule):

    find_empty(schedule)
    for course in courses:
        schedule[find_empty(schedule)].add(course, TYPE_LECTURE)


    # Get score for the Schedule
    score.calculate(schedule, courses)

# TODO: Add find empty for specific day/room/time (?)
def find_empty(schedule, max_size = 0):
    for i, object in enumerate(schedule):
        if object.course is None and object.type is None:
            return i