import random, copy, time,pickle, pygame,numpy, random

def pawn(x, y, board, turn, all_moves,moves_done):
    if len(moves_done)>0:
        last_move=moves_done[-1]      
    if turn == '2':
        opponent = '1'
        if x == 6:
            if board[x-1][y] == '. ' and board[x-2][y] == '. ':
                all_moves.append('6'+str(y)+'4'+str(y))
            if board[x-1][y] == '. ':
                all_moves.append('6'+str(y)+'5'+str(y))
        if x>0:    
            if board[x-1][y] == '. ':
                all_moves.append(str(x)+str(y)+str(x-1)+str(y))
        if x==3:
            if y == 0:
                if board[3][1]=='P1' and last_move=='1131':
                    all_moves.append('3021')
            elif y == 7:
                if board[3][6]=='P1' and '1636'==last_move:
                    all_moves.append('3726')
            elif y > 0 and y < 7:
                if board[3][y+1]=='P1' and last_move=='1'+str(y+1)+'3'+str(y+1):
                    all_moves.append('3'+str(y)+'2'+str(y+1))
                if board[3][y-1]=='P1' and last_move=='1'+str(y-1)+'3'+str(y-1):
                    all_moves.append('3'+str(y)+'2'+str(y-1))
        if y == 0:
            if board[x-1][y+1][1]==opponent:
                all_moves.append(str(x)+str(y)+str(x-1)+str(y+1))
        elif y == 7:
            if board[x-1][y-1][1]==opponent:
                all_moves.append(str(x)+str(y)+str(x-1)+str(y-1))
        elif y > 0 and y < 7:
            if board[x-1][y+1][1]==opponent:
                all_moves.append(str(x)+str(y)+str(x-1)+str(y+1))
            if board[x-1][y-1][1]==opponent:
                all_moves.append(str(x)+str(y)+str(x-1)+str(y-1))
    elif turn == '1':
        opponent = '2'
        if x == 1:
            if board[x+1][y] == '. ' and board[x+2][y] == '. ':
                all_moves.append('1'+str(y)+'3'+str(y))
            if board[x+1][y] == '. ':
                all_moves.append('1'+str(y)+'2'+str(y))
        if x<7:    
            if board[x+1][y] == '. ':
                all_moves.append(str(x)+str(y)+str(x+1)+str(y))
        if x==4:
            if y == 0:
                if board[4][1]=='P2' and last_move=='6141':
                    all_moves.append('4051')
            elif y == 7:
                if board[4][6]=='P2' and '6646'==last_move:
                    all_moves.append('4756')
            elif y > 0 and y < 7:
                if board[4][y+1]=='P2' and last_move =='6'+str(y+1)+'4'+str(y+1):
                    all_moves.append('4'+str(y)+'5'+str(y+1))
                if board[4][y-1]=='P2' and last_move =='6'+str(y-1)+'4'+str(y-1):
                    all_moves.append('4'+str(y)+'5'+str(y-1))
        if y == 0:
            if board[x+1][y+1][1]==opponent:
                all_moves.append(str(x)+str(y)+str(x+1)+str(y+1))
        elif y == 7:
            if board[x+1][y-1][1]==opponent:
                all_moves.append(str(x)+str(y)+str(x+1)+str(y-1))
        elif y > 0 and y < 7:
            if board[x+1][y+1][1]==opponent:
                all_moves.append(str(x)+str(y)+str(x+1)+str(y+1))
            if board[x+1][y-1][1]==opponent:
                all_moves.append(str(x)+str(y)+str(x+1)+str(y-1))
    return all_moves


def knight(x, y, board, turn, all_moves):
    if turn == '2':
        opponent = '1'
    elif turn == '1':
        opponent = '2'
    if x+2 <= 7:
        if y+1<=7:
            if board[x+2][y+1] == '. ' or board[x+2][y+1][1] == opponent:
                all_moves.append(str(x)+str(y)+str(x+2)+str(y+1))
        if y-1>=0:
            if board[x+2][y-1] == '. ' or board[x+2][y-1][1] == opponent:
                all_moves.append(str(x)+str(y)+str(x+2)+str(y-1))
    if x+1 <= 7:
        if y+2<=7:
            if board[x+1][y+2] == '. ' or board[x+1][y+2][1] == opponent:
                all_moves.append(str(x)+str(y)+str(x+1)+str(y+2))
        if y-2>=0:
            if board[x+1][y-2] == '. ' or board[x+1][y-2][1] == opponent:
                all_moves.append(str(x)+str(y)+str(x+1)+str(y-2))
    if x-1 >= 0:
        if y+2<=7:
            if board[x-1][y+2] == '. ' or board[x-1][y+2][1] == opponent:
                all_moves.append(str(x)+str(y)+str(x-1)+str(y+2))
        if y-2>=0:
            if board[x-1][y-2] == '. ' or board[x-1][y-2][1] == opponent:
                all_moves.append(str(x)+str(y)+str(x-1)+str(y-2))
    if x-2 >= 0:
        if y+1<=7:
            if board[x-2][y+1] == '. ' or board[x-2][y+1][1] == opponent:
                all_moves.append(str(x)+str(y)+str(x-2)+str(y+1))
        if y-1>=0:
            if board[x-2][y-1] == '. ' or board[x-2][y-1][1] == opponent:
                all_moves.append(str(x)+str(y)+str(x-2)+str(y-1))
    return all_moves


