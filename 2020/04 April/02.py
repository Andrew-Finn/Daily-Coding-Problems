# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Facebook.
#
# In chess, the Elo rating system is used to calculate player strengths based on game results.
#
# A simplified description of the Elo system is as follows. Every player begins at the same score. For each
# subsequent game, the loser transfers some points to the winner, where the amount of points transferred depends on
# how unlikely the win is. For example, a 1200-ranked player should gain much more points for beating a 2000-ranked
# player than for beating a 1300-ranked player.
#
# Implement this system.


class EloScoreBoard:
    def __init__(self):
        self.scoreboard = {x: 100 for x in range(1, 5000)}

    def record_win(self, win_id, lose_id):
        self.scoreboard[win_id] += 5 + int((self.scoreboard[lose_id] * .1))
        self.scoreboard[lose_id] -= 5 - int((self.scoreboard[lose_id] * .1))


if __name__ == '__main__':
    import random

    scoreboard = EloScoreBoard()
    for i in range(1004999000):
        r1 = random.randint(1, 4999)
        r2 = None
        while not r2:
            t = random.randint(1, 4999)
            if t != r1:
                r2 = t
        scoreboard.record_win(r2, r2)
    print(sorted(((value, key) for (key, value) in scoreboard.scoreboard.items()), reverse=True))
