from pypokerengine.utils.card_utils import gen_cards, estimate_hole_card_win_rate


class Player:
    VERSION = "Default Python folding player"

    def count_active_players(self, game_state):
        c = 0
        for player in game_state['players']:
            if player['status'] == 'active':
                c = c + 1
        
        return c

    def count_out_players(self, game_state):
        c = 0
        for player in game_state['players']:
            if player['status'] == 'out':
                c = c + 1
        
        return c

    def betRequest(self, game_state):

        ############################# Valoszinuseg Tesztelo kod #####################################

        # my_card_list = self.transform_cards(game_state["players"][0]["hole_cards"])
        # community_cards = self.transform_cards(game_state["community_cards"])

        # hole_cards = gen_cards(my_card_list)
        # community_card = gen_cards(community_cards)
        # nb_players = len(game_state["players"])
        # p = estimate_hole_card_win_rate(nb_simulation=1000, nb_player=nb_players, hole_card=hole_cards,
        #                                 community_card=community_card)
        # print("Porbability of winning with current hand: {}".format(p))


        #############################################################################################

        print("GAME DATA", game_state)
    
        if "players" in game_state.keys():
            for player in game_state['players']:
                if "name" in player.keys() and player['name'] == "HalalPoker":
                    if "hole_cards" in player.keys():
                        print("NUMBER OF ACTIVE PLAYERS", self.count_active_players(game_state))
                        print("NUMBER OF OUT PLAYERS", self.count_out_players(game_state))
                        if len(player["hole_cards"]) >=2:
                            if player["hole_cards"][0]["rank"] == player["hole_cards"][1]["rank"]:
                                print("We have pair. ALL IN", player["hole_cards"])
                                self.count_out_players(game_state) >= 2:
                                    return 4000
                                return 500
                            if (player["hole_cards"][0]["rank"] in ["10", "J", "Q", "K", "A"]) and (player["hole_cards"][1]["rank"] in ["10", "J", "Q", "K", "A"]):
                                print("We have high cards. ALL IN", player["hole_cards"])
                                self.count_out_players(game_state) >= 2:
                                    return 4000
                                return 500
                            if "minimum_raise" in game_state.keys():
                                print("Minimum raise:", game_state["minimum_raise"])
                                raise_limit = 100
                                if self.count_out_players(game_state) >= 2:
                                    raise_limit = 400
                                if game_state["minimum_raise"] < raise_limit:
                                    print("Kicsi emeles", player["hole_cards"])
                                    return game_state["minimum_raise"] + 2 * game_state["big_blind"]
        
        return 0

    def showdown(self, game_state):
        pass

    def transform_cards(self, card_list):
        card_map_1 = {"clubs": "C", "diamonds": "D", "hearts": "H", "spades": "S"}
        card_map_2 = dict()
        for i in range(1, 10):
            card_map_2["{}".format(i)] = "{}".format(i)
        card_map_2["10"] = "T"
        card_map_2["A"] = "A"
        card_map_2["J"] = "J"
        card_map_2["Q"] = "Q"
        card_map_2["K"] = "K"

        output = list()
        for card in card_list:
            output.append(card_map_1.get(card["suit"]) + card_map_2.get(card["rank"]))
        return output