def king(x, y, board, turn, all_moves):
    if turn == '2':
        opponent = '1'
    elif turn == '1':
        opponent = '2'
    if x+1<=7:
        if board[x+1][y] == '. ' or board[x+1][y][1] == opponent:
            all_moves.append(str(x)+str(y)+str(x+1)+str(y))
        if y+1<=7:
            if board[x+1][y+1] == '. ' or board[x+1][y+1][1] == opponent:
                all_moves.append(str(x)+str(y)+str(x+1)+str(y+1))
        if y-1>=0:
            if board[x+1][y-1] == '. ' or board[x+1][y-1][1] == opponent:
                all_moves.append(str(x)+str(y)+str(x+1)+str(y-1))
    if x-1>=0:
        if board[x-1][y] == '. ' or board[x-1][y][1] == opponent:
            all_moves.append(str(x)+str(y)+str(x-1)+str(y))
        if y+1<=7:
            if board[x-1][y+1] == '. ' or board[x-1][y+1][1] == opponent:
                all_moves.append(str(x)+str(y)+str(x-1)+str(y+1))
        if y-1>=0:
            if board[x-1][y-1] == '. ' or board[x-1][y-1][1] == opponent:
                all_moves.append(str(x)+str(y)+str(x-1)+str(y-1))
    if y+1<=7:
        if board[x][y+1] == '. ' or board[x][y+1][1] == opponent:
            all_moves.append(str(x)+str(y)+str(x)+str(y+1))
    if y-1>=0:
        if board[x][y-1] == '. ' or board[x][y-1][1] == opponent:
            all_moves.append(str(x)+str(y)+str(x)+str(y-1))
    
    return all_moves
    

