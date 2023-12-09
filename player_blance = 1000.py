import random
import time 

BET = 5
INIT_B = BET*(2**7)
GOAL = INIT_B + BET*10
def onePlay():
    player_blance = INIT_B
    bet_on_odd = 1 # bet on even
    bet_on_even = 0
    bet = BET
    possible_num = ["00"]
    max_lose_in_row = 0
    for i in range(0,37):
        possible_num.append(str(i))

    # Bet on even
    count_play = 0
    while player_blance > 0 and player_blance < GOAL:
        # time.sleep(0.1)
        count_play +=1
        bet = BET
        # random.shuffle(possible_num)
        land_num = random.choice(possible_num)
        # print("\nLand",land_num)
        if float(land_num) % 2 == bet_on_odd and float(land_num) != 0:
            player_blance += bet
            # print(count_play, "----- WIN -----")
            # print("player_blance",player_blance)
            # print("bet", bet)
            continue
        
        else:
            player_blance -= 10
            lost_in_a_row = 1
            
            # Then bet on odd
            # print(count_play, "----- LOSE", lost_in_a_row , "-----")
            # print("player_blance",player_blance)
            # print("bet", bet)
            while player_blance > 0:
                # time.sleep(0.1)
                count_play +=1
                # random.shuffle(possible_num)
                land_num = random.choice(possible_num)
                # print("\nLand",land_num)
                if float(land_num) % 2 == bet_on_even and float(land_num) != 0:
                    player_blance += bet
                    # print(count_play, "----- WIN -----")
                    # print("player_blance",player_blance)
                    # print("bet", bet)
                    break
                else:
                    lost_in_a_row +=1
                    
                    max_lose_in_row = max(max_lose_in_row, lost_in_a_row)
                        
                    player_blance -= bet
                    bet *=2
                    # print(count_play, "----- LOSE", lost_in_a_row , "-----")
                    # print("player_blance",player_blance)
                    # print("bet", bet)
                    
                    continue
                
    return player_blance, max_lose_in_row, count_play
                
def main():
    balance_list = []
    max_lose_list = []
    count_play_list = []
    total_play = 0
    play_count = 100
    for i in range(0,play_count):
        balance, max_lose, count_play = onePlay()
        balance_list.append(balance)
        max_lose_list.append(max_lose)
        count_play_list.append(count_play)
        total_play += count_play
    
    print()
    print("-"*20)
    count_win = 0 
    count_lose = 0
    for i in range(0,play_count):
        if balance_list[i] > 0:
            result = "WIN" 
            count_win += 1
        else:
            result = "LOSE"
            count_lose += 1
        print("✅" if count_play_list[i]>100 and result == "LOSE" else "❌", end="")
        print(result ,end="  ")
        print(balance_list[i], max_lose_list[i], count_play_list[i])
    print("\nWIN:", count_win, "LOSE", count_lose)
    print("Total play", total_play)
    print("INIT_B", INIT_B)
    print("GOAL", GOAL)

if __name__ == "__main__":
    main()
