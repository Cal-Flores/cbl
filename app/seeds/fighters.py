# from app.models import db, Fighter, environment, SCHEMA
# from sqlalchemy.sql import text

# def seed_fighters():
#     fighter_1 = Fighter(name='Charles Oliviera', nickname='Do Bronx', prof_img='', weight='155')
#     fighter_2 = Fighter(name='Isreal Adesanya', nickname='The Last Style Bender', prof_img='', weight='185')
#     fighter_3 = Fighter(name='Brandon Moreno', nickname='The Assasain Baby', prof_img='', weight='125')
#     fighter_4 = Fighter(name='Kamaru Usman', nickname='The Nigerian Nightmare', prof_img='', weight='170')


#     db.session.add(fighter_1)
#     db.session.add(fighter_2)
#     db.session.add(fighter_3)
#     db.session.add(fighter_4)
#     db.session.commit()


# def undo_users():
#     if environment == "production":
#         db.session.execute(f"TRUNCATE table {SCHEMA}.users RESTART IDENTITY CASCADE;")
#     else:
#         db.session.execute(text("DELETE FROM fighters"))

#     db.session.commit()