def rook(x, y, board, turn, all_moves):
    if turn == '2':
        opponent = '1'
    elif turn == '1':
        opponent = '2'
    if x+1<=7:
        if board[x+1][y][1] == opponent:
            all_moves.append(str(x)+str(y)+str(x+1)+str(y))
        elif board[x+1][y] == '. ':
            all_moves.append(str(x)+str(y)+str(x+1)+str(y))
            if x+2<=7:
                if board[x+2][y][1] == opponent:
                    all_moves.append(str(x)+str(y)+str(x+2)+str(y))
                elif board[x+2][y] == '. ':
                    all_moves.append(str(x)+str(y)+str(x+2)+str(y))
                    if x+3<=7:
                        if board[x+3][y][1] == opponent:
                            all_moves.append(str(x)+str(y)+str(x+3)+str(y))
                        elif board[x+3][y] == '. ':
                            all_moves.append(str(x)+str(y)+str(x+3)+str(y))
                            if x+4<=7:
                                if board[x+4][y][1] == opponent:
                                    all_moves.append(str(x)+str(y)+str(x+4)+str(y))
                                elif board[x+4][y] == '. ':
                                    all_moves.append(str(x)+str(y)+str(x+4)+str(y))
                                    if x+5<=7:
                                        if board[x+5][y][1] == opponent:
                                            all_moves.append(str(x)+str(y)+str(x+5)+str(y))
                                        elif board[x+5][y] == '. ':
                                            all_moves.append(str(x)+str(y)+str(x+5)+str(y))
                                            if x+6<=7:
                                                if board[x+6][y][1] == opponent:
                                                    all_moves.append(str(x)+str(y)+str(x+6)+str(y))
                                                elif board[x+6][y] == '. ':
                                                    all_moves.append(str(x)+str(y)+str(x+6)+str(y))
                                                    if x+7<=7:
                                                        if board[x+7][y][1] == opponent:
                                                            all_moves.append(str(x)+str(y)+str(x+7)+str(y))
                                                        if board[x+7][y] == '. ':
                                                            all_moves.append(str(x)+str(y)+str(x+7)+str(y))
                                                        
    if y-1>=0:
        if board[x][y-1][1] == opponent:
            all_moves.append(str(x)+str(y)+str(x)+str(y-1))
        elif board[x][y-1] == '. ':
            all_moves.append(str(x)+str(y)+str(x)+str(y-1))
            if y-2>=0:
                if board[x][y-2][1] == opponent:
                    all_moves.append(str(x)+str(y)+str(x)+str(y-2))
                elif board[x][y-2] == '. ':
                    all_moves.append(str(x)+str(y)+str(x)+str(y-2))
                    if y-3>=0:
                        if board[x][y-3][1] == opponent:
                            all_moves.append(str(x)+str(y)+str(x)+str(y-3))
                        elif board[x][y-3] == '. ':
                            all_moves.append(str(x)+str(y)+str(x)+str(y-3))
                            if y-4>=0:
                                if board[x][y-4][1] == opponent:
                                    all_moves.append(str(x)+str(y)+str(x)+str(y-4))
                                elif board[x][y-4] == '. ':
                                    all_moves.append(str(x)+str(y)+str(x)+str(y-4))
                                    if y-5>=0:
                                        if board[x][y-5][1] == opponent:
                                            all_moves.append(str(x)+str(y)+str(x)+str(y-5))
                                        elif board[x][y-5] == '. ':
                                            all_moves.append(str(x)+str(y)+str(x)+str(y-5))
                                            if y-6>=0:
                                                if board[x][y-6][1] == opponent:
                                                    all_moves.append(str(x)+str(y)+str(x)+str(y-6))
                                                elif board[x][y-6] == '. ':
                                                    all_moves.append(str(x)+str(y)+str(x)+str(y-6))
                                                    if y-7>=0:
                                                        if board[x][y-7][1] == opponent:
                                                            all_moves.append(str(x)+str(y)+str(x)+str(y-7))
                                                        if board[x][y-7] == '. ':
                                                            all_moves.append(str(x)+str(y)+str(x)+str(y-7))
    
    if y+1<=7:
        if board[x][y+1][1] == opponent:
            all_moves.append(str(x)+str(y)+str(x)+str(y+1))
        elif board[x][y+1] == '. ':
            all_moves.append(str(x)+str(y)+str(x)+str(y+1))
            if y+2<=7:
                if board[x][y+2][1] == opponent:
                    all_moves.append(str(x)+str(y)+str(x)+str(y+2))
                elif board[x][y+2] == '. ':
                    all_moves.append(str(x)+str(y)+str(x)+str(y+2))
                    if y+3<=7:
                        if board[x][y+3][1] == opponent:
                            all_moves.append(str(x)+str(y)+str(x)+str(y+3))
                        elif board[x][y+3] == '. ':
                            all_moves.append(str(x)+str(y)+str(x)+str(y+3))
                            if y+4<=7:
                                if board[x][y+4][1] == opponent:
                                    all_moves.append(str(x)+str(y)+str(x)+str(y+4))
                                elif board[x][y+4] == '. ':
                                    all_moves.append(str(x)+str(y)+str(x)+str(y+4))
                                    if y+5<=7:
                                        if board[x][y+5][1] == opponent:
                                            all_moves.append(str(x)+str(y)+str(x)+str(y+5))
                                        elif board[x][y+5] == '. ':
                                            all_moves.append(str(x)+str(y)+str(x)+str(y+5))
                                            if y+6<=7:
                                                if board[x][y+6][1] == opponent:
                                                    all_moves.append(str(x)+str(y)+str(x)+str(y+6))
                                                elif board[x][y+6] == '. ':
                                                    all_moves.append(str(x)+str(y)+str(x)+str(y+6))
                                                    if y+7<=7:
                                                        if board[x][y+7][1] == opponent:
                                                            all_moves.append(str(x)+str(y)+str(x)+str(y+7))
                                                        if board[x][y+7] == '. ':
                                                            all_moves.append(str(x)+str(y)+str(x)+str(y+7))

    if x-1>=0:
        if board[x-1][y][1] == opponent:
            all_moves.append(str(x)+str(y)+str(x-1)+str(y))
        elif board[x-1][y] == '. ':
            all_moves.append(str(x)+str(y)+str(x-1)+str(y))
            if x-2>=0:
                if board[x-2][y][1] == opponent:
                    all_moves.append(str(x)+str(y)+str(x-2)+str(y))
                elif board[x-2][y] == '. ':
                    all_moves.append(str(x)+str(y)+str(x-2)+str(y))
                    if x-3>=0:
                        if board[x-3][y][1] == opponent:
                            all_moves.append(str(x)+str(y)+str(x-3)+str(y))
                        elif board[x-3][y] == '. ':
                            all_moves.append(str(x)+str(y)+str(x-3)+str(y))
                            if x-4>=0:
                                if board[x-4][y][1] == opponent:
                                    all_moves.append(str(x)+str(y)+str(x-4)+str(y))
                                elif board[x-4][y] == '. ':
                                    all_moves.append(str(x)+str(y)+str(x-4)+str(y))
                                    if x-5>=0:
                                        if board[x-5][y][1] == opponent:
                                            all_moves.append(str(x)+str(y)+str(x-5)+str(y))
                                        elif board[x-5][y] == '. ':
                                            all_moves.append(str(x)+str(y)+str(x-5)+str(y))
                                            if x-6>=0:
                                                if board[x-6][y][1] == opponent:
                                                    all_moves.append(str(x)+str(y)+str(x-6)+str(y))
                                                elif board[x-6][y] == '. ':
                                                    all_moves.append(str(x)+str(y)+str(x-6)+str(y))
                                                    if x-7>=0:
                                                        if board[x-7][y][1] == opponent:
                                                            all_moves.append(str(x)+str(y)+str(x-7)+str(y))
                                                        if board[x-7][y] == '. ':
                                                            all_moves.append(str(x)+str(y)+str(x-7)+str(y))
    
    return all_moves
  
                                                                
