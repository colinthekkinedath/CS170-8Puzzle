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