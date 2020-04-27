# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
#
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).

#####################################################
#####################################################
# Please enter the number of hours you spent on this
# assignment here
"""
num_hours_i_spent_on_this_assignment = 0
"""
#
#####################################################
#####################################################

#####################################################
#####################################################
# Give one short piece of feedback about the course so far. What
# have you found most interesting? Is there a topic that you had trouble
# understanding? Are there any changes that could improve the value of the
# course to you? (We will anonymize these before reading them.)
"""
<Your feedback goes here>

"""
#####################################################
#####################################################

"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Q1.1
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print ( problem.getStartState() )
    You will get (5,5)

    print (problem.isGoalState(problem.getStartState()) )
    You will get True

    print ( problem.getSuccessors(problem.getStartState()) )
    You will get [((x1,y1),'South',1),((x2,y2),'West',1)]
    """
    "*** YOUR CODE HERE ***"
    
    from game import Directions
    from util import Stack

    goalFound = False
    takenPath = []
    nodes = util.Stack()
    searchedStates = []
    startState = problem.getStartState()

    if problem.isGoalState(startState):
    	return []

    nodes.push(startState)
    takenPath.append([])
    while goalFound == False:
    	currentState = nodes.pop()
    	currentPath = takenPath.pop()
    	if currentState not in searchedStates:
    		searchedStates.append(currentState)	
    		if problem.isGoalState(currentState):
		    	goalFound = True
		    	return currentPath	
	    	for nextState, path, cost in problem.getSuccessors(currentState):
	    		action = currentPath + [path]
		    	takenPath.append(action)
		    	nodes.push(nextState)


def breadthFirstSearch(problem):
    """
    Q1.2
    Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    from util import Queue

    goalFound = False
    takenPath = util.Queue()
    nodes = util.Queue()
    searchedStates = []
    startState = problem.getStartState()

    if problem.isGoalState(startState):
    	return []

    nodes.push(startState)
    takenPath.push([])
    while goalFound == False:
    	currentState = nodes.pop()
    	currentPath = takenPath.pop()
    	if currentState not in searchedStates:
    		searchedStates.append(currentState)	
    		if problem.isGoalState(currentState):
		    	goalFound = True
		    	return currentPath
	    	for nextState, path, cost in problem.getSuccessors(currentState):
	    		action = currentPath + [path]
		    	takenPath.push(action)
		    	nodes.push(nextState)


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """
    Q1.3
    Search the node that has the lowest combined cost and heuristic first."""
    """Call heuristic(s,problem) to get h(s) value."""
    "*** YOUR CODE HERE ***"
    from game import Directions
    from util import PriorityQueue

    goalFound = False
    nodes = util.PriorityQueue()
    searchedStates = []
    startState = problem.getStartState()

    if problem.isGoalState(startState):
    	return []

    nodes.push((startState, [], 0), 0)
    while goalFound == False:
    	currentState, currentPath, prevCost = nodes.pop()
    	if currentState not in searchedStates:
    		searchedStates.append(currentState)	
    		if problem.isGoalState(currentState):
		    	goalFound = True
		    	return currentPath
	    	for nextState, path, cost in problem.getSuccessors(currentState):
	    		action = currentPath + [path]
	    		newCost = prevCost + cost
	    		heuristicCost  = newCost + heuristic(nextState, problem)
		    	nodes.push((nextState, action, newCost),heuristicCost)


def priorityQueueDepthFirstSearch(problem):
    """
    Q1.4a.
    Reimplement DFS using a priority queue.
    """
    # the implementation gives the same result
    # However, the implementation with stack using push/pop operation is faster with O(1)
    # whereas the priority queue push/pop operation takes O(log n)

    "*** YOUR CODE HERE ***"
    from util import PriorityQueue
    goalFound = False
    priorityNumber = 0
    depth = 0;
    takenPath = util.PriorityQueue()
    nodes = util.PriorityQueue()
    searchedStates = []
    startState = problem.getStartState()
    nullCost = nullHeuristic(startState,problem)

    if problem.isGoalState(startState):
    	return []

    nodes.push(startState,0)
    takenPath.push([],0)
    while goalFound == False:
    	currentState = nodes.pop()
    	currentPath = takenPath.pop()
    	depth += 1
    	if currentState not in searchedStates:
    		searchedStates.append(currentState)
    		if problem.isGoalState(currentState):
		    	goalFound = True
		    	return currentPath	
	    	for nextState, path, cost in problem.getSuccessors(currentState):
	    		depth -= 1
	    		priorityNumber = depth;
	    		action = currentPath + [path]
		    	takenPath.push(action,priorityNumber)
		    	nodes.push(nextState,priorityNumber)
    
		    	

def priorityQueueBreadthFirstSearch(problem):
    """
    Q1.4b.
    Reimplement BFS using a priority queue.
    """
    # the implementation gives the same result
    # However, the implementation with Queue using push/pop operation is faster with O(1)
    # whereas the priority queue push/pop operation takes O(log n)

    "*** YOUR CODE HERE ***"
    from util import PriorityQueue
    goalFound = False
    takenPath = util.PriorityQueue()
    nodes = util.PriorityQueue()
    searchedStates = []
    startState = problem.getStartState()
    nullCost = nullHeuristic(startState,problem)

    if problem.isGoalState(startState):
    	return []

    nodes.push(startState,nullCost)
    takenPath.push([],nullCost)
    while goalFound == False:
    	currentState = nodes.pop()
    	currentPath = takenPath.pop()
    	if currentState not in searchedStates:
    		searchedStates.append(currentState)	
    		if problem.isGoalState(currentState):
		    	goalFound = True
		    	return currentPath	
	    	for nextState, path, cost in problem.getSuccessors(currentState):
	    		action = currentPath + [path]
		    	takenPath.push(action,nullCost)
		    	nodes.push(nextState,nullCost)

#####################################################
#####################################################
# Discuss the results of comparing the priority-queue
# based implementations of BFS and DFS with your original
# implementations.

"""
<Your discussion goes here>
"""



#####################################################
#####################################################



# Abbreviations (please DO NOT change these.)
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
bfs2 = priorityQueueBreadthFirstSearch
dfs2 = priorityQueueDepthFirstSearch