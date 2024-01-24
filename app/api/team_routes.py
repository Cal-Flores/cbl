from flask import Blueprint, jsonify
from flask_login import login_required
from app.models import User, Fighter, Team, Medal, Team_Result, Schedule, Season_Result, db, Draft_Order
from sqlalchemy import and_, or_
from flask import request

team_routes = Blueprint('teams', __name__)
#url_prefix='/api/team'


##### Get Teams #########
@team_routes.route('/')
def get_all_teams():
    all_teams = Team.query.all()
    teams = []
    teams.extend([i.to_dict() for i in all_teams])
    #### EMEGENCY ADDITIONS EDIT
    # match_10 = Season_Result(id=88,winner='Kai Kara-France',loser='Azat Maksum',method='DEC',round=3,dual_id=42)
    # match_11 = Season_Result(id=88,winner='Said Nurmagomedov',loser='Farid Basharat',method='SUB',round=3,dual_id=42)
    # match_12 = Season_Result(id=88,winner='Mark Ironside',loser='Junichiro Hoi',method='SUB',round=3,dual_id=42)
    # match_13 = Season_Result(id=88,winner='Max Askren',loser='Bryce Mitchell',method='DEC',round=3,dual_id=42)
    # match_14 = Season_Result(id=88,winner='Jordan Burroughs',loser='Dustin Poirier',method='DEC',round=3,dual_id=42)
    # match_15 = Season_Result(id=88,winner='Mark Perry',loser='Ismael Bonfim',method='SUB',round=2,dual_id=42)
    # match_16 = Season_Result(id=88,winner='Geoff Neal',loser='Logan Storley',method='DEC',round=3,dual_id=42)
    # match_17 = Season_Result(id=88,winner='Paul Craig',loser='Jake Paul',method='DEC',round=3,dual_id=42)
    # match_18 = Season_Result(id=88,winner='Ibragim Chuzhigaev',loser='Kollin Moore',method='TKO',round=1,dual_id=42)
    # match_19 = Season_Result(id=88,winner='Greg Kerkvliet',loser='Ciryl Gane',method='TKO',round=1,dual_id=42)

    # player_rn = Fighter.query.filter(Fighter.name == 'Ciryl Gane').first()
    # player_rn.losses += 1


    # db.session.add(match_10)
    # db.session.add(match_11)
    # db.session.add(match_12)
    # db.session.add(match_13)
    # db.session.add(match_14)
    # db.session.add(match_15)
    # db.session.add(match_16)
    # db.session.add(match_17)
    # db.session.add(match_18)
    # db.session.add(match_19)


    # teamonee = Team.query.filter(Team.name == 'Colony Buccaneers').first()
    # teamonee.points += 29
    # teamonee.offense += 9
    # teamonee.defense += 20
    # teamonee.curr_wins += 1


    #match_6 = Team_Result(id=97,winner='Colony Buccaneers',loser='Creekview Cowboys',winner_score=29,loser_score=21,week=6)
    # dual_6 = Schedule(id=246, week=6,team_1='Prosper Eagles',team_2='Grapevine Falcons', completed=False)
    # db.session.add(dual_6)


    # hooker = Fighter.query.filter(Fighter.name == 'Dan Hooker').first()
    # hooker.points = 6
    # db.session.commit()


    return {'All_Teams': teams}



