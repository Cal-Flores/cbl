from app.models import db, User, Fighter, Season_Result, environment, SCHEMA
from sqlalchemy.sql import text

def seed_season_results():
    match_1 = Season_Result(id=1,winner='Jordan Burroughs',loser='Justin Gaethje',method='DEC')
    match_2 = Season_Result(id=2,winner='Jordan Burroughs',loser='Dustin Poirier',method='KO',round='2')
    match_3 = Season_Result(id=3,winner='Islam Makachev',loser='Jordan Burroughs',method='SUB',round='3')
    match_4 = Season_Result(id=4,winner='Jordan Burroughs',loser='Beneil Dariush',method='S.DEC')
    match_5 = Season_Result(id=5,winner='Jordan Burroughs',loser='Rafael Fiziev',method='KO',round='1')
    match_6 = Season_Result(id=6,winner='Jordan Burroughs',loser='Stephen Thompson',method='TKO',round='1')
    match_7 = Season_Result(id=7,winner='Charles Oliviera',loser='Jordan Burroughs',method='M.DEC')

    seeds = [
        match_1, match_2, match_3, match_4, match_5, match_6, match_7
    ]

    for seed in seeds:
        db.session.add(seed)
        db.session.commit()


def undo_season_results():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.users RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM season_results"))

    db.session.commit()
