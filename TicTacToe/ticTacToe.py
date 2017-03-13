#!/Library/Frameworks/Python.framework/Versions/3.5/bin/python3

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
        curr_move = input( "Who starts first, 'o' or 'x'? " )
        self.PrintTicTacToe()
        for i in range(9):
            curr_pos  = input( "Input a number from 1-9 for " + curr_move + ": " )
            self.SetCell( curr_pos, curr_move )
            self.PrintTicTacToe()
            retval = self.CheckWinner( curr_move )
            if retval == curr_move:
                print( curr_move + " is the winner!" )
                break
            if curr_move == "x":
                curr_move = "o"
            else:
                curr_move = "x"
        if retval != "x" and retval != "o":
            print( "It's a draw!" )

def main():
    ttt = TicTacToe()
    ttt.Run()
        
if __name__ == "__main__":
    main()

