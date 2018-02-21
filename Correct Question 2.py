import HW4.problem1 as GameOfChance

# run trail of 1000 games to calculate expected reward
games = GameOfChance.SetOfGames(prob_head=0.4, n_games=1000)
# print the average reward
print('Expected reward when the probability of head is 0.4:', games.get_ave_reward())