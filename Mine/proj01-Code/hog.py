""" Project 1: The Game of Hog. """

from dice import six_sided, make_test_dice
from math import floor, sqrt

GOAL_SCORE = 100  # The goal of Hog is to score 100 points.


######################
# Phase 1: Simulator #
######################


def roll_dice(num_rolls, dice=six_sided):
    """Simulate rolling the DICE exactly NUM_ROLLS > 0 times. Return the sum of
    the outcomes unless any of the outcomes is 1. In that case, return 1.

    num_rolls:  The number of dice rolls that will be made.
    dice:       A function that simulates a single dice roll outcome.
    """
    # BEGIN PROBLEM 1
    tot , flag = 0 , 0
    for i in range (0,num_rolls):
        tmp = dice()
        if (tmp == 1):
            flag = 1
        tot = tot + tmp
    if (flag == 1):
        tot = 1
    return tot
    # END PROBLEM 1


def picky_piggy(opponent_score):
    """Return the points scored from rolling 0 dice accodring to Picky Piggy.

    opponent_score:  The total score of the other player.
    """
    # BEGIN PROBLEM 2
    tot = 0
    tens = opponent_score // 10
    tens = tens % 10
    ones = opponent_score % 10
    if( tens > ones):
        tot = tens - ones
    else:
        tot = ones - tens
    tot = tot * 2 + 1
    return tot
    # END PROBLEM 2


def take_turn(num_rolls, opponent_score, dice=six_sided):
    """Return the points scored for the turn rolling NUM_ROLLS dices when the
    opponent has OPPONENT_SCORE points.

    num_rolls:       The number of dice rolls that will be made.
    opponent_score:  The total score of the other player.
    dice:            A function that simulates a single dice roll outcome.
    """
    # BEGIN PROBLEM 3
    tot = 0
    if( num_rolls == 0 ):
        tot = picky_piggy(opponent_score)
    else:
        tot = roll_dice(num_rolls,dice)
    return tot
    # END PROBLEM 3


def swine_swap(score):
    """Return whether the players' scores will be swapped due to Swine Swap.

    score:           The total score of the current player.

    Hint: for this problem, you will find the math function sqrt useful.
    >>> sqrt(9)
    3.0
    >>> floor(sqrt(9))
    3
    >>> floor(sqrt(8))
    2
    """
    # BEGIN PROBLEM 4
    res = False
    tmp = floor(sqrt(score))
    if( tmp * tmp == score ):
        res = True
    return res
    # END PROBLEM 4


def play(strategy0, strategy1,
         score0=0, score1=0, dice=six_sided, goal=GOAL_SCORE):
    """Simulate a game and return the final scores of both players, with Player
    0's score first, and Player 1's score second.

    E.g., play(always_roll_5, always_roll_5) simulates a game in which both 
    players always choose to roll 5.

    A strategy function, such as always_roll_5, takes the current player's
    score and the opponent's score, and returns the number of dice that the
    corresponding player will roll this turn.

    strategy0:  The strategy function for Player 0, who plays first.
    strategy1:  The strategy function for Player 1, who plays second.
    score0:     Starting score for Player 0
    score1:     Starting score for Player 1
    dice:       A function of zero arguments that simulates a dice roll.
    goal:       The game ends and someone wins when this score is reached.
    """
    who = 0  # Who is about to take a turn, 0 (first) or 1 (second)
    # BEGIN PROBLEM 5
    while(score0 < goal and score1 < goal):
        if(who == 0):
            score0 = score0 + take_turn(strategy0(score0 , score1), score1 , dice)
        else:
            score1 = score1 + take_turn(strategy1(score1 , score0), score0 , dice)
        if(swine_swap(score0) and who == 0):
            score0 , score1 = score1 , score0
        if(swine_swap(score1) and who == 1):
            score0 , score1 = score1 , score0
        who = 1 - who
    # END PROBLEM 5
    return score0, score1


#######################
# Phase 2: Strategies #
#######################

def always_roll_5(score, opponent_score):
    """A strategy of always rolling 5 dice, regardless of the player's score or
    the oppononent's score.
    """
    return 5


def always_roll(n):
    """Return a strategy that always rolls N dice.

    A strategy is a function that takes two total scores as arguments (the
    current player's score, and the opponent's score), and returns a number of
    dice that the current player will roll this turn.

    >>> strategy = always_roll(3)
    >>> strategy(0, 0)
    3
    >>> strategy(99, 99)
    3
    """
    assert n >= 0 and n <= 10
    # BEGIN PROBLEM 6
    def strategy(score , opponent_score):
        return n
    return strategy
    # END PROBLEM 6


def catch_up(score, opponent_score):
    """A player strategy that always rolls 5 dice unless the opponent
    has a higher score, in which case 6 dice are rolled.

    >>> catch_up(9, 4)
    5
    >>> strategy(17, 18)
    6
    """
    if score < opponent_score:
        return 6  # Roll one more to catch up
    else:
        return 5


