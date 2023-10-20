from app.models import db, User, Fighter, Team, Tournament, environment, SCHEMA
from sqlalchemy.sql import text

def seed_teams():

    team_1 = Team(id=1,name='Centennial Patriots', logo_img='', background_img='',conf='AFC', divison='East')
    team_2 = Team(id=2,name='Katy Ravens', logo_img='', background_img='',conf='AFC', divison='North')
    team_3 = Team(id=3,name='Rockwall Vikings', logo_img='', background_img='',conf='NFC', divison='North')
    team_4 = Team(id=4,name='Azle Titans', logo_img='', background_img='',conf='AFC', divison='South')
    team_5 = Team(id=5,name='Heritage Redskins', logo_img='', background_img='',conf='NFC', divison='East')
    team_6 = Team(id=6,name='Wakeland Raiders', logo_img='', background_img='',conf='AFC', divison='West')
    team_7 = Team(id=7,name='Seguin Cardinals', logo_img='https://static.www.nfl.com/image/private/f_auto/league/u9fltoslqdsyao8cpm0k', background_img='',conf='NFC', divison='West')
    team_8 = Team(id=8,name='Liberty Saints', logo_img='', background_img='',conf='NFC', divison='South')
    team_9 = Team(id=9,name='Grapevine Falcons', logo_img='', background_img='',conf='NFC', divison='South')
    team_10 = Team(id=10,name='AM Consolidated Steelers', logo_img='', background_img='',conf='AFC', divison='West')
    team_11 = Team(id=11,name='Chisholm Trail Colts', logo_img='', background_img='',conf='AFC', divison='South')
    team_12 = Team(id=12,name='Caprock Rams', logo_img='', background_img='',conf='NFC', divison='West')
    team_13 = Team(id=13,name='Creekview Cowboys', logo_img='', background_img='',conf='NFC', divison='East')
    team_14 = Team(id=14,name='Allen Chiefs', logo_img='', background_img='',conf='AFC', divison='West')
    team_15 = Team(id=15,name='Katy Ravens', logo_img='', background_img='',conf='AFC', divison='North')
    team_16 = Team(id=16,name='Dumas 49ers', logo_img='', background_img='',conf='NFC', divison='West')
    team_17 = Team(id=17,name='Canyon Randall Packers', logo_img='', background_img='',conf='NFC', divison='North')
    team_18 = Team(id=18,name='College Station Jets', logo_img='', background_img='',conf='AFC', divison='East')
    team_19 = Team(id=19,name='Boswell Jaguars', logo_img='', background_img='',conf='AFC', divison='South')
    team_20 = Team(id=20,name='Cypress Browns', logo_img='', background_img='',conf='AFC', divison='North')
    team_21 = Team(id=21,name='Frisco Giants', logo_img='', background_img='',conf='NFC', divison='East')
    team_22 = Team(id=22,name='Lamar Dolphins', logo_img='', background_img='',conf='AFC', divison='East')
    team_23 = Team(id=23,name='Colony Buccaneers', logo_img='', background_img='',conf='NFC', divison='South')
    team_24 = Team(id=24,name='Carter Riverside Panthers', logo_img='', background_img='',conf='NFC', divison='South')
    team_25 = Team(id=25,name='Nazareth Chargers', logo_img='', background_img='',conf='AFC', divison='West')
    team_26 = Team(id=26,name='Haltom City Broncos', logo_img='', background_img='',conf='AFC', divison='West')
    team_27 = Team(id=27,name='Arlington Bills', logo_img='', background_img='',conf='AFC', divison='East')
    team_28 = Team(id=28,name='Woodland Bears', logo_img='', background_img='',conf='NFC', divison='North')
    team_29 = Team(id=29,name='Humble Lions', logo_img='', background_img='',conf='NFC', divison='North')
    team_30 = Team(id=30,name='Wylie Bengals', logo_img='', background_img='',conf='AFC', divison='North')
    team_31 = Team(id=31,name='Saginaw Seahawks', logo_img='', background_img='',conf='NFC', divison='West')
    team_32 = Team(id=32,name='Argyle Texans', logo_img='', background_img='',conf='AFC', divison='South')


    teams = [team_1, team_2, team_3, team_4, team_5, team_6, team_7, team_8, team_9, team_10, team_11, team_12, team_13, team_14, team_15, team_16, team_17, team_18, team_19, team_20, team_21, team_22, team_23, team_24, team_25, team_26, team_27, team_28, team_29, team_30, team_31, team_32]

    for team in teams:
        db.session.add(team)
        db.session.commit()



def undo_teams():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.users RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM teams"))

    db.session.commit()
