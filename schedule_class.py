class Schedule(object):
    days = ('monday', 'tuesday', 'wednesday', 'thursday', 'friday')
    times = {'9h': {}, '11h': {}, '13h': {}, '15h': {}, '17h': {}}

    def __init__(self, room_list):
        self.rooms = []
        self.week = {}

        for room in room_list:
            self.rooms.append(room)

        # empty formats
        for day in self.days:
            empty_day = {}

            for room in room_list:
                empty_day[room] = self.times.copy()

            self.week[day] = empty_day

    def add(self, path, course, type):
        # TODO
        # Course Object.
        # Location path

        # Check if same room not already taken
        if not self.week[path[0]][path[1]][path[2]]:

            self.week[path[0]][path[1]][path[2]] = {course.name: course, 'type': type}
            print course.name, "added to", path[0], path[1], path[2]
            return True

        print "Room", path[1], "is already taken."
        return False



    def swap(self, path_one, path_two):
        # TODO
        # Object, path and types
        none = None

    def find_empty(self):
        # TODO

        for day in self.days:
            for room in self.rooms:
                for time in self.times:
                    if not self.week[day][room][time]:
                        return [day, room, time]
