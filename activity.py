"""

Object representing an activity.

"""
class Activity(object):   
    def __init__(self, course, type):
        self.course = course
        self.type = type
        self.group = ""
        self.students = []
        
        
