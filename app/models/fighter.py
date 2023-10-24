from .db import db, environment, SCHEMA, add_prefix_for_prod
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

class Fighter(db.Model, UserMixin):
    __tablename__ = 'fighters'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), nullable=False,)
    nickname = db.Column(db.String(40))
    prof_img = db.Column(db.String)
    body_img = db.Column(db.String)
    medal = db.Column(db.String)
    weight = db.Column(db.String)
    team_name = db.Column(db.String)
    all_win = db.Column(db.Integer)
    all_loss = db.Column(db.Integer)
    points = db.Column(db.Integer)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'nickname': self.nickname,
            'prof_img': self.prof_img,
            'body_img': self.body_img,
            'medal': self.medal,
            'weight': self.weight,
            'all_win': self.all_win,
            'all_loss': self.all_loss,
            'points': self.points,
            'team_name': self.team_name
        }

class Tournament(db.Model, UserMixin):
    __tablename__ = 'Tournaments'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    year = db.Column(db.String)
    img = db.Column(db.String)
    cons_img = db.Column(db.String)

class Medal(db.Model, UserMixin):
    __tablename__ = 'Medals'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    fighter = db.Column(db.String)
    place = db.Column(db.String)
    year = db.Column(db.String)

    def to_dict(self):
        return {
              'id': self.id,
              'fighter': self.fighter,
              'place': self.place,
              'year': self.year
        }

class Tour_Result(db.Model, UserMixin):
    __tablename__ = 'tour_results'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    winner = db.Column(db.String)
    loser = db.Column(db.String)
    match = db.Column(db.String)
    method = db.Column(db.String)
    round = db.Column(db.String)
    year = db.Column(db.String)

    def to_dict(self):
        return {
            'id': self.id,
            'winner': self.winner,
            'loser': self.loser,
            'match': self.match,
            'round': self.round,
            'method': self.method,
            'year': self.year
        }

class Season_Result(db.Model, UserMixin):
    __tablename__ = 'season_results'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    winner = db.Column(db.String)
    loser = db.Column(db.String)
    method = db.Column(db.String)
    round = db.Column(db.String)
    dual_id = db.Column(db.Integer)

    def to_dict(self):
        return {
            'id': self.id,
            'winner': self.winner,
            'loser': self.loser,
            'method': self.method,
            'round': self.round,
            'dual_id': self.dual_id
        }


class Team(db.Model, UserMixin):
    __tablename__ = 'teams'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40))
    logo_img = db.Column(db.String)
    background_img = db.Column(db.String)
    conf = db.Column(db.String)
    divison = db.Column(db.String)
    fly = db.Column(db.String)
    bantam = db.Column(db.String)
    feather = db.Column(db.String)
    light = db.Column(db.String)
    welter = db.Column(db.String)
    middle = db.Column(db.String)
    light_heavy = db.Column(db.String)
    heavy = db.Column(db.String)



    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'logo_img': self.logo_img,
            'background_img': self.background_img,
            'conf': self.conf,
            'divison': self.divison,
            'fly_id': self.fly,
            'bantam_id': self.bantam,
            'feather_id': self.feather,
            'light_id': self.light,
            'welter_id': self.welter,
            'middle_id': self.middle,
            'light_heavy_id': self.light_heavy,
            'heavy': self.heavy
        }
