from flask import Blueprint, jsonify
from flask_login import login_required
from app.models import User, Fighter, Team
from sqlalchemy import and_, or_

team_routes = Blueprint('teams', __name__)
#url_prefix='/api/team'


##### Get Teams #########
@team_routes.route('/')
def get_all_teams():
    all_teams = Team.query.all()
    teams = []
    teams.extend([i.to_dict() for i in all_teams])
    return {'All Teams': teams}
