from .movement import (move_vertically_down,
                        move_vertically_up, 
                        move_horizontally_left, 
                        move_horizontally_right, 
                        move_diagonally_right_up, 
                        move_diagonally_left_up, 
                        move_diagonally_right_down, 
                        move_diagonally_left_down, 
                        knight_movements_dirs)

def is_valid_position(pos):
    '''
        Check validity of the "pos" tuple containing the numerical indexes of the pawn in the board.
    '''
    i, j = pos[0], pos[1]
    return (i<=8 and j<=8) and (i > 0 and j > 0)

def find_all_queen_positions(x, y):
    '''
        Finds all possible poitions where queen can move irrespective of other pawns positions.
    '''
    queen_valid_positions = set()

    pos_x, pos_y = x, y
    while is_valid_position(move_vertically_up(pos_x, pos_y)):
        pos_x, pos_y = move_vertically_up(pos_x, pos_y)
        queen_valid_positions.add((pos_x, pos_y))
    
    pos_x, pos_y = x, y
    while is_valid_position(move_vertically_down(pos_x, pos_y)):
        pos_x, pos_y = move_vertically_down(pos_x, pos_y)
        queen_valid_positions.add((pos_x, pos_y))
    
    pos_x, pos_y = x, y
    while is_valid_position(move_horizontally_left(pos_x, pos_y)):
        pos_x, pos_y = move_horizontally_left(pos_x, pos_y)
        queen_valid_positions.add((pos_x, pos_y))
    
    pos_x, pos_y = x, y
    while is_valid_position(move_horizontally_right(pos_x, pos_y)):
        pos_x, pos_y = move_horizontally_right(pos_x, pos_y)
        queen_valid_positions.add((pos_x, pos_y))
    
    pos_x, pos_y = x, y
    while is_valid_position(move_diagonally_right_up(pos_x, pos_y)):
        pos_x, pos_y = move_diagonally_right_up(pos_x, pos_y)
        queen_valid_positions.add((pos_x, pos_y))
    
    pos_x, pos_y = x, y
    while is_valid_position(move_diagonally_left_down(pos_x, pos_y)):
        pos_x, pos_y = move_diagonally_left_down(pos_x, pos_y)
        queen_valid_positions.add((pos_x, pos_y))

    pos_x, pos_y = x, y
    while is_valid_position(move_diagonally_left_up(pos_x, pos_y)):
        pos_x, pos_y = move_diagonally_left_up(pos_x, pos_y)
        queen_valid_positions.add((pos_x, pos_y))
    
    pos_x, pos_y = x, y
    while is_valid_position(move_diagonally_right_down(pos_x, pos_y)):
        pos_x, pos_y = move_diagonally_right_down(pos_x, pos_y)
        queen_valid_positions.add((pos_x, pos_y)) 

    return queen_valid_positions

def find_all_bishop_positions(x, y):
    '''
        Finds all possible poitions where bishop can move irrespective of other pawns positions
    '''
    bishop_valid_positions = set()
    pos_x, pos_y = x, y
    while is_valid_position(move_diagonally_right_up(pos_x, pos_y)):
        pos_x, pos_y = move_diagonally_right_up(pos_x, pos_y)
        bishop_valid_positions.add((pos_x, pos_y))
    
    pos_x, pos_y = x, y
    while is_valid_position(move_diagonally_left_down(pos_x, pos_y)):
        pos_x, pos_y = move_diagonally_left_down(pos_x, pos_y)
        bishop_valid_positions.add((pos_x, pos_y))
    

    pos_x, pos_y = x, y
    while is_valid_position(move_diagonally_left_up(pos_x, pos_y)):
        pos_x, pos_y = move_diagonally_left_up(pos_x, pos_y)
        bishop_valid_positions.add((pos_x, pos_y))    
    
    pos_x, pos_y = x, y
    while is_valid_position(move_diagonally_right_down(pos_x, pos_y)):
        pos_x, pos_y = move_diagonally_right_down(pos_x, pos_y)
        bishop_valid_positions.add((pos_x, pos_y)) 

    return bishop_valid_positions

