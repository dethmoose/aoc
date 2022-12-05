import aoc_utils
from enum import Enum

input_data = aoc_utils.getInputString(2)
Move = Enum("Move", ["ROCK", "PAPER", "SCISSOR"])
Goal = Enum("Goal", ["LOSE", "DRAW", "WIN"])

winning_moves = {
    Move.ROCK: Move.SCISSOR,
    Move.PAPER: Move.ROCK,
    Move.SCISSOR: Move.PAPER
}

def getMoveList(move_translation_table):
    move_list = [n.split() for n in input_data.split("\n") if n]
    move_list = [(move_translation_table.get(n[0]), move_translation_table.get(n[1])) for n in move_list]
    return move_list

def solve1():
    move_translation_table = {
        "A": Move.ROCK,
        "X": Move.ROCK,
        "B": Move.PAPER,
        "Y": Move.PAPER,
        "C": Move.SCISSOR,
        "Z": Move.SCISSOR
    }
    move_list = getMoveList(move_translation_table)
    score = 0
    for opponent, player in move_list:
        score += player.value
        if opponent == player:
            score += 3
        elif opponent == winning_moves.get(player):
            score += 6
    return score

def solve2():
    move_translation_table = {
        "A": Move.ROCK,
        "B": Move.PAPER,
        "C": Move.SCISSOR,
        "X": Goal.LOSE,
        "Y": Goal.DRAW,
        "Z": Goal.WIN
    }
    move_list = getMoveList(move_translation_table)
    score = 0
    for opponent, goal in move_list:
        if goal == Goal.WIN:
            score += winning_moves.get(winning_moves.get(opponent)).value + 6
        elif goal == Goal.LOSE:
            score += winning_moves.get(opponent).value
        else:
            score += opponent.value + 3
    return score

def main():
    print(solve1())
    print(solve2())

if __name__ == "__main__":
    main()