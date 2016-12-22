import csv


"""
    
   Object representing a roomslot.
    
"""
class Roomslot(object):
    def __init__(self, room, day, time):
        self.room = room
        self.day = day
        self.time = time

        self.activity = None

        
