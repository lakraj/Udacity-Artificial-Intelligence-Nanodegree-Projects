
# /media/lakshmi/Data_Lak_Tpad/Lak_COURSES/UDACITY/March2018_AI_Nanodegree/Term1/Project_2/AIND-Isolation-master

def custom_score(game, player):
    """Calculate the heuristic value of a game state from the point of view
    of the given player.

    This should be the best heuristic function for your project submission.

    Note: this function should be called from within a Player instance as
    `self.score()` -- you should not need to call this function directly.

    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).

    player : object
        A player instance in the current game (i.e., an object corresponding to
        one of the player objects `game.__player_1__` or `game.__player_2__`.)

    Returns
    -------
    float
        The heuristic value of the current game state to the specified player.
    """
    if game.is_loser(player):
        return float("-inf")

    if game.is_winner(player):
        return float("inf")

    my_moves = (game.get_legal_moves(player))
    opp_moves = (game.get_legal_moves(game.get_opponent(player)))

    # If the opponent hmy_score - (1-factor) * opp_scoreas np moves, always chose this move - 100% or 1
    if len(opp_moves) == 0:
        return float("+inf")
    elif len(my_moves) == 0:
        return float("-inf")
    else:
        #my_y, my_x = game.get_player_location(player)
        #opp_y, opp_x = game.get_player_location(game.get_opponent(player))
        #dist_to_opp = ((my_y - opp_y)**2 + (my_x - opp_x)**2)
        #percent_game_complete
        percent_game_complete = (game.move_count)/(game.width * game.height)
        #return float(2 * my_moves + (1 - factor) * dist_to_opp)
        #return float(my_moves/7 + (dist_to_opp - 2**0.5)/(6*2**0.5))
        #my_no_future_moves_count = 0
        #my_sum_future_moves = len(my_moves)
        #opp_no_future_moves_count = 0
        #opp_sum_future_moves = len(opp_moves)
    return float(len(my_moves) - (percent_game_complete) * len(opp_moves))



#heuristic - 2
def custom_score(game, player):
    """Calculate the heuristic value of a game state from the point of view
    of the given player.

    This should be the best heuristic function for your project submission.

    Note: this function should be called from within a Player instance as
    `self.score()` -- you should not need to call this function directly.

    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).

    player : object
        A player instance in the current game (i.e., an object corresponding to
        one of the player objects `game.__player_1__` or `game.__player_2__`.)

    Returns
    -------
    float
        The heuristic value of the current game state to the specified player.
    """
    if game.is_loser(player):
        return float("-inf")

    if game.is_winner(player):
        return float("inf")

    my_moves = (game.get_legal_moves(player))
    opp_moves = (game.get_legal_moves(game.get_opponent(player)))

    # If the opponent hmy_score - (1-factor) * opp_scoreas np moves, always chose this move - 100% or 1
    if len(opp_moves) == 0:
        return float("+inf")
    elif len(my_moves) == 0:
        return float("-inf")
    else:
        #my_y, my_x = game.get_player_location(player)
        #opp_y, opp_x = game.get_player_location(game.get_opponent(player))
        #dist_to_opp = ((my_y - opp_y)**2 + (my_x - opp_x)**2)
        #percent_game_complete
        percent_game_complete = (game.move_count)/(game.width * game.height)
        #return float(2 * my_moves + (1 - factor) * dist_to_opp)
        #return float(my_moves/7 + (dist_to_opp - 2**0.5)/(6*2**0.5))
        my_no_future_moves = 0
        #my_sum_future_moves = len(my_moves)
        #opp_no_future_moves_count = 0
        #opp_sum_future_moves = len(opp_moves)
        my_max_moves = 0
        opp_max_moves = 0
        for move in my_moves:
            no_of_moves = len(game.forecast_move(move).get_legal_moves(player))
            if not game._Board__get_moves(move):
                my_no_future_moves += 1
            if no_of_moves > my_max_moves:
                my_max_moves = no_of_moves
            #my_total_moves += no_of_moves
        for move in opp_moves:
            opp_no_of_moves = len(game.forecast_move(move).get_legal_moves(game.get_opponent(player)))
            if opp_no_of_moves > opp_max_moves:
                opp_max_moves = opp_no_of_moves
            #opp_total_moves += opp_no_of_moves
        if len(my_moves) == 1:
            if my_moves[0] in opp_moves:
                return float("-inf")
        return float((len(my_moves) + my_max_moves  - my_no_future_moves) - (percent_game_complete) * (len(opp_moves) + opp_max_moves))

        #return float(len(my_moves) - (percent_game_complete) * len(opp_moves))

