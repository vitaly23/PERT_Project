'''
    Author:  Vitaly Gorelik
    ID:      316883529
'''
import logging
from Activity import Activity
from PertManagment import CPM_Network

def main():
    
    # Create some activities for testing:
    actStart = Activity("Start", 0)
    actA = Activity("A", 4)
    actB = Activity("B", 5)
    actC = Activity("C", 3)
    actD = Activity("D", 4)
    actE = Activity("E", 3)
    actF = Activity("F", 6)
    actG = Activity("G", 4)
    actH = Activity("H", 4)
    actEnd = Activity("End", 0)
    tempActivity = Activity("temp", 5)  # Just for testings

    # Create first graph:
    g = {
        actStart: [actA],
        actA: [actB, actC, actD],
        actB: [actF],
        actC: [actE],
        actD: [actE],
        actE: [actH],
        actF: [actG],
        actG: [actEnd],
        actH: [actEnd],
        actEnd: []
     }

    # Create another graph for testing:
    withCircles = {
        actStart: [actA],
        actA: [actB, actC, actD],
        actB: [actF],
        actC: [actE],
        actD: [actE],
        actE: [actH],
        actF: [actG],
        actG: [actEnd, actH],
        actH: [actEnd, actF],
        actEnd: []
     }
    
    '''
        Check all the questions from the home work.
    '''
    print("============================== Question 1 ===================================")
    print("Initialize the project object - CPM_Network")
    newGraph = CPM_Network(g)
    print("=============================================================================\n")
    
    print("============================== Question 2 ===================================")
    print("Add activity to the project: %s, with the following activities %s" % (actH, [actEnd]))
    newGraph.addActivity(actH, [actEnd])
    print("=============================================================================\n")
    
    print("============================== Question 3 ===================================")
    print("Add temporary activity i.e for testing:")
    print("Add activity %s to the project, with the following activities %s" % (tempActivity, [actEnd]))
    newGraph.addActivity(tempActivity, [actEnd])
    print(str(newGraph))
    print("Removing the %s activity from the project" % tempActivity)
    newGraph.removeActivity(tempActivity)
    print(str(newGraph))
    print("=============================================================================\n")
    
    print("============================== Question 4 ===================================")
    print("Using another project for the test:")
    circles = CPM_Network(withCircles)
    circles.validateProject()
    print("=============================================================================\n")
        
    print("============================== Question 5 ===================================")
    isolatedActivities = newGraph.isolatedActivities()
    print("The isolated activities in the project: \n%s" % isolatedActivities)
    print("=============================================================================\n")

    print("============================== Question 6 ===================================")
    print(str(newGraph))
    print("=============================================================================\n")
    
    print("============================== Question 7 ===================================")
    criticalPath, maximumDuration = newGraph.criticalPath()
    print("The duration of the critical path is: %r" % maximumDuration)
    print("The critical paths in the project: \n%s" % criticalPath)
    print("=============================================================================\n")
    
    print("============================== Question 8 ===================================")
    newGraph.showSlackTime()
    print("=============================================================================\n")
    
    print("============================== Question 9 ===================================")
    print("The project duration is: %r" % newGraph.duration)
    print("=============================================================================\n")
    
if __name__ == "__main__":
    # Configure logger for the project:
    logging.basicConfig(level=logging.DEBUG, filename='CPM_Project.log', filemode='w',
        format='%(name)s %(levelname)s %(message)s')
    
    main()










