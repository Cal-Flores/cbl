from app.models import db, User, Fighter, environment, SCHEMA
from sqlalchemy.sql import text

def seed_fighters():
    fighter_1 = Fighter(id=1,name='Charles Oliviera', nickname='Do Bronx', prof_img='',body_img='', weight='155')
    fighter_2 = Fighter(id=2,name='Kamaru Usman', nickname='The Nigerian Nightmare', prof_img='',body_img='', weight='170')
    fighter_3 = Fighter(id=3,name='Brandon Moreno', nickname='The Assasain Baby', prof_img='',body_img='', weight='125')
    fighter_4 = Fighter(id=4,name='Alexander Volkanovski', nickname='The Great', prof_img='',body_img='', weight='145')
    fighter_5 = Fighter(id=5,name='Cody Sandhagen', nickname='The Sandman', prof_img='', body_img='', weight='135')
    fighter_6 = Fighter(id=6,name='Robert Whittaker', nickname='The Reaper', prof_img='', body_img='', weight='185')
    fighter_7 = Fighter(id=7,name='Jan Blachowitz', nickname='', prof_img='', body_img='', weight='205')
    fighter_8 = Fighter(id=8,name='Tai Tuivasa', nickname='', prof_img='', body_img='', weight='285')
    seeds = [
        fighter_1, fighter_2, fighter_3, fighter_4, fighter_5, fighter_6, fighter_7, fighter_8
    ]

    for seed in seeds:
        db.session.add(seed)
        db.session.commit()

def undo_fighters():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.users RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM fighters"))

    db.session.commit()
