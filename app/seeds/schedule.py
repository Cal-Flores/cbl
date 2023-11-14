from app.models import db, Team, Schedule, environment, SCHEMA
from sqlalchemy.sql import text
import random


def generate_week1_matchup():
    duals = [
          Schedule(id=1, week=1,team_1='Canyon Randall Packers',team_2='Dumas 49ers', completed=False),
          Schedule(id=15, week=1,team_1='College Station Jets',team_2='Wakeland Raiders', completed=False),
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
          Schedule(id=16, week=1,team_1='Lamar Dolphins',team_2='Nazareth Chargers', completed=False),
    ]
    random.shuffle(duals)
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

def generate_week4_matchup():
    duals = [
        Schedule(id=60, week=4,team_1='Katy Ravens',team_2='Prosper Eagles', completed=False),
        Schedule(id=52, week=4,team_1='Creekview Cowboys',team_2='Cypress Browns', completed=False),
        Schedule(id=64, week=4,team_1='A.M Consolidated Steelers',team_2='Heritage Coyotes', completed=False),
        Schedule(id=56, week=4,team_1='Frisco Giants',team_2='Wylie Bengals', completed=False),
        Schedule(id=54, week=4,team_1='Centennial Patriots',team_2='Grapevine Falcons', completed=False),
        Schedule(id=58, week=4,team_1='Colony Buccaneers',team_2='College Station Jets', completed=False),
        Schedule(id=62, week=4,team_1='Arlington Bills',team_2='Carter Riverside Panthers', completed=False),
        Schedule(id=49, week=4,team_1='Liberty Saints',team_2='Lamar Dolphins', completed=False),
        Schedule(id=55, week=4,team_1='Boswell Jaguars',team_2='Seguin Cardinals', completed=False),
        Schedule(id=63, week=4,team_1='Saginaw Seahawks',team_2='Azle Titans', completed=False),
        Schedule(id=50, week=4,team_1='Allen Chiefs',team_2='Humble Lions', completed=False),
        Schedule(id=61, week=4,team_1='Canyon Randall Packers',team_2='Nazareth Chargers', completed=False),
        Schedule(id=57, week=4,team_1='Haltom City Broncos',team_2='Woodland Bears', completed=False),
        Schedule(id=53, week=4,team_1='Rockwall Vikings',team_2='Wakeland Raiders', completed=False),
        Schedule(id=59, week=4,team_1='Dumas 49ers',team_2='Argyle Texans', completed=False),
        Schedule(id=51, week=4,team_1='Chisholm Trail Colts',team_2='Caprock Rams', completed=False),

    ]
    db.session.add_all(duals)
    db.session.commit()

def generate_week5_matchup():
    duals = [
        Schedule(id=72, week=5,team_1='Katy Ravens',team_2='Wylie Bengals', completed=False),
        Schedule(id=75, week=5,team_1='A.M Consolidated Steelers',team_2='Cypress Browns', completed=False),
        Schedule(id=67, week=5,team_1='Centennial Patriots',team_2='Lamar Dolphins', completed=False),
        Schedule(id=71, week=5,team_1='Arlington Bills',team_2='College Station Jets', completed=False),
        Schedule(id=80, week=5,team_1='Boswell Jaguars',team_2='Argyle Texans', completed=False),
        Schedule(id=77, week=5,team_1='Chisholm Trail Colts',team_2='Azle Titans', completed=False),
        Schedule(id=76, week=5,team_1='Allen Chiefs',team_2='Wakeland Raiders', completed=False),
        Schedule(id=66, week=5,team_1='Haltom City Broncos',team_2='Nazareth Chargers', completed=False),
        Schedule(id=79, week=5,team_1='Saginaw Seahawks',team_2='Caprock Rams', completed=False),
        Schedule(id=73, week=5,team_1='Dumas 49ers',team_2='Seguin Cardinals', completed=False),
        Schedule(id=68, week=5,team_1='Colony Buccaneers',team_2='Carter Riverside Panthers', completed=False),
        Schedule(id=69, week=5,team_1='Liberty Saints',team_2='Grapevine Falcons', completed=False),
        Schedule(id=70, week=5,team_1='Creekview Cowboys',team_2='Heritage Coyotes', completed=False),
        Schedule(id=78, week=5,team_1='Frisco Giants',team_2='Prosper Eagles', completed=False),
        Schedule(id=65, week=5,team_1='Canyon Randall Packers',team_2='Woodland Bears', completed=False),
        Schedule(id=74, week=5,team_1='Rockwall Vikings',team_2='Humble Lions', completed=False),

    ]
    db.session.add_all(duals)
    db.session.commit()


