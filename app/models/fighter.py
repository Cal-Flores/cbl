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

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'nickname': self.nickname,
            'prof_img': self.prof_img,
            'body_img': self.body_img,
            'weight': self.weight
        }

class Team(db.Model, UserMixin):
    __tablename__ = 'teams'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40))
    logo_img = db.Column(db.String)
    background_img = db.Column(db.String)
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
            'fly_id': self.fly_id,
            'bantam_id': self.bantam_id,
            'feather_id': self.feather_id,
            'light_id': self.light_id,
            'welter_id': self.welter_id,
            'middle_id': self.middle_id,
            'light_heavy_id': self.light_heavy_id,
            'heavy': self.heavy_id
        }