def find_all_knight_positions(x, y):
    '''
        Finds all possible poitions where knight can move irrespective of other pawns positions. 
    '''
    knight_valid_positions = set()
    for dir in knight_movements_dirs:
        if is_valid_position((x + dir[0], y + dir[1])):
            knight_valid_positions.add((x + dir[0], y + dir[1]))
    return knight_valid_positions

def find_all_rook_positions(x, y):
        '''
        Finds all possible poitions where rook can move irrespective of other pawns positions
        '''
        
        rook_valid_positions = set()
        pos_x, pos_y = x, y

        while is_valid_position(move_vertically_up(pos_x, pos_y)):
            pos_x, pos_y = move_vertically_up(pos_x, pos_y)
            rook_valid_positions.add((pos_x, pos_y))
        
        pos_x, pos_y = x, y
        while is_valid_position(move_vertically_down(pos_x, pos_y)):
            pos_x, pos_y = move_vertically_down(pos_x, pos_y)
            rook_valid_positions.add((pos_x, pos_y))
        
        pos_x, pos_y = x, y
        while is_valid_position(move_horizontally_left(pos_x, pos_y)):
            pos_x, pos_y = move_horizontally_left(pos_x, pos_y)
            rook_valid_positions.add((pos_x, pos_y))
        
        pos_x, pos_y = x, y
        while is_valid_position(move_horizontally_right(pos_x, pos_y)):
            pos_x, pos_y = move_horizontally_right(pos_x, pos_y)
            rook_valid_positions.add((pos_x, pos_y))
        
        return rook_valid_positions

def find_queen_valid_positions(queen_all_positions: set, bishop_all_positions: set, knight_all_positions: set, rook_all_positions: set):
    '''
        Finds all valid poitions where queen can move.
    '''
    # Q = Q - (B U K U R)
    queen_valid_positions = queen_all_positions.difference(bishop_all_positions.union(knight_all_positions, rook_all_positions))
    return queen_valid_positions

def find_bishop_valid_positions(queen_all_positions: set, bishop_all_positions: set, knight_all_positions: set, rook_all_positions: set):
    '''
        Finds all valid poitions where bishop can move
    '''
    # B = B - (Q U K U R)
    bishop_valid_positions = bishop_all_positions.difference(queen_all_positions.union(knight_all_positions, rook_all_positions))
    return bishop_valid_positions

def find_knight_valid_positions(queen_all_positions: set, bishop_all_positions: set, knight_all_positions: set, rook_all_positions: set):
    '''
        Finds all valid poitions where knight can move.
    '''
    # K = K - (B U Q U R)
    knight_valid_positions = knight_all_positions.difference(bishop_all_positions.union(queen_all_positions, rook_all_positions))
    return knight_valid_positions

def find_rook_valid_positions(queen_all_positions: set, bishop_all_positions: set, knight_all_positions: set, rook_all_positions: set):
    '''
    Finds all valid poitions where rook can move
    '''
    # R = R - (B U K U Q)
    rook_valid_positions = rook_all_positions.difference(bishop_all_positions.union(knight_all_positions, queen_all_positions))

    return rook_valid_positions

get_index = lambda chess_position: (ord(chess_position[0]) - 64, ord(chess_position[1]) - 48)  # finds numerical indices of the pawns based on the chess co-ordinates.
get_chess_co_ordinates = lambda pos: (chr(pos[0]+64) + str(pos[1]))                            # generates the chess co-ordinates based on the indices.
get_position_of_pawn = lambda positions, pawn: positions.get('postions', None).get(pawn, None) # gets the position of pawn from the request data that is send to the server.


pawn_mapper = {
    'queen'  : find_queen_valid_positions, 
    'bishop' : find_bishop_valid_positions,
    'knight' : find_knight_valid_positions,
    'rook'   : find_rook_valid_positions,
    }