##### get one team ########
@team_routes.route('/<int:id>')
def get_one_team(id):
    curr_team = Team.query.get(id)
    fly = Fighter.query.filter(and_(Fighter.team_name == curr_team.name, Fighter.weight == '125')).first()
    if fly != None:
        fly = fly.to_dict()
    bantam = Fighter.query.filter(and_(Fighter.team_name == curr_team.name, Fighter.weight == '133')).first()
    if bantam != None:
        bantam = bantam.to_dict()
    phantam = Fighter.query.filter(and_(Fighter.team_name == curr_team.name, Fighter.weight == '141')).first()
    if phantam != None:
        phantam = phantam.to_dict()
    feather = Fighter.query.filter(and_(Fighter.team_name == curr_team.name, Fighter.weight == '149')).first()
    if feather != None:
        feather = feather.to_dict()
    light = Fighter.query.filter(and_(Fighter.team_name == curr_team.name, Fighter.weight == '157')).first()
    if light != None:
        light = light.to_dict()
    cruiser = Fighter.query.filter(and_(Fighter.team_name == curr_team.name, Fighter.weight == '165')).first()
    if cruiser != None:
        cruiser = cruiser.to_dict()
    welter = Fighter.query.filter(and_(Fighter.team_name == curr_team.name, Fighter.weight == '174')).first()
    if welter != None:
        welter = welter.to_dict()
    middle = Fighter.query.filter(and_(Fighter.team_name == curr_team.name, Fighter.weight == '185')).first()
    if middle != None:
        middle = middle.to_dict()
    light_heavy = Fighter.query.filter(and_(Fighter.team_name == curr_team.name, Fighter.weight == '205')).first()
    if light_heavy != None:
        light_heavy = light_heavy.to_dict()
    heavy = Fighter.query.filter(and_(Fighter.team_name == curr_team.name, Fighter.weight == '285')).first()
    if heavy != None:
        heavy = heavy.to_dict()
    duals = Team_Result.query.filter(or_(curr_team.name == Team_Result.winner, curr_team.name == Team_Result.loser)).all()

    dict_duals = {}

    for dual in duals:
        good = dual.to_dict()
        dict_duals[dual.id] = good

    # return {'Duals': dict_duals}



    return {'Team': {
        'id': curr_team.id,
        'name': curr_team.name,
        'win': curr_team.win,
        'loss': curr_team.loss,
        'curr_wins': curr_team.curr_wins,
        'curr_loss': curr_team.curr_loss,
        'div_win': curr_team.div_win,
        'div_loss': curr_team.div_loss,
        'last_place': curr_team.last_place,
        'post_season': curr_team.post_season,
        'offense': curr_team.offense,
        'defense': curr_team.defense,
        'points': curr_team.points,
        'bg': curr_team.background_img,
        'detail_bg': curr_team.detail_bg,
        'conf': curr_team.conf,
        'divison': curr_team.divison,
        'fly': fly,
        'bantam': bantam,
        'phantam': phantam,
        'feather': feather,
        'light': light,
        'cruiser': cruiser,
        'welter': welter,
        'middle': middle,
        'light_heavy': light_heavy,
        'heavy': heavy,
        'text': curr_team.heavy,
        'border': curr_team.fly,
        'Duals': dict_duals
    }}


#################### get all duals for 1 team ####################
@team_routes.route('/duals/<int:id>')
def team_duals(id):
    team = Team.query.get(id)
    duals = Team_Result.query.filter(or_(team.name == Team_Result.winner, team.name == Team_Result.loser)).all()

    dict_duals = {}

    for dual in duals:
        good = dual.to_dict()
        dict_duals[dual.id] = good

    return {'Duals': dict_duals}

######################### get the schedule for one team ######################
@team_routes.route('/schedule/:teamId')
def team_schedule(teamId):
    team = Team.query.get(teamId)
    duals = Schedule.query.filter(_or(Schedule.team_1 == team.name, Schedule.team_2 == team.name)).all()

    dict_duals = {}

    for dual in duals:
        good = dual.to_dict()
        dict_duals[dual.id] = good

    return {'Duals': dict_duals}


####################### get all matches based on week #####################
@team_routes.route('/schedule/<int:week>')
def week_schedule(week):
    duals = Schedule.query.filter(Schedule.week == week).all()
    dict_duals = {}
    for dual in duals:
        team_1 = Team.query.filter(Team.name == dual.team_1).first().to_dict()  # Fetch team_1 details
        team_2 = Team.query.filter(Team.name == dual.team_2).first().to_dict()  # Fetch team_2 details
        good = dual.to_dict()

        good['team_1'] = team_1
        good['team_2'] = team_2

        dict_duals[dual.id] = good
    return {'Schedule': dict_duals}

