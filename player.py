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

    def is_green_active(self, game_state):
        for player in game_state['players']:
            if (player['name'] == 'AllIn') and (player['status'] == 'active'):
                return True
        
        return False

    def betRequest(self, game_state):

        ############################# par erosseg teszt #############################################

        rank_d = self.calc_rank_count(game_state["players"][0]["hole_cards"], game_state["community_cards"])
        strength = self.calc_strength(rank_d)

        print("Card strength is {}".format(strength))
        #############################################################################################

        print("GAME DATA", game_state)
    
        if "players" in game_state.keys():
            for player in game_state['players']:
                if "name" in player.keys() and player['name'] == "HalalPoker":
                    if "hole_cards" in player.keys():
                        print("NUMBER OF ACTIVE PLAYERS", self.count_active_players(game_state))
                        print("NUMBER OF OUT PLAYERS", self.count_out_players(game_state))
                        if len(player["hole_cards"]) >=2:
                            if (player["hole_cards"][0]["rank"] == player["hole_cards"][1]["rank"]) and (player["hole_cards"][1]["rank"] in ["7" ,"8", "9", "10", "J", "Q", "K", "A"]):
                                print("We have pair. ALL IN", player["hole_cards"])
                                if self.count_out_players(game_state) >= 2:
                                    return 4000
                                return 500
                            if (player["hole_cards"][0]["rank"] in ["10", "J", "Q", "K", "A"]) and (player["hole_cards"][1]["rank"] in ["10", "J", "Q", "K", "A"]):
                                print("We have high cards. ALL IN", player["hole_cards"])
                                if self.count_out_players(game_state) >= 2:
                                    return 4000
                                return 500
                            if "minimum_raise" in game_state.keys():
                                print("Minimum raise:", game_state["minimum_raise"])
                                raise_limit = 100
                                if self.count_out_players(game_state) >= 2:
                                    if self.is_green_active(game_state):
                                        raise_limit = 1600
                                    raise_limit = 400
                                if game_state["minimum_raise"] < raise_limit:
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



