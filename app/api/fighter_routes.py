from flask import Blueprint, jsonify
from flask_login import login_required
from app.models import User, Fighter, Tour_Result
from sqlalchemy import or_, and_

fighter_routes = Blueprint('fighters', __name__)
#url_prefix='/api/fighter'


########### Get Fighters ############
@fighter_routes.route('/<int:weight>')
def get_weight_fighters(weight):
    fighters = Fighter.query.filter(Fighter.weight == weight)
    all_fighters = []
    all_fighters.extend([i.to_dict() for i in fighters])
    return {'All_Fighters': all_fighters}

@fighter_routes.route('/')
def get_all_fighters():
    fighters = Fighter.query.all()
    all_fighters = []
    all_fighters.extend([i.to_dict() for i in fighters])
    return {'All_Fighters': all_fighters}

@fighter_routes.route('/fighter/<int:id>')
def get_one_fighter(id):
    fighter = Fighter.query.get(id)
    tour_fights = Tour_Result.query.filter(or_(fighter.name == Tour_Result.winner,  fighter.name == Tour_Result.loser)).all()
    dict_fights = {}

    for fight in tour_fights:
        good = fight.to_dict()
        dict_fights[fight.id] = good

    fight = fighter.to_dict()
    return {'Fighter': fight,
            'Tour_Fights': dict_fights
            }
