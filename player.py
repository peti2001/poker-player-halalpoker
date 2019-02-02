
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
                                return 250
                            if (player["hole_cards"][0]["rank"] in ["10", "J", "Q", "K", "A"]) and (player["hole_cards"][1]["rank"] in ["10", "J", "Q", "K", "A"]):
                                print("We have high cards. ALL IN", player["hole_cards"])
                                return 250
                            if "minimum_raise" in game_state.keys():
                                print("Minimum raise:", game_state["minimum_raise"])
                                raise_limit = 100
                                if self.count_out_players(game_state) >= 2:
                                    raise_limit = 200
                                if game_state["minimum_raise"] < raise_limit:
                                    print("Kicsi emeles", player["hole_cards"])
                                    return game_state["minimum_raise"] + 2 * game_state["big_blind"]
        
        return 0

    def showdown(self, game_state):
        pass

