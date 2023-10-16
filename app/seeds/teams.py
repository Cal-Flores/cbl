from app.models import db, User, Fighter, Team, environment, SCHEMA
from sqlalchemy.sql import text

def seed_teams():
    team_1 = Team(id=1,name='Centennial Patriots', logo_img='', background_img='',conf='AFC', divison='East', fly='Brandon Moreno', bantam='Cody Sandhagen', feather='Alexander Volkanovsky', light='Charles Oliviera', welter='Kamaru Usman', middle='Robert Whittaker', light_heavy='Jan Blachowitz', heavy='Tai Tuivasa')
    team_2 = Team(id=2,name='Katy Ravens', logo_img='', background_img='',conf='NFC', divison='South', fly='Brandon Moreno', bantam='Cody Sandhagen', feather='Alexander Volkanovsky', light='Charles Oliviera', welter='Kamaru Usman', middle='Robert Whittaker', light_heavy='Jan Blachowitz', heavy='Tai Tuivasa')

    db.session.add(team_1)
    db.session.add(team_2)
    db.session.commit()

def undo_teams():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.users RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM teams"))

    db.session.commit()