@team_routes.route('/schedule')
def schedule():
    duals = Schedule.query.all()
    dict_duals = {}
    for dual in duals:
        team_1 = Team.query.filter(Team.name == dual.team_1).first().to_dict()  # Fetch team_1 details
        team_2 = Team.query.filter(Team.name == dual.team_2).first().to_dict()  # Fetch team_2 details
        good = dual.to_dict()

        # Assign team details to team_1 and team_2 keys
        good['team_1'] = team_1
        good['team_2'] = team_2

        dict_duals[dual.id] = good

    return {'Schedule': dict_duals}

@team_routes.route('/scores')
def scores():
    scores = Team_Result.query.all()
    print('###########################################', scores)
    dict_scores = {}  # Corrected variable name
    for score in scores:
        good = score.to_dict()
        dict_scores[score.id] = good  # Using dict_scores instead of dict_duals
    return {'Scores': dict_scores}
############################ get info about 1 dual FORM ##########################
@team_routes.route('/game/<int:id>')
def gameTime(id):
    dual = Schedule.query.get(id)
    dual_dict = dual.to_dict()
    dict_fighters_one = {}
    dict_fighters_two = {}

    fighters_one = Fighter.query.filter(Fighter.team_name == dual.team_1).all()
    fighters_two = Fighter.query.filter(Fighter.team_name == dual.team_2).all()

    for fighter in fighters_one:
        good = fighter.to_dict()
        dict_fighters_one[fighter.id] = good

    for fighter in fighters_two:
        good = fighter.to_dict()
        dict_fighters_two[fighter.id] = good


    # print('AMYYYYYYYYUYYYY#######################', dict_fighters_one)
    # print('AMYYYYYYYYUYYYY#######################', dict_fighters_two)
    print({'Dual_Stats': {'dual': dual_dict, 'team_1': dict_fighters_one, 'team_2': dict_fighters_two}})
    return {'Dual_Stats': {
        'dual': dual_dict,
        'team_1': dict_fighters_one,
        'team_2': dict_fighters_two
    }}



############### MEGA FORM ##############
@team_routes.route('/gameFinish/<int:id>', methods=['POST'])
def game_results(id):
    data = request.get_json()


    score_one = data.get('scoreOne')
    score_two = data.get('scoreTwo')

    schedule = Schedule.query.get(id)
    schedule.completed = True
    db.session.commit()
    team_1 = schedule.team_1
    team_2 = schedule.team_2

    actual_team_one = Team.query.filter(Team.name == team_1).first()
    actual_team_two = Team.query.filter(Team.name == team_2).first()

    actual_team_one.points += int(score_one)
    actual_team_two.points += int(score_two)
    db.session.commit()


    if score_one > score_two:
        new_res = Team_Result(id=id, week=schedule.week, winner=team_1, loser=team_2, winner_score=score_one, loser_score=score_two)
        actual_team_one.curr_wins += 1
        actual_team_two.curr_loss += 1
        db.session.add(new_res)
        db.session.commit()
        if schedule.week == '3' or schedule.week == '5' or schedule.week == '8' or schedule.week == '11' or schedule.week == '14' or schedule.week == '16':
             actual_team_one.div_win += 1
             actual_team_two.div_loss += 1
             db.session.commit()
    else:
        new_res = Team_Result(id=id, week=schedule.week, winner=team_2, loser=team_1, winner_score=score_two, loser_score=score_one)
        actual_team_two.curr_wins += 1
        actual_team_one.curr_loss += 1
        db.session.add(new_res)
        db.session.commit()
        if schedule.week == '3' or schedule.week == '5' or schedule.week == '8' or schedule.week == '11' or schedule.week == '14' or schedule.week == '16':
             actual_team_two.div_win += 1
             actual_team_one.div_loss += 1
             db.session.commit()


    # Process each fight in the 'fights' list
    for fight in data.get('fights', []):
        winner = fight.get('winner')
        loser = fight.get('loser')
        method = fight.get('method')
        round = fight.get('round')


        fight_winner = Fighter.query.filter(Fighter.name == winner).first()
        fight_winner.wins = fight_winner.wins + 1
        # fight_winner.all_win = fight_winner.all_win + 1
        if method == 'KO' or method == 'TKO' or method == 'SUB':
            fight_winner.points += 7
        elif method == 'M.DEC':
            fight_winner.points += 5
        else:
            fight_winner.points += 3

        fight_loser = Fighter.query.filter(Fighter.name == loser).first()
        fight_loser.losses = fight_loser.losses + 1
        # fight_loser.all_loss = fight_loser.all_loss + 1


        weight_classes = ['125', '133', '141', '149', '157']

        # Check if the fight winner's weight is in the specified weight classes
        if fight_winner.weight in weight_classes:
            # If the winner's team has the same name as the actual_team_one
            if fight_winner.team_name == actual_team_one.name:
                if method in ['KO', 'TKO', 'SUB']:
                    actual_team_one.offense += 7
                elif method == 'M.DEC':
                    actual_team_one.offense += 5
                else:
                    actual_team_one.offense += 3
            else:
                # Increment the opponent's defense points
                if method in ['KO', 'TKO', 'SUB']:
                    actual_team_two.offense += 7
                elif method == 'M.DEC':
                    actual_team_two.offense += 5
                else:
                    actual_team_two.offense += 3
        else:
            # Perform opposite logic for different weight classes
            if fight_winner.team_name == actual_team_one.name:
                # Increment opponent's defense points
                if method in ['KO', 'TKO', 'SUB']:
                    actual_team_one.defense += 7
                elif method == 'M.DEC':
                    actual_team_one.defense += 5
                else:
                    actual_team_one.defense += 3
            else:
                # Increment own team's offense points
                if method in ['KO', 'TKO', 'SUB']:
                    actual_team_two.defense += 7
                elif method == 'M.DEC':
                    actual_team_two.defense += 5
                else:
                    actual_team_two.defense += 3

        new_res = Season_Result(id=id,winner=winner, loser=loser,method=method,round=round,dual_id=id)
        db.session.add(new_res)
        db.session.commit()


    return {'team': 'team'}


