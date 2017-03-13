#!/Library/Frameworks/Python.framework/Versions/3.5/bin/python3

import sys
import re

class TicTacToe( object ):

    def __init__( self ):
        self.list = [
            [ "1", "2", "3" ],
            [ "4", "5", "6" ],
            [ "7", "8", "9" ],
        ]

    def SetCell( self, cellnum, x_or_o ):
        if cellnum == "1":
            self.list[0][0] = x_or_o
        elif cellnum == "2":
            self.list[0][1] = x_or_o
        elif cellnum == "3":
            self.list[0][2] = x_or_o
        elif cellnum == "4":
            self.list[1][0] = x_or_o
        elif cellnum == "5":
            self.list[1][1] = x_or_o
        elif cellnum == "6":
            self.list[1][2] = x_or_o
        elif cellnum == "7":
            self.list[2][0] = x_or_o
        elif cellnum == "8":
            self.list[2][1] = x_or_o
        elif cellnum == "9":
            self.list[2][2] = x_or_o

    def CheckWinner( self, x_or_o ):
        if ( ( self.list[0][0] == x_or_o and self.list[0][1] == x_or_o and self.list[0][2] == x_or_o ) or
             ( self.list[1][0] == x_or_o and self.list[1][1] == x_or_o and self.list[1][2] == x_or_o ) or
             ( self.list[2][0] == x_or_o and self.list[2][1] == x_or_o and self.list[2][2] == x_or_o ) or
             ( self.list[0][0] == x_or_o and self.list[1][0] == x_or_o and self.list[2][0] == x_or_o ) or
             ( self.list[0][1] == x_or_o and self.list[1][1] == x_or_o and self.list[2][1] == x_or_o ) or
             ( self.list[0][2] == x_or_o and self.list[1][2] == x_or_o and self.list[2][2] == x_or_o ) or
             ( self.list[0][0] == x_or_o and self.list[1][1] == x_or_o and self.list[2][2] == x_or_o ) or
             ( self.list[0][2] == x_or_o and self.list[1][1] == x_or_o and self.list[2][0] == x_or_o ) ):
             return x_or_o
        else:
             return "-"

    def PrintTicTacToe( self ):
        print( self.list[0][0] + " " + self.list[0][1] + " " + self.list[0][2] )
        print( self.list[1][0] + " " + self.list[1][1] + " " + self.list[1][2] )
        print( self.list[2][0] + " " + self.list[2][1] + " " + self.list[2][2] )

    def Run( self ):
        inputStr = "Who starts first, 'o' or 'x'? "
        while True:
            player = input( inputStr )
            out = re.match( '[ox]|quit', player )
            if player == "quit":
                sys.exit( 0 )
            if out:
                break
        self.PrintTicTacToe()
        options = list( range( 1, 10 ) )
        i = 0
        while True:
            if i == 9:
                break
            while True:
                curr_pos  = input( "Pick a number from 1-9 for " + player + ": " )
                out = re.match( '[1-9]|quit', curr_pos )
                if curr_pos == "quit":
                    sys.exit( 0 )
                if out:
                    break
            if int(curr_pos) in options:
                options.remove( int( curr_pos ) )
            else:
                print( curr_pos + " position has already been picked" )
                continue
            self.SetCell( curr_pos, player )
            self.PrintTicTacToe()
            retval = self.CheckWinner( player )
            if retval == player:
                print( player + " is the winner!" )
                break
            if player == "x":
                player = "o"
            else:
                player = "x"
            i += 1
        if retval != "x" and retval != "o":
            print( "It's a draw!" )

def main():
    ttt = TicTacToe()
    ttt.Run()
        
if __name__ == "__main__":
    main()