def bishop(x, y, board, turn, all_moves):
    if turn == '2':
        opponent = '1'
    elif turn == '1':
        opponent = '2'
    if x+1<=7 and y+1<=7:
        if board[x+1][y+1][1] == opponent:
            all_moves.append(str(x)+str(y)+str(x+1)+str(y+1))
        elif board[x+1][y+1] == '. ':
            all_moves.append(str(x)+str(y)+str(x+1)+str(y+1))
            if x+2<=7 and y+2<=7:
                if board[x+2][y+2][1] == opponent:
                    all_moves.append(str(x)+str(y)+str(x+2)+str(y+2))
                elif board[x+2][y+2] == '. ':
                    all_moves.append(str(x)+str(y)+str(x+2)+str(y+2))
                    if x+3<=7 and y+3<=7:
                        if board[x+3][y+3][1] == opponent:
                            all_moves.append(str(x)+str(y)+str(x+3)+str(y+3))
                        elif board[x+3][y+3] == '. ':
                            all_moves.append(str(x)+str(y)+str(x+3)+str(y+3))
                            if x+4<=7 and y+4<=7:
                                if board[x+4][y+4][1] == opponent:
                                    all_moves.append(str(x)+str(y)+str(x+4)+str(y+4))
                                elif board[x+4][y+4] == '. ':
                                    all_moves.append(str(x)+str(y)+str(x+4)+str(y+4))
                                    if x+5<=7 and y+5<=7:
                                        if board[x+5][y+5][1] == opponent:
                                            all_moves.append(str(x)+str(y)+str(x+5)+str(y+5))
                                        elif board[x+5][y+5] == '. ':
                                            all_moves.append(str(x)+str(y)+str(x+5)+str(y+5))
                                            if x+6<=7 and y+6<=7:
                                                if board[x+6][y+6][1] == opponent:
                                                    all_moves.append(str(x)+str(y)+str(x+6)+str(y+6))
                                                elif board[x+6][y+6] == '. ':
                                                    all_moves.append(str(x)+str(y)+str(x+6)+str(y+6))
                                                    if x+7<=7 and y+7<=7:
                                                        if board[x+7][y+7][1] == opponent:
                                                            all_moves.append(str(x)+str(y)+str(x+7)+str(y+7))
                                                        if board[x+7][y+7] == '. ':
                                                            all_moves.append(str(x)+str(y)+str(x+7)+str(y+7))
                                                        
    if x+1<=7 and y-1>=0:
        if board[x+1][y-1][1] == opponent:
            all_moves.append(str(x)+str(y)+str(x+1)+str(y-1))
        elif board[x+1][y-1] == '. ':
            all_moves.append(str(x)+str(y)+str(x+1)+str(y-1))
            if x+2<=7 and y-2>=0:
                if board[x+2][y-2][1] == opponent:
                    all_moves.append(str(x)+str(y)+str(x+2)+str(y-2))
                elif board[x+2][y-2] == '. ':
                    all_moves.append(str(x)+str(y)+str(x+2)+str(y-2))
                    if x+3<=7 and y-3>=0:
                        if board[x+3][y-3][1] == opponent:
                            all_moves.append(str(x)+str(y)+str(x+3)+str(y-3))
                        elif board[x+3][y-3] == '. ':
                            all_moves.append(str(x)+str(y)+str(x+3)+str(y-3))
                            if x+4<=7 and y-4>=0:
                                if board[x+4][y-4][1] == opponent:
                                    all_moves.append(str(x)+str(y)+str(x+4)+str(y-4))
                                elif board[x+4][y-4] == '. ':
                                    all_moves.append(str(x)+str(y)+str(x+4)+str(y-4))
                                    if x+5<=7 and y-5>=0:
                                        if board[x+5][y-5][1] == opponent:
                                            all_moves.append(str(x)+str(y)+str(x+5)+str(y-5))
                                        elif board[x+5][y-5] == '. ':
                                            all_moves.append(str(x)+str(y)+str(x+5)+str(y-5))
                                            if x+6<=7 and y-6>=0:
                                                if board[x+6][y-6][1] == opponent:
                                                    all_moves.append(str(x)+str(y)+str(x+6)+str(y-6))
                                                elif board[x+6][y-6] == '. ':
                                                    all_moves.append(str(x)+str(y)+str(x+6)+str(y-6))
                                                    if x+7<=7 and y-7>=0:
                                                        if board[x+7][y-7][1] == opponent:
                                                            all_moves.append(str(x)+str(y)+str(x+7)+str(y-7))
                                                        if board[x+7][y-7] == '. ':
                                                            all_moves.append(str(x)+str(y)+str(x+7)+str(y-7))
    
    if x-1>=0 and y+1<=7:
        if board[x-1][y+1][1] == opponent:
            all_moves.append(str(x)+str(y)+str(x-1)+str(y+1))
        elif board[x-1][y+1] == '. ':
            all_moves.append(str(x)+str(y)+str(x-1)+str(y+1))
            if x-2>=0 and y+2<=7:
                if board[x-2][y+2][1] == opponent:
                    all_moves.append(str(x)+str(y)+str(x-2)+str(y+2))
                elif board[x-2][y+2] == '. ':
                    all_moves.append(str(x)+str(y)+str(x-2)+str(y+2))
                    if x-3>=0 and y+3<=7:
                        if board[x-3][y+3][1] == opponent:
                            all_moves.append(str(x)+str(y)+str(x-3)+str(y+3))
                        elif board[x-3][y+3] == '. ':
                            all_moves.append(str(x)+str(y)+str(x-3)+str(y+3))
                            if x-4>=0 and y+4<=7:
                                if board[x-4][y+4][1] == opponent:
                                    all_moves.append(str(x)+str(y)+str(x-4)+str(y+4))
                                elif board[x-4][y+4] == '. ':
                                    all_moves.append(str(x)+str(y)+str(x-4)+str(y+4))
                                    if x-5>=0 and y+5<=7:
                                        if board[x-5][y+5][1] == opponent:
                                            all_moves.append(str(x)+str(y)+str(x-5)+str(y+5))
                                        elif board[x-5][y+5] == '. ':
                                            all_moves.append(str(x)+str(y)+str(x-5)+str(y+5))
                                            if x-6>=0 and y+6<=7:
                                                if board[x-6][y+6][1] == opponent:
                                                    all_moves.append(str(x)+str(y)+str(x-6)+str(y+6))
                                                elif board[x-6][y+6] == '. ':
                                                    all_moves.append(str(x)+str(y)+str(x-6)+str(y+6))
                                                    if x-7>=0 and y+7<=7:
                                                        if board[x-7][y+7][1] == opponent:
                                                            all_moves.append(str(x)+str(y)+str(x-7)+str(y+7))
                                                        if board[x-7][y+7] == '. ':
                                                            all_moves.append(str(x)+str(y)+str(x-7)+str(y+7))

    if x-1>=0 and y-1>=0:
        if board[x-1][y-1][1] == opponent:
            all_moves.append(str(x)+str(y)+str(x-1)+str(y-1))
        elif board[x-1][y-1] == '. ':
            all_moves.append(str(x)+str(y)+str(x-1)+str(y-1))
            if x-2>=0 and y-2>=0:
                if board[x-2][y-2][1] == opponent:
                    all_moves.append(str(x)+str(y)+str(x-2)+str(y-2))
                elif board[x-2][y-2] == '. ':
                    all_moves.append(str(x)+str(y)+str(x-2)+str(y-2))
                    if x-3>=0 and y-3>=0:
                        if board[x-3][y-3][1] == opponent:
                            all_moves.append(str(x)+str(y)+str(x-3)+str(y-3))
                        elif board[x-3][y-3] == '. ':
                            all_moves.append(str(x)+str(y)+str(x-3)+str(y-3))
                            if x-4>=0 and y-4>=0:
                                if board[x-4][y-4][1] == opponent:
                                    all_moves.append(str(x)+str(y)+str(x-4)+str(y-4))
                                elif board[x-4][y-4] == '. ':
                                    all_moves.append(str(x)+str(y)+str(x-4)+str(y-4))
                                    if x-5>=0 and y-5>=0:
                                        if board[x-5][y-5][1] == opponent:
                                            all_moves.append(str(x)+str(y)+str(x-5)+str(y-5))
                                        elif board[x-5][y-5] == '. ':
                                            all_moves.append(str(x)+str(y)+str(x-5)+str(y-5))
                                            if x-6>=0 and y-6>=0:
                                                if board[x-6][y-6][1] == opponent:
                                                    all_moves.append(str(x)+str(y)+str(x-6)+str(y-6))
                                                elif board[x-6][y-6] == '. ':
                                                    all_moves.append(str(x)+str(y)+str(x-6)+str(y-6))
                                                    if x-7>=0 and y-7>=0:
                                                        if board[x-7][y-7][1] == opponent:
                                                            all_moves.append(str(x)+str(y)+str(x-7)+str(y-7))
                                                        if board[x-7][y-7] == '. ':
                                                            all_moves.append(str(x)+str(y)+str(x-7)+str(y-7))
    
    return all_moves
    
    
