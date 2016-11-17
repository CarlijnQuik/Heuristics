import csv

class Schedule(object):
    days = ('monday', 'tuesday', 'wednesday', 'thursday', 'friday')
    times = {'9h': {}, '11h': {}, '13h': {}, '15h': {}}

    def __init__(self, room_list):
        self.rooms = room_list
        self.week = {}

        # empty formats
        for day in self.days:
            empty_day = {}

            for room in room_list:
                empty_day[room] = self.times.copy()
                if room == 'C0.110':
                    empty_day[room]['17h'] = {}

            self.week[day] = empty_day


    def add(self, path, course, group = None):
        # type: (object, object, object) -> object
        # TODO
        # Course Object.
        # Location path

        # TODO
        # WORKS??
        if len(path) is not 3:
            print "Invalid path!"
            return False

        # Check if same room not already taken
        if not self.week[path['day']][path['room']][path['time']]:

            self.week[path['day']][path['room']][path['time']] = {'course': course, 'group': group}

            print "\t", course.name, "added to", path['day'], path['room'], path['time']
            return True

        print "Room", path[1], "is already taken."
        return False

    def swap(self, path_one, path_two):
        # TODO
        # Object, path and types


        try:
            placeHolder = self.week[path_one['day']][path_one['room']][path_one['time']]
            self.week[path_one['day']][path_one['room']][path_one['time']] = self.week[path_two['day']][path_two['room']][path_two['time']]
            self.week[path_two['day']][path_two['room']][path_two['time']] = placeHolder
        except:
            print 'Could not swap', path_one, 'and', path_two

    def find_empty(self, size = 0, day = days[0]):
        for room in self.week[day]:
            for time in self.week[day][room]:
                if not self.week[day][room][time]:

                    # Only check if all people fit. Not smaller groups etc.
                    if size is not 0 and int(size) <= int(self.rooms[room].capacity):
                        return {'day': day, 'room': room, 'time': time}
                    elif size is 0:
                        return {'day': day, 'room': room, 'time': time}

        print 'No suitable room found!'
        return False

    def find_emptyrandom(self, size=0):
        for day in self.week:
            for room in self.week[day]:
                for time in self.week[day][room]:
                    if not self.week[day][room][time]:

                        # Only check if all people fit. Not smaller groups etc.
                        if size is not 0 and int(size) <= int(self.rooms[room].capacity):
                            return {'day': day, 'room': room, 'time': time}
                        elif size is 0:
                            return {'day': day, 'room': room, 'time': time}

        print 'No suitable room found!'

    # Write schedule to a readable CSV file format
    def write_csv(self):
        with open("output_files/schedule2.csv", "wb+") as csvfile:
            cursor = csv.writer(csvfile)
            for day in self.week:
                for room in self.week[day]:
                    for time in self.week[day][room]:
                        if self.week[day][room][time]:
                            course_name = self.week[day][room][time]['course'].name
                            course_type = self.week[day][room][time]

                            cursor.writerow([day, room, time, course_name])
            print "Output file generated!"