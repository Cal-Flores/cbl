from app.models import db, User, Fighter, environment, SCHEMA
from sqlalchemy.sql import text

def seed_fighters():
    fighter_1 = Fighter(id=1,name='Charles Oliviera', nickname='Do Bronx', prof_img='', weight='155')

    db.session.add(fighter_1)
    db.session.commit()

def undo_fighters():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.users RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM fighters"))

    db.session.commit()