def queen(x, y, board, turn, all_moves):
    return bishop(x, y, board, turn, all_moves) + rook(x, y, board, turn, all_moves)


def castle(x, y, board, turn, all_moves, moves_done):
    self_long = True
    self_short = True
    if turn=='1':
        if board[0][4] != '. ' or board[0][5]!='. ' or board[0][6]!='. ':
            self_long = False
        if board[0][2] != '. ' or board[0][1]!='. ':
            self_short = False
    elif turn=='2':
        if board[7][4] != '. ' or board[7][5]!='. ' or board[7][6]!='. ':
            self_long = False
        if board[7][1] != '. ' or board[7][2]!='. ':
            self_short = False
    for j in range(len(moves_done)):
        if turn=='1':
            if moves_done[j][0]=='0' and moves_done[j][1]=='3':
                self_long, self_short = False, False
            elif moves_done[j][0]=='0' and moves_done[j][1]=='0':
                self_short = False
            elif moves_done[j][0]=='0' and moves_done[j][1]=='7':
                self_long = False
        elif turn=='2':
            if moves_done[j][0]=='7' and moves_done[j][1]=='3':
                self_long, self_short = False, False
            elif moves_done[j][0]=='7' and moves_done[j][1]=='0':
                self_short = False
            elif moves_done[j][0]=='7' and moves_done[j][1]=='7':
                self_long = False
    if turn=='1':
        if board[0][3]=='K1':
            if board[0][0]!='R1':
                self_short=False
            if board[0][7]!='R1':
                self_long=False
        else:
            self_long, self_short=False,False
    elif turn=='2':
        if board[7][3]=='K2':
            if board[7][0]!='R2':
                self_short=False
            if board[7][7]!='R2':
                self_long=False
        else:
            self_long, self_short=False,False
    if self_long == True:
        if turn=='1':
            all_moves.append('0305')
        else:
            all_moves.append('7375')
    if self_short == True:
        if turn=='1':
            all_moves.append('0301')
        else:
            all_moves.append('7371')
    return all_moves


