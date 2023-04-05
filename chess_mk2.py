import random, copy, time, sys, pickle, numpy, pygame

#Piece identifiers
noPiece = 0
King = 1
Pawn = 2
Knight = 3
Bishop = 4
Rook = 5
Queen = 6
White = 8
Black = 16

#Graphics
images=[0 for i in range(23)]
images[Bishop+Black] = pygame.image.load(r'C:\Users\sunke\Desktop\Kellen\Programming\python\projects\chess\images\Chess_bdl45.png')
images[Bishop+White] = pygame.image.load(r'C:\Users\sunke\Desktop\Kellen\Programming\python\projects\chess\images\Chess_bll45.png')
images[Pawn+Black] = pygame.image.load(r'C:\Users\sunke\Desktop\Kellen\Programming\python\projects\chess\images\Chess_pdl45.png')
images[Pawn+White] = pygame.image.load(r'C:\Users\sunke\Desktop\Kellen\Programming\python\projects\chess\images\Chess_pll45.png')
images[Rook+Black] = pygame.image.load(r'C:\Users\sunke\Desktop\Kellen\Programming\python\projects\chess\images\Chess_rdl45.png')
images[Rook+White] = pygame.image.load(r'C:\Users\sunke\Desktop\Kellen\Programming\python\projects\chess\images\Chess_rll45.png')
images[Knight+Black] = pygame.image.load(r'C:\Users\sunke\Desktop\Kellen\Programming\python\projects\chess\images\Chess_ndl45.png')
images[Knight+White] = pygame.image.load(r'C:\Users\sunke\Desktop\Kellen\Programming\python\projects\chess\images\Chess_nll45.png')
images[Queen+Black] = pygame.image.load(r'C:\Users\sunke\Desktop\Kellen\Programming\python\projects\chess\images\Chess_qdl45.png')
images[Queen+White] = pygame.image.load(r'C:\Users\sunke\Desktop\Kellen\Programming\python\projects\chess\images\Chess_qll45.png')
images[King+Black] = pygame.image.load(r'C:\Users\sunke\Desktop\Kellen\Programming\python\projects\chess\images\Chess_kdl45.png')
images[King+White] = pygame.image.load(r'C:\Users\sunke\Desktop\Kellen\Programming\python\projects\chess\images\Chess_kll45.png')