#heristic - 3 - XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
def custom_score(game, player):
    """Calculate the heuristic value of a game state from the point of view
    of the given player.

    This should be the best heuristic function for your project submission.

    Note: this function should be called from within a Player instance as
    `self.score()` -- you should not need to call this function directly.

    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).

    player : object
        A player instance in the current game (i.e., an object corresponding to
        one of the player objects `game.__player_1__` or `game.__player_2__`.)

    Returns
    -------
    float
        The heuristic value of the current game state to the specified player.
    """
    if game.is_loser(player):
        return float("-inf")

    if game.is_winner(player):
        return float("inf")

    my_moves = (game.get_legal_moves(player))
    opp_moves = (game.get_legal_moves(game.get_opponent(player)))

    # If the opponent hmy_score - (1-factor) * opp_scoreas np moves, always chose this move - 100% or 1
    if len(opp_moves) == 0:
        return float("+inf")
    elif len(my_moves) == 0:
        return float("-inf")
    else:
        #my_y, my_x = game.get_player_location(player)
        #opp_y, opp_x = game.get_player_location(game.get_opponent(player))
        #dist_to_opp = ((my_y - opp_y)**2 + (my_x - opp_x)**2)
        #percent_game_complete
        percent_game_complete = (game.move_count)/(game.width * game.height)
        '''if len(my_moves) == 1:
            if my_moves[0] in opp_moves:
                return float("-inf")'''
        #return float(2 * my_moves + (1 - factor) * dist_to_opp)
        #return float(my_moves/7 + (dist_to_opp - 2**0.5)/(6*2**0.5))
        my_no_future_moves = 0
        #my_sum_future_moves = len(my_moves)
        #opp_no_future_moves_count = 0
        #opp_sum_future_moves = len(opp_moves)
        my_max_moves = 0
        opp_max_moves = 0
        for move in my_moves:
            no_of_moves = len(game.forecast_move(move).get_legal_moves(player))
            if not game._Board__get_moves(move):
                my_no_future_moves += 1
            if no_of_moves > my_max_moves:
                my_max_moves = no_of_moves
            #my_total_moves += no_of_moves
        for move in opp_moves:
            opp_no_of_moves = len(game.forecast_move(move).get_legal_moves(game.get_opponent(player)))
            if opp_no_of_moves > opp_max_moves:
                opp_max_moves = opp_no_of_moves
            #opp_total_moves += opp_no_of_moves
        '''if percent_game_complete < 0.6:
            return float((len(my_moves) + my_max_moves  - my_no_future_moves) - (len(opp_moves) + opp_max_moves))
        else:
            return float((len(my_moves) + my_max_moves  - my_no_future_moves))'''
        #return float(len(my_moves) - (percent_game_complete) * len(opp_moves))
        return float((len(my_moves) + my_max_moves  - my_no_future_moves) - (len(opp_moves) + opp_max_moves))

