import schedule_class

TYPE_LECTURE = 'lecture'
TYPE_SEMINAR = 'seminar'
TYPE_PRACTICUM = 'practicum'

def alg(students, courses, rooms):
    print 'Creating schedule..'
    schedule = schedule_class.Schedule(rooms)

    # Fill schedule with all possible courses
    # Not checking max_students and room size
    for course in courses:
        print course.name
        for i in range(int(course.q_lecture)):
            path = schedule.find_empty(len(course.student_list))
            schedule.add([path['day'], path['room'], path['time']], course, TYPE_LECTURE)

        for i in range(int(course.q_seminar)):
            path = schedule.find_empty(len(course.student_list))
            schedule.add([path['day'], path['room'], path['time']], course, TYPE_SEMINAR)

        for i in range(int(course.q_practicum)):
            path = schedule.find_empty(len(course.student_list))
            schedule.add([path['day'], path['room'], path['time']], course, TYPE_PRACTICUM)

    schedule.write_csv()

    # Swap course X with course Y (indicated by path)
    # schedule.swap({'day': 'friday', 'room': 'B0.201', 'time': '11h'}, {'day': 'wednesday', 'room': 'B0.201', 'time': '9h'})

# Integrate point system or seperate that too?
def find_conflict(schedule):
    # TODO
    none = None