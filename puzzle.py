def main():
    print('Welcome to 862332810, 862344897 8 puzzle solver.')

def goalState(puzzle):
    goalStatePuzzle = (["1", "2", "3"], ["4", "5", "6"], ["7", "8", "0"])

    if puzzle == goalStatePuzzle:
        return True
    
    return False

if __name__ == "__main__":
    main()