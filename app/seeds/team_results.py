from app.models import db, User, Fighter, Season_Result, environment, Team_Result, SCHEMA
from sqlalchemy.sql import text

def seed_team_results():
    #  match_1 = Team_Result(id=1,winner='Creekview Cowboys',loser='Frisco Giants',winner_score=40,loser_score=0,week=1)
    #  match_2 = Team_Result(id=2,winner='Creekview Cowboys',loser='College Station Jets',winner_score=30,loser_score=3,week=2)
    #  match_3 = Team_Result(id=3,winner='Seguin Cardinals',loser='Creekview Cowboys',winner_score=26,loser_score=18,week=3)
    #  match_4 = Team_Result(id=4,winner='Creekview Cowboys',loser='Centennial Patriots',winner_score=19,loser_score=18,week=4)
    #  match_5 = Team_Result(id=5,winner='Dumas 49ers',loser='Creekview Cowboys',winner_score=32,loser_score=10,week=5)
    #  match_6 = Team_Result(id=6,winner='Creekview Cowboys',loser='Nazareth Chargers',winner_score=20,loser_score=17,week=6)


    #
    pass

def undo_team_results():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.users RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM team_results"))

    db.session.commit()
