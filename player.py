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

    def calc_strength(self, game_state):

        order_map1 = {
            'A': 1,
            '2': 2,
            '3': 3,
            '4': 4,
            '5': 5,
            '6': 6,
            '7': 7,
            '8': 8,
            '9': 9,
            'T': 10,
            'J': 11,
            'Q': 12,
            'K': 13
        }

        order_map2 = {
            '2': 2,
            '3': 3,
            '4': 4,
            '5': 5,
            '6': 6,
            '7': 7,
            '8': 8,
            '9': 9,
            'T': 10,
            'J': 11,
            'Q': 12,
            'K': 13,
            'A': 14
        }

        hole_cards = game_state["players"][0]["hole_cards"]
        community_cards = game_state["community_cards"]
        colors = dict()
        ranks = dict()
        rank_list = list()
        for card in hole_cards + community_cards:
            if card["rank"] not in ranks.keys():
                ranks[card["rank"]] = 0
            ranks[card["rank"]] += 1
            rank_list.append(card["rank"])

            if card["suit"] not in colors.keys():
                colors[card["suit"]] = 0

            colors[card["suit"]] += 1
        print(colors)
        print(ranks)

        sample = ",".join([str(d) for d in range(1, 15)])
        card_line_1 = [order_map1.get(c) for c in rank_list]
        card_line_1.sort()
        card_line_2 = [order_map2.get(c) for c in rank_list]
        card_line_2.sort()
        card_line_joined = list()
        if len(card_line_1) == 5:
            card_line_joined.append(card_line_1)
            card_line_joined.append(card_line_2)
        if len(card_line_1) == 6:
            for i in range(2):
                card_line_joined.append(card_line_1[i:i + 5])
                card_line_joined.append(card_line_2[i:i + 5])
        if len(card_line_1) == 7:
            for i in range(3):
                card_line_joined.append(card_line_1[i:i + 5])
                card_line_joined.append(card_line_2[i:i + 5])

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
            return 7
        if (three_same == 1) & (two_same == 1):
            return 6
        if max(colors.values()) > 4:
            return 5
        for card_line in card_line_joined:
            s = ",".join([str(c) for c in card_line])
            if s in sample:
                print(s)
                return 4
        if (three_same == 1) & (two_same == 0):
            return 3
        if two_same == 2:
            return 2
        if two_same == 1:
            return 1
        return 0


