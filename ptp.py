import schedule_class
#import score

"""
Activiteiten, aantal vakken, max bonus, max malus
5: 2 - 40 - 80 (5-4 = 1 dus 4*10 = 40 minpunten per vak)
4: 6 - 120 - 180
3: 5 - 100 - 100
2: 10 - 200 - 100

Zaalsloten per dag: 4*7 = 28
Zaalsloten per week: 5*28 = 140
Totaal aantal activiteiten = 88 + 7 (vakken met 1 activiteit) = 95

Dag, max activiteiten bij optimaal (zaalgrootte niet meegerekend)
Ma - 23
Di - 18
Wo - 7
Do - 17
Vr - 23

Max bonus = 460
Max malus = 460

Dit algortime sorteert de lijst met vakken van veel activiteiten naar weinig activiteiten en plaatst ze een voor een op de meest gunstige dagen in het rooster.
Totale bonus-malus = 440

"""
def scores_random_schedules(schedule, courses, number_random_schedules):
    random_schedules_scores = []
    for i in range(number_random_schedules):
        random_schedule = copy.deepcopy(schedule)
        random_schedule = loader.random_fill_schedule(random_schedule, courses)
        random_schedule_score = score.calculate(random_schedule, courses)
        random_schedules_scores.append(random_schedule_score)
    srs = random_schedules_scores
    plt.plot(range(0,len(srs)),srs , "o")
    srs_average = sum(srs)/len(srs)
    srs_max = max(srs)
    plt.title(str(number_random_schedules) + " random schedules scores with an average score of " + str(srs_average) + " and a maximum value of " + str(srs_max))
    plt.show()
    return srs


def alg(students, courses, rooms):
    print 'Creating schedule..'
    schedule = schedule_class.Schedule(rooms)
    sortedcourses = sorted(courses, key=lambda course: course.activities)
    sortedcourses.reverse()

    # Fill schedule with all possible courses
    # Not checking max_students
    for course in sortedcourses:
        print course.name

        if course.activities is 5:
            try:
                path = schedule.find_empty(len(course.student_list), 'monday')
                schedule.add({'day': path['day'], 'room': path['room'], 'time': path['time']}, course)
                path = schedule.find_empty(len(course.student_list), 'tuesday')
                schedule.add({'day': path['day'], 'room': path['room'], 'time': path['time']}, course)
                path = schedule.find_empty(len(course.student_list), 'wednesday')
                schedule.add({'day': path['day'], 'room': path['room'], 'time': path['time']}, course)
                path = schedule.find_empty(len(course.student_list), 'thursday')
                schedule.add({'day': path['day'], 'room': path['room'], 'time': path['time']}, course)
                path = schedule.find_empty(len(course.student_list), 'friday')
                schedule.add({'day': path['day'], 'room': path['room'], 'time': path['time']}, course)
            except IOError:
                print "not 5"

        elif course.activities is 4:
            try:
                path = schedule.find_empty(len(course.student_list), 'monday')
                schedule.add({'day': path['day'], 'room': path['room'], 'time': path['time']}, course)
                path = schedule.find_empty(len(course.student_list), 'tuesday')
                schedule.add({'day': path['day'], 'room': path['room'], 'time': path['time']}, course)
                path = schedule.find_empty(len(course.student_list), 'thursday')
                schedule.add({'day': path['day'], 'room': path['room'], 'time': path['time']}, course)
                path = schedule.find_empty(len(course.student_list), 'friday')
                schedule.add({'day': path['day'], 'room': path['room'], 'time': path['time']}, course)
            except IOError:
                print "not 4"

        elif course.activities is 3:
            path = schedule.find_empty(len(course.student_list), 'monday')
            if (path):
                schedule.add({'day': path['day'], 'room': path['room'], 'time': path['time']}, course)
                path = schedule.find_empty(len(course.student_list), 'wednesday')
                if(path):
                    schedule.add({'day': path['day'], 'room': path['room'], 'time': path['time']}, course)
                    path = schedule.find_empty(len(course.student_list), 'friday')
                    if(path):
                        schedule.add({'day': path['day'], 'room': path['room'], 'time': path['time']}, course)
            else:
                print "no 3"

        elif course.activities is 2:
            pathmo = schedule.find_empty(len(course.student_list), 'monday')
            pathtu = schedule.find_empty(len(course.student_list), 'tuesday')
            pathwe = schedule.find_empty(len(course.student_list), 'wednesday')
            pathth = schedule.find_empty(len(course.student_list), 'thursday')
            pathfr = schedule.find_empty(len(course.student_list), 'friday')

            if (pathtu and pathfr):
                schedule.add({'day': pathtu['day'], 'room': pathtu['room'], 'time': pathtu['time']}, course)
                schedule.add({'day': pathfr['day'], 'room': pathfr['room'], 'time': pathfr['time']}, course)
                print "bonus 20"
            elif(pathmo and pathth):
                schedule.add({'day': pathmo['day'], 'room': pathmo['room'], 'time': pathmo['time']}, course)
                schedule.add({'day': pathth['day'], 'room': pathth['room'], 'time': pathth['time']}, course)
                print "bonus 20"
            elif(pathmo and pathwe):
                schedule.add({'day': pathmo['day'], 'room': pathmo['room'], 'time': pathmo['time']}, course)
                schedule.add({'day': pathwe['day'], 'room': pathwe['room'], 'time': pathwe['time']}, course)
            elif(pathwe and pathfr):
                schedule.add({'day': pathwe['day'], 'room': pathwe['room'], 'time': pathwe['time']}, course)
                schedule.add({'day': pathfr['day'], 'room': pathfr['room'], 'time': pathfr['time']}, course)
            elif(pathtu and pathth):
                schedule.add({'day': pathtu['day'], 'room': pathtu['room'], 'time': pathtu['time']}, course)
                schedule.add({'day': pathth['day'], 'room': pathth['room'], 'time': pathth['time']}, course)
            elif(pathmo and pathfr):
                schedule.add({'day': pathmo['day'], 'room': pathmo['room'], 'time': pathmo['time']}, course)
                schedule.add({'day': pathfr['day'], 'room': pathfr['room'], 'time': pathfr['time']}, course)
            elif(pathwe and pathth):
                schedule.add({'day': pathwe['day'], 'room': pathwe['room'], 'time': pathwe['time']}, course)
                schedule.add({'day': pathth['day'], 'room': pathth['room'], 'time': pathth['time']}, course)
            elif(pathwe and pathtu):
                schedule.add({'day': pathwe['day'], 'room': pathwe['room'], 'time': pathwe['time']}, course)
                schedule.add({'day': pathtu['day'], 'room': pathtu['room'], 'time': pathtu['time']}, course)
            elif(pathth and pathfr):
                schedule.add({'day': pathth['day'], 'room': pathth['room'], 'time': pathth['time']}, course)
                schedule.add({'day': pathfr['day'], 'room': pathfr['room'], 'time': pathfr['time']}, course)
            elif(pathmo and pathtu):
                schedule.add({'day': pathmo['day'], 'room': pathmo['room'], 'time': pathmo['time']}, course)
                schedule.add({'day': pathtu['day'], 'room': pathtu['room'], 'time': pathtu['time']}, course)
            else:
                print "no room found"

    schedule.write_csv()






    # Get score for the Schedule
    #score.calculate(schedule)

    # Swap course X with course Y (indicated by path)
    # schedule.swap({'day': 'friday', 'room': 'B0.201', 'time': '11h'}, {'day': 'wednesday', 'room': 'B0.201', 'time': '9h'})

# Integrate point system or seperate that too?
def find_conflict(schedule):
    # TODO
    none = None
