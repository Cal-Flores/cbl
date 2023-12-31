from .db import db, environment, SCHEMA, add_prefix_for_prod
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

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
    wins = db.Column(db.Integer, default=0)
    losses = db.Column(db.Integer, default=0)
    trade = db.Column(db.Boolean, default=False)
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
            'wins': self.wins,
            'losses': self.losses,
            'all_win': self.all_win,
            'all_loss': self.all_loss,
            'points': self.points,
            'team_name': self.team_name,
            'trade': self.trade
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
    detail_bg = db.Column(db.String)
    win =  db.Column(db.Integer)
    loss =  db.Column(db.Integer)
    points =  db.Column(db.Integer)
    offense =  db.Column(db.Integer)
    defense =  db.Column(db.Integer)
    conf = db.Column(db.String)
    divison = db.Column(db.String)
    post_season = db.Column(db.String)
    curr_wins = db.Column(db.Integer)
    curr_loss = db.Column(db.Integer)
    div_win = db.Column(db.Integer, default=0)
    div_loss = db.Column(db.Integer, default=0)
    last_place = db.Column(db.String)
    fly = db.Column(db.String)
    bantam = db.Column(db.String)
    feather = db.Column(db.String)
    light = db.Column(db.String)
    welter = db.Column(db.String)
    middle = db.Column(db.String)
    light_heavy = db.Column(db.String)
    heavy = db.Column(db.String)

    draft_order = relationship("Draft_Order", backref="draft_order")



    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'win': self.win,
            'loss': self.loss,
            'points': self.points,
            'offense': self.offense,
            'defense': self.defense,
            'logo_img': self.logo_img,
            'background_img': self.background_img,
            'detail_bg': self.detail_bg,
            'conf': self.conf,
            'divison': self.divison,
            'post_season': self.post_season,
            'last_place': self.last_place,
            'curr_wins':self.curr_wins,
            'curr_loss':self.curr_loss,
            'div_win':self.div_win,
            'div_loss':self.div_loss,
            'fly_id': self.fly,
            'bantam_id': self.bantam,
            'feather_id': self.feather,
            'light_id': self.light,
            'welter_id': self.welter,
            'middle_id': self.middle,
            'light_heavy_id': self.light_heavy,
            'heavy': self.heavy
        }

class Team_Result(db.Model, UserMixin):
    __tablename__ = 'team_results'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    winner = db.Column(db.String)
    loser = db.Column(db.String)
    winner_score = db.Column(db.Integer)
    loser_score = db.Column(db.Integer)
    week = db.Column(db.Integer)

    def to_dict(self):
        return {
            'id': self.id,
            'winner': self.winner,
            'loser': self.loser,
            'winner_score': self.winner_score,
            'loser_score': self.loser_score,
            'week': self.week
        }

class Schedule(db.Model, UserMixin):
    __tablename__ = 'schedules'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    week = db.Column(db.Integer)
    team_1 = db.Column(db.String)
    team_2 = db.Column(db.String)
    completed = db.Column(db.Boolean)

    def to_dict(self):
        return {
            'id': self.id,
            'week': self.week,
            'team_1':self.team_1,
            'team_2': self.team_2,
            'completed': self.completed
        }

class Draft_Order(db.Model, UserMixin):
    __tablename__ = 'draft_orders'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}


    id = db.Column(db.Integer, primary_key=True)
    team = db.Column(db.String)
    pick = db.Column(db.Integer)
    round = db.Column(db.Integer)
    completed = db.Column(db.Boolean, default=False)

    #relationship
    team = db.Column(db.String, ForeignKey('teams.name'))


    def to_dict(self):
        return {
            'id': self.id,
            'team': self.team,
            'pick': self.pick,
            'round': self.round,
            'completed': self.completed
        }