def generate_week6_matchup():
    duals = [
        Schedule(id=88, week=6,team_1='Colony Buccaneers',team_2='Creekview Cowboys', completed=False),
        Schedule(id=94, week=6,team_1='Liberty Saints',team_2='Frisco Giants', completed=False),
        Schedule(id=88, week=6,team_1='Prosper Eagles',team_2='Grapevine Falcons', completed=False),
        Schedule(id=83, week=6,team_1='Heritage Coyotes',team_2='Carter Riverside Panthers', completed=False),
        Schedule(id=96, week=6,team_1='Saginaw Seahawks',team_2='Canyon Randall Packers', completed=False),
        Schedule(id=93, week=6,team_1='Rockwall Vikings',team_2='Dumas 49ers', completed=False),
        Schedule(id=95, week=6,team_1='Humble Lions',team_2='Seguin Cardinals', completed=False),
        Schedule(id=82, week=6,team_1='Caprock Rams',team_2='Woodland Bears', completed=False),
        Schedule(id=90, week=6,team_1='Katy Ravens',team_2='Boswell Jaguars', completed=False),
        Schedule(id=86, week=6,team_1='A.M Consolidated Steelers',team_2='Chisholm Trail Colts', completed=False),
        Schedule(id=92, week=6,team_1='Cypress Browns',team_2='Azle Titans', completed=False),
        Schedule(id=85, week=6,team_1='Wylie Bengals',team_2='Argyle Texans', completed=False),
        Schedule(id=81, week=6,team_1='Centennial Patriots',team_2='Allen Chiefs', completed=False),
        Schedule(id=91, week=6,team_1='Haltom City Broncos',team_2='Arlington Bills', completed=False),
        Schedule(id=89, week=6,team_1='Nazareth Chargers',team_2='College Station Jets', completed=False),
        Schedule(id=84, week=6,team_1='Lamar Dolphins',team_2='Wakeland Raiders', completed=False),


    ]
    db.session.add_all(duals)
    db.session.commit()


def generate_week7_matchup():
    duals = [
        Schedule(id=99, week=7,team_1='Katy Ravens',team_2='Frisco Giants', completed=False),
        Schedule(id=107, week=7,team_1='A.M Consolidated Steelers',team_2='Creekview Cowboys', completed=False),
        Schedule(id=103, week=7,team_1='Cypress Browns',team_2='Heritage Coyotes', completed=False),
        Schedule(id=112, week=7,team_1='Wylie Bengals',team_2='Prosper Eagles', completed=False),
        Schedule(id=106, week=7,team_1='Centennial Patriots',team_2='Liberty Saints', completed=False),
        Schedule(id=110, week=7,team_1='Colony Buccaneers',team_2='Arlington Bills', completed=False),
        Schedule(id=100, week=7,team_1='College Station Jets',team_2='Carter Riverside Panthers', completed=False),
        Schedule(id=102, week=7,team_1='Grapevine Falcons',team_2='Lamar Dolphins', completed=False),
        Schedule(id=105, week=7,team_1='Saginaw Seahawks',team_2='Chisholm Trail Colts', completed=False),
        Schedule(id=101, week=7,team_1='Boswell Jaguars',team_2='Dumas 49ers', completed=False),
        Schedule(id=97, week=7,team_1='Seguin Cardinals',team_2='Argyle Texans', completed=False),
        Schedule(id=109, week=7,team_1='Azle Titans',team_2='Caprock Rams', completed=False),
        Schedule(id=111, week=7,team_1='Canyon Randall Packers',team_2='Haltom City Broncos', completed=False),
        Schedule(id=108 , week=7,team_1='Allen Chiefs',team_2='Rockwall Vikings', completed=False),
        Schedule(id=104, week=7,team_1='Nazareth Chargers',team_2='Woodland Bears', completed=False),
        Schedule(id=98, week=7,team_1='Wakeland Raiders',team_2='Humble Lions', completed=False),
    ]
    db.session.add_all(duals)
    db.session.commit()

