#!/Library/Frameworks/Python.framework/Versions/3.5/bin/python3

from ticTacToe import TicTacToe
from ticTacToeUsingDict import TicTacToeUsingDict

def main():
    moves1 = [ "1", "2", "5", "9", "7", "4", "8", "3", "6" ]
    moves2 = [ "1", "2", "3", "4", "5", "6", "8", "7", "9" ]
    moves3 = [ "2", "1", "3", "5", "4", "9", "6", "7", "8" ]

    print( "------------------------------------------" )
    print( "TicTacToe using array implementation.     " )
    print( "------------------------------------------" )
    ttt = TicTacToe( True )
    ttt.Run( "o", moves1 )
    ttt.Run( "o", moves2 )
    ttt.Run( "o", moves3 )
    # Interactive run. Will fail in Jenkins.
    # ttt.Run()

    print( "------------------------------------------" )
    print( "TicTacToe using dictionary implementation." )
    print( "------------------------------------------" )
    tttDict = TicTacToeUsingDict( True )
    tttDict.Run( "x", moves3 )
    tttDict.Run( "x", moves2 )
    tttDict.Run( "x", moves1 )
    # Interactive run. Will fail in Jenkins.
    # tttDict.Run()
        
if __name__ == "__main__":
    main()

