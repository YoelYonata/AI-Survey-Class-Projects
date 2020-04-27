# multiAgents.py
# --------------
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


from util import manhattanDistance
from game import Directions
import random, util
import sys

from game import Agent

class ReflexAgent(Agent):
    """
      A reflex agent chooses an action at each choice point by examining
      its alternatives via a state evaluation function.

      The code below is provided as a guide.  You are welcome to change
      it in any way you see fit, so long as you don't touch our method
      headers.
    """


    def getAction(self, gameState):
        """
        You do not need to change this method, but you're welcome to.

        getAction chooses among the best options according to the evaluation function.

        Just like in the previous project, getAction takes a GameState and returns
        some Directions.X for some X in the set {North, South, West, East, Stop}
        """
        # Collect legal moves and successor states
        legalMoves = gameState.getLegalActions()

        # Choose one of the best actions
        scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
        bestScore = max(scores)
        bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
        chosenIndex = random.choice(bestIndices) # Pick randomly among the best

        "Add more of your code here if you want to"

        return legalMoves[chosenIndex]

    def evaluationFunction(self, currentGameState, action):
        """
        Design a better evaluation function here.

        The evaluation function takes in the current and proposed successor
        GameStates (pacman.py) and returns a number, where higher numbers are better.

        The code below extracts some useful information from the state, like the
        remaining food (newFood) and Pacman position after moving (newPos).
        newScaredTimes holds the number of moves that each ghost will remain
        scared because of Pacman having eaten a power pellet.

        Print out these variables to see what you're getting, then combine them
        to create a masterful evaluation function.
        """
        # Useful information you can extract from a GameState (pacman.py)
        successorGameState = currentGameState.generatePacmanSuccessor(action)
        newPos = successorGameState.getPacmanPosition()
        newFood = successorGameState.getFood()
        newGhostStates = successorGameState.getGhostStates()
        newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]

        "*** YOUR CODE HERE ***"
        score = successorGameState.getScore()
        foodList = newFood.asList()
        minDistanceGhost = float('inf')
        minDistanceFood = float('inf')

        #keep moving
        if currentGameState.getPacmanPosition() == newPos:
            return -999

        #food score
        foodDist = [manhattanDistance(newPos, food) for food in foodList]
        if foodDist:
        	minDistanceFood = min(foodDist)

        #ghost score
        for ghost in newGhostStates:
        	ghostPos = ghostState.getPosition()
        	ghostDist = manhattanDistance(newPos, ghostPos) 
        	if ghostDist < minDistanceGhost and ghostDist > 0:
        		minDistanceGhost = ghostDist

       	score = score + (10/ minDistanceFood) - (10/minDistanceGhost)

        return score

def scoreEvaluationFunction(currentGameState):
    """
      This default evaluation function just returns the score of the state.
      The score is the same one displayed in the Pacman GUI.

      This evaluation function is meant for use with adversarial search agents
      (not reflex agents).
    """
    return currentGameState.getScore()

class MultiAgentSearchAgent(Agent):
    """
      This class provides some common elements to all of your
      multi-agent searchers.  Any methods defined here will be available
      to the MinimaxPacmanAgent, AlphaBetaPacmanAgent & ExpectimaxPacmanAgent.

      You *do not* need to make any changes here, but you can if you want to
      add functionality to all your adversarial search agents.  Please do not
      remove anything, however.

      Note: this is an abstract class: one that should not be instantiated.  It's
      only partially specified, and designed to be extended.  Agent (game.py)
      is another abstract class.
    """

    def __init__(self, evalFn = 'scoreEvaluationFunction', depth = '2'):
        self.index = 0 # Pacman is always agent index 0
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)

class MinimaxAgent(MultiAgentSearchAgent):
    """
      Your minimax agent (question 2)
    """

    def getAction(self, gameState):
        """
          Returns the minimax action from the current gameState using self.depth
          and self.evaluationFunction.

          Here are some method calls that might be useful when implementing minimax.

          gameState.getLegalActions(agentIndex):
            Returns a list of legal actions for an agent
            agentIndex=0 means Pacman, ghosts are >= 1

          gameState.generateSuccessor(agentIndex, action):
            Returns the successor game state after an agent takes an action

          gameState.getNumAgents():
            Returns the total number of agents in the game
        """
        "*** YOUR CODE HERE ***"

        #pacman
        def maxAgent (gameState, depth):
        	actions = gameState.getLegalActions(0)
        	maxScore = -float('inf')
        	bestAction = Directions.STOP

        	if depth == self.depth:
        		return (self.evaluationFunction(gameState), Directions.STOP)

        	if len(actions) == 0:
        		return (self.evaluationFunction(gameState), Directions.STOP)

        	for action in actions:
        		newState = gameState.generateSuccessor(0, action)
        		newScore = minAgent(newState,1,depth)[0]
        		if newScore > maxScore:
        			maxScore = newScore
        			bestAction = action
        	return (maxScore, bestAction)

        #ghost
        def minAgent (gameState, ghostID, depth):
        	actions = gameState.getLegalActions(ghostID)
        	minScore = float('inf')
        	bestAction = Directions.STOP

        	if len(actions) == 0:
        		return (self.evaluationFunction(gameState), Directions.STOP)

        	for action in actions:
        		newState = gameState.generateSuccessor(ghostID, action)
        		if ghostID == gameState.getNumAgents() - 1: 
        			newScore = maxAgent (newState, depth+1)[0]
        		else:
        			newScore = minAgent(newState, ghostID+1, depth)[0]

        		if newScore < minScore:
        			minScore = newScore
        			bestAction = action

        	return (minScore, bestAction)

        return maxAgent (gameState, 0) [1]