def generate_week8_matchup():
    duals = [
        Schedule(id=121, week=8,team_1='Canyon Randall Packers',team_2='Humble Lions', completed=False),
        Schedule(id=128, week=8,team_1='Rockwall Vikings',team_2='Woodland Bears', completed=False), ##128
        Schedule(id=114, week=8,team_1='Creekview Cowboys',team_2='Prosper Eagles', completed=False),
        Schedule(id=126, week=8,team_1='Frisco Giants',team_2='Heritage Coyotes', completed=False),
        Schedule(id=120, week=8,team_1='Colony Buccaneers',team_2='Grapevine Falcons', completed=False),
        Schedule(id=124, week=8,team_1='Saginaw Seahawks',team_2='Seguin Cardinals', completed=False),
        Schedule(id=113, week=8,team_1='Dumas 49ers',team_2='Caprock Rams', completed=False),
        Schedule(id=127, week=8,team_1='Liberty Saints',team_2='Carter Riverside Panthers', completed=False),
        Schedule(id=117, week=8,team_1='Allen Chiefs',team_2='Nazareth Chargers', completed=False),
        Schedule(id=123, week=8,team_1='Haltom City Broncos',team_2='Wakeland Raiders', completed=False),
        Schedule(id=116, week=8,team_1='Boswell Jaguars',team_2='Azle Titans', completed=False),
        Schedule(id=119, week=8,team_1='Chisholm Trail Colts',team_2='Argyle Texans', completed=False),
        Schedule(id=122, week=8,team_1='Centennial Patriots',team_2='College Station Jets', completed=False),
        Schedule(id=125, week=8,team_1='Arlington Bills',team_2='Lamar Dolphins', completed=False),
        Schedule(id=115, week=8,team_1='Katy Ravens',team_2='Cypress Browns', completed=False),
        Schedule(id=118, week=8,team_1='A.M Consolidated Steelers',team_2='Wylie Bengals', completed=False),

    ]
    db.session.add_all(duals)
    db.session.commit()

def generate_week9_matchup():
    duals = [
        Schedule(id=133, week=9,team_1='Saginaw Seahawks',team_2='Creekview Cowboys', completed=False),
        Schedule(id=143, week=9,team_1='Dumas 49ers',team_2='Frisco Giants', completed=False),
        Schedule(id=137, week=9,team_1='Prosper Eagles',team_2='Saginaw Seahawks', completed=False),
        Schedule(id=140, week=9,team_1='Caprock Rams',team_2='Heritage Coyotes', completed=False),
        Schedule(id=130, week=9,team_1='Colony Buccaneers',team_2='Canyon Randall Packers', completed=False),
        Schedule(id=142, week=9,team_1='Liberty Saints',team_2='Rockwall Vikings', completed=False),
        Schedule(id=132, week=9,team_1='Humble Lions',team_2='Grapevine Falcons', completed=False),
        Schedule(id=139, week=9,team_1='Woodland Bears',team_2='Carter Riverside Panthers', completed=False),
        Schedule(id=136, week=9,team_1='Katy Ravens',team_2='Allen Chiefs', completed=False),
        Schedule(id=144, week=9,team_1='A.M Consolidated Steelers',team_2='Haltom City Broncos', completed=False),
        Schedule(id=129, week=9,team_1='Nazareth Chargers',team_2='Cypress Browns', completed=False),
        Schedule(id=135, week=9,team_1='Wylie Bengals',team_2='Wakeland Raiders', completed=False),
        Schedule(id=138, week=9,team_1='Centennial Patriots',team_2='Boswell Jaguars', completed=False),
        Schedule(id=141, week=9,team_1='Chisholm Trail Colts',team_2='Arlington Bills', completed=False),
        Schedule(id=131, week=9,team_1='College Station Jets',team_2='Azle Titans', completed=False),
        Schedule(id=134, week=9,team_1='Lamar Dolphins',team_2='Argyle Texans', completed=False),
    ]
    db.session.add_all(duals)
    db.session.commit()

