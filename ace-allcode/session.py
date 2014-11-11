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
        self.image_list = list()
        self.log_err_list = list()
        for i in range(15):
            self.log_err_list.append(0)
        self.total_estimates = 0
        
    def isComplete(self):
        if len(self.estimate_list) > 9:
            return True
        else:
            return False
            
    def addEstimate(self, estimate):
        self.estimate_list.append(estimate)
        
        
    def addImage(self, image):
        self.image_list.append(image)