#heuristic-4- XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
def custom_score(game, player):
    """Calculate the heuristic value of a game state from the point of view
    of the given player.

    This should be the best heuristic function for your project submission.

    Note: this function should be called from within a Player instance as
    `self.score()` -- you should not need to call this function directly.

    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).

    player : object
        A player instance in the current game (i.e., an object corresponding to
        one of the player objects `game.__player_1__` or `game.__player_2__`.)

    Returns
    -------
    float
        The heuristic value of the current game state to the specified player.
    """
    if game.is_loser(player):
        return float("-inf")

    if game.is_winner(player):
        return float("inf")

    my_moves = (game.get_legal_moves(player))
    opp_moves = (game.get_legal_moves(game.get_opponent(player)))

    # If the opponent hmy_score - (1-factor) * opp_scoreas np moves, always chose this move - 100% or 1
    if len(opp_moves) == 0:
        return float("+inf")
    elif len(my_moves) == 0:
        return float("-inf")
    else:
        #my_y, my_x = game.get_player_location(player)
        #opp_y, opp_x = game.get_player_location(game.get_opponent(player))
        #dist_to_opp = ((my_y - opp_y)**2 + (my_x - opp_x)**2)
        #percent_game_complete
        percent_game_complete = (game.move_count)/(game.width * game.height)
        '''if len(my_moves) == 1:
            if my_moves[0] in opp_moves:
                return float("-inf")'''
        #return float(2 * my_moves + (1 - factor) * dist_to_opp)
        #return float(my_moves/7 + (dist_to_opp - 2**0.5)/(6*2**0.5))
        my_no_future_moves = 0
        #my_sum_future_moves = len(my_moves)
        #opp_no_future_moves_count = 0
        #opp_sum_future_moves = len(opp_moves)
        my_max_moves = 0
        opp_max_moves = 0
        for move in my_moves:
            no_of_moves = len(game.forecast_move(move).get_legal_moves(player))
            if not game._Board__get_moves(move):
                my_no_future_moves += 1
            if no_of_moves > my_max_moves:
                my_max_moves = no_of_moves
            #my_total_moves += no_of_moves
        for move in opp_moves:
            opp_no_of_moves = len(game.forecast_move(move).get_legal_moves(game.get_opponent(player)))
            if opp_no_of_moves > opp_max_moves:
                opp_max_moves = opp_no_of_moves
            #opp_total_moves += opp_no_of_moves
        '''if percent_game_complete < 0.6:
            return float((len(my_moves) + my_max_moves  - my_no_future_moves) - (len(opp_moves) + opp_max_moves))
        else:
            return float((len(my_moves) + my_max_moves  - my_no_future_moves))'''
        #return float(len(my_moves) - (percent_game_complete) * len(opp_moves))
        return float((len(my_moves) + my_max_moves  - my_no_future_moves) -(1- percent_game_complete)* (len(opp_moves) + opp_max_moves))


#heuristic - 5- XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

def custom_score(game, player):
    """Calculate the heuristic value of a game state from the point of view
    of the given player.

    This should be the best heuristic function for your project submission.

    Note: this function should be called from within a Player instance as
    `self.score()` -- you should not need to call this function directly.

    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).

    player : object
        A player instance in the current game (i.e., an object corresponding to
        one of the player objects `game.__player_1__` or `game.__player_2__`.)

    Returns
    -------
    float
        The heuristic value of the current game state to the specified player.
    """
    if game.is_loser(player):
        return float("-inf")

    if game.is_winner(player):
        return float("inf")

    my_moves = (game.get_legal_moves(player))
    opp_moves = (game.get_legal_moves(game.get_opponent(player)))

    # If the opponent hmy_score - (1-factor) * opp_scoreas np moves, always chose this move - 100% or 1
    if len(opp_moves) == 0:
        return float("+inf")
    elif len(my_moves) == 0:
        return float("-inf")
    else:
        #my_y, my_x = game.get_player_location(player)
        #opp_y, opp_x = game.get_player_location(game.get_opponent(player))
        #dist_to_opp = ((my_y - opp_y)**2 + (my_x - opp_x)**2)
        #percent_game_complete
        percent_game_complete = (game.move_count)/(game.width * game.height)
        '''if len(my_moves) == 1:
            if my_moves[0] in opp_moves:
                return float("-inf")'''
        #return float(2 * my_moves + (1 - factor) * dist_to_opp)
        #return float(my_moves/7 + (dist_to_opp - 2**0.5)/(6*2**0.5))
        my_no_future_moves = 0
        #my_sum_future_moves = len(my_moves)
        #opp_no_future_moves_count = 0
        #opp_sum_future_moves = len(opp_moves)
        my_max_moves = 0
        opp_max_moves = 0
        for move in my_moves:
            no_of_moves = len(game.forecast_move(move).get_legal_moves(player))
            if not game._Board__get_moves(move):
                my_no_future_moves += 1
            if no_of_moves > my_max_moves:
                my_max_moves = no_of_moves
            #my_total_moves += no_of_moves
        for move in opp_moves:
            opp_no_of_moves = len(game.forecast_move(move).get_legal_moves(game.get_opponent(player)))
            if opp_no_of_moves > opp_max_moves:
                opp_max_moves = opp_no_of_moves
            #opp_total_moves += opp_no_of_moves
        '''if percent_game_complete < 0.6:
            return float((len(my_moves) + my_max_moves  - my_no_future_moves) - (len(opp_moves) + opp_max_moves))
        else:
            return float((len(my_moves) + my_max_moves  - my_no_future_moves))'''
        #return float(len(my_moves) - (percent_game_complete) * len(opp_moves))
        return float((len(my_moves) + my_max_moves  - my_no_future_moves) -(percent_game_complete)* (len(opp_moves) + opp_max_moves))


