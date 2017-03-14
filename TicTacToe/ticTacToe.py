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

    def Run( self ):
        player = self.__PickXOrOPlayer()
        self.__PrintTicTacToe()
        positions_left = list( range( 1, 10 ) )
        i = 0
        while True:
            curr_pos = self.__PickANumber( player )
            if int(curr_pos) in positions_left:
                positions_left.remove( int(curr_pos) )
            else:
                print( curr_pos + " position has already been picked" )
                continue
            self.__SetCell( curr_pos, player )
            self.__PrintTicTacToe()
            if i > 3:
                retval = self.__CheckWinner( player )
                if retval == player:
                    print( player + " is the winner!" )
                    break
            if player == "x":
                player = "o"
            else:
                player = "x"
            i += 1
            if i == 9:
                break
        if retval != "x" and retval != "o":
            print( "It's a draw!" )

    def SimulatedRun( self ):
        player = "o"
        self.__PrintTicTacToe()
        positions_left = list( range( 1, 10 ) )
        i = 0
        seq = [ "1", "2", "5", "9", "7", "4", "8", "3", "6" ]
        while True:
            curr_pos = seq[i]
            if int(curr_pos) in positions_left:
                positions_left.remove( int(curr_pos) )
            else:
                print( curr_pos + " position has already been picked" )
                continue
            self.__SetCell( curr_pos, player )
            self.__PrintTicTacToe()
            if i > 3:
                retval = self.__CheckWinner( player )
                if retval == player:
                    print( player + " is the winner!" )
                    break
            if player == "x":
                player = "o"
            else:
                player = "x"
            i += 1
            if i == 9:
                break
        if retval != "x" and retval != "o":
            print( "It's a draw!" )
    def __SetCell( self, cellnum, x_or_o ):
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

    def __CheckWinner( self, x_or_o ):
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

    def __PrintTicTacToe( self ):
        print( self.list[0][0] + " " + self.list[0][1] + " " + self.list[0][2] )
        print( self.list[1][0] + " " + self.list[1][1] + " " + self.list[1][2] )
        print( self.list[2][0] + " " + self.list[2][1] + " " + self.list[2][2] )

    def __PickXOrOPlayer( self ):
        inputStr = "Who starts first, 'o' or 'x'? "
        while True:
            player = input( inputStr )
            out = re.match( '[ox]$|quit', player )
            if player == "quit":
                sys.exit( 0 )
            if out:
                break
            else:
                print( "Not a valid player!" )
        return player

    def __PickANumber( self, player ):
        while True:
            curr_pos  = input( "Pick a number from 1-9 for " + player + ": " )
            out = re.match( '[1-9]$|quit', curr_pos )
            if curr_pos == "quit":
                sys.exit( 0 )
            if out:
                break
            else:
                print( "Not a valid pick!" )
        return curr_pos