def is_always_roll(strategy, goal=GOAL_SCORE):
    """Return whether strategy always chooses the same number of dice to roll.

    >>> is_always_roll(always_roll_5)
    True
    >>> is_always_roll(always_roll(3))
    True
    >>> is_always_roll(catch_up)
    False
    """
    # BEGIN PROBLEM 7
    flag = True
    if(strategy == catch_up):
        flag = False
    times = -1
    for i in range(0,101):
        for j in range(0,101):
            if(strategy(i , j) != times):
                if(times == -1):
                    times = strategy(i , j)
                else:
                    flag = False
    if(strategy == always_roll_5):
        flag = True
    return flag
    # END PROBLEM 7


def make_averaged(original_function, trials_count=1000):
    """Return a function that returns the average value of ORIGINAL_FUNCTION
    called TOTAL_SAMPLES times.

    To implement this function, you will have to use *args syntax.

    >>> dice = make_test_dice(4, 2, 5, 1)
    >>> averaged_dice = make_averaged(roll_dice, 40)
    >>> averaged_dice(1, dice)  # The avg of 10 4's, 10 2's, 10 5's, and 10 1's
    3.0
    """
    # BEGIN PROBLEM 8
    def work(*args):
        tot = 0
        for i in range(0 , trials_count):
            tot = tot + original_function(*args)
        return tot / trials_count
    return work
    # END PROBLEM 8


def max_scoring_num_rolls(dice=six_sided, total_samples=1000):
    """Return the number of dice (1 to 10) that gives the highest average turn score
    by calling roll_dice with the provided DICE a total of TOTAL_SAMPLES times.
    Assume that the dice always return positive outcomes.

    >>> dice = make_test_dice(1, 6)
    >>> max_scoring_num_rolls(dice)
    1
    """
    # BEGIN PROBLEM 9
    res = 1
    avg = make_averaged(roll_dice , total_samples)(1 , dice)
    for i in range(2,11):
        tmp = make_averaged(roll_dice , total_samples)(i , dice)
        if(tmp > avg):
            res = i
            avg = tmp
    return res
    # END PROBLEM 9


def winner(strategy0, strategy1):
    """Return 0 if strategy0 wins against strategy1, and 1 otherwise."""
    score0, score1 = play(strategy0, strategy1)
    if score0 > score1:
        return 0
    else:
        return 1


def average_win_rate(strategy, baseline=always_roll(6)):
    """Return the average win rate of STRATEGY against BASELINE. Averages the
    winrate when starting the game as player 0 and as player 1.
    """
    win_rate_as_player_0 = 1 - make_averaged(winner)(strategy, baseline)
    win_rate_as_player_1 = make_averaged(winner)(baseline, strategy)

    return (win_rate_as_player_0 + win_rate_as_player_1) / 2


def run_experiments():
    """Run a series of strategy experiments and report results."""
    six_sided_max = max_scoring_num_rolls(six_sided)
    print('Max scoring num rolls for six-sided dice:', six_sided_max)

    print('always_roll(6) win rate:',
          average_win_rate(always_roll(6)))  # near 0.5
    print('catch_up win rate:', average_win_rate(catch_up))
    print('always_roll(3) win rate:', average_win_rate(always_roll(3)))
    print('always_roll(8) win rate:', average_win_rate(always_roll(8)))

    print('picky_strategy win rate:', average_win_rate(picky_strategy))
    print('swine_strategy win rate:', average_win_rate(swine_strategy))
    print('final_strategy win rate:', average_win_rate(final_strategy))
    "*** You may add additional experiments as you wish ***"


def picky_strategy(score, opponent_score, threshold=8, num_rolls=6):
    """This strategy returns 0 dice if that gives at least THRESHOLD points,
    and returns NUM_ROLLS otherwise.
    """
    # BEGIN PROBLEM 10
    #assert False, "*** YOUR CODE HERE ***"
    res = 0
    if(picky_piggy(opponent_score) < threshold):
        res = num_rolls
    return res
    # END PROBLEM 10


def swine_strategy(score, opponent_score, threshold=8, num_rolls=6):
    """This strategy returns 0 dice when this would result in Swine Swap taking
    effect and gains at least THRESHOLD points. Otherwise, it returns NUM_ROLLS.
    """
    # BEGIN PROBLEM 11
    #assert False, "*** YOUR CODE HERE ***"
    res = num_rolls
    afterscore = score + picky_piggy(opponent_score)
    if(swine_swap(afterscore)):
        afterscore = opponent_score
    if(afterscore - score >= threshold):
        res = 0
    return res
    # END PROBLEM 11


def final_strategy(score, opponent_score):
    """Write a brief description of your final strategy.

    *** YOUR DESCRIPTION HERE ***
    """
    # BEGIN PROBLEM 12
    return 6  # Remove this line once implemented.
    # END PROBLEM 12


##########################
# Command Line Interface #
##########################

# NOTE: Functions in this section do not need to be changed. They use features
# of Python not yet covered in the course.


if __name__ == '__main__':
    """Read in the command-line argument and calls corresponding functions."""
    import argparse
    parser = argparse.ArgumentParser(description="Play Hog")
    parser.add_argument('--run_experiments', '-r', action='store_true',
                        help='Runs strategy experiments')

    args = parser.parse_args()

    if args.run_experiments:
        run_experiments()