def generate_week10_matchup():
    duals = [
        Schedule(id=148, week=10,team_1='Katy Ravens',team_2='Creekview Cowboys', completed=False),
        Schedule(id=153, week=10,team_1='A.M Consolidated Steelers',team_2='Frisco Giants', completed=False),
        Schedule(id=157, week=10,team_1='Cypress Browns',team_2='Prosper Eagles', completed=False),
        Schedule(id=159, week=10,team_1='Heritage Coyotes',team_2='Wylie Bengals', completed=False),
        Schedule(id=145, week=10,team_1='Centennial Patriots',team_2='Colony Buccaneers', completed=False),
        Schedule(id=152, week=10,team_1='Liberty Saints',team_2='Arlington Bills', completed=False),
        Schedule(id=150, week=10,team_1='College Station Jets',team_2='Grapevine Falcons', completed=False),
        Schedule(id=155, week=10,team_1='Lamar Dolphins',team_2='Carter Riverside Panthers', completed=False),
        Schedule(id=147, week=10,team_1='Boswell Jaguars',team_2='Saginaw Seahawks', completed=False),
        Schedule(id=160, week=10,team_1='Dumas 49ers',team_2='Chisholm Trail Colts', completed=False), ###160
        Schedule(id=156, week=10,team_1='Seguin Cardinals',team_2='Azle Titans', completed=False),
        Schedule(id=149, week=10,team_1='Caprock Rams',team_2='Argyle Texans', completed=False),
        Schedule(id=154, week=10,team_1='Allen Chiefs',team_2='Canyon Randall Packers', completed=False),
        Schedule(id=158, week=10,team_1='Rockwall Vikings',team_2='Haltom City Broncos', completed=False),
        Schedule(id=146, week=10,team_1='Humble Lions',team_2='Nazareth Chargers', completed=False),
        Schedule(id=151, week=10,team_1='Woodland Bears',team_2='Wakeland Raiders', completed=False),
    ]
    db.session.add_all(duals)
    db.session.commit()