def possible_moves(board, turn, position, all_moves, moves_done):
    for x in range(len(board)):
        for y in range(len(board)):
            if board[x][y][1] == turn:
                if board[x][y][0] == 'P':
                    all_moves = pawn(x, y, board, turn, all_moves,moves_done)
                elif board[x][y][0] == 'N':
                    all_moves = knight(x, y, board, turn, all_moves)
                elif board[x][y][0] == 'B':
                    all_moves = bishop(x, y, board, turn, all_moves)
                elif board[x][y][0] == 'R':
                    all_moves = rook(x, y, board, turn, all_moves)
                elif board[x][y][0] == 'Q':
                    all_moves = queen(x, y, board, turn, all_moves)
                elif board[x][y][0] == 'K':
                    all_moves = king(x, y, board, turn, all_moves)
                
            else:
                continue
    all_moves=castle(x, y, board, turn, all_moves, moves_done)
    return all_moves


def change_board(board, move, turn,moves_done):
    x,y=int(move[0]), int(move[1])
    if len(moves_done)>1:
        last_move=moves_done[-2]
    else:
        last_move='9999'
    if (move == '0301' and turn == '1' and board[0][3]=='K1'): #what happens if another piece does this move
        board[0][1]='K1'
        board[0][2]='R1'
        board[0][0], board[0][3]='. ', '. '
    elif turn=='2' and board[7][3]=='K2' and move == '7371':
        board[7][1]='K2'
        board[7][2]='R2'
        board[7][0], board[7][3]='. ', '. '
    elif (turn == '1' and move =='0305' and board[0][3]=='K1'):
        board[0][5]='K1'
        board[0][4]='R1'
        board[0][7], board[0][3]='. ', '. '
    elif turn=='2' and board[7][3]=='K2' and move == '7375':
        board[7][5]='K2'
        board[7][4]='R2'
        board[7][7], board[7][3]='. ', '. '
    elif turn=='1' and x==4 and y+1==int(move[3]) and move[2]=='5' and board[x][y]=='P1' and board[x][y+1]=='P2' and last_move== ('6'+str(y+1)+'4'+str(y+1)):
        piece = board[x][y]
        board[x][y] = '. '
        board[x][y+1] = '. '
        board[int(move[2])][int(move[3])] = piece
    elif last_move== ('6'+str(y-1)+'4'+str(y-1)) and turn=='1' and board[x][y]=='P1' and board[x][y-1]=='P2' and x==4 and y-1==int(move[3]) and move[2]=='5':
        piece = board[x][y]
        board[x][y] = '. '
        board[x][y-1] = '. '
        board[int(move[2])][int(move[3])] = piece
    elif turn=='2' and x==3 and y+1==int(move[3]) and move[2]=='2' and board[x][y]=='P1' and board[x][y+1]=='P2' and last_move==('1'+str(y+1)+'3'+str(y+1)):
        piece = board[x][y]
        board[x][y] = '. '
        board[x][y+1] = '. '
        board[int(move[2])][int(move[3])] = piece
    elif turn=='2' and x==3 and y-1==int(move[3]) and move[2]=='2' and board[x][y]=='P1' and board[x][y-1]=='P2' and last_move==('1'+str(y-1)+'3'+str(y-1)):
        piece = board[x][y]
        board[x][y] = '. '
        board[x][y-1] = '. '
        board[int(move[2])][int(move[3])] = piece
    else:
        piece = board[int(move[0])][int(move[1])]
        board[int(move[0])][int(move[1])] = '. '
        board[int(move[2])][int(move[3])] = piece
    return board


def count_pieces(board,turn):
    count=0
    for x in board:
        for y in x:
            if y[1]==turn and (y[0] == 'R' or y[0] == 'B' or y[0] == 'N'):
                count+=1
    return count
    

def endgame(board):
    endgame=False
    a,b,c,d=False,False,True,True
    for x in range(len(board)):
        if 'Q1' in board[x]:
            c=False
            if count_pieces(board, '1')<=1:
                a=True
        if 'Q2' in board[x]:
            d=False
            if count_pieces(board, '2')<=1:
                b=True
    if (a and b) or (c and d):
        endgame=True
    return endgame
    
    
