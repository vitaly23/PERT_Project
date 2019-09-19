'''
    Author:  Vitaly Gorelik
    ID:      316883529
'''

from Logging import MyLogger

class Activity(MyLogger):
    
    def __init__(self, name, duration=0):
        self.logger.debug("Initialize new activity with parameters: name=%s, duration=%r" % (name, duration))
        self._name = name
        self._duration = duration
        self._earlyStart = 0 
        self._earlyFinish = 0 
        self._latestStart = 0
        self._latestFinish = 1000000  # Error value 
        self._slackTime = 0
        
    @property
    def name(self):
        self.logger.debug("Return the activity name: %s" % self._name)
        return self._name
    
    @name.setter
    def name(self, name):
        self.logger.debug("Set the activity name from: %s to %s" % self._name, name)
        self._name = name
        
    @property
    def duration(self):
        self.logger.debug("Return the activity duration: %r" % self._duration)
        return self._duration
    
    @duration.setter
    def duration(self, duration):
        self.logger.debug("Set the activity duration from: %r to %r" % self._duration, duration)
        self._duration = duration
        
    @property
    def earlyStart(self):
        self.logger.debug("Return the activity early start: %r" % self._earlyStart)
        return self._earlyStart
    
    @earlyStart.setter
    def earlyStart(self, earlyStart):
        self.logger.debug("Set the activity early start from: %r to %r" % (self._earlyStart, earlyStart))
        self._earlyStart = earlyStart

    @property
    def earlyFinish(self):
        self.logger.debug("Return the activity early finish: %r" % self._earlyFinish)
        return self._earlyFinish
    
    @earlyFinish.setter
    def earlyFinish(self, earlyFinish):
        self.logger.debug("Set the activity early finish from: %r to %r" % (self._earlyFinish, earlyFinish))
        self._earlyFinish = earlyFinish
        
    @property
    def latestStart(self):
        self.logger.debug("Return the activity latest start: %r" % self._latestStart)
        return self._latestStart
    
    @latestStart.setter
    def latestStart(self, latestStart):
        self.logger.debug("Set the activity latest start from: %r to %r" % (self._latestStart, latestStart))
        self._latestStart = latestStart 

    @property
    def latestFinish(self):
        self.logger.debug("Return the activity latest finish: %r" % self._latestFinish)
        return self._latestFinish
    
    @latestFinish.setter
    def latestFinish(self, latestFinish):
        self.logger.debug("Set the activity latest finish from: %r to %r" % (self._latestFinish, latestFinish))
        self._latestFinish = latestFinish 
        
    @property
    def slackTime(self):
        self.logger.debug("Return the activity slack time: %r" % self._latestFinish)
        return self._slackTime
    
    @slackTime.setter
    def slackTime(self, slackTime):
        self.logger.debug("Set the activity slack time from: %r to %r" % (self._slackTime, slackTime))
        self._slackTime = slackTime
        
    def __repr__(self):
        self.logger.debug("Return the activity __repr__ function")
        return "[%s:%r]" % (self.name, self.duration)
    
    def __str__(self):
        self.logger.debug("Return the activity __str__ function")
        return "[%s:%r]" % (self.name, self.duration)
    
    def __eq__(self, other):
        self.logger.debug("Use the activity __eq__ function with the value %s" % str(other))
        return (self._name == other.name and self._duration == other.duration)
    
    def __nq__(self, other):
        self.logger.debug("Use the activity __nq__ function with the value %s" % str(other))
        return not (self == other)
    
    def __hash__(self):
        self.logger.debug("Return the activity __hash__ function")
        return id(self)
    
    '''
        Helper function to shoe in debug and other cases the activity in more details, 
        i.g: the name, the duration and the times: the early start, early finish, 
        latest start, latest finish and slack time.  
    '''
    def showActivityDetails(self):
        self.logger.debug("Return the activity showActivityDetails function")
        return "[%s:%r ES:%r EF:%r LS:%r LF:%r ST:%r]" % (self.name, self.duration, self.earlyStart,
            self.earlyFinish, self.latestStart, self.latestFinish, self.slackTime)    
