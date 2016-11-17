import csv


class Roomslot(object):
    def __init__(self, room, day, time):
        self.room = room
        self.day = day
        self.time = time

        self.course = None
        self.type = None

    def add(self, course, type):
        self.course = course
        self.type = type