def generate_week11_matchup():
    duals = [
        Schedule(id=168, week=11,team_1='Canyon Randall Packers',team_2='Woodland Bears', completed=False),
        Schedule(id=163, week=11,team_1='Rockwall Vikings',team_2='Humble Lions', completed=False),
        Schedule(id=173, week=11,team_1='Creekview Cowboys',team_2='Heritage Coyotes', completed=False),
        Schedule(id=166, week=11,team_1='Frisco Giants',team_2='Prosper Eagles', completed=False),
        Schedule(id=175, week=11,team_1='Colony Buccaneers',team_2='Carter Riverside Panthers', completed=False),
        Schedule(id=162, week=11,team_1='Liberty Saints',team_2='Grapevine Falcons', completed=False),
        Schedule(id=171, week=11,team_1='Saginaw Seahawks',team_2='Caprock Rams', completed=False),
        Schedule(id=176, week=11,team_1='Dumas 49ers',team_2='Seguin Cardinals', completed=False),
        Schedule(id=169, week=11,team_1='Allen Chiefs',team_2='Wakeland Raiders', completed=False),
        Schedule(id=165, week=11,team_1='Haltom City Broncos',team_2='Nazareth Chargers', completed=False),
        Schedule(id=172, week=11,team_1='Boswell Jaguars',team_2='Argyle Texans', completed=False),
        Schedule(id=167, week=11,team_1='Chisholm Trail Colts',team_2='Azle Titans', completed=False),
        Schedule(id=174, week=11,team_1='Centennial Patriots',team_2='Lamar Dolphins', completed=False),
        Schedule(id=170, week=11,team_1='Arlington Bills',team_2='College Station Jets', completed=False),
        Schedule(id=161, week=11,team_1='Katy Ravens',team_2='Wylie Bengals', completed=False),
        Schedule(id=164, week=11,team_1='A.M Consolidated Steelers',team_2='Cypress Browns', completed=False),
    ]
    db.session.add_all(duals)
    db.session.commit()


def generate_week12_matchup():
    duals = [
        Schedule(id=177, week=12,team_1='Creekview Cowboys',team_2='Grapevine Falcons', completed=False),
        Schedule(id=184, week=12,team_1='Frisco Giants',team_2='Carter Riverside Panthers', completed=False),
        Schedule(id=190, week=12,team_1='Colony Buccaneers',team_2='Prosper Eagles', completed=False),
        Schedule(id=180, week=12,team_1='Liberty Saints',team_2='Heritage Coyotes', completed=False),
        Schedule(id=186, week=12,team_1='Canyon Randall Packers',team_2='Seguin Cardinals', completed=False),
        Schedule(id=192, week=12,team_1='Rockwall Vikings',team_2='Caprock Rams', completed=False), ### 192
        Schedule(id=183, week=12,team_1='Saginaw Seahawks',team_2='Humble Lions', completed=False),
        Schedule(id=189, week=12,team_1='Dumas 49ers',team_2='Woodland Bears', completed=False),
        Schedule(id=179, week=12,team_1='Katy Ravens',team_2='Azle Titans',completed=False),
        Schedule(id=187, week=12,team_1='A.M Consolidated Steelers',team_2='Argyle Texans', completed=False),
        Schedule(id=191, week=12,team_1='Boswell Jaguars',team_2='Cypress Browns', completed=False),
        Schedule(id=181, week=12,team_1='Chisholm Trail Colts',team_2='Wylie Bengals', completed=False),
        Schedule(id=185, week=12,team_1='Centennial Patriots',team_2='Nazareth Chargers', completed=False),
        Schedule(id=188, week=12,team_1='Arlington Bills',team_2='Wakeland Raiders', completed=False),
        Schedule(id=178, week=12,team_1='Allen Chiefs',team_2='College Station Jets', completed=False),
        Schedule(id=182, week=12,team_1='Haltom City Broncos',team_2='Lamar Dolphins', completed=False),
    ]
    db.session.add_all(duals)
    db.session.commit()

