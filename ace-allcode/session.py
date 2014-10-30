"""
session.py

Contains data structures for sessions and estimates.
Used by Trainer and Stats
"""

class Estimate():
    def __init__(self,estimate,actual):
        self.estimate = estimate
        self.actual = actual
        
        
class Session():
    def __init__(self):
        self.error_sum = 0.0
        self.time = None
        self.estimate_list = list()
        
    def isComplete(self):
        if len(self.estimate_list) > 9:
            return True
        else:
            return False
            
    def addEstimate(self, estimate):
        self.estimate_list.append(estimate)