class AlphaBetaAgent(MultiAgentSearchAgent):
    """
      Your minimax agent with alpha-beta pruning (question 3)
    """

    def getAction(self, gameState):
        """
          Returns the minimax action using self.depth and self.evaluationFunction
        """
        "*** YOUR CODE HERE ***"
        def maxAgent (gameState, depth, alpha, beta):
        	actions = gameState.getLegalActions(0)
        	maxScore = -float('inf')
        	bestAction = Directions.STOP

        	if depth == self.depth:
        		return (self.evaluationFunction(gameState), Directions.STOP)

        	if len(actions) == 0:
        		return (self.evaluationFunction(gameState), Directions.STOP)

        	for action in actions:
        		if beta < alpha:
        			return(maxScore,bestAction)
        		newState = gameState.generateSuccessor(0, action)
        		newScore = minAgent(newState,1,depth,alpha,beta)[0]
        		if newScore > maxScore:
        			maxScore = newScore
        			bestAction = action
        		if newScore > alpha:
        			alpha = newScore
        	return (maxScore, bestAction)

        #ghost
        def minAgent (gameState, ghostID, depth, alpha, beta):
        	actions = gameState.getLegalActions(ghostID)
        	minScore = float('inf')
        	bestAction = Directions.STOP

        	if len(actions) == 0:
        		return (self.evaluationFunction(gameState), Directions.STOP)

        	for action in actions:
        		if beta < alpha:
        			return(minScore,bestAction)
        		newState = gameState.generateSuccessor(ghostID, action)
        		if ghostID == gameState.getNumAgents() - 1: 
        			newScore = maxAgent (newState, depth+1, alpha, beta)[0]
        		else:
        			newScore = minAgent(newState, ghostID+1, depth, alpha, beta)[0]

        		if newScore < minScore:
        			minScore = newScore
        			bestAction = action
        		if newScore < beta:
        			beta = newScore

        	return (minScore, bestAction)

        return maxAgent (gameState, 0, -float('inf'), float('inf')) [1]

class ExpectimaxAgent(MultiAgentSearchAgent):
    """
      Your expectimax agent (question 4)
    """

    def getAction(self, gameState):
        """
          Returns the expectimax action using self.depth and self.evaluationFunction

          All ghosts should be modeled as choosing uniformly at random from their
          legal moves.
        """
        "*** YOUR CODE HERE ***"
        def maxAgent (gameState, depth):
        	actions = gameState.getLegalActions(0)
        	maxScore = -float('inf')
        	bestAction = Directions.STOP

        	if depth == self.depth:
        		return (self.evaluationFunction(gameState), Directions.STOP)

        	if len(actions) == 0:
        		return (self.evaluationFunction(gameState), Directions.STOP)

        	for action in actions:
        		newState = gameState.generateSuccessor(0, action)
        		newScore = expAgent(newState,1,depth)[0]
        		if newScore > maxScore:
        			maxScore = newScore
        			bestAction = action
        	return (maxScore, bestAction)
 
    	def expAgent (gameState, ghostID, depth):
	    	actions = gameState.getLegalActions(ghostID)
	    	score = 0
	    	bestAction = Directions.STOP

	    	if len(actions) == 0:
	    		return (self.evaluationFunction(gameState), Directions.STOP)

	    	for action in actions:
	    		probability = 1.0/len(actions)
	    		newState = gameState.generateSuccessor(ghostID, action)
	    		if ghostID == gameState.getNumAgents() - 1: 
	    			newScore = maxAgent (newState, depth+1)[0]
	    		else:
	    			newScore = expAgent(newState, ghostID+1, depth)[0]
    			score += probability*newScore
        	return (score, bestAction)

        return maxAgent (gameState, 0) [1]


def betterEvaluationFunction(currentGameState):
    """
      Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
      evaluation function (question 5).

      DESCRIPTION: <write something here so we know what you did>
      I am using the  evaluation function from question 1, except this one will also consider
      eating the capsules and makes sure to eat as long as there is still food left.
    """
    "*** YOUR CODE HERE ***"
    newPos = currentGameState.getPacmanPosition()
    newFood = currentGameState.getFood()
    newGhostStates = currentGameState.getGhostStates()
    newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]
    capsulePos = currentGameState.getCapsules()

    score = currentGameState.getScore()
    foodList = newFood.asList()
    minDistanceGhost = float('inf')
    minDistanceFood = float('inf')

    #food score
    foodDist = [manhattanDistance(newPos, food) for food in foodList]
    if foodDist:
    	minDistanceFood = min(foodDist)
    if len(foodDist) > 0:
    	score -= max(foodDist)

    #ghost score
    for ghost in newGhostStates:
    	ghostPos = ghostState.getPosition()
    	ghostDist = manhattanDistance(newPos, ghostPos) 
    	if ghostDist < minDistanceGhost and ghostDist > 0:
    		minDistanceGhost = ghostDist

    capsuleDist = [manhattanDistance(newPos, capsule) for capsule in capsulePos]
    if capsuleDist:
    	minCapsuleDist = min(capsuleDist)
    	score += 20/minCapsuleDist

   
    score = score + (10/ minDistanceFood) - (10/minDistanceGhost)

    return score



# Abbreviation
better = betterEvaluationFunction

