'''
     Author:  Vitaly Gorelik
     ID:      316883529
'''

from Activity import Activity
from Logging import MyLogger
   
class CPM_Network(MyLogger):
    
    '''
    (Question 1)
        Initialize the project from given python dictionary or create empty dictionary.
    '''
    def __init__(self, dictGraph=None):
        self.logger.debug("Initialize new CPM network with dictionary:%s" % dictGraph)
        
        if dictGraph == None:
            dictGraph = dict()
        
        self._dictGraph = dictGraph
        self._criticalPathDuration = -1  # Error initialization
        self._criticalPath = []  # Error initialization
        self._isolatedActivities = []  # Error initialization
    
    '''
    (Question 9)
        Property for the CPM network that retrieve the project duration. 
        The entire duration of the project based of the duration of the critical path.
    '''
    @property
    def duration(self):
        self.logger.debug("Return the CPM network duration")
        return self.__criticalPathDuration()

    '''
    (Question 2)
        Add activity to the project: get activity and the if following activities 
        as list of activities.
        Each activity contain at least name and duration.  
        After calculate the project duration and critical path.
    '''
    def addActivity(self, activityToAdd, followActivities=[]):
        self.logger.debug("Add new activity: %s with the following activities: %s" % (activityToAdd, followActivities))
        
        if activityToAdd not in self._dictGraph:
            self._dictGraph[activityToAdd] = followActivities
        
        # update the project critical path:
        self.criticalPath()
        
    '''
    (Question 3)
        Remove activity from the project and all the instance of it as following activity.
    '''
    def removeActivity(self, activityToRemove):
        self.logger.debug("Remove activity: %s from the project" % activityToRemove)
        
        self._dictGraph.pop(activityToRemove)
        
        for theActivity in self._dictGraph:
            
            i = 0
            numOfFollow = len(self._dictGraph[theActivity])
            
            while(i < numOfFollow):
                # If the follow activity is the activity to be remove:
                if(self._dictGraph[theActivity][i] == activityToRemove):
                    del self._dictGraph[theActivity][i]
                    # Update the number of the following activities:
                    numOfFollow = len(self.dictGraph[theActivity])
                else:
                    i += 1
        
        # update the project critical path:
        self.criticalPath()
    
    '''
    (Question 4)
        Interface the the method '__displayCircles'.
        This function helps to validate the project and find circle's activities
        in the project and display them.
    '''
    def validateProject(self):
        self.logger.debug("Validate the project")
        
        print("Validates the project...")
        self.__displayCircles(self.__findStartActivity(), self.__findEndActivity())
        print("Complete validate the project.")
    
    '''
        Find circle paths - the recursion function.
    '''
    def __displayCircles(self, startActivity, endActivity, circularPath=[]):
        self.logger.debug("Circles: start activity = %s, end activity = %s" % (startActivity, endActivity))
        
        # Check if the start activity is in the graph:
        if (startActivity not in self._dictGraph):
            return list()  # empty list
        
        circularPath = circularPath + [startActivity]
        
        # Check in the starting point the same as the ending point:
        if (startActivity == endActivity):
            return list(circularPath)    
        
        for activity in self._dictGraph[startActivity]:
            if activity not in circularPath:
                extended_paths = self.__displayCircles(activity, endActivity, circularPath)
            else:
                circularPath = circularPath + [activity] 
                print("Circle path in the project: ", circularPath)
                return
    
    '''
    (Question 5)
        Find isolated activities in the projects.
        An activities without following or ascending another activity.
        Return the isolated activities in the project.
    '''
    def isolatedActivities(self):
        self.logger.debug("Search isolated activities")

        isolated = []
        tempFollowingActivities = [x for k, x in self._dictGraph.items()]  # Extract the following activities 
        followingActivities = []
        
        # Build one item at place list: 
        for activities in tempFollowingActivities:
            for i in activities:
                followingActivities.append(i)
         
        # Scan if their activity without following:
        for activity in self._dictGraph:
            if not self._dictGraph[activity]:
                isolated += [activity]
        
        # Scan if their activities that only connected and not have following activities.
        '''
        Example: assume we have dictionary as follow:
        g = {actA: [actB], actB: [actC,actD], actD: [actE,actF],actF: [actG],actG: []}
        Activities: 'actC' and 'actE' are isolated activities.
            'actC' because it dosen't have following activities.
            'actE' because it dosen't have following activities.
        '''
        for activity in followingActivities:
            try:
                if not self._dictGraph[activity]:
                    isolated += [activity]
                    
            # Catch if we try to look for activity used in the dictionary 
            # and not have following activities:
            except KeyError:
                isolated += [activity]
                
        # Save for latter usage:
        self._isolatedActivities = list(set(isolated))
         
        return self._isolatedActivities
    
    '''
    (Question 7)
        Finds the critical paths in the project by examining all the available paths
        and their durations.
        Return the paths with the maximum duration in the project as list and the 
        maximum duration as second variable. 
    '''    
    def criticalPath(self):
        self.logger.debug("Calculate the critical path in the project")

        allPaths = self.__allAvailablePaths()

        maxDuration = 0  # Hold the critical path duration
        pathsDuration = []  # Holds all the paths durations
        pathWithMaxDuration = list()  # Holds the critical paths
        
        # Get the maximum duration time in the project
        for path in allPaths:
            pathDuration = self.__pathDuration(path)  # Get the specific path duration:
            pathsDuration.append(pathDuration)  # Each index holds the duration

            # If we reach longer duration:
            if (pathDuration > maxDuration):
                maxDuration = pathDuration
        
        # Setup list with all the critical paths in the graph:
        for index, duration in enumerate(pathsDuration):
            if (duration == maxDuration):
                pathWithMaxDuration.append(allPaths[index])  # Get the path consider to be critical 
                
        # save for latter usage:
        self._criticalPathDuration = maxDuration
        self._criticalPath = pathWithMaxDuration

        return pathWithMaxDuration, maxDuration
    
    '''
        Helper function to get the critical path duration.
        Check if the critical path not calculated yet, and return the value as needed.
        Assume the criticalPath() function calculate and change the _criticalPathDuration attribute.  
    '''
    def __criticalPathDuration(self):
        self.logger.debug("helper function: __criticalPathDuration()")
        
        # Check if to active the calculation:
        if(self._criticalPathDuration == -1):
            self.criticalPath()
        
        # return the critical path duration as needed:
        return self._criticalPathDuration
    
    '''
        Helper function to get the critical path.
        Check if the critical path not calculated yet, and return the value as needed.
        Assume the criticalPath() function calculate and change the _criticalPath attribute.  
    '''
    def __criticalPath(self):
        self.logger.debug("helper function: __criticalPath()")
        
        # Check if to active the calculation:
        if(self._criticalPath == []):
            self.criticalPath()
        
        # return the critical path as needed:
        return self._criticalPath
    
    '''
        Helper function to get the duration of specific given path.
        Return the duration: Sum of all the activities in the path.
    '''
    def __pathDuration(self, path):
        self.logger.debug("helper function: __pathDuration()")
        
        pathDuration = 0
        
        for activity in path:
            pathDuration += activity.duration
            
        return pathDuration
    
    '''
        Use as an interface from outside to the recursion function "__paths".
        Initialized the needed lists, set the bounds activities and return the 
        available paths in the project: from the begin to end.
    '''
    def __allAvailablePaths(self):
        self.logger.debug("helper function: __allAvailablePaths()")
        
        paths = []
        path = []
        theAvailablePaths = self.__paths(self.__findStartActivity(), self.__findEndActivity(), path, paths)
        return theAvailablePaths
    
    '''
        Recursive implementation to find all the paths in the project.
        Return list that contains list of all the activities in a certain path
        was found. 
    '''
    def __paths(self, startActivity, endActivity, path=[], paths=[]):
        self.logger.debug("Search paths: start activity = %s, end activity = %s" % (startActivity, endActivity))
        
        if startActivity not in self._dictGraph:
            return None
        
        path.append(startActivity)
        
        
        if startActivity == endActivity:
            paths.append(self.__cloneList(path))
        else:
            for activity in self._dictGraph[startActivity]:
                self.__paths(activity, endActivity, path, paths)
        path.remove(startActivity)
        return paths

    '''
    (Question 8)
        Display the slack time for each activity that isn't in the critical path.
        Display the activity in descending order.
    '''
    def showSlackTime(self):
        self.logger.debug("Calculate slack time")

        # Fill the times data for each activity:
        self.setupEarlyTimes()
        self.setupLatestTimes()
        
        # Calculate the slack time for each activity in the project: 
        self.__calculateSlackTime()

        # Get the critical path of the project - to remove it:
        criticalPaths = self.__criticalPath()
        
        # Setup new list of activities to be edited:
        activities = self.__cloneList(self._dictGraph.keys())
        
        # Remove the activities found in the cricitalPaths
        for path in criticalPaths:
            for activity in path:
                if(activity in activities):
                    # Remove activities found in the critical path:
                    activities.remove(activity)
        
        print("Show slack times for activities in the project:")
        
        for activity in sorted(activities, key=lambda x: x.slackTime, reverse=True):
            print("Activity %s has slack time = %r" % (activity.name, activity.slackTime))

    def setupEarlyTimes(self):
        self.logger.debug("Calculate early times for each activity")
        self.__setupEarlyTimes(self.__findStartActivity(), self.__findEndActivity(), 0)
        

    def __setupEarlyTimes(self, startActivity, endActivity, earlyStart=0):
        self.logger.debug("Setup early times: start activity = %s, end activity = %s" % (startActivity, endActivity))
        
        # If reach follow activity without continue or to an end of path: 
        if (startActivity not in self._dictGraph) or (startActivity == endActivity):
            # Check if the early start need to be update:
            if(startActivity.earlyStart < earlyStart):
                startActivity.earlyStart = earlyStart
                startActivity.earlyFinish = startActivity.earlyStart + startActivity.duration 
            return
        
        else:
            # If we in the first activity:
            if(earlyStart == 0):
                startActivity.earlyStart = 0
                startActivity.earlyFinish = startActivity.earlyStart + startActivity.duration
                
            # Check if the early start need to be update:
            elif(startActivity.earlyStart < earlyStart):
                startActivity.earlyStart = earlyStart
                startActivity.earlyFinish = startActivity.earlyStart + startActivity.duration
            
            # increase the early start for the next iteration:
            earlyStart = earlyStart + startActivity.duration
                
            for activity in self._dictGraph[startActivity]:
                # Check the next path -> the follow activities from this activity:
                self.__setupEarlyTimes(activity, endActivity, earlyStart)
        return
    
    def setupLatestTimes(self):
        self.logger.debug("Calculate latest times for each activity")
        self.__setupLatestTimes(self.__findEndActivity(), self.__findStartActivity(), self.__criticalPathDuration())
        

    def __setupLatestTimes(self, startActivity, endActivity, latestFinish=0):
        self.logger.debug("Setup latest times: start activity = %s, end activity = %s" % (startActivity, endActivity))
        
        # If reach follow activity without continue or to an end of path: 
        if (startActivity not in self._dictGraph) or (startActivity == endActivity):
            # Check if the early start need to be update:
            if(startActivity.latestFinish > latestFinish):
                startActivity.latestFinish = latestFinish
                startActivity.latestStart = startActivity.latestFinish - startActivity.duration 
            return
        
        else:
            # Check if the early start need to be update:
            if(startActivity.latestFinish > latestFinish):
                startActivity.latestFinish = latestFinish
                startActivity.latestStart = startActivity.latestFinish - startActivity.duration
             
            # decrease the latest finish for the next iteration:
            latestFinish = latestFinish - startActivity.duration
            
            for activity in self._dictGraph:
                if(startActivity in self._dictGraph[activity]):
                    # Check the next path -> the follow activities from this activity:
                    self.__setupLatestTimes(activity, endActivity, latestFinish)
        return
    
    def __calculateSlackTime(self):
        self.logger.debug("Helper function: __calculateSlackTime()")
        for activity in self._dictGraph:
            activity.slackTime = activity.latestStart - activity.earlyStart 
    
    '''
        Helper method to find the start activity (no one is previous to the start point)
        Assume that there is just one start activity (as in real project)
    '''
    def __findStartActivity(self):
        self.logger.debug("Helper function: __findStartActivity()")
        for vertex in self._dictGraph:
            isFound = False
            for value in self._dictGraph.values():
                if vertex in value:
                    isFound = True

            if isFound == False:
                start = vertex
                return start

    '''
        Helper method to find the end activity (no one is after the end point)
        Assume that there is just one end activity (as in real project)
    '''
    def __findEndActivity(self):
        self.logger.debug("Helper function: __findEndActivity()")
        for vertex in self._dictGraph:
                if len(self._dictGraph[vertex]) == 0:  # The end point has no value -> no activity after him (list at length 0)
                    return vertex

    '''
        Helper function to clone list by it's values.
        Return new list that contain the element from a given list.
    '''
    def __cloneList(self, lst):
        self.logger.debug("Helper function: __cloneList() on the list: %s" % lst)
        temp = list()
    
        for item in lst:
            temp.append(item)
        
        return temp
  
    
    '''
    (Question 6)
        Define the string representation for this class object instance. 
    '''
    def __str__(self):
        self.logger.debug("Return the __str__ function")
        
        res = "Project details:\n"
        res += "Structure: "
        sortedDict = sorted(self._dictGraph)
        
        # Concatenate the project activities with their relation:
        for activity in sortedDict:
            if self._dictGraph[activity]:
                
                res += str(activity.name) + "->"
                lenOfFollows = len(self._dictGraph[activity])
                
                i = 0
                while(i < lenOfFollows):
                    res += str(self._dictGraph[activity][i].name)
                    
                    if not(i == lenOfFollows - 1):
                        res += ","
                        
                    i += 1 
                res += " | " 
        return res
