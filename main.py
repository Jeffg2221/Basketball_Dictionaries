from Player import Player, jason, kevin, kyrie, players

# Create your Player instances here!
player_jason = Player(jason)
player_kevin = Player(kevin)
player_kyrie = Player(kyrie)
print(player_jason)
print(player_kevin)
print(player_kyrie)

new_team = Player.get_team(players)
print(new_team)