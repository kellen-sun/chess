import RPi.GPIO as GPIO
import time
from stockfish import Stockfish

GPIO.setmode(GPIO.BCM)
control1 = 2
control2 = 3
control3 = 4
GPIO.setup(control1, GPIO.OUT)
GPIO.setup(control2, GPIO.OUT)
GPIO.setup(control3, GPIO.OUT)

toggle = 17
GPIO.setup(toggle, GPIO.OUT)

readinput = [27, 22, 10, 9, 11, 5, 6, 13]
for i in readinput:
	GPIO.setup(i, GPIO.IN)


stockfish = Stockfish("/Users/sunke/Work/stockfish_15.1_win_x64_avx2/stockfish_15.1_win_x64_avx2/stockfish-windows-2022-x86-64-avx2.exe")

stockfish.set_fen_position("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1")


def get_current_board_pos():
    piece_location = []
    #if a piece is there and 0 if there's no piece
    for i in readinput:
        GPIO.output(toggle, True)
        GPIO.output(toggle, False)
        GPIO.output(control1, False)
        GPIO.output(control2, False)
        GPIO.output(control3, False)
        time.sleep(0.2)
        piece_location.append(GPIO.input(i))
        
        GPIO.output(toggle, True)
        GPIO.output(toggle, False)
        GPIO.output(control1, False)
        GPIO.output(control2, False)
        GPIO.output(control3, True)
        time.sleep(0.2)
        piece_location.append(GPIO.input(i))
        
        GPIO.output(toggle, True)
        GPIO.output(toggle, False)
        GPIO.output(control1, False)
        GPIO.output(control2, True)
        GPIO.output(control3, False)
        time.sleep(0.2)
        piece_location.append(GPIO.input(i))
        
        GPIO.output(toggle, True)
        GPIO.output(toggle, False)
        GPIO.output(control1, False)
        GPIO.output(control2, True)
        GPIO.output(control3, True)
        time.sleep(0.2)
        piece_location.append(GPIO.input(i))
        
        GPIO.output(toggle, True)
        GPIO.output(toggle, False)
        GPIO.output(control1, True)
        GPIO.output(control2, False)
        GPIO.output(control3, False)
        time.sleep(0.2)
        piece_location.append(GPIO.input(i))
        
        GPIO.output(toggle, True)
        GPIO.output(toggle, False)
        GPIO.output(control1, True)
        GPIO.output(control2, False)
        GPIO.output(control3, True)
        time.sleep(0.2)
        piece_location.append(GPIO.input(i))
        
        GPIO.output(toggle, True)
        GPIO.output(toggle, False)
        GPIO.output(control1, True)
        GPIO.output(control2, True)
        GPIO.output(control3, False)
        time.sleep(0.2)
        piece_location.append(GPIO.input(i))
        
        GPIO.output(toggle, True)
        GPIO.output(toggle, False)
        GPIO.output(control1, True)
        GPIO.output(control2, True)
        GPIO.output(control3, True)
        time.sleep(0.2)
        piece_location.append(GPIO.input(i))
    return piece_location



noPiece = 0
King = 1
Pawn = 2
Knight = 3
Bishop = 4
Rook = 5
Queen = 6
White = 8
Black = 16
pieces = {"r": Black+Rook, "n": Knight+Black, "b": Bishop+Black, "q":Black+Queen, "k":King+Black, "p":Pawn+Black, "R": White+Rook, "N": Knight+White, "B": Bishop+White, "Q":White+Queen, "K":King+White, "P":Pawn+White, " ": 0}

board = []
temp = stockfish.get_board_visual().split("\n")
for i in range(len(temp)-1):
    if temp[i][2]=="-" or temp[i][2]=="a":
        continue
    else:
        for j in range(8):
            board.append(pieces[temp[i][2+j*4]])

