"""
Quoridor student player starter file

Author: Adam Oest
Author: Troy Caro <twc9438@rit.edu>
Date: July, 2012
"""

# Imports the player move class as well as the board size constant
from Model.interface import PlayerMove, BOARD_DIM
from .playerData import PlayerData
from .Board import BoardData
from .myQueue import *


def init(logger, playerId, numWalls, playerHomes):
    """
        Part 1 - 4

        The engine calls this function once at the beginning of the game.
        The student player module uses this function to initialize its data
        structures to the initial game state.

        Parameters
            logger: a reference to the logger object. The player model uses
                logger.write(msg) and logger.error(msg) to log diagnostic
                information.

            playerId: this player's number, from 1 to 4

            numWalls: the number of walls each player is given initially

            playerHomes: An ordered tuple of player locations
                         A location is a 2-element tuple of (row,column).
                         If any player has already been eliminated from
                         the game (rare), there will be a bool False in
                         that player's spot in the tuple instead of a
                         location.

        returns:
            a PlayerData object containing all of this player module's data
    """

    # This is where you must initialize all the information in your PlayerData
    # object. It should store things like how many players and initial
    # configuration of the board.
    #
    # Sample code body
    #
    # In the example code body below, the PlayerData class contained in the
    # file playerData.py is just used as an example. Feel free to alter it.
    # Just make sure it contains everything you need.
    board = BoardData(9, 9)
    board.build(9, 9)
    playerData = PlayerData(logger, playerId, list(playerHomes), board, [0, 0])

    return playerData


def last_move(playerData, move):
    """
        Parts 1 - 4

        The engine calls this function after any player module, including this one,
        makes a valid move in the game.

        The engine also calls this function repeatedly at the start of the game if
        there have been some moves specified in the configuration file's PRE_MOVE
        variable.

        The student player module updates its data structure with the information
        about the move.

        Parameters
            playerData: this player's data, originally built by this
                        module in init()

            move: the instance of PlayerMove that describes the move just made

        returns:
            this player module's updated (playerData) data structure
    """

    # Update your playerData object with the latest move.
    # Remember that this code is called even for your own moves.
    if (move.move):
        playerData.currentLocation = [move.r2, move.c2]
    else:
        # Vert wall
        if move.c1 == move.c2:
            playerData.board.data[move.r1][move.c1].neighbors.remove([move.r1, move.c1 - 1])
            playerData.board.data[move.r1][move.c1 - 1].neighbors.remove([move.r1, move.c1])
            playerData.board.data[move.r1 + 1][move.c1].neighbors.remove([move.r1 + 1, move.c1 - 1])
            playerData.board.data[move.r1 + 1][move.c1 - 1].neighbors.remove([move.r1 + 1, move.c1])
        # Horozontal wall
        else:
            playerData.board.data[move.r1][move.c1].neighbors.remove([move.r1 - 1, move.c1])
            playerData.board.data[move.r1 - 1][move.c1].neighbors.remove([move.r1, move.c1])
            playerData.board.data[move.r1][move.c1 + 1].neighbors.remove([move.r1 - 1, move.c1 + 1])
            playerData.board.data[move.r1 - 1][move.c1 + 1].neighbors.remove([move.r1, move.c1 + 1])
        playerData.board.walls.append([move.r1, move.c1, move.r2, move.c2])

    return playerData


def get_neighbors(playerData, r, c):
    """
        Part 1

        This function is used only in part 1 mode. The engine calls it after
        all PRE_MOVEs have been made. (See the config.cfg file.)

        Parameters
            playerData: this player's data, originally built by this
                        module in init()
            r: row coordinate of starting position for this player's piece
            c: column coordinate of starting position for this player's piece

        returns:
            a list of coordinate pairs (a list of lists, e.g. [[0,0], [0,2]],
            not a list of tuples) denoting all the reachable neighboring squares
            from the given coordinate. "Neighboring" means exactly one move
            away.
    """

    # Use your playerData object to get a list of neighbors

    return playerData.board.data[r][c].neighbors


def get_shortest_path(playerData, r1, c1, r2, c2):
    """
        Part 1

        This function is only called in part 1 mode. The engine calls it when
        a shortest path is requested by the user via the graphical interface.

        Parameters
            playerData: this player's data, originally built by this
                        module in init()
            r1: row coordinate of starting position
            c1: column coordinate of starting position
            r2: row coordinate of destination position
            c2: column coordinate of destination position

        returns:
            a list of coordinates that form the shortest path from the starting
            position to the destination, inclusive. The format is an ordered
            list of coordinate pairs (a list of lists, e.g.,
            [[0,0], [0,1], [1,1]], not a list of tuples).
            If there is no path, an empty list, [], should be returned.
    """

    # Use your playerData object to find a shortest path using breadth-first
    # search (BFS).
    # You will probably find the get_neighbors function helpful.
    dispenser = Queue()
    enqueue([r1, c1], dispenser)
    predecessors = {}
    predecessors[(r1, c1)] = None

    while not emptyQueue(dispenser):
        current = front(dispenser)
        dequeue(dispenser)
        if current[0] == r2 and current[1] == c2:
            break

        for neighbor in get_neighbors(playerData, current[0], current[1]):
            if neighbor not in predecessors:
                predecessors[neighbor] = current
                enqueue(neighbor, dispenser)

    return []


def move(playerData):
    """
        Part 3 - 4

        The engine calls this function at each moment when it is this
        player's turn to make a move. This function decides what kind of
        move, wall placement or piece move, to make.

        Parameters
            playerData: this player's data, originally built by this
                        module in init()

        returns:
            the move chosen, in the form of an instance of PlayerMove
    """

    # This function is called when it's your turn to move

    # Here you'll figure out what kind of move to make and then return that
    # move. We recommend that you don't update your data structures here,
    # but rather in last_move. If you do it here, you'll need a special case
    # check in last_move to make sure you don't update your data structures
    # twice.

    # In part 3, any legal move is acceptable. In part 4, you will want to
    # implement a strategy

    # Placeholder, fill in these values yourself
    move = PlayerMove(-1, False, -1, -1, -1, -1)

    return move


def player_invalidated(playerData, playerId):
    """
        Part 3 - 4

        The engine calls this function when another player has made
        an invalid move or has raised an exception ("crashed").

        Parameters
            playerData: this player's data, originally built by this
                        module in init()
            playerId: the ID of the player being invalidated

        returns:
            this player's updated playerData
    """

    # Update your player data to reflect the invalidation.
    # FYI, the player's piece is removed from the board,
    # but not its walls.

    # When you are working on part 4, there is a small chance you'd
    # want to change your strategy when a player is kicked out.

    return playerData
