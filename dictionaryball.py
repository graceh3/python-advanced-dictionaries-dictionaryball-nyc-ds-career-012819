game_dictionary = {
    'home':{
        'team_name': 'Brooklyn Nets',
         'colors': ['Black', 'White'],
         'players': [{
             'player_name': 'Allen Anderson',
             'number': 0,
             'shoe': 16,
             'points': 22,
             'rebounds': 12,
             'assists': 12,
             'steals': 3,
             'blocks': 1,
             'slam_dunks': 1},
  {'player_name': 'Reggie Evans',
   'number': 30,
   'shoe': 14,
   'points': 12,
   'rebounds': 12,
   'assists': 12,
   'steals': 12,
   'blocks': 12,
   'slam_dunks': 7},
  {'player_name': 'Brook Lopez',
   'number': 11,
   'shoe': 17,
   'points': 17,
   'rebounds': 19,
   'assists': 10,
   'steals': 3,
   'blocks': 1,
   'slam_dunks': 15},
  {'player_name': 'Mason Plumlee',
   'number': 1,
   'shoe': 19,
   'points': 26,
   'rebounds': 12,
   'assists': 6,
   'steals': 3,
   'blocks': 8,
   'slam_dunks': 5},
  {'player_name': 'Jason Terry',
   'number': 31,
   'shoe': 15,
   'points': 19,
   'rebounds': 2,
   'assists': 2,
   'steals': 4,
   'blocks': 11,
   'slam_dunks': 1}]},
'away': {'team_name': 'Charlotte Hornets',
 'colors': ['Turquoise', 'Purple'],
 'players': [{'player_name': 'Jeff Adrien',
   'number': 4,
   'shoe': 18,
   'points': 10,
   'rebounds': 1,
   'assists': 1,
   'steals': 2,
   'blocks': 7,
   'slam_dunks': 2},
  {'player_name': 'Bismak Biyombo',
   'number': 0,
   'shoe': 16,
   'points': 12,
   'rebounds': 4,
   'assists': 7,
   'steals': 7,
   'blocks': 15,
   'slam_dunks': 10},
  {'player_name': 'DeSagna Diop',
   'number': 2,
   'shoe': 14,
   'points': 24,
   'rebounds': 12,
   'assists': 12,
   'steals': 4,
   'blocks': 5,
   'slam_dunks': 5},
  {'player_name': 'Ben Gordon',
   'number': 8,
   'shoe': 15,
   'points': 33,
   'rebounds': 3,
   'assists': 2,
   'steals': 1,
   'blocks': 1,
   'slam_dunks': 0},
  {'player_name': 'Brendan Haywood',
   'number': 33,
   'shoe': 15,
   'points': 6,
   'rebounds': 12,
   'assists': 12,
   'steals': 22,
   'blocks': 5,
   'slam_dunks': 12}]}}

def game_dict():
    return game_dictionary

def num_points_scored(name):
    for team in game_dict():
        for i in range(len(game_dict()[team]['players'])):
            if game_dict()[team]['players'][i]['player_name'] == name:
                return game_dict()[team]['players'][i]['points']
            
def shoe_size(name):
    for team in game_dict():
        for i in range(len(game_dict()[team]['players'])):
            if game_dict()[team]['players'][i]['player_name'] == name:
                return game_dict()[team]['players'][i]['shoe']           

def team_colors(name):
    for team in game_dict():
        if team == name:
            return game_dict()[team]['colors']

def team_names(dictionary):
    teams = []
    for team in dictionary:
        teams.append(dictionary[team]['team_name'])
    return teams

def player_numbers(team_name):
    jersey_nums = []
    for team in game_dict():
        if team_name == game_dict()[team]['team_name']:
            for i in range(len(game_dict()[team]['players'])):
                jersey_nums.append(game_dict()[team]['players'][i]['number'])
    return jersey_nums

def player_stats(players_name):
    for team in game_dict():
        for i in range(len(game_dict()[team]['players'])):
            if game_dict()[team]['players'][i]['player_name'] == players_name:
                return game_dict()[team]['players'][i]

def big_shoe_rebounds():
    temp_shoe = 0
    temp_player = []
    for team in game_dict():
        for player in game_dict()[team]['players']:
            if player['shoe'] > temp_shoe:
                temp_shoe = player['shoe']
                temp_player = []
                temp_player.append((player['player_name'], player['rebounds']))
            elif player['shoe'] == temp_shoe:
                temp_shoe = player['shoe']
                temp_player.append((player['player_name'], player['rebounds']))
            else:
                pass
            
    return temp_player

def good_practices():
    for location, team_stats in game_dict().items():
    # are you ABSOLUTELY SURE what 'location' and 'team_stats' are? use pdb.set_trace() to find out!
    import pdb; pdb.set_trace()
      for stats, data in team_stats.items():
        # are you ABSOLUTELY SURE what 'stats' and 'data' are? use pdb.set_trace() to find out!
        import pdb; pdb.set_trace()
        # what is 'data' at each level of the for loop block? when will we be able to iterate through a list? 
        # When would the following line of code break?
        for item in data:
            print(item)
           
(good_practices())