def move_evaluation(board, position, tables1,tables2):
    # if double pawn -70
    b1=0
    b2=0
    end=endgame(board)
    for x in range(len(board)):
        for y in range(len(board)):
            v=board[x][y]
            if v == 'P1':
                position=position+tables1[v][x][y]
                position = position + 100
            elif v == 'P2':
                position=position-tables2[v][x][y]
                position = position - 100
            elif v == 'R1':
                position=position+tables1[v][x][y]
                position = position +500
            elif v == 'R2':
                position = position -(500+tables2[v][x][y])
            elif v == 'N1':
                position = position +320
                position=position+tables1[v][x][y]
            elif v == 'N2':
                position = position -320
                position=position-tables2[v][x][y]
            elif v =='B1':
                b1+=1
                position = position +330
                position=position+tables1[v][x][y]
            elif v =='B2':
                b2+=1
                position = position -330
                position=position-tables2[v][x][y]
            elif v == 'Q1':
                position = position +900 
                position=position+tables1[v][x][y]          
            elif v == 'Q2':
                position = position -900
                position=position-tables2[v][x][y]
            elif v == 'K1' and not end:
                position = position +20000
                position=position+tables1[v][x][y]
            elif v == 'K2' and not end:
                position = position -20000
                position=position-tables2[v][x][y]
            elif v == 'K1' and end:
                position = position +20000
                position=position+tables1['E1'][x][y]
            elif v == 'K2' and end:
                position = position -20000
                position=position-tables2['E2'][x][y]
    if b2==2:
        position-=50
    if b1==2:
        position+=50
    position=round(position,4)
    return position


def print_board(board,dis,images,graphic):
    board=numpy.rot90(board, 2)
    if not graphic:
        for x in range(len(board)):
            for y in range(len(board)):
                print(board[x][y], end=" "),
            print('')
    else:
        board_setup(dis)
        for x in range(len(board)):
            for y in range(len(board)):
                if board[x][y] != '. ':
                    dis.blit(images[board[x][y]], (60*y, 60*x))
        pygame.display.update()
        return dis


def random_best(position, board, all_moves, moves_done, turn,count,tables1,tables2,depth):
    if depth==2:
        if turn=='2':
            opponent='1'
        else:
            opponent='2'
        b=possible_moves(board, opponent, position, all_moves, moves_done)
        g={}
        for x in b:
            boarda = copy.deepcopy(board)
            boarda = change_board(boarda, x, opponent, moves_done)
            all_moves=[]
            a = possible_moves(boarda, turn, position, all_moves, moves_done)
            c=[]
            for y in a:
                boardb = copy.deepcopy(boarda)
                boardb = change_board(boardb, y, turn, moves_done)
                count+=1
                c.append(move_evaluation(boardb, position,tables1,tables2))
                #c.append(quiesce(boardb,'1',all_moves,moves_done,tables1,tables2))
            g[x]=max(c)
        if turn == "1":
            if len(g.keys())>3:
            #if there's more than 3 possible moves, then we pick the 3 best ones
                toconsider = []
                m=10**5
                for key in g.keys():
                    if g[key]<m:
                        m=g[key]
                        index = key
                toconsider.append(index)
                m=10**5
                for key in g.keys():
                    if g[key]<m and key!=toconsider[0]:
                        m=g[key]
                        index = key
                toconsider.append(index)
                m=10**5
                for key in g.keys():
                    if g[key]<m and key!=toconsider[0] and key!=toconsider[-1]:
                        m=g[key]
                        index = key
                toconsider.append(index)
                #then tries to add some randomness to its playing
                #might need to play around with the probability stuff
                temp=random.uniform(0.0,1.0/g[toconsider[0]]+1.0/g[toconsider[1]]+1.0/g[toconsider[2]])
                if temp<1.0/g[toconsider[0]]:
                    return toconsider[0],count
                if temp<1.0/g[toconsider[0]]+1.0/g[toconsider[1]]:
                    return toconsider[1],count
                else:
                    return toconsider[-1], count
            else:
                move = min(g, key=g.get)
                return move, count
        else:
            if len(g.keys())>3:
                toconsider = []
                m=-10**5
                for key in g.keys():
                    if g[key]>m:
                        m=g[key]
                        index = key
                toconsider.append(index)
                m=-10**5
                for key in g.keys():
                    if g[key]>m and key!=toconsider[0]:
                        m=g[key]
                        index = key
                toconsider.append(index)
                m=-10**5
                for key in g.keys():
                    if g[key]>m and key!=toconsider[0] and key!=toconsider[-1]:
                        m=g[key]
                        index = key
                toconsider.append(index)
                #then tries to add some randomness to its playing
                #might need to play around with the probability stuff
                temp=random.uniform(0.0,1.0/g[toconsider[0]]+1.0/g[toconsider[1]]+1.0/g[toconsider[2]])
                if temp<1.0/g[toconsider[0]]:
                    return toconsider[0],count
                if temp<1.0/g[toconsider[0]]+1.0/g[toconsider[1]]:
                    return toconsider[1],count
                else:
                    return toconsider[-1], count
            else:
                move = max(g, key=g.get)
                return move, count

    elif depth==3:
        b=possible_moves(board, turn, position, all_moves, moves_done)
        g=[]
        h=[]
        if turn=='2':
            opponent='1'
        else:
            opponent='2'
        for x in b:
            boarda = copy.deepcopy(board)
            boarda = change_board(boarda, x, turn, moves_done)
            all_moves=[]
            a = possible_moves(boarda, opponent, position, all_moves, moves_done)
            c=[]
            for y in a:
                boardb = copy.deepcopy(boarda)
                boardb = change_board(boardb, y, opponent, moves_done)
                d=[]
                all_moves=[]
                third = possible_moves(boardb, turn, position, all_moves, moves_done)
                for w in third:
                    boardc = copy.deepcopy(boardb)
                    boardc = change_board(boardc, w, turn, moves_done)
                    d.append(move_evaluation(boardc, position,tables1,tables2))
                    #d.append(quiesce(boardc,'2',all_moves,moves_done,tables1,tables2))
                    
                    count+=1
                c.append(min(d))
            g.append(max(c))
            h.append(x)
        minimum = min(g)
        indices = [i for i, v in enumerate(g) if v == minimum]
        k=[]
        for t in indices:
            k.append(h[t])
        move=random.choice(k)
        return move,count