def sorter(conf, div, name):
    teams = []

    team_objects = Team.query.filter(and_(Team.conf == conf, Team.divison == div)) \
        .order_by(
            Team.curr_wins.desc(),
            Team.div_win.desc(),
            Team.points.desc()
        ) \
        .all()

    for team in team_objects:
        teams.append(team.to_dict())

    return {name: teams}


######################## Standings Page ##########################
@team_routes.route('/standings')
def standings():
    afc_north = sorter('AFC', 'North', 'aNorth')
    afc_south = sorter('AFC', 'South', 'aSouth')
    afc_east = sorter('AFC', 'East', 'aEast')
    afc_west = sorter('AFC', 'West', 'aWest')

    nfc_north = sorter('NFC', 'North', 'nNorth')
    nfc_east = sorter('NFC', 'East', 'nEast')
    nfc_south = sorter('NFC', 'South', 'nSouth')
    nfc_west = sorter('NFC', 'West', 'nWest')



    return {
        "standings": {
            "aNorth": afc_north,
            "aSouth": afc_south,
            "aEast": afc_east,
            "aWest": afc_west,
            'nNorth': nfc_north,
            'nSouth': nfc_south,
            'nEast': nfc_east,
            'nWest': nfc_west
        }
    }

################## Playoff picture ##########################
@team_routes.route('/playoffs')
def playoffs():
    # Fetch standings as before
    afc_north = sorter('AFC', 'North', 'aNorth')
    afc_south = sorter('AFC', 'South', 'aSouth')
    afc_east = sorter('AFC', 'East', 'aEast')
    afc_west = sorter('AFC', 'West', 'aWest')

    nfc_north = sorter('NFC', 'North', 'nNorth')
    nfc_east = sorter('NFC', 'East', 'nEast')
    nfc_south = sorter('NFC', 'South', 'nSouth')
    nfc_west = sorter('NFC', 'West', 'nWest')

    # Get the first-place teams from each division in the AFC and NFC
    afc_leaders = afc_north['aNorth'][:1] + afc_south['aSouth'][:1] + afc_east['aEast'][:1] + afc_west['aWest'][:1]
    nfc_leaders = nfc_north['nNorth'][:1] + nfc_east['nEast'][:1] + nfc_south['nSouth'][:1] + nfc_west['nWest'][:1]

    # Sort the AFC and NFC leader lists based on the given criteria
    afc_sorted_leaders = sorted(afc_leaders, key=lambda team: (team['curr_wins'], team['div_win'], team['points']), reverse=True)
    nfc_sorted_leaders = sorted(nfc_leaders, key=lambda team: (team['curr_wins'], team['div_win'], team['points']), reverse=True)

    # Remove first-place teams from each division in the AFC
    afc_teams = afc_north['aNorth'][1:] + afc_south['aSouth'][1:] + afc_east['aEast'][1:] + afc_west['aWest'][1:]
    nfc_teams = nfc_north['nNorth'][1:] + nfc_east['nEast'][1:] + nfc_south['nSouth'][1:] + nfc_west['nWest'][1:]

    # Sort the remaining 12 teams based on the same criteria as before
    afc_playoff_teams = sorted(afc_teams, key=lambda team: (team['curr_wins'], team['div_win'], team['points']), reverse=True)
    nfc_playoff_teams = sorted(nfc_teams, key=lambda team: (team['curr_wins'], team['div_win'], team['points']), reverse=True)

    return {
        "afc_leaders": afc_sorted_leaders,
        "nfc_leaders": nfc_sorted_leaders,
        "afc_playoff_teams": afc_playoff_teams,
        "nfc_playoff_teams": nfc_playoff_teams
    }

