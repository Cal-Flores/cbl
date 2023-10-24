from flask import Blueprint, jsonify
from flask_login import login_required
from app.models import User, Fighter, Tour_Result, Medal, Team, Season_Result
from sqlalchemy import or_, and_

fighter_routes = Blueprint('fighters', __name__)
#url_prefix='/api/fighter'


########### Get Fighters ############
@fighter_routes.route('/<int:weight>')
def get_weight_fighters(weight):
    fighters = Fighter.query.filter(Fighter.weight == weight).order_by(Fighter.name)
    all_fighters = []
    all_fighters.extend([i.to_dict() for i in fighters])
    return {'All_Fighters': all_fighters}

@fighter_routes.route('/')
def get_all_fighters():
    fighters = Fighter.query.order_by(Fighter.name).all()
    all_fighters = []
    all_fighters.extend([i.to_dict() for i in fighters])
    return {'All_Fighters': all_fighters}

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
            'last_opp': last_opp
            }
