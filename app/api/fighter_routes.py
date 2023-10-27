from flask import Blueprint, jsonify, request, jsonify
from flask_login import login_required
from app.forms import SearchForm, DraftForm
from app.models import User, db,Fighter, Tour_Result, Medal, Team, Season_Result
from sqlalchemy import or_, and_

fighter_routes = Blueprint('fighters', __name__)
#url_prefix='/api/fighter'


########### Get Fighters ############
@fighter_routes.route('/search', methods=['GET', 'POST'])
def search():

    form = SearchForm()

    if form.validate_on_submit:
        results = form.data['search']
        results = results.lower()
        all_fighters = Fighter.query.all()
        fighters = []
        for fighter in all_fighters:
            if results in fighter.name.lower():

                fighters.append({
                    'id': fighter.id,
                    'name': fighter.name,
                    'nickname': fighter.nickname,
                    'prof_img': fighter.prof_img,
                    'body_img': fighter.body_img,
                    'medal': fighter.medal,
                    'weight': fighter.weight,
                    'wins': fighter.wins,
                    'losses': fighter.losses,
                    'all_win': fighter.all_win,
                    'all_loss': fighter.all_loss,
                    'points': fighter.points,
                    'team_name': fighter.team_name
                })
        return {'All_Fighters': fighters}
    return 'BAD REQ'

################## get all fighter from a weight class #############################
@fighter_routes.route('/<int:weight>')
def get_weight_fighters(weight):
    fighters = Fighter.query.filter(Fighter.weight == weight).order_by(Fighter.name)
    all_fighters = []
    all_fighters.extend([i.to_dict() for i in fighters])
    return {'All_Fighters': all_fighters}

############################# remove a fighter from a team ##########################
@fighter_routes.route('/cut/<int:id>')
def cut_fighter(id):
    """Remove A fighter from a team"""
    fighter = Fighter.query.get(id)
    fighter.team_name = 'Free Agent'
    db.session.commit()
    return {'Fighter': 'cut'}


############################ get all fighters ####################
@fighter_routes.route('/')
def get_all_fighters():
    fighters = Fighter.query.order_by(Fighter.name).all()
    all_fighters = []
    all_fighters.extend([i.to_dict() for i in fighters])
    return {'All_Fighters': all_fighters}

############################### draft a player ######################
@fighter_routes.route('/draft', methods=['POST'])
def draft_fighter():
    data = request.get_json()  # Parse JSON data from the request body
    team_name = data['team']
    weight_class = data['weightClass']
    fighter_id = data['fighterId']
    team = Team.query.filter(Team.name == team_name)
    fighter = Fighter.query.get(fighter_id)

    active_fighter = Fighter.query.filter(and_(Fighter.team_name == team_name, Fighter.weight == weight_class)).first()
    if active_fighter:
        return jsonify({'error': 'There is an active Fighter at this weight'}), 400  # Return an error response with status code 400
    else:
        fighter.weight = weight_class
        fighter.team_name = team_name
        db.session.commit()

    fighter = fighter.to_dict()
    return {'fighter': fighter}


########################## get a single fighter ######################
@fighter_routes.route('/fighter/<int:id>')
def get_one_fighter(id):
    fighter = Fighter.query.get(id)
    tour_fights = Tour_Result.query.filter(or_(fighter.name == Tour_Result.winner,  fighter.name == Tour_Result.loser)).all()
    season_fights = Season_Result.query.filter(or_(fighter.name == Season_Result.winner, fighter.name == Season_Result.loser)).all()
    all_medals = Medal.query.filter(Medal.fighter == fighter.name).all()
    team = Team.query.filter(Team.name == fighter.team_name).first()
    team = team.to_dict()

    last_opp = {'winner': None, 'loser':None}
    last_match = None
    if len(tour_fights) > 0:
        last_match = tour_fights[len(tour_fights) - 1]
        if last_match.winner == fighter.name:
            last_opp = Fighter.query.filter(Fighter.name == last_match.loser).first()
            last_opp = last_opp.to_dict()
        else:
            last_opp = Fighter.query.filter(Fighter.name == last_match.winner).first()
            last_opp = last_opp.to_dict()

    last_season = {'winner': None, 'loser': None}
    last_smatch = None
    if len(season_fights) > 0:
        last_smatch = season_fights[len(season_fights) -1]
        if last_smatch.winner == fighter.name:
            last_season = Fighter.query.filter(Fighter.name == last_smatch.loser).first()
            last_season = last_season.to_dict()
        else:
            last_season = Fighter.query.filter(Fighter.name == last_smatch.winner).first()
            last_season = last_season.to_dict()



    dict_fights = {}
    dict_medals = {}
    dict_season_fights = {}

    for fight in season_fights:
        good = fight.to_dict()
        dict_season_fights[fight.id] = good

    for fight in tour_fights:
        good = fight.to_dict()
        dict_fights[fight.id] = good

    for medal in all_medals:
        good = medal.to_dict()
        dict_medals[medal.id] = good

    fight = fighter.to_dict()
    return {'Fighter': fight,
            'Tour_Fights': dict_fights,
            'Season_Fights': dict_season_fights,
            'Medals': dict_medals,
            'Team': team,
            'last_opp': last_opp,
            'last_season': last_season
            }