@team_routes.route('/order')
def order():
    all_picks = Draft_Order.query.all()
    picks = []

    for pick in all_picks:
        # Assuming to_dict() returns serializable data for Draft_Order
        pick_data = pick.to_dict()

        # Fetch the associated Team information
        team = Team.query.filter_by(name=pick.team).first()
        if team:
            # Add the serialized Team data to the pick's information
            pick_data['team_info'] = team.to_dict()  # Assuming to_dict() exists for Team

        picks.append(pick_data)

    return jsonify({'Picks': picks})


def calculate_elo_rating(winner_rating, loser_rating, k=32):
    """
    Calculate new Elo ratings after a game.

    Args:
    - winner_rating: Elo rating of the winner
    - loser_rating: Elo rating of the loser
    - k: Weight constant (default is 32)

    Returns:
    - Tuple of updated Elo ratings for the winner and loser
    """
    winner_expected = 1 / (1 + 10 ** ((loser_rating - winner_rating) / 400))
    loser_expected = 1 / (1 + 10 ** ((winner_rating - loser_rating) / 400))

    winner_new_rating = winner_rating + k * (1 - winner_expected)
    loser_new_rating = loser_rating + k * (0 - loser_expected)

    return winner_new_rating, loser_new_rating

# Example usage:
winner_rating = 1600
loser_rating = 1400

new_winner_rating, new_loser_rating = calculate_elo_rating(winner_rating, loser_rating)

print(f"New winner rating: {new_winner_rating}")
print(f"New loser rating: {new_loser_rating}")


def calculate_elo_rating(winner_rating, loser_rating, k=32):
    """
    Calculate new Elo ratings after a game.

    Args:
    - winner_rating: Elo rating of the winner
    - loser_rating: Elo rating of the loser
    - k: Weight constant (default is 32)

    Returns:
    - Tuple of updated Elo ratings for the winner and loser
    """
    winner_expected = 1 / (1 + 10 ** ((loser_rating - winner_rating) / 400))
    loser_expected = 1 / (1 + 10 ** ((winner_rating - loser_rating) / 400))

    winner_new_rating = winner_rating + k * (1 - winner_expected)
    loser_new_rating = loser_rating + k * (0 - loser_expected)

    # Alternatively, you can use the following lines to round the ratings to integers
    # winner_new_rating = round(winner_rating + k * (1 - winner_expected))
    # loser_new_rating = round(loser_rating + k * (0 - loser_expected))

    return winner_new_rating, loser_new_rating

# Example usage:
winner_rating = 1600
loser_rating = 1400

new_winner_rating, new_loser_rating = calculate_elo_rating(winner_rating, loser_rating)

print(f"New winner rating: {new_winner_rating}")
print(f"New loser rating: {new_loser_rating}")
