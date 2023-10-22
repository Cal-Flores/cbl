from app.models import db, User, Fighter, Tour_Result, environment, SCHEMA
from sqlalchemy.sql import text

def seed_tour_results():
    match_1 = Tour_Result(id=1,winner='Jordan Burroughs',loser='Franklin Gomez',match='Round of 32',method='M.DEC',round='',year='2020')
    match_2 = Tour_Result(id=2,winner='Jordan Burroughs',loser='Tony Ferguson',match='Round of 16',method='S.DEC',round='',year='2020')
    match_3 = Tour_Result(id=3,winner='Jordan Burroughs',loser='Denis Tsargush',match='Quater-Final',method='M.DEC',round='',year='2020')
    match_4 = Tour_Result(id=4,winner='Charles Oliviera',loser='Jordan Burroughs',match='Semi-Final',method='DEC',round='',year='2020')
    match_5 = Tour_Result(id=5,winner='Jordan Burroughs',loser='Justin Gaethje',match='Cons-Semi',method='S.DEC',round='',year='2020')
    match_6 = Tour_Result(id=6,winner='Khabib Nurmagomedov',loser='Jordan Burroughs',match='Bronze Medal Match',method='DEC',round='`',year='2020')

    seeds = [
        match_1, match_2, match_3, match_4, match_5, match_6
        ]

    for seed in seeds:
        db.session.add(seed)
        db.session.commit()

def undo_tour_results():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.users RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM tour_results"))

    db.session.commit()
