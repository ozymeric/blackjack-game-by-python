logo = """
.------.        _     _            _    _            _    
|A_  _ |.      | |   | |          | |  (_)          | |   
|( \/ ).-----. | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  | | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ | | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / | |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                        _/ |                
      `------'                       |__/           
"""

account = """
    _   ___ ___ ___  _   _ _  _ _____   _ 
   /_\ / __/ __/ _ \| | | | \| |_   _| (_)
  / _ \ (_| (_| (_) | |_| | .` | | |    _ 
 /_/ \_\___\___\___/ \___/|_|\_| |_|   (_)
 """

win = """
 __ __   ___   __ __      __    __  ____  ____       __ 
|  T  T /   \ |  T  T    |  T__T  Tl    j|    \     |  T
|  |  |Y     Y|  |  |    |  |  |  | |  T |  _  Y    |  |
|  ~  ||  O  ||  |  |    |  |  |  | |  | |  |  |    |__j
l___, ||     ||  :  |    l  `  '  ! |  | |  |  |     __ 
|     !l     !l     |     \      /  j  l |  |  |    |  T
l____/  \___/  \__,_j      \_/\_/  |____jl__j__j    l__j
"""
lose = """
  ___  ___   _   _    ___ ___  __      _____ _  _ ___ _ 
 |   \| __| /_\ | |  | __| _ \ \ \    / /_ _| \| / __| |
 | |) | _| / _ \| |__| _||   /  \ \/\/ / | || .` \__ \_|
 |___/|___/_/ \_\____|___|_|_\   \_/\_/ |___|_|\_|___(_)
 """

blackjack = """
 _____  ____   _____  _____  __ ___   ____  _____  _____  __ ___
/  _  \/  _/  /  _  \/     \|  |  /   \_  \/  _  \/     \|  |  /
|  _  <|  |---|  _  ||  |--||  _ <  ---|  ||  _  ||  |--||  _ < 
\_____/\_____/\__|__/\_____/|__|__\ \_____/\__|__/\_____/|__|__\
"""

tie = """
  ___ _____ _ ____       _      _____ ___ _____ _ 
 |_ _|_   _( ) ___|     / \    |_   _|_ _| ____| |
  | |  | | |/\___ \    / _ \     | |  | ||  _| | |
  | |  | |    ___) |  / ___ \    | |  | || |___|_|
 |___| |_|   |____/  /_/   \_\   |_| |___|_____(_)
 """

loser = """
 ___      _______  _______  _______  ______      __   __   __  
|   |    |       ||       ||       ||    _ |    |  | |  | |  | 
|   |    |   _   ||  _____||    ___||   | ||    |  | |  | |  | 
|   |    |  | |  || |_____ |   |___ |   |_||_   |  | |  | |  | 
|   |___ |  |_|  ||_____  ||    ___||    __  |  |__| |__| |__| 
|       ||       | _____| ||   |___ |   |  | |   __   __   __  
|_______||_______||_______||_______||___|  |_|  |__| |__| |__| 
 """


winner = """
 __    __  ____  ____   ____     ___  ____   __ 
|  T__T  Tl    j|    \ |    \   /  _]|    \ |  T
|  |  |  | |  T |  _  Y|  _  Y /  [_ |  D  )|  |
|  |  |  | |  | |  |  ||  |  |Y    _]|    / |__j
l  `  '  ! |  | |  |  ||  |  ||   [_ |    \  __ 
 \      /  j  l |  |  ||  |  ||     T|  .  Y|  T
  \_/\_/  |____jl__j__jl__j__jl_____jl__j\_jl__j
                                                
"""

import random

import os
clear = lambda: os.system('clear')

player_s_account = int(
    input("Set your account... \nHow much money do yu have?: $"))
dealer_s_account = player_s_account
bet_amount = int(
    input("\nSet the bet amount... \nHow much bet in a round?: $"))
