from blackjack import *
from time import sleep


player_input = 0
players = []
dealer = Player("Dealer", 0)

while player_input < 7:
    name = input("\nPlease enter your name: ")
    bal = int(input("How many chips would you like to buy? "))
    players.append(Player(name, bal))
    ans = input("Add more players? (y/n)")

    if ans == 'n':
        break

    player_input += 1


def playon():
    print("\n\t\t\tRound Finished")
    global players, dealer
    bankrupt = []
    for player in players:
        player.hand = []
        if player.bal == 0:
            print("{} has lost all of their money".format(player.name))
            bankrupt.append(player)

    for i in range(len(bankrupt)):
        players.remove(bankrupt[-1])

    dealer.hand = []
    ans = input("Continue playing? (Y/N)").strip()

    if ans.upper() == "N":
        global playing
        playing = False
        input("\n\t\t\tGame over!")


playing = True

while playing:

#####################################################################

# Print everyone's balance in a nice format at the start of each round

#####################################################################
    
    print("\n\t\t\tPlayers' balance")
    for player in players:
        print("\n\t\t\t{}\t|\t${}".format(player.name, player.bal))

    deck = Deck()

    print("""\n
                ██████╗░███████╗░██████╗░██╗███╗░░██╗
                ██╔══██╗██╔════╝██╔════╝░██║████╗░██║
                ██████╦╝█████╗░░██║░░██╗░██║██╔██╗██║
                ██╔══██╗██╔══╝░░██║░░╚██╗██║██║╚████║
                ██████╦╝███████╗╚██████╔╝██║██║░╚███║
                ╚═════╝░╚══════╝░╚═════╝░╚═╝╚═╝░░╚══╝\n""")



    for player in players:
        wager = round(float(input("\nPlace your wager {} (min: $5 | max: $500): ".format(player.name))),2)

        if wager < player.bal:
            if 5 <= wager <= 500:
                player.wager = wager
            elif wager > 500:
                player.wager = 500
            else:
                player.wager = 5
        else:
            player.wager = player.bal

        player.bal -= player.wager

    print("\n\nDealer is dealing cards...")
    sleep(1)

    out = [] ## Players who have Blackjack as their first two cards

    for player in players:
        player_cards = deck.deal(2)
        player.hand += player_cards

        sleep(1)
        print("\n{} gets: {} of {} and {} of {} | Total of {}"
            .format(player.name, player.hand[0][0],  player.hand[0][1],  player.hand[1][0],  player.hand[1][1], player.hand_total()))
        sleep(1)

        if player.has_blackjack():
            sleep(1)
            print("\n\t\t\t{} has Blackjack!".format(player.name))
            out.append(player)
    
    for i in range(len(out)):
        players.remove(out[-1])


    dealer_cards = deck.deal(2)
    dealer.hand += dealer_cards

    should_check = False 

    if dealer_cards[0][0] == 'A' or dealer_cards[0][0] in Card().tens: 
    ## Identifies if the dealer should check his other card to see if he has Blackjack
        should_check = True


    print("\nDealer gets: {} of {}"
        .format(dealer_cards[0][0], dealer_cards[0][1]))


    if should_check:
        print("\nDealer checks his other card...")
        sleep(3)
        if dealer.has_blackjack():
            print("\n\t\t\tThe dealer has Blackjack.")

            for player in players:
                print("{} loses their wager".format(player.name))
                player.wager = 0

            for player in out:
                print("\nIt is a push. {}'s wager is returned.".format(player.name))
                player.bal += player.wager
                player.wager = 0
                players.append(player)

            playon()
            continue ############################################################ Next round goes here

        else:
            print("The dealer does not have Blackjack.")
            for player in out:
                player.wins(1.5)

    else:
        for player in out:
            player.wins(1.5)
        
    sleep(2)

    bust_count = 0
    for player in players:
        print("\n{}: Hit, stand, double down, split or surrender".format(player.name))
        choice = input(": ").strip()

        if choice.lower() == "hit":

            sleep(1)
            
            while True:

                print("{} hits!".format(player.name))
                sleep(1)
                new_card = player.hit()
                print("\n{} gets: {} of {} | Total of {}"
                    .format(player.name, new_card[0],  new_card[1], player.hand_total()))
                sleep(1)

                if player.hand_total() == 21:
                    break

                if not player.busted() :

                    again = input("hit or stand\n:").strip()

                    if again.lower() == "hit":
                        continue
                    else:
                        print("{} stands.".format(player.name))
                        break
                else:
                    print("\nBust!")
                    player.wager = 0
                    print("{} loses their wager".format(player.name))
                    out.append(player)
                    bust_count += 1
                    break

        elif choice.lower() == "stand":
            print("\n{} stands.".format(player.name))

    for i in range(bust_count):
        players.remove(out[-1])

    if len(players) == 0:
        print("Dealer wins")
        for player in out:
            players.append(player)
        playon()
        continue ################################################################# Next round

    sleep(1)
    print("\nDealer flips his face-down card...")
    sleep(2)
    print("\nDealer gets: {} of {} | Total of {}"
        .format(dealer_cards[1][0], dealer_cards[1][1], dealer.hand_total()))

    while True:
        if not dealer.busted():
            if dealer.hand_total() >= 17:
                print("\nDealer stands.")
                break
            else:
                print("\nDealer hits.")
                sleep(1)
                extra_card = dealer.hit()
                print("\nDealer gets: {} of {} | Total of {}"
                    .format(extra_card[0],  extra_card[1], dealer.hand_total()))
                sleep(3)
        else:
            print("\nBust!\n")
            for player in players:
                player.wins(1)
            break
            

    if dealer.busted():
        for player in out:
            players.append(player)
        playon()
        continue ############################################################# Next round

    for player in players:
        sleep(2)
        if player.hand_total()>dealer.hand_total():
            player.wins(1)

        elif player.hand_total() == dealer.hand_total():
            print("\nIt is a push. {}'s wager is returned.".format(player.name))
            player.bal += player.wager
            player.wager = 0

        else:
            print("{} loses their wager".format(player.name))
            player.wager = 0

    
    for player in out:
        players.append(player)
    sleep(2)
    playon()
    continue ################################################################### Next round





