import random
import time
import math
import numpy as np
def pass_right(list_players, current_player):
    if current_player == 99:
        list_players[0] +=1
        list_players[99] -= 1
        return list_players
    else:
        list_players[current_player] -=1
        list_players[current_player + 1] += 1
        return list_players

def pass_left(list_players,current_player):
    if current_player == 0:
        list_players[99] +=1
        list_players[0] -= 1
        return list_players
    else:
        list_players[current_player] -=1
        list_players[current_player - 1] += 1
        return list_players
    

def roll_dice(list_players, current_player):
    roll_dice = random.randint(1,6)
    if roll_dice == 6:
        return pass_right(list_players,current_player)
    if roll_dice == 1:
        return pass_left(list_players, current_player)
    
    return list_players

def round_game(list_players):
    players_w_dice = []
    for i in range(len(list_players)):
        if list_players[i] == 1:
            players_w_dice.append(i)
        if list_players[i] == 2:
            #print(list_players[i], i)
            return i
    
    #print(players_w_dice)
    if len(players_w_dice) == 1:
        #returns loser
        return players_w_dice[0]
    #each player with dice rolls it 

    for i in range(len(players_w_dice)):
        players = roll_dice(list_players, players_w_dice[i])
    return 10000

def average(list_data):
    sum = 0
    for i in range(len(list_data)):
        sum += list_data[i]
    return sum/float(i)

def variance(list_data):
    avg = average(list_data)
    var = 0
    for i in range(len(list_data)):
        var += (list_data[i] - avg)**2
    size_sample = len(list_data)
    var /= float(len(list_data))

    return math.sqrt(var)/size_sample
    

dice = []
for i in range(10000):
    dice.append(random.randint(1,6))
print(average(dice), variance(dice))


total_games = []
losers = []
for i in range(1000):
    #0 --> no dice
    players = [0]*100
    #players sit in circle
    #opposite sides do have circle
    players[0] = 1
    players[49] = 1

    loser = 1000
    rounds = 0
    while(loser > 100):
        loser = round_game(players)
        rounds += 1
    total_games.append(rounds)
    losers.append(loser)


#print("Rounds: ", total_games)
#print("Losers: ", losers)

print(average(total_games),"+-",variance(total_games))