def generate_week13_matchup():
    duals = [
        Schedule(id=201, week=13,team_1='Creekview Cowboys',team_2='Carter Riverside Panthers', completed=False),
        Schedule(id=198, week=13,team_1='Frisco Giants',team_2='Grapevine Falcons', completed=False),
        Schedule(id=204, week=13,team_1='Colony Buccaneers',team_2='Heritage Coyotes', completed=False),
        Schedule(id=194, week=13,team_1='Liberty Saints',team_2='Prosper Eagles', completed=False),
        Schedule(id=206, week=13,team_1='Canyon Randall Packers',team_2='Caprock Rams', completed=False),
        Schedule(id=200, week=13,team_1='Rockwall Vikings',team_2='Seguin Cardinals', completed=False),
        Schedule(id=203, week=13,team_1='Saginaw Seahawks',team_2='Woodland Bears', completed=False),
        Schedule(id=196, week=13,team_1='Dumas 49ers',team_2='Humble Lions', completed=False),
        Schedule(id=208, week=13,team_1='Katy Ravens',team_2='Argyle Texans', completed=False), ### 208
        Schedule(id=193, week=13,team_1='A.M Consolidated Steelers',team_2='Azle Titans', completed=False),
        Schedule(id=199, week=13,team_1='Boswell Jaguars',team_2='Wylie Bengals', completed=False),
        Schedule(id=207, week=13,team_1='Chisholm Trail Colts',team_2='Cypress Browns', completed=False),
        Schedule(id=197, week=13,team_1='Centennial Patriots',team_2='Wakeland Raiders', completed=False),
        Schedule(id=205, week=13,team_1='Arlington Bills',team_2='Nazareth Chargers', completed=False),
        Schedule(id=195, week=13,team_1='Allen Chiefs',team_2='Lamar Dolphins', completed=False),
        Schedule(id=202, week=13,team_1='Haltom City Broncos',team_2='College Station Jets', completed=False),
    ]
    db.session.add_all(duals)
    db.session.commit()


def generate_week14_matchup():
    duals = [
        Schedule(id=209, week=14,team_1='Katy Ravens',team_2='Cypress Browns', completed=False),
        Schedule(id=219, week=14,team_1='A.M Consolidated Steelers',team_2='Wylie Bengals', completed=False),
        Schedule(id=223, week=14,team_1='Centennial Patriots',team_2='College Station Jets', completed=False),
        Schedule(id=214, week=14,team_1='Arlington Bills',team_2='Lamar Dolphins', completed=False),
        Schedule(id=218, week=14,team_1='Boswell Jaguars',team_2='Azle Titans', completed=False),
        Schedule(id=225, week=14,team_1='Chisholm Trail Colts',team_2='Argyle Texans', completed=False), ##225
        Schedule(id=211, week=14,team_1='Allen Chiefs',team_2='Nazareth Chargers', completed=False),
        Schedule(id=221, week=14,team_1='Haltom City Broncos',team_2='Wakeland Raiders', completed=False),
        Schedule(id=216, week=14,team_1='Canyon Randall Packers',team_2='Humble Lions', completed=False),
        Schedule(id=224, week=14,team_1='Rockwall Vikings',team_2='Woodland Bears', completed=False),
        Schedule(id=220, week=14,team_1='Creekview Cowboys',team_2='Prosper Eagles', completed=False),
        Schedule(id=210, week=14,team_1='Frisco Giants',team_2='Heritage Coyotes', completed=False),
        Schedule(id=215, week=14,team_1='Colony Buccaneers',team_2='Grapevine Falcons', completed=False),
        Schedule(id=217, week=14,team_1='Liberty Saints',team_2='Carter Riverside Panthers', completed=False),
        Schedule(id=213, week=14,team_1='Saginaw Seahawks',team_2='Seguin Cardinals', completed=False),
        Schedule(id=222, week=14,team_1='Dumas 49ers',team_2='Caprock Rams', completed=False),
    ]
    db.session.add_all(duals)
    db.session.commit()

