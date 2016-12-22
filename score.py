VALID_SCHEDULE = 1000
INVALID_SCHEDULE = 0

from collections import Counter


"""

    Calculate the score of the input schedule.
        This function calls all calculator parts and returns the final score.

"""
def calculate(schedule, courses):
    score = 0

    # Bonus.
    score += check_valid_schedule(schedule, courses)
    score += check_spreading(schedule, courses)

    # Malus.
    score -= check_small_room(schedule)[1]
    score -= check_day_duplicate(schedule)[1]
    score -= check_multiple_activities(schedule)[1]
    score -= check_special_timeslot(schedule)[1]

    return score


"""

    Check if all activities are in the schedule.

"""
def check_valid_schedule(schedule, courses):
    count = 0
    total = 0

    # Groups have more timeslots filled.
    for course in courses:       
        if len(course.groups) > 0:
            total += course.q_practicum * len(course.groups)
            total += course.q_seminar * len(course.groups)
            total += course.q_lecture
        else:
            total += course.q_total

    # Check amount of activities in schedule.
    for i, roomslot in enumerate(schedule):
        if roomslot.activity:
            count += 1

    if total == count:
        return VALID_SCHEDULE
    else:
        return INVALID_SCHEDULE

    
"""

    Checks the special timeslot C0.110 @ 1700.

"""
def check_special_timeslot(schedule):
    score = 0
    conflict_list = []

    for i, roomslot in enumerate(schedule):
        if roomslot.room.name == "C0.110":
            if roomslot.time == "1700":
                if roomslot.activity:
                    if roomslot.activity.course:
                        
                        # Room is used.
                        conflict_list.append(i)
                        score += 50

    return conflict_list, score


"""

    Check the spreading across the week for every course and groups.

"""
def check_spreading(schedule, courses):

    # Hardcoded spreadings.
    SPREADING_1 = ["monday", "thursday"]
    SPREADING_2 = ["tuesday", "friday"]

    SPREADING_3 = ["monday", "wednesday", "friday"]
    SPREADING_4 = ["monday", "tuesday", "thursday", "friday"]

    score = 0
    course_spreadings = {}

    # Generate a dictionary for every course group.
    for i, roomslot in enumerate(schedule):
        if roomslot.activity:

            # Add activity to correct key/hash if it has a group.
            if roomslot.activity.group is not "":
                key = roomslot.activity.course.name + roomslot.activity.group
                if key in course_spreadings.keys():
                    course_spreadings[key].append(roomslot.day)
                else:
                    course_spreadings[key] = [roomslot.day]
                    
            # Add lectures to all groups within the course.        
            else:                
                if len(roomslot.activity.course.groups) > 0:
                    for group in roomslot.activity.course.groups:
                        key = roomslot.activity.course.name + group

                        if key in course_spreadings.keys():
                            course_spreadings[key].append(roomslot.day)
                        else:
                            course_spreadings[key] = [roomslot.day]
                            
                # Course only has lectures.
                else:
                    key = roomslot.activity.course.name

                    if key in course_spreadings.keys():
                        course_spreadings[key].append(roomslot.day)
                    else:
                        course_spreadings[key] = [roomslot.day]

    # Go over the list generated above.
    for course in courses:
        if len(course.groups) > 0:

            # Check spreading for every course group.
            for group in course.groups:
                key = course.name + group
                
                # Spreading depends on total lessons.
                if course.q_total == 2:
                    if course_spreadings[key] == SPREADING_1 or course_spreadings[key] == SPREADING_2:               
                        score += (20 / len(course.groups))
                        # Spreading is okay.

                elif course.q_total == 3:
                    if course_spreadings[key] == SPREADING_3:
                        score += (20 / len(course.groups))
                        # Spreading is okay.


                elif course.q_total == 4:
                    if course_spreadings[key] == SPREADING_4:
                        score += (20 / len(course.groups))
                        # Spreading is okay.

        else:
            key = course.name
            if course.q_total == 2:
                if course_spreadings[key] == SPREADING_1 or course_spreadings[key] == SPREADING_2:
                    score += 20
                    # Spreading is okay.

            elif course.q_total == 3:
                if course_spreadings[key] == SPREADING_3:
                    score += 20
                    # Spreading is okay.

            elif course.q_total == 4:
                if course_spreadings[key] == SPREADING_4:
                    score += 20
                    # Spreading is okay.

    return score


