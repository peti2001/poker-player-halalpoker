from pypokerengine.utils.card_utils import gen_cards, estimate_hole_card_win_rate


class Player:
    VERSION = "Default Python folding player"

    def betRequest(self, game_state):

        ############################# par erosseg teszt #############################################

        rank_d = self.calc_rank_count(game_state["players"][0]["hole_cards"], game_state["community_cards"])
        strength = self.calc_strength(rank_d)

        print("Card strength is {}".format(strength))
        #############################################################################################

        ############################# Valoszinuseg Tesztelo kod #####################################

#        #my_card_list = self.transform_cards(game_state["players"][0]["hole_cards"])
        #community_cards = self.transform_cards(game_state["community_cards"])

        #hole_cards = gen_cards(my_card_list)
        #community_card = gen_cards(community_cards)
        #nb_players = len(game_state["players"])
        #p = estimate_hole_card_win_rate(nb_simulation=1000, nb_player=nb_players, hole_card=hole_cards,
#                                        community_card=community_card)
        #print("Porbability of winning with current hand: {}".format(p))


        #############################################################################################

        print("GAME DATA", game_state)
        print("Minimum raise:", game_state["minimum_raise"])
        if "players" in game_state.keys():
            for player in game_state['players']:
                if "name" in player.keys() and player['name'] == "HalalPoker":
                    if "hole_cards" in player.keys():
                        if len(player["hole_cards"]) >=2:
                            if player["hole_cards"][0]["rank"] == player["hole_cards"][1]["rank"]:
                                print("We have pair. ALL IN", player["hole_cards"])
                                return 1000
                            if (player["hole_cards"][0]["rank"] in ["10", "J", "Q", "K", "A"]) and (player["hole_cards"][1]["rank"] in ["10", "J", "Q", "K", "A"]):
                                print("We have high cards. ALL IN", player["hole_cards"])
                                
                                return 1000
        if int(game_state["minimum_raise"]) < 100:
            print("Kicsi emeles", player["hole_cards"])
            return game_state["minimum_raise"] + 2 * game_state["big_blind"]
        return 0

    def showdown(self, game_state):
        pass

    def calc_rank_count(self, hole_cards, community_cards):
        ranks = dict()
        for card in hole_cards + community_cards:
            if card["rank"] not in ranks.keys():
                ranks[card["rank"]] = 0
            ranks[card["rank"]] += 1
        return ranks

    def calc_strength(self, rank_dict):
        two_same = 0
        three_same = 0
        four_same = 0
        for rank, val in rank_dict.items():
            if val == 2:
                two_same += 1
            if val == 3:
                three_same += 1
            if val == 4:
                four_same += 1
        if four_same == 1:
            return 5
        if (three_same == 1) & (two_same == 1):
            return 4
        if (three_same == 1) & (two_same == 0):
            return 3
        if two_same == 2:
            return 2
        if two_same == 1:
            return 1
        return 0



