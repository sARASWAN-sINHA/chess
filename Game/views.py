from rest_framework.viewsets import ViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK


from util.services import generate_all_positions_for_pawns, find_valid_position_for_pawn
class PawnPositionsViewSet(ViewSet):

    @action(detail=False, methods=['GET'])
    def knight(self, request, *args, **kwargs):
        '''
            Will generate all the valid positions for Knight
            given the positions of other pawns.
        '''
        positions = request.data
        pawns_all_positions = generate_all_positions_for_pawns(positions=positions)
        knight_valid_position_chess_coordinates = find_valid_position_for_pawn('knight', *pawns_all_positions)
        return Response({'valid_response': knight_valid_position_chess_coordinates}, status=HTTP_200_OK)
    
    @action(detail=False, methods=['GET'])
    def rook(self, request, *args, **kwargs):
        '''
            Will generate all the valid positions for Rook
            given the positions of other pawns.
        '''
        positions = request.data
        pawns_all_positions = generate_all_positions_for_pawns(positions=positions)
        rook_valid_position_chess_coordinates = find_valid_position_for_pawn('rook', *pawns_all_positions)
        return Response({'valid_response': rook_valid_position_chess_coordinates}, status=HTTP_200_OK)
    
    @action(detail=False, methods=['GET'])
    def bishop(self, request, *args, **kwargs):
        '''
            Will generate all the valid positions for Bishop
            given the positions of other pawns.
        '''
        positions = request.data
        pawns_all_positions = generate_all_positions_for_pawns(positions=positions)
        bishop_valid_position_chess_coordinates = find_valid_position_for_pawn('bishop', *pawns_all_positions)
        return Response({'valid_response': bishop_valid_position_chess_coordinates}, status=HTTP_200_OK)
    
    @action(detail=False, methods=['GET'])
    def queen(self, request, *args, **kwargs):
        '''
            Will generate the all valid positions for Queen
            given the positions of other pawns.
        '''
        positions = request.data
        pawns_all_positions = generate_all_positions_for_pawns(positions=positions)
        queen_valid_position_chess_coordinates = find_valid_position_for_pawn('queen', *pawns_all_positions)
        return Response({'valid_response': queen_valid_position_chess_coordinates}, status=HTTP_200_OK)
    

    