def alphabeta(alpha, beta, depth, position, board, all_moves, moves_done, turn, count,tables1,tables2):
    bestscore=-99999
    if depth==0:
        count+=1
        value=-quiesce(board,turn,all_moves,moves_done,tables1,tables2)
        return value,count
    if turn=='1':
        t='2'
    else:
        t='1'
    for move in possible_moves(board,turn,position,all_moves,moves_done):
        boarda=copy.deepcopy(board)
        boarda=change_board(boarda,move,t,moves_done)
        a=alphabeta(-beta,-alpha,depth-1,position,boarda,all_moves,moves_done,t,count,tables1,tables2)
        score,count=-a[1],a[0]
        if score>=beta:
            return score, count
        if( score > bestscore ):
            bestscore = score
        if( score > alpha ):
            alpha = score  
    return bestscore,count
    
    
def selectmove(depth,board, turn, position, all_moves, moves_done,count,tables1,tables2):
    bestMove = ''
    bestValue = -99999
    alpha = -100000
    beta = 100000
    if turn=='1':
        t='2'
    else:
        t='1'
    for move in possible_moves(board,turn,position,all_moves,moves_done):
        boarda=copy.deepcopy(board)
        boarda=change_board(boarda,move,t,moves_done)
        a=alphabeta(-beta,-alpha,depth-1,position,boarda,all_moves,moves_done,t,count,tables1,tables2)
        moveValue,count=-a[0],a[1]
        if moveValue>bestValue:
            bestValue=moveValue
            bestMove=move
        if moveValue>alpha:
            alpha=moveValue
    return bestMove,count


def quiesce(board,turn,all_moves,moves_done,tables1,tables2):
    maxscore=-99999
    if turn=='1':
        t='2'
    else:
        t='1'
    for move in possible_moves(board,turn,0,all_moves,moves_done):
        if iscapture(board,move,t,moves_done):
            board=change_board(board,move,t,moves_done)
            w=-quiesce(board,t,all_moves,moves_done,tables1,tables2)
            if w>maxscore:
                maxscore=w
        else:
            return move_evaluation(board, 0, tables1,tables2)
    return maxscore
    

def iscapture(board, move,turn, moves_done):
    x,y=int(move[0]), int(move[1])
    if len(moves_done)>1:
        last_move=moves_done[-2]
    else:
        last_move='9999'
    if turn=='1':
        opponent='2'
    else:
        opponent='1'
    capture=False
    if (move == '0301' and turn == '1' and board[0][3]=='K1'):
        pass
    elif turn=='2' and board[7][3]=='K2' and move == '7371':
        pass
    elif (turn == '1' and move =='0305' and board[0][3]=='K1'):
        pass
    elif turn=='2' and board[7][3]=='K2' and move == '7375':
        pass
    elif turn=='1' and x==4 and y+1==int(move[3]) and move[2]=='5' and board[x][y]=='P1' and board[x][y+1]=='P2' and last_move== ('6'+str(y+1)+'4'+str(y+1)):
        capture=True
    elif last_move== ('6'+str(y-1)+'4'+str(y-1)) and turn=='1' and board[x][y]=='P1' and board[x][y-1]=='P2' and x==4 and y-1==int(move[3]) and move[2]=='5':
        capture=True
    elif turn=='2' and x==3 and y+1==int(move[3]) and move[2]=='2' and board[x][y]=='P1' and board[x][y+1]=='P2' and last_move==('1'+str(y+1)+'3'+str(y+1)):
        capture=True
    elif turn=='2' and x==3 and y-1==int(move[3]) and move[2]=='2' and board[x][y]=='P1' and board[x][y-1]=='P2' and last_move==('1'+str(y-1)+'3'+str(y-1)):
        capture=True
    else:
        if board[int(move[2])][int(move[3])][1] == opponent:
            capture=True
    return capture


def board_setup(dis):
    dis.fill((100,50,0))
    for x in range(0,8):
        if x%2!=0:
            for y in range(1,8,2):
                button = pygame.Rect(60*x, 60*y, 60, 60)
                pygame.draw.rect(dis, [202, 164, 114], button)
        else:
            for y in range(0,8,2):
                button = pygame.Rect(60*x, 60*y, 60, 60)
                pygame.draw.rect(dis, [202, 164, 114], button)

