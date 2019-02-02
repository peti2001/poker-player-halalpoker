
class Player:
    VERSION = "Default Python folding player"

    def betRequest(self, game_state):
        print("GAME DATA", game_state)
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
        if game_state["minimum_raise"] < 50:
            print("Kicsi emeles", player["hole_cards"])
            return game_state["minimum_raise"] + game_state["big_blind"]
        return 0

    def showdown(self, game_state):
        pass