class Board:
    """All information necessary for a board position"""
    def __init__(self, board, castling, turn, en_passant_target, all_moves):
        self.board = board
        self.castling = castling
        self.turn = turn
        self.en_passant_target = en_passant_target
        self.all_moves = all_moves

    def move(self, move):
        """Given a move the board is changed accordingly"""
        #write exceptions for castling and en_passant
        move1 = move%65-1
        move0 = move//65-1
        self.board[move1]=self.board[move0]
        self.board[move0]=0
        self.turn = 1-self.turn

    def possible_moves(self):
        """Returns the possible moves"""
        self.pmoves = []
        for i in range(len(self.board)):
            piece = self.board[i]
            #i is the position on the board, piece is which piece it is.
            if piece>0 and piece//8 == self.turn+1:
                if piece==Knight+(1+self.turn)*8:
                    increments = [-17, -15, -10, -6, 6, 10, 15, 17]
                    for j in increments:
                        if 0<=j+i<64 and abs(i%8 -(i+j)%8)<=2:
                            #checks the square the knight is jumping to exists on the board
                            if self.board[i+j]//8!=self.turn+1:
                                #checks the landing square is not occupied by a piece of the same color
                                self.pmoves.append(65*(i+1)+i+j+1)
                if piece==King+(1+self.turn)*8:
                    increments = [-9, -8, -7, -1, 1, 7, 8, 9]
                    for j in increments:
                        if 0<=j+i<64 and abs(i%8 -(i+j)%8)<=1:
                            #checks the square the king is jumping to exists on the board
                            if self.board[i+j]//8!=self.turn+1:
                                #checks the landing square is not occupied by a piece of the same color
                                self.pmoves.append(65*(i+1)+i+j+1)
                if piece==Rook+(1+self.turn)*8 or piece==Queen+(1+self.turn)*8:
                    increments = [-8, -1, 1, 8]
                    for j in increments:
                        for k in range(1, 8):
                            if 0<=i+k*j<64 and (i//8==(i+k*j)//8 or i%8==(i+k*j)%8):
                                if self.board[i+k*j]//8 != self.turn+1 and self.board[i+k*j]!=0:
                                    #if taking piece of opposite color
                                    self.pmoves.append(65*(i+1)+i+k*j+1)
                                    break
                                elif self.board[i+k*j]==0:
                                    #if empty square
                                    self.pmoves.append(65*(i+1)+i+k*j+1)
                                else:
                                    break
                if piece==Bishop+(1+self.turn)*8 or piece==Queen+(1+self.turn)*8:
                    increments = [-9, -7, 7, 9]
                    for j in increments:
                        for k in range(1, 8):
                            if 0<=i+k*j<64 and ((i+k*j)%8+(i+k*j)//8)%2==(i//8+i%8)%2:
                                if self.board[i+k*j]//8 != self.turn+1 and self.board[i+k*j]!=0:
                                    #if taking piece of opposite color
                                    self.pmoves.append(65*(i+1)+i+k*j+1)
                                    break
                                elif self.board[i+k*j]==0:
                                    #if empty square
                                    self.pmoves.append(65*(i+1)+i+k*j+1)
                                else:
                                    break
                if piece==Pawn+(1+self.turn)*8:
                    
        return self.pmoves
        

#Starting position
currentboard = Board([21, 19, 20, 22, 17, 20, 19, 21, 18, 18, 18, 18, 18, 18, 18, 18, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 10, 10, 10, 10, 10, 10, 10, 13, 11, 12, 14, 9, 12, 11, 13], "KQkq", 0, -1, [])

#0 represents white's turn, 1 represents black's turn
#Capital letter for white's castling

move = 0 #takes the form 65*(first position+1) + second position +1
#move variable is to track where the user clicked

#PyGame Setup
pygame.init()
pygame.display.set_caption('Chess')
dis = pygame.display.set_mode((480, 480))
game_not_over = True


def update_board_graphics(board, dis, images):
    '''Updates the pygame display with the current position of pieces on the baord.'''
    dis.fill((100,50,0))
    for x in range(8):
        for y in range(8):
            if (x+y)%2==0:
                square = pygame.Rect(60*x, 60*y, 60, 60)
                pygame.draw.rect(dis, [202, 164, 114], square)
    for x in range(8):
        for y in range(8):
            if board[x*8+y] != 0:
                dis.blit(images[board[x*8+y]], (60*y, 60*x))
    return dis

def fen_builder(string):
    """Builds a board position given the FEN string"""
    parts = string.split()
    strboard = parts[0]
    board = []
    count = 0
    lookup = {
        "r":21,
        "n":19,
        "b":20,
        "q":22,
        "k":17,
        "p":18,
        "R":13,
        "N":11,
        "B":12,
        "Q":14,
        "K":9,
        "P":10
    }
    while True:
        if strboard[count] == "/":
            pass
        elif count==len(strboard):
            break
        elif strboard[count].isdigit():
            for i in range(int(strboard[count])):
                board.append(0)
        else:
            board.append(lookup[strboard[count]])
        count+=1
    #parts[1] is whose turn it is
    #parts[2] is which castling are allowed
    #parts[3] is enpassant target
    return board, parts[1], parts[2], parts[3]

dis = update_board_graphics(currentboard.board, dis, images)
pygame.display.update()

#Main game loop
while game_not_over:
    if move%65!=0:
        #if there's not a selected square then reset it (make the move then reset)
        currentboard.possible_moves()
        if move in currentboard.pmoves:
            currentboard.move(move)
        move=0
        dis=update_board_graphics(currentboard.board, dis, images)
        pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            x,y = mouse_pos[0]//60, mouse_pos[1]//60
            if move==0:
                move=65*(8*y+x+1)
            else:
                move+=8*y+x+1
            #Adds the square clicked on to the current move
            pygame.draw.circle(dis, (0,0,250), (x*60+30, y*60+30), 30, 4)
            pygame.display.update()
