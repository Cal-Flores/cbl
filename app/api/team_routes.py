from flask import Blueprint, jsonify
from flask_login import login_required
from app.models import User, Fighter, Team, Medal, Team_Result, Schedule, Season_Result, db
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

    # Print the received data
    print('Received Data:', data)
    print('Received ID:', id)

    for fight in data:
        winner = fight.get('winner')
        loser = fight.get('loser')
        method = fight.get('method')
        round = fight.get('round')

        fight_winner = Fighter.query.filter(Fighter.name == winner).first()
        fight_winner.wins = fight_winner.wins + 1
        fight_winner.all_win = fight_winner.all_win + 1
        if method == 'KO' or method == 'TKO' or method == 'SUB':
            fight_winner.points += 6
        elif method == 'M.DEC':
            fight_winner.points += 4
        else:
            fight_winner.points += 3

        fight_loser = Fighter.query.filter(Fighter.name == loser).first()
        fight_loser.wins = fight_loser.losses + 1
        fight_loser.all_win = fight_loser.all_loss + 1

        new_res = Season_Result(id=id,winner=winner, loser=loser,method=method,round=round,dual_id=100)
        db.session.add(new_res)
        db.session.commit()

    return {'team': 'team'}
