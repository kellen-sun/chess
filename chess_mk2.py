import random, copy, time, sys, pickle, numpy, pygame, cProfile

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

totalcount = 0

#boardevaluation constants
with open("boardevaluation.pickle", "rb") as f:
    boardevaluation = pickle.load(f)
#opening games database
with open("Games.txt", "r") as f:
    games = f.readlines()
games = [games[i].split() for i in range(len(games))]

class Board:
    """All information necessary for a board position"""
    def __init__(self, board, castling, turn, en_passant_target, all_moves):
        self.board = board
        self.castling = castling
        self.turn = turn
        self.en_passant_target = en_passant_target
        self.all_moves = all_moves
        self.eg = self.endgame()

    def endgame(self):
        cc1 = 0
        cc2 = 0
        for x in self.board:
            if x == Rook+White or x==Knight+White or x==Bishop+White:
                cc1+=1
            if x == Rook+Black or x==Knight+Black or x==Bishop+Black:
                cc2+=1
        return ((Queen+White not in self.board) and (Queen+Black not in self.board)) or (cc1<=1 and cc2<=1)
    
    def move(self, move):
        """Given a move the board is changed accordingly"""
        #write exceptions for castling and en_passant
        global games
        move1 = move%65-1
        move0 = move//65-1
        if (move0==0 or move0==4 or move1==0) and 3 in self.castling:
            self.castling.remove(3)
        if (move0==7 or move0==4 or move1==7) and 2 in self.castling:
            self.castling.remove(2)
        if (move0==63 or move0==60 or move1==63) and 0 in self.castling:
            self.castling.remove(0)
        if (move0==56 or move0==60 or move1==56) and 1 in self.castling:
            self.castling.remove(1)
        if self.board[move0]==King+8*(self.turn+1) and move0%8==4 and move1%8==6:
            self.board[move1-1]=self.board[move1+1]
            self.board[move1+1]=0
        if self.board[move0]==King+8*(self.turn+1) and move0%8==4 and move1%8==2:
            self.board[move1+1]=self.board[move1-2]
            self.board[move1-2]=0
        self.board[move1]=self.board[move0]
        self.board[move0]=0
        if self.board[move1]==Pawn+(1+self.turn)*8 and (move1//8 == 0 or move1//8==7):
            self.board[move1]=Queen+(1+self.turn)*8
        if self.en_passant_target==move1 and self.board[move1]==(self.turn+1)*8+Pawn:
            self.board[8*(move0//8)+move1%8]=0
        self.en_passant_target = -1
        if self.board[move1]==(self.turn+1)*8+Pawn and (move1==move0+16 or move1==move0-16):
            self.en_passant_target = (move0+move1)//2
        self.turn = 1-self.turn
        self.all_moves.append(move)

    def move1(self, move):
        global games
        newgames = []
        if len(games)>0:
            for i in games:
                if self.PNGformatter(move)==i[len(self.all_moves)]:
                    newgames.append(i)
        games = newgames
        self.all_moves.append(move)
        move1 = move%65-1
        move0 = move//65-1
        if (move0==0 or move0==4 or move1==0) and 3 in self.castling:
            self.castling.remove(3)
        if (move0==7 or move0==4 or move1==7) and 2 in self.castling:
            self.castling.remove(2)
        if (move0==63 or move0==60 or move1==63) and 0 in self.castling:
            self.castling.remove(0)
        if (move0==56 or move0==60 or move1==56) and 1 in self.castling:
            self.castling.remove(1)
        if self.board[move0]==King+8*(self.turn+1) and move0%8==4 and move1%8==6:
            self.board[move1-1]=self.board[move1+1]
            self.board[move1+1]=0
        if self.board[move0]==King+8*(self.turn+1) and move0%8==4 and move1%8==2:
            self.board[move1+1]=self.board[move1-2]
            self.board[move1-2]=0
        self.board[move1]=self.board[move0]
        self.board[move0]=0
        if self.board[move1]==Pawn+(1+self.turn)*8 and (move1//8 == 0 or move1//8==7):
            self.board[move1]=Queen+(1+self.turn)*8
        if self.en_passant_target==move1 and self.board[move1]==(self.turn+1)*8+Pawn:
            self.board[8*(move0//8)+move1%8]=0
        self.en_passant_target = -1
        if self.board[move1]==(self.turn+1)*8+Pawn and (move1==move0+16 or move1==move0-16):
            self.en_passant_target = (move0+move1)//2
        self.turn = 1-self.turn

    def undomove(self, move):
        board, turn, castling, en_passant_target = [[21, 19, 20, 22, 17, 20, 19, 21, 18, 18, 18, 18, 18, 18, 18, 18, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 10, 10, 10, 10, 10, 10, 10, 13, 11, 12, 14, 9, 12, 11, 13], 0, [0, 1, 2, 3], -1]
        self.board = board
        self.castling = castling
        self.turn = turn
        self.en_passant_target = en_passant_target
        moves = self.all_moves
        self.all_moves = []
        #self.eg = self.endgame()
        moves.pop(-1)
        for i in moves:
            self.move(i)
    
    def possible_moves(self):
        """Returns the possible moves (in reality the pseudo legal moves)"""
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
                    #castling but will need to fix castling into and away from checks
                    for j in self.castling:
                        if j//2==self.turn:
                            if j%2==0:
                                if i+2<64:
                                    if self.board[i+1]==0 and self.board[i+2]==0 and self.board[i+3]==(self.turn+1)*8+Rook:
                                        self.pmoves.append(65*(i+1)+i+3)
                            if j%2==1:
                                if i-3>=0:
                                    if self.board[i-1]==0 and self.board[i-2]==0 and self.board[i-3]==0 and self.board[i-4]==(self.turn+1)*8+Rook:
                                        self.pmoves.append(65*(i+1)+i-1)
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
                    increments = [[-9, -7, -8, -16], [7, 9, 8, 16]]
                    #capturing pieces
                    for j in range(2):
                        if 0<=i+increments[self.turn][j]<64:
                            if (self.board[i+increments[self.turn][j]]//8!=self.turn+1 and self.board[i+increments[self.turn][j]]!=0) or (self.board[i+increments[self.turn][j]]==0 and i+increments[self.turn][j]==self.en_passant_target):
                                if abs(i%8-(i+increments[self.turn][j])%8)<=1:
                                    self.pmoves.append(65*(i+1)+i+increments[self.turn][j]+1)
                    #moving one square up
                    if 0<=i+increments[self.turn][2]<64:
                        if self.board[i+increments[self.turn][2]]==0:
                            self.pmoves.append(65*(i+1)+i+increments[self.turn][2]+1)
                            if 0<=i+increments[self.turn][3]<64:
                                if self.board[i+increments[self.turn][3]]==0 and i//8==[6, 1][self.turn]:
                                    self.pmoves.append(65*(i+1)+i+increments[self.turn][3]+1)
        return self.pmoves
    
    def legalmoves(self):
        """Returns truly legal moves checking that a move doesn't lead to capture of the king"""
        pmoves = self.possible_moves()
        lmoves = []
        for i in pmoves:
            #test = Board(copy.copy(self.board), copy.copy(self.castling), self.turn, self.en_passant_target, copy.copy(self.all_moves))
            test = Board(self.board.copy(), self.castling.copy(), self.turn, self.en_passant_target, self.all_moves.copy())
            #test = copy.deepcopy(self)
            test.move(i)
            next = test.possible_moves()
            br = True
            for j in next:
                if test.board[j%65-1]%8==King:
                    br = False
            if br:
                lmoves.append(i)
            #self.undomove(i)
        return lmoves
    
    def evaluateboard(self):
        """Gives a value for the current board by evaluating the value of pieces and their positions"""
        global totalcount
        totalcount+=1
        eval = 0
        if self.eg==False:
            self.eg = self.endgame()
        for i in range(len(self.board)):
            piece = self.board[i]
            #those are the values of each pieces with the pawn set at 100 points
            basevalues = {0:0, 9:20000, 10:100, 11:320, 12:330, 13:500, 14:900,
                          17:-20000, 18:-100, 19:-320, 20:-330, 21:-500, 22:-900}
            eval+=basevalues[piece]
            #depending on the location of the piece additional smaller value points are added or subtracted
            if not (self.eg and piece%8==King):
                if piece%8 in boardevaluation.keys():
                    if piece//8-1==0:
                        eval+=boardevaluation[piece%8][i]
                    else:
                        eval-=boardevaluation[piece%8][63-i]
            else:
                if piece//8-1==0:
                    eval+=boardevaluation['E2'][i]
                else:
                    eval-=boardevaluation['E2'][63-i]
        return eval
    
    def PNGformatter(self, move):
        move1 = move%65-1
        move0 = move//65-1
        is_check = self.is_check(move)
        capture = self.is_capture(move)
        #castling
        startingpieces = {1:"K", 2:"", 3:"N", 4:"B", 5:"R", 6:"Q"}
        startingpiece = startingpieces[self.board[move0]%8]
        endsquare = chr(move1%8+97)+str(8-move1//8)
        if capture:
            finalmove = startingpiece+"x"+endsquare
        else:
            finalmove = startingpiece+endsquare
        if is_check:
            finalmove+="+"
        if startingpiece == "" and capture:
            finalmove = chr(move0%8+97)+finalmove
            return finalmove
        elif startingpiece == "R" or startingpiece == "N":
            possible = self.possible_moves()
            for i in possible:
                movei1 = i%65-1
                movei0 = i//65-1
                if i != move:
                    if movei1 == move1 and self.board[movei0] == self.board[move0]:
                        if movei0//8==move0//8:
                            finalmove = finalmove[0]+chr(move0%8+97)+finalmove[1:]
                            break
                        elif movei0%8==move0%8:
                            finalmove = finalmove[0]+chr(move0//8+97)+finalmove[1:]
                            break
            return finalmove
        elif startingpiece=="K" and abs(move0-move1)>1:
            if move0-move1 == 2:
                return "O-O-O"
            if move1-move0==2:
                return "O-O"
        return finalmove
    
    def is_capture(self, move):
        move1 = move%65-1
        move0 = move//65-1
        if (self.board[move1]//8+self.board[move0]//8)==3:
            return True
        return False
    
    def is_check(self, move):
        self.move(move)
        temp = self.in_check()
        self.undomove(move)
        return temp
    
    def in_check(self):
        self.turn = 1-self.turn
        for i in self.possible_moves():
            move1=i%65-1
            if self.board[move1]==8*(self.turn+1)+King:
                self.turn = 1-self.turn
                return True
        self.turn = 1-self.turn
        return False
    
    def choosemove(self):
        moves = self.legalmoves()
        bestevaluation = -10**10
        bestmove = -1
        for i in moves:
            newBoard = Board(self.board.copy(), self.castling.copy(), self.turn, self.en_passant_target, self.all_moves.copy())
            newBoard.move(i)
            evaluation = -newBoard.evaluateboard()
            if evaluation > bestevaluation:
                bestmove = i
                bestevaluation = evaluation
        return bestmove

    def choosemove2(self, depth):
        if depth==0:
            return self.evaluateboard(), -1
        moves = self.legalmoves()
        if len(moves)==0:
            if self.in_check():
                return -10**8, -1
            else:
                return 0, -1
        bestEvaluation = -10**8
        for i in moves:
            self.move(i)
            evaluation, temp = self.choosemove2(depth-1)
            evaluation = -evaluation
            if evaluation>bestEvaluation:
                bestmove = i
                bestEvaluation=evaluation
            self.undomove(i)
        return bestEvaluation, bestmove
    
    def quiesce(self, alpha, beta):
        evaluation = self.evaluateboard()
        if evaluation>=beta:
            return beta
        alpha = max(alpha, evaluation)
        moves = self.legalmoves()
        for i in moves:
            if self.is_capture(i) or self.is_check(i):
                self.move(i)
                evaluation = -self.quiesce(-beta, -alpha)
                self.undomove(i)
                if evaluation>=beta:
                    return beta
                if evaluation>alpha:
                    alpha=evaluation
        return alpha

    def book(self):
        #removing from the games database
        global games
        if len(games)==0:
            return False
        movePNG = random.choice(games)[len(self.all_moves)]
        print(movePNG)
        moves = self.possible_moves()
        for i in moves:
            if self.PNGformatter(i)==movePNG:
                return i
        return False

    def choosemove3(self, depth, alpha, beta, ply):
        global bestmove
        if ply==0:
            a = self.book()
            if a:
                bestmove = a
                return a
        if depth==0:
            if ply%2==1:
                return self.quiesce(alpha, beta)
            else:
                return -self.quiesce(alpha, beta)
        moves = self.legalmoves()
        if len(moves)==0:
            if self.in_check():
                return -10**8
            else:
                return 0
        if ply>0:
            if alpha>=beta:
                return alpha
        for i in moves:
            self.move(i)
            evaluation = -self.choosemove3(depth-1, -beta, -alpha, ply+1)
            #evaluation = evaluation
            self.undomove(i)
            if evaluation>=beta:
                return beta
            if evaluation>alpha:
                #bestmove = i
                alpha=evaluation
                if ply==0:
                    bestmove = i
        return alpha
        
        
#Starting position
currentboard = Board([21, 19, 20, 22, 17, 20, 19, 21, 18, 18, 18, 18, 18, 18, 18, 18, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 10, 10, 10, 10, 10, 10, 10, 13, 11, 12, 14, 9, 12, 11, 13], [0, 1, 2, 3], 0, -1, [])

#0 represents white's turn, 1 represents black's turn
#0 for white king side castle, 1 for white queen, 2 for black king side, 3 for black queen side

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
        if count==len(strboard):
            break
        elif strboard[count] == "/":
            pass
        elif strboard[count].isdigit():
            for i in range(int(strboard[count])):
                board.append(0)
        else:
            board.append(lookup[strboard[count]])
        count+=1
    if parts[1]=="w":
        parts[1]=0
    else:
        parts[1]=1
    castling_allowed = []
    if "K" in parts[2]:
        castling_allowed.append(0)
    if "Q" in parts[2]:
        castling_allowed.append(1)
    if "k" in parts[2]:
        castling_allowed.append(2)
    if "q" in parts[2]:
        castling_allowed.append(3)
    if parts[3]=="-":
        parts[3]=-1
    else:
        parts[3]=ord(parts[3][0])-97+(8-parts[3][1])*8
    
    #parts[1] is whose turn it is
    #parts[2] is which castling are allowed
    #parts[3] is enpassant target
    return board, parts[1], castling_allowed, parts[3]

dis = update_board_graphics(currentboard.board, dis, images)
pygame.display.update()

#Main game loop
while game_not_over:
    if move%65!=0:
        #if there's not a selected square then reset it (make the move then reset)
        currentboard.evaluateboard()
        if move in currentboard.legalmoves():
            #print(currentboard.PNGformatter(move))
            currentboard.move1(move)
            
            move=0
            dis=update_board_graphics(currentboard.board, dis, images)
            pygame.display.update()
            totalcount = 0
            t = time.time()
            bestmove = -1
            #cProfile.run("currentboard.choosemove3(3, -10**8, -10**8, 0)")
            out1 = currentboard.choosemove3(1, -10**9, 10**9, 0)
            print(time.time()-t, "s for", totalcount, "moves evaluated.")
            #print(currentboard.PNGformatter(bestmove))
            currentboard.move1(bestmove)
            
            dis=update_board_graphics(currentboard.board, dis, images)
            pygame.display.update()
        else:
            move = 0
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
