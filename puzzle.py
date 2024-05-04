import math
from nodeClass import node

def main():
    print('Welcome to 862332810, 862344897 8 puzzle solver.')

    inputpuzzle = input("Type '1' to use a default puzzle, or '2' to enter your own puzzle.\n")

    inputnum = int(inputpuzzle)

    if inputnum == 1:
        puzzle = (["1", "2", "3"], ["4", "5", "6"], ["7", "8", "0"])

    elif inputnum == 2:
        print('Enter your puzzle, use a zero to represent the blank')

        row1 = input("Enter the first row, use space or tabs between numbers\n")
        row2 = input("Enter the second row, use space or tabs between numbers\n")
        row3 = input("Enter the third row, use space or tabs between numbers\n")

        print('\n')

        row1 = row1.split(' ')
        row2 = row2.split(' ')
        row3 = row3.split(' ')

        puzzle = row1, row2, row3


    inputalgo = input('Enter your choice of algorithm \n1. Uniform Cost Search \n2. A* with the Misplaced Tile heuristic. \n3. A* with the Euclidean distance heuristic.\n')

    algofunction = int(inputalgo)


def goalState(puzzle):
    goalStatePuzzle = (["1", "2", "3"], ["4", "5", "6"], ["7", "8", "0"])

    if puzzle == goalStatePuzzle:
        return True
    
    return False

def misplacedTileHeuristic(puzzle):
    goalStatePuzzle = (["1", "2", "3"], ["4", "5", "6"], ["7", "8", "0"])
    misplacedTiles = 0

    for i in range(len(puzzle)):
        for j in range(len(puzzle)):
            if (puzzle[i][j] != goalStatePuzzle[i][j]) and (int(puzzle[i][j]) != 0):
                misplacedTiles += 1

    return misplacedTiles

def euclideanDistanceHeuristic(puzzle):
    goalStatePuzzle = (["1", "2", "3"], ["4", "5", "6"], ["7", "8", "0"])
    totalDistance = 0

    for i in range(len(puzzle)):
        for j in range(len(puzzle)):
            if puzzle[i][j] != "0":  
                num = int(puzzle[i][j])
                goal_i, goal_j = findNumberPosition(goalStatePuzzle, num)
                distance = math.sqrt((i - goal_i)**2 + (j - goal_j)**2)
                totalDistance += distance

    return totalDistance

def findNumberPosition(puzzle, num):
    for i in range(len(puzzle)):
        for j in range(len(puzzle)):
            if puzzle[i][j] == str(num):
                return i, j

if __name__ == "__main__":
    main()