#heauristic - 6- XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
def custom_score(game, player):
    """Calculate the heuristic value of a game state from the point of view
    of the given player.

    This should be the best heuristic function for your project submission.

    Note: this function should be called from within a Player instance as
    `self.score()` -- you should not need to call this function directly.

    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).

    player : object
        A player instance in the current game (i.e., an object corresponding to
        one of the player objects `game.__player_1__` or `game.__player_2__`.)

    Returns
    -------
    float
        The heuristic value of the current game state to the specified player.
    """
    if game.is_loser(player):
        return float("-inf")

    if game.is_winner(player):
        return float("inf")

    my_moves = (game.get_legal_moves(player))
    opp_moves = (game.get_legal_moves(game.get_opponent(player)))

    # If the opponent hmy_score - (1-factor) * opp_scoreas np moves, always chose this move - 100% or 1
    if len(opp_moves) == 0:
        return float("+inf")
    elif len(my_moves) == 0:
        return float("-inf")
    else:
        #my_y, my_x = game.get_player_location(player)
        #opp_y, opp_x = game.get_player_location(game.get_opponent(player))
        #dist_to_opp = ((my_y - opp_y)**2 + (my_x - opp_x)**2)
        #percent_game_complete
        percent_game_complete = (game.move_count)/(game.width * game.height)
        '''if len(my_moves) == 1:
            if my_moves[0] in opp_moves:
                return float("-inf")'''
        #return float(2 * my_moves + (1 - factor) * dist_to_opp)
        #return float(my_moves/7 + (dist_to_opp - 2**0.5)/(6*2**0.5))
        my_no_future_moves = 0
        #my_sum_future_moves = len(my_moves)
        #opp_no_future_moves_count = 0
        #opp_sum_future_moves = len(opp_moves)
        my_max_moves = 0
        opp_max_moves = 0
        for move in my_moves:
            no_of_moves = len(game.forecast_move(move).get_legal_moves(player))
            if not game._Board__get_moves(move):
                my_no_future_moves += 1
            if no_of_moves > my_max_moves:
                my_max_moves = no_of_moves
            #my_total_moves += no_of_moves
        for move in opp_moves:
            opp_no_of_moves = len(game.forecast_move(move).get_legal_moves(game.get_opponent(player)))
            if opp_no_of_moves > opp_max_moves:
                opp_max_moves = opp_no_of_moves
            #opp_total_moves += opp_no_of_moves
        '''if percent_game_complete < 0.6:
            return float((len(my_moves) + my_max_moves  - my_no_future_moves) - (len(opp_moves) + opp_max_moves))
        else:
            return float((len(my_moves) + my_max_moves  - my_no_future_moves))'''
        #return float(len(my_moves) - (percent_game_complete) * len(opp_moves))
        return float((len(my_moves) + my_max_moves - (1-percent_game_complete)*(len(opp_moves) + opp_max_moves)))

#heuristic - 7 - heuristic - 4
def custom_score(game, player):
    """Calculate the heuristic value of a game state from the point of view
    of the given player.

    This should be the best heuristic function for your project submission.

    Note: this function should be called from within a Player instance as
    `self.score()` -- you should not need to call this function directly.

    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).

    player : object
        A player instance in the current game (i.e., an object corresponding to
        one of the player objects `game.__player_1__` or `game.__player_2__`.)

    Returns
    -------
    float
        The heuristic value of the current game state to the specified player.
    """
    if game.is_loser(player):
        return float("-inf")

    if game.is_winner(player):
        return float("inf")

    my_moves = (game.get_legal_moves(player))
    opp_moves = (game.get_legal_moves(game.get_opponent(player)))

    # If the opponent hmy_score - (1-factor) * opp_scoreas np moves, always chose this move - 100% or 1
    '''if len(opp_moves) == 0:
        return float("+inf")
    elif len(my_moves) == 0:
        return float("-inf")
    else:'''
    #my_y, my_x = game.get_player_location(player)
    #opp_y, opp_x = game.get_player_location(game.get_opponent(player))
    #dist_to_opp = ((my_y - opp_y)**2 + (my_x - opp_x)**2)
    #percent_game_complete
    percent_game_complete = (game.move_count)/(game.width * game.height)
    '''if len(my_moves) == 1:
        if my_moves[0] in opp_moves:
            return float(-100)
    #return float(2 * my_moves + (1 - factor) * dist_to_opp)
    #return float(my_moves/7 + (dist_to_opp - 2**0.5)/(6*2**0.5))
    my_no_future_moves = 0
    #my_sum_future_moves = len(my_moves)
    #opp_no_future_moves_count = 0
    #opp_sum_future_moves = len(opp_moves)
    my_max_moves = 0
    opp_max_moves = 0
    for move in my_moves:
        no_of_moves = len(game.forecast_move(move).get_legal_moves(player))
        if not game._Board__get_moves(move):
            my_no_future_moves += 1
        if no_of_moves > my_max_moves:
            my_max_moves = no_of_moves
        #my_total_moves += no_of_moves
    for move in opp_moves:
        opp_no_of_moves = len(game.forecast_move(move).get_legal_moves(game.get_opponent(player)))
        if opp_no_of_moves > opp_max_moves:
            opp_max_moves = opp_no_of_moves
        #opp_total_moves += opp_no_of_moves'''
    if percent_game_complete < 0.9:
        return float(len(my_moves) - (percent_game_complete)*(len(opp_moves)))
    else:
        if len(my_moves) == 1:
            if my_moves[0] in opp_moves:
                return float(-100)
        my_max_moves = 0
        for move in my_moves:
            no_of_moves = len(game.forecast_move(move).get_legal_moves(player))
            if no_of_moves > my_max_moves:
                my_max_moves = no_of_moves
            #my_total_moves += no_of_moves
        return float(my_max_moves + len(my_moves))

