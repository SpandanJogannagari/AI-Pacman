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
    Search the deepest nodes in the search tree first.
    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.
    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:
    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    #We are using stack datastructure for dfs.
    state_space = util.Stack()
    initial_position = problem.getStartState()
    visited_node=[]     #using a list to store the visited nodes to avoid unnecessary repetition
    initial_path=[]        #initializing the path to an empty list
    state_space.push([initial_position,initial_path]) #pushing the stack with initial position and initial path
    while not state_space.isEmpty():
        current_node_stats=state_space.pop()    
        current_position =current_node_stats[0]
        current_direction = current_node_stats[1]
        if current_position not in visited_node:
            visited_node.append(current_position)
            if problem.isGoalState(current_position):
                return current_direction
            child_nodes = problem.getSuccessors(current_position) #get all the successors for the current node
            i=0

            while i < len(child_nodes): #adding the successors to the state space
                child_position= child_nodes[i][0]
                child_direction=child_nodes[i][1]
                state_space.push([child_position,current_direction+[child_direction]])
                i+=1

            # The below commented code is used to test by traversing from left to right.
            # j=len(child_nodes)-1
            # while j >=0:
            #     child_position= child_nodes[j][0]
            #     child_direction=child_nodes[j][1]
            #     state_space.push([child_position,current_direction+[child_direction]])
            #     j-=1

    util.raiseNotDefined()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    state_space = util.Queue()
    initial_position = problem.getStartState()
    visited_node=[]
    initial_path=[]
    state_space.push([initial_position,initial_path])
    while not state_space.isEmpty():
        current_node_stats=state_space.pop()
        current_position =current_node_stats[0]
        current_direction = current_node_stats[1]
        if current_position not in visited_node:
            visited_node.append(current_position)
            if problem.isGoalState(current_position): #check if we have reached goal position
                return current_direction
            child_nodes = problem.getSuccessors(current_position) # print(child_nodes)
            i=0
            while i < len(child_nodes):
                child_position= child_nodes[i][0]
                child_direction=child_nodes[i][1]
                state_space.push([child_position,current_direction+[child_direction]])
                i+=1

    util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    state_space = util.PriorityQueue()
    initial_position = problem.getStartState()
    visited_node=[]
    initial_path=[]
    initial_cost=0
    state_space.push([initial_position,initial_path,initial_cost],0)
    while not state_space.isEmpty():
        current_node_stats=state_space.pop()
        current_position =current_node_stats[0]
        current_direction = current_node_stats[1]
        current_cost= current_node_stats[2]
        if current_position not in visited_node: #check if we have reached goal position
            visited_node.append(current_position)
            if problem.isGoalState(current_position):
                return current_direction
            child_nodes = problem.getSuccessors(current_position)
            i=0
            while i < len(child_nodes):
                child_position= child_nodes[i][0]
                child_direction=child_nodes[i][1]
                child_cost=child_nodes[i][2]
                state_space.push([child_position,current_direction+[child_direction],current_cost+child_cost],current_cost+child_cost)
                i+=1
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    state_space = util.PriorityQueue()
    initial_position = problem.getStartState()
    visited_node=set()
    initial_path=[]
    initial_cost=0
    state_space.push([initial_position,initial_path,initial_cost],0)
    while not state_space.isEmpty():
        current_node_stats=state_space.pop()
        current_position =current_node_stats[0]
        current_direction = current_node_stats[1]
        current_cost= current_node_stats[2]
        if current_position not in visited_node:
            visited_node.add(current_position) # check if our current postion is the goal position
            if problem.isGoalState(current_position):
                return current_direction
            child_nodes = problem.getSuccessors(current_position)
            i=0
            while i < len(child_nodes):
                child_position= child_nodes[i][0]
                child_direction=child_nodes[i][1]
                child_cost=child_nodes[i][2]
                state_space.push([child_position,current_direction+[child_direction],current_cost+child_cost],current_cost+child_cost+heuristic(child_position,problem))
                i+=1
    util.raiseNotDefined()

    
# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch