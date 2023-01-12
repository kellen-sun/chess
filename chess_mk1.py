#14.03.2020
#Main File
import random, copy, time, sys, pickle, numpy

print(sys.version)
graphic = True
if graphic:
    import pygame
    
'''from chess_pieces import (pawn, knight, rook, king, bishop,
queen, castle, possible_moves, change_board, move_evaluation, print_board, 
random_best, board_setup, alphabeta, quiesce, selectmove)'''

from chess_pieces import random_best, print_board, endgame, possible_moves,change_board,selectmove 

#alpha-beta pruning (calculate current or will be average board pos, and only consider better moves)
#more depth
#opening book
#better piece position value, double pawns...
#bitboards?
#issue with the white queen

def promotion(board, turn):
    if turn=='1':
        for x in range(len(board)):
            if board[7][x]=='P1':
                board[7][x]='Q1'
    elif turn=='2':
        for x in range(len(board)):
            if board[0][x]=='P2':
                board[0][x]='Q2'

sys.setrecursionlimit(10000)

board = [
['R1', 'N1', 'B1', 'K1', 'Q1', 'B1', 'N1', 'R1'],
['P1', 'P1', 'P1', 'P1', 'P1', 'P1', 'P1', 'P1'],
['. ', '. ', '. ', '. ', '. ', '. ', '. ', '. '],
['. ', '. ', '. ', '. ', '. ', '. ', '. ', '. '],
['. ', '. ', '. ', '. ', '. ', '. ', '. ', '. '],
['. ', '. ', '. ', '. ', '. ', '. ', '. ', '. '],
['P2', 'P2', 'P2', 'P2', 'P2', 'P2', 'P2', 'P2'],
['R2', 'N2', 'B2', 'K2', 'Q2', 'B2', 'N2', 'R2'],
]


tables2={
'P2':[
[0,0,0,0,0,0,0,0],
[50, 50, 50, 50, 50, 50, 50, 50],
[10, 10, 20, 30, 30, 20, 10, 10],
[5,  5, 10, 27, 27, 10,  5,  5],
[0,  0,  0, 24, 24,  0,  0,  0],
[5, -5,-10,  0,  0,-10, -5,  5],
[5, 10, 10,-27,-27, 10, 10,  5],
[0,  0,  0,  0,  0,  0,  0,  0]
],
'N2':[
[-50,-37,-30,-30,-30,-30,-37,-50],
[-40,-25,  0,  0,  0,  0,-25,-40],
[-30,  0, 10, 15, 15, 10,  0,-30],
[-30,  5, 15, 20, 20, 15,  5,-30],
[-30,  0, 15, 20, 20, 15,  0,-30],
[-30,  6, 10, 15, 15, 10,  6,-30],
[-40,-25,  0,  5,  5,  0,-25,-40],
[-50,-37,-30,-30,-30,-30,-37,-50]
],
'B2':[
[-20,-10,-10,-10,-10,-10,-10,-20],
[-10,  0,  0,  0,  0,  0,  0,-10],
[-10,  0,  5, 10, 10,  5,  0,-10],
[-10,  5,  5, 10, 10,  5,  5,-10],
[-10,  0, 10, 10, 10, 10,  0,-10],
[-10, 10, 10, 10, 10, 10, 10,-10],
[-10,  5,  0,  0,  0,  0,  5,-10],
[-20,-10,-10,-10,-10,-10,-10,-20]
],
'R2':[
[0,  0,  0,  0,  0,  0,  0,  0],
[  5, 10, 10, 10, 10, 10, 10,  5],
[ -5,  0,  0,  0,  0,  0,  0, -5],
[ -5,  0,  0,  0,  0,  0,  0, -5],
[ -5,  0,  0,  0,  0,  0,  0, -5],
[ -5,  0,  0,  0,  0,  0,  0, -5],
[ -5,  0,  0,  0,  0,  0,  0, -5],
[  0,  0,  0,  5,  5,  0,  0,  0]
],
'Q2':[
[-20,-10,-10, -5, -5,-10,-10,-20],
[-10,  0,  0,  0,  0,  0,  0,-10],
[-10,  0,  5,  5,  5,  5,  0,-10],
[ -5,  0,  5,  5,  5,  5,  0, -5],
[  0,  0,  5,  5,  5,  5,  0, -5],
[-10,  5,  5,  5,  5,  5,  0,-10],
[-10,  0,  5,  0,  0,  0,  0,-10],
[-20,-10,-10, -5, -5,-10,-10,-20]
],
'K2':[
[-30,-40,-40,-50,-50,-40,-40,-30],
[-30,-40,-40,-50,-50,-40,-40,-30],
[-30,-40,-40,-50,-50,-40,-40,-30],
[-30,-40,-40,-50,-50,-40,-40,-30],
[-20,-30,-30,-40,-40,-30,-30,-20],
[-10,-20,-20,-20,-20,-20,-20,-10],
[ 20, 20,  0,  0,  0,  0, 20, 20],
[ 20, 30, 10,  0,  0, 10, 30, 20]
],
'E2':[
[-50,-40,-30,-20,-20,-30,-40,-50],
[-30,-20,-10,  0,  0,-10,-20,-30],
[-30,-10, 20, 30, 30, 20,-10,-30],
[-30,-10, 30, 40, 40, 30,-10,-30],
[-30,-10, 30, 40, 40, 30,-10,-30],
[-30,-10, 20, 30, 30, 20,-10,-30],
[-30,-30,  0,  0,  0,  0,-30,-30],
[-50,-30,-30,-30,-30,-30,-30,-50]
]
}
tables1 = {}
for r in tables2.keys():
    tables1[r[0]+'1']=numpy.flip(tables2[r],1)

