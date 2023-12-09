import random
import time 

INIT_BLANCE = 275
GOAL = INIT_BLANCE + INIT_BLANCE*0.25
BET = 5
ROULETTE_NUMS = [-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]
BET_ON = []
    
print("INIT_BLANCE", INIT_BLANCE)
print("GOAL", GOAL)
print("BET", BET)

def drawNum():
    random.shuffle(ROULETTE_NUMS)
    return random.choice(ROULETTE_NUMS)

def oneTurn(player_blance, previous_bet_amount, bet_amount, count, print_on):
    if print_on: time.sleep(0.5)
    if player_blance - bet_amount > 0 and player_blance < GOAL:
        if print_on: print(f"---------{count}-----------\nPlayer Balance: {player_blance}\nBet Amount: {bet_amount}")
        # Draw a num
        result_num = drawNum()
        # Check win/lose
        # WIN
        if result_num in BET_ON:
            if print_on: print(f"✅WIN\nLand: {result_num}\nEarn: {bet_amount*2}")
            player_blance += bet_amount*2
            previous_bet_amount = 0
            bet_amount = BET
            count +=1
            return oneTurn(player_blance, previous_bet_amount, bet_amount, count=count, print_on=print_on)
            
        # LOSE
        else:
            if print_on: print(f"❌LOSE\nLand: {result_num}\nLost: {bet_amount}")
            player_blance -= bet_amount
            new_bet_amount = bet_amount + previous_bet_amount
            previous_bet_amount = bet_amount
            bet_amount = new_bet_amount
            count +=1
            return oneTurn(player_blance, previous_bet_amount, bet_amount, count=count, print_on=print_on)
            
    elif player_blance - bet_amount < 0:
        # if print_on: print("Insuffient balance!!!")
        return player_blance, count
    elif player_blance >= GOAL:
        # if print_on: print("GOAL has reached!!!")
        return player_blance, count
    else:
        # if print_on: print("Error!!!")
        return player_blance, count
 
def main():
    
    while len(BET_ON) < 12:
        num = drawNum()
        if num not in BET_ON:
            BET_ON.append(num)
    print(BET_ON)
    
    win = 0
    lose = 0
    play_count = 10000
    play_count_list = []
    for i in range(play_count):
        result, count = oneTurn(player_blance=INIT_BLANCE, previous_bet_amount= 0 , bet_amount=BET, count=0, print_on=False)
        play_count_list.append(float(count))
        if result >= GOAL:
            win+=1
        else:
            lose+=1
    # print("WIN", win)
    # print("LOSE", lose)
    print("WIN Rate", float(win)/float(play_count))
    print("Average Count Play:", sum(play_count_list) / len(play_count_list) )
        
    # balance_list = []
    # max_lose_list = []
    # count_play_list = []
    # total_play = 0
    # play_count = 100
    # for i in range(0,play_count):
    #     balance, max_lose, count_play = onePlay()
    #     balance_list.append(balance)
    #     max_lose_list.append(max_lose)
    #     count_play_list.append(count_play)
    #     total_play += count_play
    
    # print()
    # print("-"*20)
    # count_win = 0 
    # count_lose = 0
    # for i in range(0,play_count):
    #     if balance_list[i] > 0:
    #         result = "WIN" 
    #         count_win += 1
    #     else:
    #         result = "LOSE"
    #         count_lose += 1
    #     print("✅" if count_play_list[i]>100 and result == "LOSE" else "❌", end="")
    #     print(result ,end="  ")
    #     print(balance_list[i], max_lose_list[i], count_play_list[i])
    # print("\nWIN:", count_win, "LOSE", count_lose)
    # print("Total play", total_play)
    # print("INIT_B", INIT_B)
    # print("GOAL", GOAL)

if __name__ == "__main__":
    main()
