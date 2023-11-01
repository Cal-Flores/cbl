from app.models import db, Team, Schedule, environment, SCHEMA
from sqlalchemy.sql import text


def generate_week1_matchup():
    duals = [
          Schedule(id=1, week=1,team_1='Canyon Randall Packers',team_2='Dumas 49ers', completed=False),
          Schedule(id=2, week=1,team_1='Saginaw Seahawks',team_2='Rockwall Vikings', completed=False),
          Schedule(id=3, week=1,team_1='Humble Lions',team_2='Caprock Rams', completed=False),
          Schedule(id=4, week=1,team_1='Woodland Bears',team_2='Seguin Cardinals', completed=False),
          Schedule(id=5, week=1,team_1='Creekview Cowboys',team_2='Liberty Saints', completed=False),
          Schedule(id=6, week=1,team_1='Frisco Giants',team_2='Colony Buccaneers', completed=False),
          Schedule(id=7, week=1,team_1='Prosper Eagles',team_2='Carter Riverside Panthers', completed=False),
          Schedule(id=8, week=1,team_1='Heritage Coyotes',team_2='Grapevine Falcons', completed=False),
          Schedule(id=10, week=1,team_1='Katy Ravens',team_2='Chisholm Trail Colts', completed=False),
          Schedule(id=9, week=1,team_1='A.M Consolidated Steelers',team_2='Boswell Jaguars', completed=False),
          Schedule(id=11, week=1,team_1='Cypress Browns',team_2='Argyle Texans', completed=False),
          Schedule(id=12, week=1,team_1='Wylie Bengals',team_2='Azle Titans', completed=False),
          Schedule(id=13, week=1,team_1='Centennial Patriots',team_2='Haltom City Broncos', completed=False),
          Schedule(id=14, week=1,team_1='Arlington Bills',team_2='Allen Chiefs', completed=False),
          Schedule(id=15, week=1,team_1='College Station Jets',team_2='Wakeland Raiders', completed=False),
          Schedule(id=16, week=1,team_1='Lamar Dolphins',team_2='Nazareth Chargers', completed=False),
    ]
    db.session.add_all(duals)
    db.session.commit()

def generate_week2_matchup():
    duals = [
         Schedule(id=17, week=2,team_1='Katy Ravens',team_2='Heritage Coyotes', completed=False),
         Schedule(id=18, week=2,team_1='A.M Consolidated Steelers',team_2='Prosper Eagles', completed=False),
         Schedule(id=19, week=2,team_1='Cypress Browns',team_2='Frisco Giants', completed=False),
         Schedule(id=20, week=2,team_1='Wylie Bengals',team_2='Creekview Cowboys', completed=False),
         Schedule(id=21, week=2,team_1='Centennial Patriots',team_2='Carter Riverside Panthers', completed=False),
         Schedule(id=22, week=2,team_1='Arlington Bills',team_2='Grapevine Falcons', completed=False),
         Schedule(id=23, week=2,team_1='College Station Jets',team_2='Liberty Saints', completed=False),
         Schedule(id=24, week=2,team_1='Lamar Dolphins',team_2='Colony Buccaneers', completed=False),
         Schedule(id=25, week=2,team_1='Boswell Jaguars',team_2='Caprock Rams', completed=False),
         Schedule(id=26, week=2,team_1='Chisholm Trail Colts',team_2='Seguin Cardinals', completed=False),
         Schedule(id=27, week=2,team_1='Azle Titans',team_2='Dumas 49ers', completed=False),
         Schedule(id=28, week=2,team_1='Argyle Texans',team_2='Saginaw Seahawks', completed=False),
         Schedule(id=29, week=2,team_1='Allen Chiefs',team_2='Woodland Bears', completed=False),
         Schedule(id=30, week=2,team_1='Haltom City Broncos',team_2='Humble Lions', completed=False),
         Schedule(id=31, week=2,team_1='Nazareth Chargers',team_2='Rockwall Vikings', completed=False),
         Schedule(id=32, week=2,team_1='Wakeland Raiders',team_2='Canyon Randall Packers', completed=False),
    ]
    db.session.add_all(duals)
    db.session.commit()


def generate_week3_matchup():
    duals = [
        Schedule(id=33, week=3,team_1='Creekview Cowboys',team_2='Frisco Giants', completed=False),
        Schedule(id=34, week=3,team_1='Prosper Eagles',team_2='Heritage Coyotes', completed=False),
        Schedule(id=35, week=3,team_1='Rockwall Vikings',team_2='Canyon Randall Packers', completed=False),
        Schedule(id=36, week=3,team_1='Humble Lions',team_2='Woodland Bears', completed=False),
        Schedule(id=37, week=3,team_1='Colony Buccaneers',team_2='Liberty Saints', completed=False),
        Schedule(id=38, week=3,team_1='Grapevine Falcons',team_2='Carter Riverside Panthers', completed=False),
        Schedule(id=39, week=3,team_1='Saginaw Seahawks',team_2='Dumas 49ers', completed=False),
        Schedule(id=40, week=3,team_1='Seguin Cardinals',team_2='Caprock Rams', completed=False),
        Schedule(id=41, week=3,team_1='A.M Consolidated Steelers',team_2='Katy Ravens', completed=False),
        Schedule(id=42, week=3,team_1='Cypress Browns',team_2='Wylie Bengals', completed=False),
        Schedule(id=43, week=3,team_1='Centennial Patriots',team_2='Arlington Bills', completed=False),
        Schedule(id=44, week=3,team_1='Boswell Jaguars',team_2='Chisholm Trail Colts', completed=False),
        Schedule(id=45, week=3,team_1='Azle Titans',team_2='Argyle Texans', completed=False),
        Schedule(id=46, week=3,team_1='Wakeland Raiders',team_2='Nazareth Chargers', completed=False),
        Schedule(id=47, week=3,team_1='Allen Chiefs',team_2='Haltom City Broncos', completed=False),
        Schedule(id=48, week=3,team_1='Lamar Dolphins',team_2='College Station Jets', completed=False),
    ]


    db.session.add_all(duals)
    db.session.commit()

def seed_all_schedule():
    generate_week1_matchup()
    generate_week2_matchup()
    generate_week3_matchup()


def undo_schedule():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.users RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM schedules"))

    db.session.commit()