turn = '2'
position = 0
troll=True
game_not_over = True
all_moves = []
moves_done = []

images={}
if graphic:
    images['B2'] = pygame.image.load(r'C:\Users\sunke\Desktop\Kellen\Programming\python\projects\chess\images\Chess_bdl45.jpg')
    images['B1'] = pygame.image.load(r'C:\Users\sunke\Desktop\Kellen\Programming\python\projects\chess\images\Chess_bll45.jpg')
    images['P2'] = pygame.image.load(r'C:\Users\sunke\Desktop\Kellen\Programming\python\projects\chess\images\Chess_pdl45.jpg')
    images['P1'] = pygame.image.load(r'C:\Users\sunke\Desktop\Kellen\Programming\python\projects\chess\images\Chess_pll45.jpg')
    images['R2'] = pygame.image.load(r'C:\Users\sunke\Desktop\Kellen\Programming\python\projects\chess\images\Chess_rdl45.jpg')
    images['R1'] = pygame.image.load(r'C:\Users\sunke\Desktop\Kellen\Programming\python\projects\chess\images\Chess_rll45.jpg')
    images['N2'] = pygame.image.load(r'C:\Users\sunke\Desktop\Kellen\Programming\python\projects\chess\images\Chess_ndl45.jpg')
    images['N1'] = pygame.image.load(r'C:\Users\sunke\Desktop\Kellen\Programming\python\projects\chess\images\Chess_nll45.jpg')
    images['Q2'] = pygame.image.load(r'C:\Users\sunke\Desktop\Kellen\Programming\python\projects\chess\images\Chess_qdl45.jpg')
    images['Q1'] = pygame.image.load(r'C:\Users\sunke\Desktop\Kellen\Programming\python\projects\chess\images\Chess_qll45.jpg')
    images['K2'] = pygame.image.load(r'C:\Users\sunke\Desktop\Kellen\Programming\python\projects\chess\images\Chess_kdl45.jpg')
    images['K1'] = pygame.image.load(r'C:\Users\sunke\Desktop\Kellen\Programming\python\projects\chess\images\Chess_kll45.jpg')


    pygame.init()
    pygame.display.set_caption('Chess')
    dis = pygame.display.set_mode((480, 480))
else:
    dis=''

print_board(board,dis,images,graphic)
move=''
while game_not_over:
    if troll and endgame(board):
        troll=False
        dis.blit(pygame.font.SysFont("comicsansms", 36).render("We're in the endgame now.", True, (250, 0, 0)), [10, 200])
        pygame.display.update()
        time.sleep(3)
        print_board(board,dis,images,graphic)
    if graphic:
        if len(move)!=2:
            move=''
            dis=print_board(board,dis,images,graphic)
            pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                q,w = mouse_pos[0]//60, mouse_pos[1]//60
                move=move+str(7-w)+str(7-q)
                pygame.draw.circle(dis, (0,0,250), (q*60+25,w*60+25), 20,1)  
                pygame.display.update()
    else:
        move = input('Your move? ')
    position=0
    if len(move)==4:
        print(move)
        if move in possible_moves(board, '1', position, all_moves, moves_done):
            moves_done.append(move)
            change_board(board, move, '1', moves_done)
            promotion(board, '1')
            dis=print_board(board,dis,images,graphic)
            if graphic:
                pygame.display.update()
            all_moves=[]
            count=0
            t=time.time()
            move,count=random_best(position, board, all_moves, moves_done, turn,count,tables1,tables2,2)
            #move,count=selectmove(2,board,turn,position,all_moves, moves_done, count,tables1,tables2)
            print('')
            print('Computer analyzed '+str(count)+' moves in '+str(round(time.time()-t,4))+' seconds.')
            print(move)
            print('')
            moves_done.append(move)
            board=change_board(board, move, '2',moves_done)
            promotion(board, '2')
            dis=print_board(board,dis,images,graphic)
            if graphic:
                pygame.display.update()
        else:
            print('illegal move')
    all_moves = []
