class node:
    def __init__(self, puzzle):
        self.puzzle = puzzle
        self.cost = 0
        self.depth = 0
        self.parent = None
        self.child1 = 0
        self.child2 = 0
        self.child3 = 0
        self.child4 = 0
        self.expanded = False