from flask import Blueprint, jsonify
from flask_login import login_required
from app.models import User, Fighter

fighter_routes = Blueprint('fighters', __name__)
#url_prefix='/api/fighter'


########### Get Fighters ############
@fighter_routes.route('/all_fighters/<int:weight>')
def get_weight_fighters(weight):
    fighters = Fighter.query.filter(Fighter.weight == weight)
    all_fighters = []
    all_fighters.extend([i.to_dict() for i in fighters])
    return {'All_Fighters': all_fighters}

@fighter_routes.route('/all_fighters')
def get_all_fighters():
    fighters = Fighter.query.all()
    all_fighters = []
    all_fighters.extend([i.to_dict() for i in fighters])
    return {'All_Fighters': all_fighters}
