from app.models import db, User, Fighter, Season_Result, environment, SCHEMA
from sqlalchemy.sql import text

def seed_season_results():
    pass


def undo_season_results():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.users RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM season_results"))

    db.session.commit()
