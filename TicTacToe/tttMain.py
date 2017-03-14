#!/Library/Frameworks/Python.framework/Versions/3.5/bin/python3

from ticTacToe import TicTacToe

def main():
    moves = [ "1", "2", "5", "9", "7", "4", "8", "3", "6" ]
    # moves = [ "1", "2", "3", "4", "5", "6", "8", "7", "9" ]
    ttt = TicTacToe()
    # ttt.Run( "o", moves )
    ttt.Run()
        
if __name__ == "__main__":
    main()