#heauristic -8 - heuristic -3

def custom_score(game, player):
    """Calculate the heuristic value of a game state from the point of view
    of the given player.

    This should be the best heuristic function for your project submission.

    Note: this function should be called from within a Player instance as
    `self.score()` -- you should not need to call this function directly.

    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).

    player : object
        A player instance in the current game (i.e., an object corresponding to
        one of the player objects `game.__player_1__` or `game.__player_2__`.)

    Returns
    -------
    float
        The heuristic value of the current game state to the specified player.
    """
    if game.is_loser(player):
        return float("-inf")

    if game.is_winner(player):
        return float("inf")

    my_moves = (game.get_legal_moves(player))
    opp_moves = (game.get_legal_moves(game.get_opponent(player)))
    percent_game_complete = (game.move_count)/(game.width * game.height)
    my_max_moves = 0
    my_no_future_moves=0
    opp_no_future_moves=0
    my_total_moves = len(my_moves)
    opp_total_moves = len(opp_moves)
    for move in my_moves:
        no_of_moves = len(game.forecast_move(move).get_legal_moves(player))
        if not game._Board__get_moves(move):
            my_no_future_moves += 1
        if no_of_moves > my_max_moves:
            my_max_moves = no_of_moves
            my_total_moves += no_of_moves
    for move in opp_moves:
        opp_total_moves += len(game.forecast_move(move).get_legal_moves(game.get_opponent(player)))
        if not game._Board__get_moves(move):
            opp_no_future_moves +=1
    if percent_game_complete < 0.9:
        return float(my_total_moves - my_no_future_moves - percent_game_complete*(opp_total_moves - opp_no_future_moves))
    else:
        if len(my_moves) == 1:
            if my_moves[0] in opp_moves:
                return float(-100)
        return float(my_max_moves + len(my_moves))


#heuristic - 9 - heuristic - 5
def custom_score(game, player):
    """Calculate the heuristic value of a game state from the point of view
    of the given player.

    This should be the best heuristic function for your project submission.

    Note: this function should be called from within a Player instance as
    `self.score()` -- you should not need to call this function directly.

    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).

    player : object
        A player instance in the current game (i.e., an object corresponding to
        one of the player objects `game.__player_1__` or `game.__player_2__`.)

    Returns
    -------
    float
        The heuristic value of the current game state to the specified player.
    """
    if game.is_loser(player):
        return float("-inf")

    if game.is_winner(player):
        return float("inf")

    my_moves = (game.get_legal_moves(player))
    opp_moves = (game.get_legal_moves(game.get_opponent(player)))

    # If the opponent hmy_score - (1-factor) * opp_scoreas np moves, always chose this move - 100% or 1
    '''if len(opp_moves) == 0:
        return float("+inf")
    elif len(my_moves) == 0:
        return float("-inf")
    else:'''
    #my_y, my_x = game.get_player_location(player)
    #opp_y, opp_x = game.get_player_location(game.get_opponent(player))
    #dist_to_opp = ((my_y - opp_y)**2 + (my_x - opp_x)**2)
    #percent_game_complete
    percent_game_complete = (game.move_count)/(game.width * game.height)

    #my_max_moves = 0
    my_total_moves = len(my_moves)
    opp_total_moves = len(opp_moves)
    for move in my_moves:
        no_of_moves = len(game.forecast_move(move).get_legal_moves(player))
        #if no_of_moves > my_max_moves:
        #    my_max_moves = no_of_moves
        my_total_moves += no_of_moves
    for move in opp_moves:
        opp_total_moves += len(game.forecast_move(move).get_legal_moves(game.get_opponent(player)))
    if percent_game_complete < 0.8:
        return float(my_total_moves - percent_game_complete*(opp_total_moves))
        #return float(len(my_moves) - (percent_game_complete)*(len(opp_moves)))
    else:
        if len(my_moves) == 1:
            if my_moves[0] in opp_moves:
                return float(-100)
        '''my_max_moves = 0
        for move in my_moves:
            no_of_moves = len(game.forecast_move(move).get_legal_moves(player))
            if no_of_moves > my_max_moves:
                my_max_moves = no_of_moves
            #my_total_moves += no_of_moves'''
        return float(my_total_moves)
    #return float(len(my_moves) - (percent_game_complete) * len(opp_moves))
    #return float((len(my_moves) + my_max_moves - (1-percent_game_complete)*(len(opp_moves) + opp_max_moves)))