game = 0
while player_s_account > 0 and dealer_s_account > 0:

    def deal_card():
        cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        return random.choice(cards)

    clear()
    print(account)
    print(f"Your Account: {player_s_account} $")
    print(f"Dealer's Account: {dealer_s_account} $\n")

    player_s_account -= bet_amount
    dealer_s_account -= bet_amount
    bet_on_table = bet_amount * 2

    print(f"Bet Amount: {bet_amount} $")
    print(f"Bet On Table: {bet_on_table} $\n")

    print(f"Your Current Account: {player_s_account} $")
    print(f"Dealer's Current Account: {dealer_s_account} $\n")
    input("Let's Play... \nType Enter:")
    clear()
    print(logo)
    game += 1
    print(f" ROUND: {game} ".center(30, '_'))

    player_s_hand = [deal_card(), deal_card()]
    dealer_s_hand = [deal_card(), deal_card()]

    if sum(player_s_hand) > 21:
        player_s_hand[0] = 1
    if sum(dealer_s_hand) > 21:
        dealer_s_hand[0] = 1

    print(f"\nDealer's Hand: {dealer_s_hand[0]}")
    print(f"Your Hand: {player_s_hand} - Total: {sum(player_s_hand)}")

    if sum(player_s_hand) == 21 and sum(dealer_s_hand) != 21:
        clear()
        print(blackjack)
        print(win)
        print(
            f"Dealer's Hand: {dealer_s_hand} - Total: {sum(dealer_s_hand)}\n")
        print(f"Your Hand: {player_s_hand} - Total: {sum(player_s_hand)}\n")
        player_s_account += bet_on_table
        print(f"\nYour Current Account: {player_s_account} $")
        print(f"Dealer's Current Account: {dealer_s_account} $\n")
        input("Type Enter To Continue...")
        clear()
    elif sum(dealer_s_hand) == 21 and sum(player_s_hand) != 21:
        clear()
        print(blackjack)
        print(lose)
        print(
            f"Dealer's Hand: {dealer_s_hand} - Total: {sum(dealer_s_hand)}\n")
        print(f"Your Hand: {player_s_hand} - Total: {sum(player_s_hand)}")
        dealer_s_account += bet_on_table
        print(f"\nYour Current Account: {player_s_account} $")
        print(f"Dealer's Current Account: {dealer_s_account} $\n")
        input("Type Enter To Continue...")
        clear()
    elif sum(player_s_hand) == 21 and sum(dealer_s_hand) == 21:
        clear()
        print(tie)
        print(
            f"Dealer's Hand: {dealer_s_hand} - Total: {sum(dealer_s_hand)}\n")
        print(f"Your Hand: {player_s_hand} - Total: {sum(player_s_hand)}\n")
        player_s_account += bet_amount
        dealer_s_account += bet_amount
        print(f"\nYour Current Account: {player_s_account} $")
        print(f"Dealer's Current Account: {dealer_s_account} $\n")
        input("Type Enter To Continue...")
        clear()
    elif sum(player_s_hand) < 21 and sum(dealer_s_hand) < 21:
        choice = input("\nHit or Stand? Type 'H' or 'S': ").lower()
        clear()
        while True:
            if choice == "s":
                while sum(dealer_s_hand) < 17:
                    dealer_s_hand.append(deal_card())
                    if sum(dealer_s_hand) > 21 and (11 in dealer_s_hand):
                        a = dealer_s_hand.index(11)
                        dealer_s_hand.insert(a,1)
                        dealer_s_hand.remove(11)
                if sum(dealer_s_hand) == 21:
                    print(blackjack)
                    print(lose)
                    print(
                        f"\nDealer's Hand: {dealer_s_hand} - Total: {sum(dealer_s_hand)}"
                    )
                    print(
                        f"Your Hand: {player_s_hand} - Total: {sum(player_s_hand)}\n"
                    )
                    dealer_s_account += bet_on_table
                    print(f"Your Current Account: {player_s_account} $")
                    print(f"Dealer's Current Account: {dealer_s_account} $\n")
                    input("Type Enter To Continue...")
                    clear()
                    break
                elif sum(dealer_s_hand) > 21:
                    print(win)
                    print(
                        f"\nDealer's Hand: {dealer_s_hand} - Total: {sum(dealer_s_hand)}"
                    )
                    print(
                        f"Your Hand: {player_s_hand} - Total: {sum(player_s_hand)}\n"
                    )
                    player_s_account += bet_on_table
                    print(f"Your Current Account: {player_s_account} $")
                    print(f"Dealer's Current Account: {dealer_s_account} $\n")
                    input("Type Enter To Continue...")
                    clear()
                    break
                elif (sum(player_s_hand) < 21 and sum(dealer_s_hand) < 21
                      ) and (sum(player_s_hand) > sum(dealer_s_hand)):
                    print(win)
                    print(
                        f"\nDealer's Hand: {dealer_s_hand} - Total: {sum(dealer_s_hand)}"
                    )
                    print(
                        f"Your Hand: {player_s_hand} - Total: {sum(player_s_hand)}\n"
                    )
                    player_s_account += bet_on_table
                    print(f"Your Current Account: {player_s_account} $")
                    print(f"Dealer's Current Account: {dealer_s_account} $\n")
                    input("Type Enter To Continue...")
                    clear()
                    break
                elif (sum(player_s_hand) < 21 and sum(dealer_s_hand) < 21
                      ) and (sum(player_s_hand) < sum(dealer_s_hand)):
                    print(lose)
                    print(
                        f"\nDealer's Hand: {dealer_s_hand} - Total: {sum(dealer_s_hand)}"
                    )
                    print(
                        f"Your Hand: {player_s_hand} - Total: {sum(player_s_hand)}\n"
                    )
                    dealer_s_account += bet_on_table
                    print(f"Your Current Account: {player_s_account} $")
                    print(f"Dealer's Current Account: {dealer_s_account} $\n")
                    input("Type Enter To Continue...")
                    clear()
                    break
                elif (sum(player_s_hand) < 21
                      and sum(dealer_s_hand) < 21) and (sum(player_s_hand)
                                                        == sum(dealer_s_hand)):
                    print(tie)
                    print(
                        f"\nDealer's Hand: {dealer_s_hand} - Total: {sum(dealer_s_hand)}"
                    )
                    print(
                        f"Your Hand: {player_s_hand} - Total: {sum(player_s_hand)}\n"
                    )
                    player_s_account += bet_amount
                    dealer_s_account += bet_amount
                    print(f"Your Current Account: {player_s_account} $")
                    print(f"Dealer's Current Account: {dealer_s_account} $\n")
                    input("Type Enter To Continue...")
                    clear()
                    break
            elif choice == "h":
                player_s_hand.append(deal_card())
                while sum(player_s_hand) > 21 and (11 in player_s_hand):
                        b = player_s_hand.index(11)
                        player_s_hand.insert(b,1)
                        player_s_hand.remove(11)
                if sum(player_s_hand) > 21:	
                    print(lose)
                    print(
                        f"\nDealer's Hand: {dealer_s_hand} - Total: {sum(dealer_s_hand)}"
                    )
                    print(
                        f"Your Hand: {player_s_hand} - Total: {sum(player_s_hand)}\n"
                    )
                    dealer_s_account += bet_on_table
                    print(f"Your Current Account: {player_s_account} $")
                    print(f"Dealer's Current Account: {dealer_s_account} $\n")
                    input("Type Enter To Continue...")
                    clear()
                    break
                elif sum(player_s_hand) == 21:
                    print(blackjack)
                    print(win)
                    print(
                        f"Dealer's Hand: {dealer_s_hand} - Total: {sum(dealer_s_hand)}"
                    )
                    print(
                        f"Your Hand: {player_s_hand} - Total: {sum(player_s_hand)}\n"
                    )
                    player_s_account += bet_on_table
                    print(f"Your Current Account: {player_s_account} $")
                    print(f"Dealer's Current Account: {dealer_s_account} $\n")
                    input("Type Enter To Continue...")
                    clear()
                    break
                elif sum(player_s_hand) < 21:
                    print(f"\nDealer's Hand: {dealer_s_hand[0]}")
                    print(
                        f"Your Hand: {player_s_hand} - Total: {sum(player_s_hand)}"
                    )
                    choice = input("\nHit or Stand? Type 'H' or 'S': ").lower()
                    clear()
if player_s_account == 0:
    print(loser)
else:
    print(winner)
