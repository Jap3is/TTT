#!/Library/Frameworks/Python.framework/Versions/3.5/bin/python3

import sys
import re

class TicTacToe( object ):
    __gameCount = 0

    def __init__( self, showResultOnly=False ):
        self.list = [
            "1", "2", "3",
            "4", "5", "6",
            "7", "8", "9"
        ]
        self.showResultOnly = showResultOnly
        TicTacToe.__gameCount = 0

    def Run( self, player=None, moves=None ):
        MAX_CELLS = 9
        MAX_IDX_WO_WINNER = 3
        self.__ResetCells()
        if player == None:
            player = self.__PickXOrOPlayer()
        if self.showResultOnly == False:
            self.__PrintTicTacToe()
        positions_left = list( range( 1, MAX_CELLS+1 ) )
        i = 0
        while True:
            if moves == None:
                curr_pos = self.__PickANumber( player )
            else:
                curr_pos = moves[i]
            if int(curr_pos) in positions_left:
                positions_left.remove( int(curr_pos) )
            else:
                print( curr_pos + " position has already been picked" )
                continue
            self.__SetCell( curr_pos, player )
            if self.showResultOnly == False:
                self.__PrintTicTacToe()
            if i > MAX_IDX_WO_WINNER:
                retval = self.__CheckWinner( player )
                if retval == player:
                    break
            if player == "x":
                player = "o"
            else:
                player = "x"
            i += 1
            if i == MAX_CELLS:
                break
        TicTacToe.__gameCount += 1
        self.__PrintGameResult( retval )

    def __PrintGameResult( self, retval ):
        print( "-- Game " + str( TicTacToe.__gameCount ) + " Result --" )
        if retval != "x" and retval != "o":
            print( "It's a draw!" )
        else:
            print( retval + " is the winner!" )
        self.__PrintTicTacToe()

    def __ResetCells( self ):
        self.list = [
            "1", "2", "3",
            "4", "5", "6",
            "7", "8", "9"
        ]

    def __SetCell( self, cellnum, x_or_o ):
        self.list[int(cellnum)-1] = x_or_o

    def __CheckWinner( self, x_or_o ):
        if ( ( self.list[0] == x_or_o and self.list[1] == x_or_o and self.list[2] == x_or_o ) or
             ( self.list[3] == x_or_o and self.list[4] == x_or_o and self.list[5] == x_or_o ) or
             ( self.list[6] == x_or_o and self.list[7] == x_or_o and self.list[8] == x_or_o ) or
             ( self.list[0] == x_or_o and self.list[3] == x_or_o and self.list[6] == x_or_o ) or
             ( self.list[1] == x_or_o and self.list[4] == x_or_o and self.list[7] == x_or_o ) or
             ( self.list[2] == x_or_o and self.list[5] == x_or_o and self.list[8] == x_or_o ) or
             ( self.list[0] == x_or_o and self.list[4] == x_or_o and self.list[8] == x_or_o ) or
             ( self.list[2] == x_or_o and self.list[4] == x_or_o and self.list[6] == x_or_o ) ):
             return x_or_o
        else:
             return "-"

    def __PrintTicTacToe( self ):
        print( self.list[0] + " " + self.list[1] + " " + self.list[2] )
        print( self.list[3] + " " + self.list[4] + " " + self.list[5] )
        print( self.list[6] + " " + self.list[7] + " " + self.list[8] )

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

