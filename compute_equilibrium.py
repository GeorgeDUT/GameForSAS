"""
experiment settings
all components: [MV101, P101, MV201, P302, MV302, P402, P501, MV501]
1_bad P101 is bad
1_bad_2 P501 is bad
2_bad P101, P501 is bad
"""
import gambit
import time

# import sys
# print('Python: {}'.format(sys.version))

def psum(alist):
    return_sum = 0.0
    for a in alist:
        if a>=0:
            return_sum = return_sum + a
    return return_sum

start_time = time.time()
print('start time',start_time)

g_good = gambit.Game.read_game("gametree/8_player_2_bad_mv302p402")
# g_bad = gambit.Game.read_game("gametree/8_player_1_bad_p501")
# g_101_bad = gambit.Game.read_game("gametree/8_player_1_bad_mv501")
# g_501_bad = gambit.Game.read_game("gametree/8_player_1_bad_mv501")

solver = gambit.nash.ExternalLogitSolver()

 p_good = solver.solve(g_good)
 for i in range(len(p_good)):
     print(p_good[i])
 for i in range(len(g_good.players)):
     print('utility',i,':',p_good[0].payoff(g_good.players[i]))
 end_time = time.time()
 print("time_cost",end_time-start_time)

# p_bad = solver.solve(g_bad)
# for i in range(len(p_bad)):
#     print(p_bad[i])
# for i in range(len(g_bad.players)):
#     print('utility',i,':',p_bad[0].payoff(g_bad.players[i]))
#
# end_time = time.time()
# print("time_cost",end_time-start_time)
#
# p_101_bad = solver.solve(g_101_bad)
# for i in range(len(p_101_bad)):
#     print(p_101_bad[i])
# for i in range(len(g_101_bad.players)):
#     print('utility',i,':',p_101_bad[0].payoff(g_101_bad.players[i]))
#
# end_time = time.time()
# print("time_cost",end_time-start_time)

# p_501_bad = solver.solve(g_501_bad)
# for i in range(len(p_501_bad)):
#     print(p_501_bad[i])
# for i in range(len(g_501_bad.players)):
#     print('utility', i, ':', p_501_bad[0].payoff(g_501_bad.players[i]))
