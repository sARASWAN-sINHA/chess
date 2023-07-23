from rest_framework.viewsets import ViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK


from util.services import generate_all_positions_for_pawns
from util.utility import (
                          find_knight_valid_positions, 
                          find_rook_valid_positions, 
                          find_bishop_valid_positions, 
                          find_queen_valid_positions,
                        )
from util.utility import get_chess_co_ordinates


class PawnPositionsViewSet(ViewSet):

    @action(detail=False, methods=['GET'])
    def knight(self, request, *args, **kwargs):
        '''
            Will generate the valid position for Knight
            given the positions of other pawns.
        '''
        positions = request.data
        queen_all_positions, bishop_all_positions, knight_all_positions, rook_all_positions = generate_all_positions_for_pawns(positions=positions)
        knight_valid_positions= find_knight_valid_positions(queen_all_positions, bishop_all_positions, knight_all_positions, rook_all_positions)
        knight_valid_position_chess_coordinates = list(map(get_chess_co_ordinates, knight_valid_positions))
        knight_valid_position_chess_coordinates.sort()
        return Response({'valid_response': knight_valid_position_chess_coordinates}, status=HTTP_200_OK)
    
    @action(detail=False, methods=['GET'])
    def rook(self, request, *args, **kwargs):
        '''
            Will generate the valid position for Rook
            given the positions of other pawns.
        '''
        positions = request.data
        queen_all_positions, bishop_all_positions, knight_all_positions, rook_all_positions = generate_all_positions_for_pawns(positions=positions)
        rook_valid_positions= find_rook_valid_positions(queen_all_positions, bishop_all_positions, knight_all_positions, rook_all_positions)
        rook_valid_position_chess_coordinates = list(map(get_chess_co_ordinates, rook_valid_positions))
        rook_valid_position_chess_coordinates.sort()
        return Response({'valid_response': rook_valid_position_chess_coordinates}, status=HTTP_200_OK)
    
    @action(detail=False, methods=['GET'])
    def bishop(self, request, *args, **kwargs):
        '''
            Will generate the valid position for Bishop
            given the positions of other pawns.
        '''
        positions = request.data
        queen_all_positions, bishop_all_positions, knight_all_positions, rook_all_positions = generate_all_positions_for_pawns(positions=positions)
        bishop_valid_positions= find_bishop_valid_positions(queen_all_positions, bishop_all_positions, knight_all_positions, rook_all_positions)
        bishop_valid_position_chess_coordinates = list(map(get_chess_co_ordinates, bishop_valid_positions))
        bishop_valid_position_chess_coordinates.sort()
        return Response({'valid_response': bishop_valid_position_chess_coordinates}, status=HTTP_200_OK)
    
    @action(detail=False, methods=['GET'])
    def queen(self, request, *args, **kwargs):
        '''
            Will generate the valid position for Queen
            given the positions of other pawns.
        '''
        positions = request.data
        queen_all_positions, bishop_all_positions, knight_all_positions, rook_all_positions = generate_all_positions_for_pawns(positions=positions)
        queen_valid_positions= find_queen_valid_positions(queen_all_positions, bishop_all_positions, knight_all_positions, rook_all_positions)
        queen_valid_position_chess_coordinates = list(map(get_chess_co_ordinates, queen_valid_positions))
        queen_valid_position_chess_coordinates.sort()
        return Response({'valid_response': queen_valid_position_chess_coordinates}, status=HTTP_200_OK)
    

    