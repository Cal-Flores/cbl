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
    weight = db.Column(db.String)
    team_name = db.Column(db.String)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'nickname': self.nickname,
            'prof_img': self.prof_img,
            'body_img': self.body_img,
            'weight': self.weight
        }

class Tournament(db.Model, UserMixin):
    __tablename__ = 'Tournaments'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    year = db.Column(db.String)
    img = db.Column(db.String)
    cons_img = db.Column(db.String)

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