"""

    Check for overpupulation of a room.

"""
def check_small_room(schedule):
    score = 0
    conflict_list = []

    for i, roomslot in enumerate(schedule):
        if roomslot.activity:
            if roomslot.activity.course:
                if roomslot.room.capacity < len(roomslot.activity.course.student_list):
                    
                    # Too many students in the room.
                    conflict_list.append(i)
                    score += len(roomslot.activity.course.student_list) - roomslot.room.capacity

    return conflict_list, score


"""

    Check if a course is planned twice on the same day.
        This excludes courses of the same type, they can not be duplicate.

"""
def check_day_duplicate(schedule):
    conflict_list = []

    day_activity_list = {}
    
    # Go over all roomslots.
    for i, roomslot in enumerate(schedule):
        if roomslot.activity:

            # Filter for groups.
            if roomslot.activity.group is not "":
                
                 # Hash key exists.
                if roomslot.day in day_activity_list.keys():                  
                    day_activity_list[roomslot.day].append({"key": str(roomslot.activity.course) + roomslot.activity.group, "index": i})
                
                # Hash key does not exist.
                else:                    
                    day_activity_list[roomslot.day] = [{"key": str(roomslot.activity.course) + roomslot.activity.group, "index": i}]
            elif len(roomslot.activity.course.groups):
                for group in roomslot.activity.course.groups:
                    
                    # Hash key exists.
                    if roomslot.day in day_activity_list.keys():                      
                        day_activity_list[roomslot.day].append({"key": str(roomslot.activity.course) + group, "index": i})
                        
                    # Hash key does not exist.
                    else:                        
                        day_activity_list[roomslot.day] = [{"key": str(roomslot.activity.course) + group, "index": i}]
            else:
                
                # Hash key exists.
                if roomslot.day in day_activity_list.keys():                   
                    day_activity_list[roomslot.day].append({"key": str(roomslot.activity.course), "index": i})
                    
                # Hash key does not exist.    
                else:                    
                    day_activity_list[roomslot.day] = [{"key": str(roomslot.activity.course), "index": i}]

    # Go over generated day_activity_list to find doubles.
    for i in day_activity_list:
        day_activities = day_activity_list[i]

        key_list = []
        for item in day_activities:
            if item['key'] in key_list:
                
                # Key is duplicate, so is the course.
                conflict_list.append(item['index'])
            else:
                key_list.append(item['key'])


    return conflict_list, len(conflict_list)


"""

    Check for hour conflicts per student in the schedule.

"""
def check_multiple_activities(schedule):
    conflict_list = []
    daytime_activity_list = {}

    # Create lists using day and time as hash.
    for i, roomslot in enumerate(schedule):
        if roomslot.activity:
            key = roomslot.day + roomslot.time
            
            # Day has entry.
            if key in daytime_activity_list.keys():                
                daytime_activity_list[key].append({"activity": roomslot.activity, "index": i})
                
            # Day no entry.   
            else:              
                daytime_activity_list[key] = [{"activity": roomslot.activity, "index": i}]

    # For every daytime list.
    for daytime in daytime_activity_list:        
        student_list = []

        # Per dictionary.
        for item in daytime_activity_list[daytime]:            
            for student in item['activity'].students:
                
                 # Student has double.
                if student in student_list:                  
                    conflict_list.append(item['index'])
                else:
                    student_list.append(student)

    return conflict_list, len(conflict_list)
