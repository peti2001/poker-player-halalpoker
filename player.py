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

        hand_strength = self.calc_strength(game_state)

        print("Card strength is {}".format(hand_strength))
        #############################################################################################

        print("GAME DATA", game_state)
    
        if "players" in game_state.keys():
            for player in game_state['players']:
                if "name" in player.keys() and player['name'] == "HalalPoker":
                    if "hole_cards" in player.keys():
                        print("NUMBER OF ACTIVE PLAYERS", self.count_active_players(game_state))
                        print("NUMBER OF OUT PLAYERS", self.count_out_players(game_state))
                        print("HANDS STRENGHT", hand_strength)
                        if len(player["hole_cards"]) >=2:
                            # if hand_strength >= 2:
                            #     print("We have something good: ", hand_strength)
                            #     return 4000
                            if (player["hole_cards"][0]["rank"] == player["hole_cards"][1]["rank"]) and (player["hole_cards"][1]["rank"] in ["7" ,"8", "9", "10", "J", "Q", "K", "A"]):
                                print("We have pair. ALL IN", player["hole_cards"])
                                if self.count_out_players(game_state) >= 2:
                                    print("Raise 4000, two players")
                                    return 4000
                                print("Raise 500, 4 or 3 players")
                                return 500
                            if (player["hole_cards"][0]["rank"] in ["10", "J", "Q", "K", "A"]) and (player["hole_cards"][1]["rank"] in ["10", "J", "Q", "K", "A"]):
                                print("We have high cards. ALL IN", player["hole_cards"])
                                if self.count_out_players(game_state) >= 2:
                                    print("Raise 4000, two players")
                                    return 4000
                                print("Raise 4000, 3,4 players")
                                return 500
                            if "minimum_raise" in game_state.keys():
                                print("Minimum raise:", game_state["minimum_raise"])
                                raise_limit = 100
                                if self.count_out_players(game_state) >= 2:
                                    raise_limit = 200
                                    if self.is_green_active(game_state):
                                        raise_limit = 800
                                    print("RAise limit:", raise_limit)
                                if game_state["minimum_raise"] < raise_limit:
                                    print("Kicsi emeles. Minimum raise:", game_state["minimum_raise"], " Big Blind", game_state["big_blind"])
                                    return game_state["minimum_raise"] + 2 * game_state["big_blind"]
        
        return 0

    def showdown(self, game_state):
        pass

    def calc_strength(self, game_state):

        hole_cards = game_state["players"][0]["hole_cards"]
        community_cards = game_state["community_cards"]
        colors = dict()
        ranks = dict()
        for card in hole_cards + community_cards:
            if card["rank"] not in ranks.keys():
                ranks[card["rank"]] = 0
            ranks[card["rank"]] += 1

            if card["suit"] not in colors.keys():
                colors[card["suit"]] = 0

            colors[card["suit"]] += 1
        print(colors)
        print(ranks)
        if max(colors.values()) > 4:
            return 4

        two_same = 0
        three_same = 0
        four_same = 0
        for rank, val in ranks.items():
            if val == 2:
                two_same += 1
            if val == 3:
                three_same += 1
            if val == 4:
                four_same += 1
        if four_same == 1:
            return 6
        if (three_same == 1) & (two_same == 1):
            return 5
        if (three_same == 1) & (two_same == 0):
            return 3
        if two_same == 2:
            return 2
        if two_same == 1:
            return 1
        return 0