def generate_week15_matchup():
    duals = [
        Schedule(id=227, week=15,team_1='Canyon Randall Packers',team_2='Creekview Cowboys', completed=False),
        Schedule(id=236, week=15,team_1='Rockwall Vikings',team_2='Frisco Giants', completed=False),
        Schedule(id=240, week=15,team_1='Humble Lions',team_2='Prosper Eagles', completed=False),
        Schedule(id=231, week=15,team_1='Woodland Bears',team_2='Heritage Coyotes', completed=False),
        Schedule(id=235, week=15,team_1='Saginaw Seahawks',team_2='Colony Buccaneers', completed=False),
        Schedule(id=238, week=15,team_1='Liberty Saints',team_2='Dumas 49ers', completed=False),
        Schedule(id=228, week=15,team_1='Seguin Cardinals',team_2='Grapevine Falcons', completed=False),
        Schedule(id=242, week=15,team_1='Caprock Rams',team_2='Carter Riverside Panthers', completed=False), ## 242
        Schedule(id=232, week=15,team_1='Centennial Patriots',team_2='Katy Ravens', completed=False),
        Schedule(id=241, week=15,team_1='A.M Consolidated Steelers',team_2='Arlington Bills', completed=False),
        Schedule(id=226, week=15,team_1='College Station Jets',team_2='Cypress Browns', completed=False),
        Schedule(id=237, week=15,team_1='Lamar Dolphins',team_2='Wylie Bengals', completed=False),
        Schedule(id=230, week=15,team_1='Allen Chiefs',team_2='Boswell Jaguars', completed=False),
        Schedule(id=239, week=15,team_1='Chisholm Trail Colts',team_2='Haltom City Broncos', completed=False),
        Schedule(id=234, week=15,team_1='Nazareth Chargers',team_2='Azle Titans', completed=False),
        Schedule(id=229, week=15,team_1='Wakeland Raiders',team_2='Argyle Texans', completed=False),
    ]
    db.session.add_all(duals)
    db.session.commit()

def generate_week16_matchup():
    duals = [
        Schedule(id=243, week=16,team_1='Katy Ravens',team_2='A.M Consolidated Steelers', completed=False),
        Schedule(id=237, week=16,team_1='Cypress Browns',team_2='Wylie Bengals', completed=False),
        Schedule(id=228, week=16,team_1='Centennial Patriots',team_2='Arlington Bills', completed=False),
        Schedule(id=235, week=16,team_1='College Station Jets',team_2='Lamar Dolphins', completed=False),
        Schedule(id=231, week=16,team_1='Boswell Jaguars',team_2='Chisholm Trail Colts', completed=False),
        Schedule(id=233, week=16,team_1='Azle Titans',team_2='Argyle Texans', completed=False),
        Schedule(id=245, week=16,team_1='Allen Chiefs',team_2='Haltom City Broncos', completed=False),
        Schedule(id=236, week=16,team_1='Nazareth Chargers',team_2='Wakeland Raiders', completed=False),
        Schedule(id=227, week=16,team_1='Canyon Randall Packers',team_2='Rockwall Vikings', completed=False),
        Schedule(id=234, week=16,team_1='Humble Lions',team_2='Woodland Bears', completed=False),
        Schedule(id=232, week=16,team_1='Creekview Cowboys',team_2='Frisco Giants', completed=False),
        Schedule(id=226, week=16,team_1='Prosper Eagles',team_2='Heritage Coyotes', completed=False),
        Schedule(id=229, week=16,team_1='Colony Buccaneers',team_2='Liberty Saints', completed=False),
        Schedule(id=244, week=16,team_1='Grapevine Falcons',team_2='Carter Riverside Panthers', completed=False),
        Schedule(id=238, week=16,team_1='Saginaw Seahawks',team_2='Dumas 49ers', completed=False),
        Schedule(id=230, week=16,team_1='Seguin Cardinals',team_2='Caprock Rams', completed=False),
    ]
    db.session.add_all(duals)
    db.session.commit()


def seed_all_schedule():
    generate_week1_matchup()
    generate_week2_matchup()
    generate_week3_matchup()
    generate_week4_matchup()
    generate_week5_matchup()
    generate_week6_matchup()
    generate_week7_matchup()
    generate_week8_matchup()
    generate_week9_matchup()
    generate_week10_matchup()
    generate_week11_matchup()
    generate_week12_matchup()
    generate_week13_matchup()
    generate_week14_matchup()
    generate_week15_matchup()
    generate_week16_matchup()


def undo_schedule():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.users RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM schedules"))

    db.session.commit()
