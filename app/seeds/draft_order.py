from app.models import db, Team, Schedule, environment, SCHEMA, Draft_Order
from sqlalchemy.sql import text

def seed_draft_order():
    order = [
  #####################################        ROUND ONE     #############################
        Draft_Order(id=1,team='Wakeland Raiders', pick=1, round=1),
        Draft_Order(id=2,team='Argyle Texans', pick=2, round=1),
        Draft_Order(id=3,team='Carter Riverside Panthers', pick=3, round=1),
        Draft_Order(id=4,team='Wylie Bengals', pick=4, round=1),
        # BENGALS deducted a 2nd pick Pavlovich
        Draft_Order(id=5,team='Grapevine Falcons', pick=5, round=1),
        Draft_Order(id=6,team='Lamar Dolphins', pick=6, round=1),
        Draft_Order(id=7,team='Woodland Bears', pick=7, round=1),
        Draft_Order(id=8,team='Caprock Rams', pick=8, round=1),
        Draft_Order(id=9,team='Prosper Eagles', pick=9, round=1),
        Draft_Order(id=10,team='Cypress Browns', pick=10, round=1),
        Draft_Order(id=11,team='Seguin Cardinals', pick=11, round=1),
        Draft_Order(id=12,team='College Station Jets', pick=12, round=1),
        Draft_Order(id=13,team='Heritage Coyotes', pick=13, round=1),
        Draft_Order(id=14,team='Azle Titans', pick=14, round=1),
        Draft_Order(id=15,team='Arlington Bills', pick=15, round=1),
        # BILLS deducted a 2nd round pick Arnold Allen
        Draft_Order(id=16,team='Frisco Giants', pick=16, round=1),
        Draft_Order(id=17,team='Nazareth Chargers', pick=17, round=1),
        Draft_Order(id=18,team='Dumas 49ers', pick=18, round=1),
        ## 49ERS deducted a 2nd and 5th round pick Umar, Nicalou
        Draft_Order(id=19,team='Creekview Cowboys', pick=19, round=1),
        # COWBOYS deducted a 4th round pick Said nurmagomedov
        Draft_Order(id=20,team='Chisholm Trail Colts', pick=20, round=1),
        ## COLTS deducted a 3rd round pick Kevin Holland, Matt Schnell
        Draft_Order(id=21,team='Humble Lions', pick=21, round=1),
        ## LIONS deducted a 2nd round pick Pantoja
        Draft_Order(id=22,team='Allen Chiefs', pick=22, round=1),
        Draft_Order(id=23,team='Boswell Jaguars', pick=23, round=1),
        Draft_Order(id=24,team='Canyon Randall Packers', pick=24, round=1),
        ## PACKERS deducted a 2nd round pick Alex Peireira
        Draft_Order(id=25,team='A.M Consolidated Steelers', pick=25, round=1),
        # STEELERS deducted a 2nd round pick Belal Mohammed
        Draft_Order(id=26,team='Haltom City Broncos', pick=26, round=1),
        Draft_Order(id=27,team='Rockwall Vikings', pick=27, round=1),
        Draft_Order(id=28,team='Colony Buccaneers', pick=28, round=1),
        Draft_Order(id=29,team='Liberty Saints', pick=29, round=1),
        Draft_Order(id=30,team='Katy Ravens', pick=30, round=1),
        ## RAVENS deducted a 3rd round pick Jalin Turner
        Draft_Order(id=31,team='Saginaw Seahawks', pick=31, round=1),
        ## SEAHAWKS deducted a 2nd round pick Brandon Royval
        Draft_Order(id=32,team='Centennial Patriots', pick=32, round=1),
        ## PATRIOTS DEDUCTED A 3RD ROUND PICK Nikita krylov

#####################################       ROUND TWO     #############################

        Draft_Order(id=33,team='Wakeland Raiders', pick=1, round=2),
        Draft_Order(id=34,team='Argyle Texans', pick=2, round=2),
        Draft_Order(id=35,team='Carter Riverside Panthers', pick=3, round=2),
        Draft_Order(id=37,team='Grapevine Falcons', pick=5, round=2),
        Draft_Order(id=38,team='Lamar Dolphins', pick=6, round=2),
        Draft_Order(id=39,team='Woodland Bears', pick=7, round=2),
        Draft_Order(id=40,team='Caprock Rams', pick=8, round=2),
        Draft_Order(id=41,team='Prosper Eagles', pick=9, round=2),
        Draft_Order(id=42,team='Cypress Browns', pick=10, round=2),
        Draft_Order(id=43,team='Seguin Cardinals', pick=11, round=2),
        Draft_Order(id=44,team='College Station Jets', pick=12, round=2),
        Draft_Order(id=45,team='Heritage Coyotes', pick=13, round=2),
        Draft_Order(id=46,team='Azle Titans', pick=14, round=2),
        Draft_Order(id=48,team='Frisco Giants', pick=16, round=2),
        Draft_Order(id=49,team='Nazareth Chargers', pick=17, round=2),
        Draft_Order(id=51,team='Creekview Cowboys', pick=19, round=2),
        # COWBOYS deducted a 4th round pick Said nurmagomedov
        Draft_Order(id=52,team='Chisholm Trail Colts', pick=20, round=2),
        ## COLTS deducted a 3rd round pick Kevin Holland, Matt Schnell
        Draft_Order(id=54,team='Allen Chiefs', pick=22, round=2),
        Draft_Order(id=55,team='Boswell Jaguars', pick=23, round=2),
        Draft_Order(id=58,team='Haltom City Broncos', pick=26, round=2),
        Draft_Order(id=59,team='Rockwall Vikings', pick=27, round=2),
        Draft_Order(id=60,team='Colony Buccaneers', pick=28, round=2),
        Draft_Order(id=61,team='Liberty Saints', pick=29, round=2),
        Draft_Order(id=62,team='Katy Ravens', pick=30, round=2),
        ## RAVENS deducted a 3rd round pick Jalin Turner
        Draft_Order(id=64,team='Centennial Patriots', pick=32, round=2),
        ## PATRIOTS DEDUCTED A 3RD ROUND PICK Nikita krylov

    ]


    db.session.add_all(order)
    db.session.commit()




def undo_order():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.users RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM draft_orders"))

    db.session.commit()
