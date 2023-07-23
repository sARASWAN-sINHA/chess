'''
    Verical movements.
'''
def move_vertically_up(i, j):
    return (i, j+1)

def move_vertically_down(i, j):
    return (i, j-1)

'''
    Horizontal movements.
'''
def move_horizontally_left(i, j):
    return (i-1, j)

def move_horizontally_right(i, j):
    return (i+1, j)

'''
    Diagonal movements.
'''

# diagonally up
def move_diagonally_right_up(i, j):
    return (i+1, j+1)

def move_diagonally_left_up(i, j):
    return (i-1, j+1)

#diagonally down
def move_diagonally_right_down(i, j):
    return (i+1, j-1)

def move_diagonally_left_down(i, j):
    return (i-1, j-1)


'''
    Specific movements of the Knight Pawn.

'''
knight_movements_dirs = [
    (1, 2), (1, -2),
    (-1, 2), (-1, -2),
    (2, 1), (2, -1),
    (-2, 1), (-2, -1),  
]
