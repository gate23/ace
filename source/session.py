"""
session.py

Contains data structures for sessions and estimates.
Used by Trainer and Stats
"""
        
"""
Session:
    Stores useful data about a session that
    we save to file and use for displaying stats.
"""      
class Session():
    def __init__(self,length):
        self.length = length;
        
        self.error_sum = 0.0
        self.time = None #this is set once the session is completed
        self.estimate_list = list()
        self.image_list = list()
        self.log_err_list = list() 
        
        #The magic 15 below comes from the 15 log error values possible
        #given the 8 ranges we currently have to choose from (-7,-6,..,0,..7)
        for i in range(15):
            self.log_err_list.append(0)
        self.total_estimates = 0
        
    def isComplete(self):
        if len(self.estimate_list) > self.length-1:
            return True
        else:
            return False
            
    def addEstimate(self, estimate):
        self.estimate_list.append(estimate)
               
    def addImage(self, image):
        self.image_list.append(image)

"""
Estimate:
    This simple class is used by session, which keeps a list
    of all estimates in each session.
"""
class Estimate():
    def __init__(self,estimate,actual):
        self.estimate = estimate
        self.actual = actual