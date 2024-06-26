import math
import copy
import time

def main():
    print('Welcome to 862332810, 862344897, 862385153, 862368434 8 puzzle solver.')

    # Asks user to choose a default puzzle or enter their own
    inputpuzzle = input("Type '1' to use a default puzzle, or '2' to enter your own puzzle.\n")

    inputnum = int(inputpuzzle)

    if inputnum == 1:
        puzzle = (["1", "2", "3"], ["4", "0", "6"], ["7", "5", "8"])

    elif inputnum == 2:
        # Takes user input for their own puzzle
        print('Enter your puzzle, use a zero to represent the blank')

        rows = []
        for i in range(3):
            row_input = input(f"Enter row {i+1}, use space or tabs between numbers\n")
            row_values = row_input.split()
            rows.append(row_values)

        print('\n')

        puzzle = tuple(rows)


    # Asks user to choose an algorithm
    inputalgo = input('Enter your choice of algorithm \n1. Uniform Cost Search \n2. A* with the Misplaced Tile heuristic. \n3. A* with the Euclidean distance heuristic.\n')

    algofunction = int(inputalgo)

    solvePuzzle(puzzle, algofunction)

# Function to solve the puzzle
def solvePuzzle(puzzle, algofunction):

    initialTime = time.time()

    queue = [] # Priority queue
    visited = [] # List to keep track of visited nodes 
    visitedCount = -1
    queueSize = 0
    maxSize = -1

    # Sets the heuristic value based on the algorithm chosen
    if algofunction == 1:
        heuristic = 0

    elif algofunction == 2:
        heuristic = misplacedTileHeuristic(puzzle)
    
    elif algofunction == 3:
        heuristic = euclideanDistanceHeuristic(puzzle)

    # Creates the initial node
    n = node(puzzle)
    n.cost = heuristic
    n.depth = 0
    queue.append(n)

    visited.append(n.puzzle)
    queueSize += 1
    maxSize += 1

    while True:
        # Sorts the queue based on the algorithm chosen
        if algofunction != 1:
            queue = sorted(queue, key=lambda x: (x.depth + x.cost, x.depth))

        if len(queue) == 0:
            print('No solution found')
            return
            
        firstNode = queue.pop(0) # Removes the first node from the queue
        if firstNode.expanded is False:
            visitedCount += 1
            firstNode.expanded = True

        maxSize -= 1

        if goalState(firstNode.puzzle):
            print('Goal! \n\nTo solve this problem the search algorithm expanded a total of ' + str(visitedCount) + ' nodes.')
            print('The maximum number of nodes in the queue at any one time was '+ str(maxSize) + '.')
            print('The depth of the goal node was ' + str(firstNode.depth))
            print('The time taken was ' + str(time.time() - initialTime) + ' seconds')
            return
            
        if visitedCount != 0:
            print('The best state to expand with a g(n) = ' + str(firstNode.depth) + ' and h(n) = ' + str(firstNode.cost)
                  + ' is...\n' + str(firstNode.puzzle) + '\tExpanding this node...\n')
        
        else:
            print('Expanding this node...\n' + str(firstNode.puzzle) + '\n')
        
        expandNode = expand(firstNode, visited) # Expands the current node

        arr = [expandNode.child1, expandNode.child2, expandNode.child3, expandNode.child4]

        for i in arr:
            if i is not None:
                # Sets the cost and depth for children based on the algorithm chosen
                if algofunction == 1:
                    i.depth = firstNode.depth + 1
                    i.cost = 0
                elif algofunction == 2:
                    i.depth = firstNode.depth + 1
                    i.cost = misplacedTileHeuristic(i.puzzle)
                elif algofunction == 3:
                    i.depth = firstNode.depth + 1
                    i.cost = euclideanDistanceHeuristic(i.puzzle)
                
                queue.append(i)
                visited.append(i.puzzle)
                queueSize += 1

        # Updates the maximum size of the queue
        if queueSize > maxSize:
            maxSize = queueSize


# Function to check if the puzzle is in the goal state
def goalState(puzzle):
    goalStatePuzzle = (["1", "2", "3"], ["4", "5", "6"], ["7", "8", "0"])

    if puzzle == goalStatePuzzle:
        return True
    
    return False

# Heuristic functions
def misplacedTileHeuristic(puzzle):
    goalStatePuzzle = (["1", "2", "3"], ["4", "5", "6"], ["7", "8", "0"])
    misplacedTiles = 0

    # Counts the number of misplaced tiles
    for i in range(len(puzzle)):
        for j in range(len(puzzle)):
            if (puzzle[i][j] != goalStatePuzzle[i][j]) and (puzzle[i][j] != "0"):
                misplacedTiles += 1

    return misplacedTiles

def euclideanDistanceHeuristic(puzzle):
    goalStatePuzzle = (["1", "2", "3"], ["4", "5", "6"], ["7", "8", "0"])
    totalDistance = 0

    # Calculates the Euclidean distance for each number in the puzzle
    for i in range(len(puzzle)):
        for j in range(len(puzzle)):
            if puzzle[i][j] != "0":  
                num = int(puzzle[i][j])
                goal_i, goal_j = findNumberPosition(goalStatePuzzle, num)
                distance = math.sqrt((i - goal_i)**2 + (j - goal_j)**2)
                totalDistance += distance

    return totalDistance

# helper function for the Euclidean Distance Heuristic
def findNumberPosition(puzzle, num):
    for i in range(len(puzzle)):
        for j in range(len(puzzle)):
            if puzzle[i][j] == str(num):
                return i, j

# Function to expand the current node
def expand(expandingNode, visited):
    row = 0
    col = 0

    # Finds the position of the blank tile
    for i in range(len(expandingNode.puzzle)):
        for j in range(len(expandingNode.puzzle)):
            if (expandingNode.puzzle[i][j] == "0"):
                row = i
                col = j
    
    # Generates child nodes by moving the blank tile in all possible directions
    # Create a deep copy so the puzzle knows where to expand
    # moving Left
    if col > 0:
        moveLeft = copy.deepcopy(expandingNode.puzzle)
        holder = moveLeft[row][col]
        moveLeft[row][col] = moveLeft[row][col - 1]
        moveLeft[row][col - 1] = holder

        if moveLeft not in visited:
            expandingNode.child1 = node(moveLeft)

    # moving Right
    if col < len(expandingNode.puzzle) - 1:
        moveRight = copy.deepcopy(expandingNode.puzzle)
        holder = moveRight[row][col]
        moveRight[row][col] = moveRight[row][col + 1]
        moveRight[row][col + 1] = holder

        if moveRight not in visited:
            expandingNode.child2 = node(moveRight)

    # moving Up
    if row > 0:
        moveUp = copy.deepcopy(expandingNode.puzzle)
        holder = moveUp[row][col]
        moveUp[row][col] = moveUp[row - 1][col]
        moveUp[row - 1][col] = holder

        if moveUp not in visited:
            expandingNode.child3 = node(moveUp)

    # moving Down
    if row < len(expandingNode.puzzle) - 1:
        moveDown = copy.deepcopy(expandingNode.puzzle)
        holder = moveDown[row][col]
        moveDown[row][col] = moveDown[row + 1][col]
        moveDown[row + 1][col] = holder

        if moveDown not in visited:
            expandingNode.child4 = node(moveDown)

    return expandingNode

# Defines the node class
class node:
    def __init__(self, puzzle):
        self.puzzle = puzzle
        self.cost = 0
        self.depth = 0
        self.parent = None
        self.child1 = None
        self.child2 = None
        self.child3 = None
        self.child4 = None
        self.expanded = False

if __name__ == "__main__":
    main()