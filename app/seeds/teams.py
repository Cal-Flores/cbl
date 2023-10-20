from app.models import db, User, Fighter, Team, Tournament, environment, SCHEMA
from sqlalchemy.sql import text

def seed_teams():

    team_1 = Team(id=1,name='Centennial Patriots', logo_img='https://res.cloudinary.com/nflleague/image/private/f_auto/league/moyfxx3dq5pio4aiftnc', background_img='https://res.cloudinary.com/nflleague/image/private/f_auto/league/slea5gcxabohzknqnexo',conf='AFC', divison='East')
    team_2 = Team(id=2,name='Katy Ravens', logo_img='https://res.cloudinary.com/nflleague/image/private/f_auto/league/ucsdijmddsqcj1i9tddd', background_img='https://res.cloudinary.com/nflleague/image/private/f_auto/league/o2k317ev82s6pa26dos7',conf='AFC', divison='North')
    team_3 = Team(id=3,name='Rockwall Vikings', logo_img='https://res.cloudinary.com/nflleague/image/private/f_auto/league/teguylrnqqmfcwxvcmmz', background_img='https://res.cloudinary.com/nflleague/image/private/f_auto/league/fnmak0n2pitv59qqmaen',conf='NFC', divison='North')
    team_4 = Team(id=4,name='Azle Titans', logo_img='https://static.www.nfl.com/image/private/f_auto/league/pln44vuzugjgipyidsre', background_img='https://static.www.nfl.com/image/private/f_auto/league/pctgb2f0u7z0oiwpaci3',conf='AFC', divison='South')
    team_5 = Team(id=5,name='Heritage Coyotes', logo_img='https://s3-us-west-2.amazonaws.com/sportshub2-uploads-prod/files/sites/2008/2018/01/16215212/frisco-heritage-clear-1.png', background_img='https://static.www.nfl.com/image/private/f_auto/league/kajwfzxaiqkjvgxozpat',conf='NFC', divison='East')
    team_6 = Team(id=6,name='Wakeland Raiders', logo_img='https://static.www.nfl.com/image/private/f_auto/league/gzcojbzcyjgubgyb6xf2', background_img='https://static.www.nfl.com/image/private/f_auto/league/rthdytrwns8g5aed2uou',conf='AFC', divison='West')
    team_7 = Team(id=7,name='Seguin Cardinals', logo_img='https://static.www.nfl.com/image/private/f_auto/league/u9fltoslqdsyao8cpm0k', background_img='https://static.www.nfl.com/image/private/f_auto/league/zglirxlttuukonnz1il0',conf='NFC', divison='West')
    team_8 = Team(id=8,name='Liberty Saints', logo_img='https://static.www.nfl.com/image/private/f_auto/league/grhjkahghjkk17v43hdx', background_img='https://static.www.nfl.com/image/private/f_auto/league/qk0qesy5im61qccr5vp0',conf='NFC', divison='South')
    team_9 = Team(id=9,name='Grapevine Falcons', logo_img='https://static.www.nfl.com/image/private/f_auto/league/d8m7hzpsbrl6pnqht8op', background_img='https://static.www.nfl.com/image/private/f_auto/league/dgksdhs7zhmrioliyq9c',conf='NFC', divison='South')
    team_10 = Team(id=10,name='A.M Consolidated Steelers', logo_img='https://res.cloudinary.com/nflleague/image/private/f_auto/league/xujg9t3t4u5nmjgr54wx', background_img='https://res.cloudinary.com/nflleague/image/private/f_auto/league/s2ugk74phksrnbla46e7',conf='AFC', divison='West')
    team_11 = Team(id=11,name='Chisholm Trail Colts', logo_img='https://static.www.nfl.com/image/private/f_auto/league/ketwqeuschqzjsllbid5', background_img='https://static.www.nfl.com/image/private/f_auto/league/q1v6xhz44symvucjoxym',conf='AFC', divison='South')
    team_12 = Team(id=12,name='Caprock Rams', logo_img='https://static.www.nfl.com/image/private/f_auto/league/ayvwcmluj2ohkdlbiegi', background_img='https://static.www.nfl.com/image/private/f_auto/league/eo223qd5mlxrna3bbdiv',conf='NFC', divison='West')
    team_13 = Team(id=13,name='Creekview Cowboys', logo_img='https://static.www.nfl.com/image/private/f_auto/league/ieid8hoygzdlmzo0tnf6', background_img='https://static.www.nfl.com/image/private/f_auto/league/q7qakjbkb5wt7q943epi',conf='NFC', divison='East')
    team_15 = Team(id=15,name='Allen Chiefs', logo_img='https://res.cloudinary.com/nflleague/image/private/f_auto/league/ujshjqvmnxce8m4obmvs', background_img='https://res.cloudinary.com/nflleague/image/private/f_auto/league/ginftk4rv6gflay6mwur',conf='AFC', divison='West')
    team_14 = Team(id=14,name='Prosper Eagles', logo_img='https://res.cloudinary.com/nflleague/image/private/f_auto/league/puhrqgj71gobgdkdo6uq', background_img='https://res.cloudinary.com/nflleague/image/private/f_auto/league/p8xl6x8jfe3acs71jtit',conf='NFC', divison='East')
    team_16 = Team(id=16,name='Dumas 49ers', logo_img='https://res.cloudinary.com/nflleague/image/private/f_auto/league/dxibuyxbk0b9ua5ih9hn', background_img='https://res.cloudinary.com/nflleague/image/private/f_auto/league/aedv7exzsect9be58i0h',conf='NFC', divison='West')
    team_17 = Team(id=17,name='Canyon Randall Packers', logo_img='https://res.cloudinary.com/nflleague/image/private/f_auto/league/gppfvr7n8gljgjaqux2x', background_img='https://res.cloudinary.com/nflleague/image/private/f_auto/league/nn9yhffph5ty4qj2gqwu',conf='NFC', divison='North')
    team_18 = Team(id=18,name='College Station Jets', logo_img='https://static.www.nfl.com/image/private/f_auto/league/ekijosiae96gektbo4iw', background_img='https://static.www.nfl.com/image/private/f_auto/league/pvenefwq5pl3xxql9ez6',conf='AFC', divison='East')
    team_19 = Team(id=19,name='Boswell Jaguars', logo_img='https://res.cloudinary.com/nflleague/image/private/f_auto/league/qycbib6ivrm9dqaexryk', background_img='https://res.cloudinary.com/nflleague/image/private/f_auto/league/wok03vphgjx4knlyggx4',conf='AFC', divison='South')
    team_20 = Team(id=20,name='Cypress Browns', logo_img='https://static.www.nfl.com/image/private/f_auto/league/fgbn8acp4opvyxk13dcy', background_img='https://static.www.nfl.com/image/private/f_auto/league/skdxhpn1dmksuyrtwc7q',conf='AFC', divison='North')
    team_21 = Team(id=21,name='Frisco Giants', logo_img='https://res.cloudinary.com/nflleague/image/private/f_auto/league/t6mhdmgizi6qhndh8b9p', background_img='https://res.cloudinary.com/nflleague/image/private/f_auto/league/i94f24mjvgoc64hnqw3o',conf='NFC', divison='East')
    team_22 = Team(id=22,name='Lamar Dolphins', logo_img='https://res.cloudinary.com/nflleague/image/private/f_auto/league/lits6p8ycthy9to70bnt', background_img='https://res.cloudinary.com/nflleague/image/private/f_auto/league/xfxniandqn2wglltlxgm',conf='AFC', divison='East')
    team_23 = Team(id=23,name='Colony Buccaneers', logo_img='https://static.www.nfl.com/image/private/f_auto/league/v8uqiualryypwqgvwcih', background_img='https://static.www.nfl.com/image/private/f_auto/league/odiwi0h6uplawxy54sqc',conf='NFC', divison='South')
    team_24 = Team(id=24,name='Carter Riverside Panthers', logo_img='https://static.www.nfl.com/image/private/f_auto/league/ervfzgrqdpnc7lh5gqwq', background_img='https://static.www.nfl.com/image/private/f_auto/league/eyotndxveoeyibcbag5k',conf='NFC', divison='South')
    team_25 = Team(id=25,name='Nazareth Chargers', logo_img='https://static.www.nfl.com/image/private/f_auto/league/dhfidtn8jrumakbogeu4', background_img='https://static.www.nfl.com/image/private/f_auto/league/mkla4gj5w7882z6q0ywz',conf='AFC', divison='West')
    team_26 = Team(id=26,name='Haltom City Broncos', logo_img='https://res.cloudinary.com/nflleague/image/private/f_auto/league/t0p7m5cjdjy18rnzzqbx', background_img='https://res.cloudinary.com/nflleague/image/private/f_auto/league/zclpmokppqisomcdnnsh',conf='AFC', divison='West')
    team_27 = Team(id=27,name='Arlington Bills', logo_img='https://res.cloudinary.com/nflleague/image/private/f_auto/league/giphcy6ie9mxbnldntsf', background_img='https://res.cloudinary.com/nflleague/image/private/f_auto/league/kujtrvt65vrfbzvlp9p7',conf='AFC', divison='East')
    team_28 = Team(id=28,name='Woodland Bears', logo_img='https://static.www.nfl.com/image/private/f_auto/league/ijrplti0kmzsyoaikhv1', background_img='https://static.www.nfl.com/image/private/f_auto/league/egkztdkxkhpio4a3unxg',conf='NFC', divison='North')
    team_29 = Team(id=29,name='Humble Lions', logo_img='https://res.cloudinary.com/nflleague/image/private/f_auto/league/ocvxwnapdvwevupe4tpr', background_img='https://res.cloudinary.com/nflleague/image/private/f_auto/league/dlyxxmgt52d7anojsknk',conf='NFC', divison='North')
    team_30 = Team(id=30,name='Wylie Bengals', logo_img='https://res.cloudinary.com/nflleague/image/private/f_auto/league/okxpteoliyayufypqalq', background_img='https://res.cloudinary.com/nflleague/image/private/f_auto/league/maacoshfmktzddy1ob56',conf='AFC', divison='North')
    team_31 = Team(id=31,name='Saginaw Seahawks', logo_img='https://res.cloudinary.com/nflleague/image/private/f_auto/league/gcytzwpjdzbpwnwxincg', background_img='https://res.cloudinary.com/nflleague/image/private/f_auto/league/yfmuzipdfeduwgu4kfta',conf='NFC', divison='West')
    team_32 = Team(id=32,name='Argyle Texans', logo_img='https://static.www.nfl.com/image/private/f_auto/league/bpx88i8nw4nnabuq0oob', background_img='https://static.www.nfl.com/image/private/f_auto/league/fwylmmv0iz3dpwx9mcwj',conf='AFC', divison='South')


    teams = [team_1, team_2, team_3, team_4, team_5, team_6, team_7, team_8, team_9, team_10, team_11, team_12, team_13, team_14, team_15, team_16, team_17, team_18, team_19, team_20, team_21, team_22, team_23, team_24, team_25, team_26, team_27, team_28, team_29, team_30, team_31, team_32]

    for team in teams:
        db.session.add(team)
        db.session.commit()



def undo_teams():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.users RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM teams"))

    db.session.commit()