#heuristic - 10 - heuristic 6
def custom_score(game, player):
    """Calculate the heuristic value of a game state from the point of view
    of the given player.

    This should be the best heuristic function for your project submission.

    Note: this function should be called from within a Player instance as
    `self.score()` -- you should not need to call this function directly.

    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).

    player : object
        A player instance in the current game (i.e., an object corresponding to
        one of the player objects `game.__player_1__` or `game.__player_2__`.)

    Returns
    -------
    float
        The heuristic value of the current game state to the specified player.
    """
    if game.is_loser(player):
        return float("-inf")

    if game.is_winner(player):
        return float("inf")

    my_moves = (game.get_legal_moves(player))
    opp_moves = (game.get_legal_moves(game.get_opponent(player)))

    # If the opponent hmy_score - (1-factor) * opp_scoreas np moves, always chose this move - 100% or 1
    '''if len(opp_moves) == 0:
        return float("+inf")
    elif len(my_moves) == 0:
        return float("-inf")
    else:'''
    #my_y, my_x = game.get_player_location(player)
    #opp_y, opp_x = game.get_player_location(game.get_opponent(player))
    #dist_to_opp = ((my_y - opp_y)**2 + (my_x - opp_x)**2)
    #percent_game_complete
    percent_game_complete = (game.move_count)/(game.width * game.height)
    '''if len(my_moves) == 1:
        if my_moves[0] in opp_moves:
            return float(-100)
    #return float(2 * my_moves + (1 - factor) * dist_to_opp)
    #return float(my_moves/7 + (dist_to_opp - 2**0.5)/(6*2**0.5))
    my_no_future_moves = 0
    #my_sum_future_moves = len(my_moves)
    #opp_no_future_moves_count = 0
    #opp_sum_future_moves = len(opp_moves)
    my_max_moves = 0
    opp_max_moves = 0
    for move in my_moves:
        no_of_moves = len(game.forecast_move(move).get_legal_moves(player))
        if not game._Board__get_moves(move):
            my_no_future_moves += 1
        if no_of_moves > my_max_moves:
            my_max_moves = no_of_moves
        #my_total_moves += no_of_moves
    for move in opp_moves:
        opp_no_of_moves = len(game.forecast_move(move).get_legal_moves(game.get_opponent(player)))
        if opp_no_of_moves > opp_max_moves:
            opp_max_moves = opp_no_of_moves
        #opp_total_moves += opp_no_of_moves'''
    if percent_game_complete < 0.9:
        w, h = game.width / 2., game.height / 2.
        y, x = game.get_player_location(player)
        center_dist_factor = ((h - y)**2 + (w - x)**2)/10
        return float(len(my_moves) + percent_game_complete*center_dist_factor - (percent_game_complete)*(len(opp_moves)))
    else:
        if len(my_moves) == 1:
            if my_moves[0] in opp_moves:
                return float(-100)
        my_max_moves = 0
        for move in my_moves:
            no_of_moves = len(game.forecast_move(move).get_legal_moves(player))
            if no_of_moves > my_max_moves:
                my_max_moves = no_of_moves
            #my_total_moves += no_of_moves
        return float(my_max_moves + len(my_moves))
