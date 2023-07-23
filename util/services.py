
from rest_framework.exceptions import ValidationError
from rest_framework.status import HTTP_400_BAD_REQUEST


from .utility import( 
                        get_position_of_pawn,
                        get_index,
                    )

from .utility import(
                        find_all_bishop_positions,
                        find_all_queen_positions,
                        find_all_knight_positions,
                        find_all_rook_positions
                    )


def generate_all_positions_for_pawns(positions: dict, ):
    '''
        Generates all positions of all pawns 
        taking the rules of chess in account.
    '''
    queen_position  = get_position_of_pawn(positions=positions, pawn='Queen')
    bishop_position = get_position_of_pawn(positions=positions, pawn='Bishop')
    knight_position = get_position_of_pawn(positions=positions, pawn='Knight')
    rook_position   = get_position_of_pawn(positions=positions, pawn='Rook')

    if not queen_position:
        raise ValidationError({'message': 'Data missing'}, code=HTTP_400_BAD_REQUEST)
    
    if not bishop_position:
        raise ValidationError({'message': 'Data missing'}, code=HTTP_400_BAD_REQUEST)
    
    if not knight_position:
        raise ValidationError({'message': 'Data missing'}, code=HTTP_400_BAD_REQUEST)
    
    if not rook_position:
        raise ValidationError({'message': 'Data missing'}, code=HTTP_400_BAD_REQUEST)
    
    queen_x, queen_y = get_index(queen_position)
    bishop_x, bishop_y = get_index(bishop_position)
    knight_x, knight_y = get_index(knight_position)
    rook_x, rook_y = get_index(rook_position)


    queen_all_positions = find_all_queen_positions(queen_x, queen_y)
    bishop_all_positions = find_all_bishop_positions(bishop_x, bishop_y )
    knight_all_positions = find_all_knight_positions(knight_x, knight_y)
    rook_all_positions = find_all_rook_positions(rook_x, rook_y)


    return (queen_all_positions, bishop_all_positions, knight_all_positions, rook_all_positions)