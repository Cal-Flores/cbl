from app.models import db, User, Fighter, environment, SCHEMA
from sqlalchemy.sql import text

def seed_fighters():
    # fighter_1 = Fighter(id=1,name='Charles Oliviera', nickname='Do Bronx', prof_img='',body_img='', weight='155', team_name='Grapevine Falcons')
    # fighter_2 = Fighter(id=2,name='Kamaru Usman', nickname='The Nigerian Nightmare', prof_img='',body_img='', weight='170',team_name='Arlington Bills')
    # fighter_3 = Fighter(id=3,name='Brandon Moreno', nickname='The Assasain Baby', prof_img='',body_img='', weight='125',team_name='Haltom City Broncos')
    # fighter_4 = Fighter(id=4,name='Alexander Volkanovski', nickname='The Great', prof_img='',body_img='', weight='145',team_name='Dumas 49ers')
    # fighter_5 = Fighter(id=5,name='Cody Sandhagen', nickname='The Sandman', prof_img='', body_img='', weight='135',team_name='Centennial Patriots')
    # fighter_6 = Fighter(id=6,name='Robert Whittaker', nickname='The Reaper', prof_img='', body_img='', weight='185',team_name='Rockwall Vikings')
    # fighter_7 = Fighter(id=7,name='Jan Blachowitz', nickname='', prof_img='', body_img='', weight='205',team_name='Seguin Cardinals')
    # fighter_8 = Fighter(id=8,name='Tai Tuivasa', nickname='', prof_img='', body_img='', weight='285',team_name='Creekview Cowboys')


    #################### FLYWEIGT ############
    fighter_1 = Fighter(id=1,name='Tatsumitsu Wada', nickname='', prof_img='',body_img='', weight='125', team_name='Frisco Giants')
    fighter_2 = Fighter(id=2,name='Spencer Lee', nickname='', prof_img='',body_img='', weight='125', team_name='Argyle Texans')
    fighter_3 = Fighter(id=3,name='Roman Vlasov', nickname='', prof_img='',body_img='', weight='125', team_name='Arlington Bills')
    fighter_4 = Fighter(id=4,name='Tagir Ulanbekov', nickname='', prof_img='',body_img='', weight='125', team_name='Canyon Randall Packers')
    fighter_5 = Fighter(id=5,name='David Dvorak', nickname='', prof_img='',body_img='', weight='125', team_name='Nazareth Chargers')
    fighter_7 = Fighter(id=7,name='Nurisam Sanayev', nickname='', prof_img='',body_img='', weight='125', team_name='Liberty Saints')
    fighter_6 = Fighter(id=6,name='Askar Askarov', nickname='', prof_img='',body_img='', weight='125', team_name='Lamar Dolphins')
    fighter_8 = Fighter(id=8,name='Kai Kara-France', nickname='', prof_img='',body_img='', weight='125', team_name='Colony Buccaneers')
    fighter_9 = Fighter(id=9,name='Brandon Moreno', nickname='', prof_img='',body_img='', weight='125', team_name='Haltom City Broncos')
    fighter_10 = Fighter(id=10,name='Adriano Moraes', nickname='', prof_img='',body_img='', weight='125', team_name='Centennial Patriots')
    fighter_11 = Fighter(id=11,name='Alexandre Pantoja', nickname='', prof_img='',body_img='', weight='125', team_name='Humble Lions')
    fighter_12 = Fighter(id=12,name='Thomas Gilman', nickname='', prof_img='',body_img='', weight='125', team_name='Boswell Jaguars')
    fighter_13 = Fighter(id=13,name='Nick Suriano', nickname='', prof_img='',body_img='', weight='125', team_name='Carter Riverside Panthers')
    fighter_14 = Fighter(id=14,name='Yowlys Bonne', nickname='', prof_img='',body_img='', weight='125', team_name='Woodland Bears')
    fighter_15 = Fighter(id=15,name='Alan Gomes', nickname='', prof_img='',body_img='', weight='125', team_name='Azle Titans')
    fighter_16 = Fighter(id=16,name='Demetrious Johnson', nickname='Mighty Mouse', prof_img='',body_img='', weight='125', team_name='College Station Jets')
    fighter_29 = Fighter(id=29,name='Kumar Ravi', nickname='', prof_img='',body_img='', weight='125', team_name='A.M Consolidated Steelers')
    #################### BANTAM ####################
    fighter_17 = Fighter(id=17,name='Yusup Saduliev', nickname='', prof_img='',body_img='', weight='135', team_name='Argyle Texan')
    fighter_18 = Fighter(id=18,name='Jose Aldo', nickname='', prof_img='',body_img='', weight='135', team_name='A.M Consolidated Steelers')
    fighter_19 = Fighter(id=19,name='Petr Yan', nickname='', prof_img='',body_img='', weight='135', team_name='Caprock Rams')
    fighter_20 = Fighter(id=20,name='Seth Gross', nickname='', prof_img='',body_img='', weight='135', team_name='Haltom City Broncos')
    fighter_21 = Fighter(id=21,name='Divedson Figuredo', nickname='', prof_img='',body_img='', weight='135', team_name='Allen Chiefs')
    fighter_22 = Fighter(id=22,name='Marcos Maidana', nickname='', prof_img='',body_img='', weight='135', team_name='Carter Riverside Panthers')
    fighter_23 = Fighter(id=23,name='Cory Sandhagen', nickname='', prof_img='',body_img='', weight='135', team_name='Centennial Patriots')
    fighter_24 = Fighter(id=24,name='Aljamain Sterling', nickname='', prof_img='',body_img='', weight='135', team_name='Frisco Giants')
    fighter_25 = Fighter(id=25,name='Khasan Magomedsharipov', nickname='', prof_img='',body_img='', weight='135', team_name='Rockwall Vikings')
    fighter_26 = Fighter(id=26,name="Sean O'Malley", nickname='', prof_img='',body_img='', weight='135', team_name='Azle Titans')
    fighter_27 = Fighter(id=27,name='Roman Bravo-Young', nickname='', prof_img='',body_img='', weight='135', team_name='Saginaw Seahawks')
    ################### FEATHER #######################
    fighter_28 = Fighter(id=28,name='Alexander Volkanovsky', nickname='', prof_img='',body_img='', weight='149', team_name='Dumas 49ers')
    fighter_30 = Fighter(id=30,name='Giga Chikadze', nickname='', prof_img='',body_img='', weight='149', team_name='Chisholm Trail Colts')
    fighter_31 = Fighter(id=31,name='Bryce Mitchell', nickname='', prof_img='',body_img='', weight='149', team_name='Creekview Cowboys')
    fighter_32 = Fighter(id=32,name='Max Holloway', nickname='', prof_img='',body_img='', weight='149', team_name='A.M Consolidated Steelers')
    fighter_33 = Fighter(id=33,name='Yair Rodriguez', nickname='', prof_img='',body_img='', weight='149', team_name='Carter Riverside Panthers')
    fighter_34 = Fighter(id=34,name='Yianni Diakomihalis', nickname='', prof_img='',body_img='', weight='149', team_name='Heritage Coyotes')
    fighter_35 = Fighter(id=35,name='Ilia Topuria', nickname='', prof_img='',body_img='', weight='149', team_name='Azle Titans')
    fighter_36 = Fighter(id=36,name='Henry Cejudo', nickname='', prof_img='',body_img='', weight='149', team_name='Haltom City Broncos')
    fighter_37 = Fighter(id=37,name='Arnold Allen', nickname='', prof_img='',body_img='', weight='149', team_name='Arlington Bills')
    fighter_38 = Fighter(id=38,name='Gadzimurad Rashidov', nickname='', prof_img='',body_img='', weight='149', team_name='College Station Jets')
    ###################### LIGHT #############################
    fighter_39 = Fighter(id=39,name='Charles Oliviera', nickname='', prof_img='',body_img='', weight='157', team_name='Grapevine Falcons')
    fighter_40 = Fighter(id=40,name='Khabib Nurmagomedov', nickname='', prof_img='',body_img='', weight='157', team_name='College Station Jets')
    fighter_41 = Fighter(id=41,name='Islam Makachev', nickname='', prof_img='',body_img='', weight='157', team_name='Canyon Randall Packers')
    fighter_42 = Fighter(id=42,name='Jordan Burroughs', nickname='', prof_img='',body_img='', weight='157', team_name='Colony Buccaneers')
    fighter_43 = Fighter(id=43,name='Georges St.Pierre', nickname='', prof_img='',body_img='', weight='157', team_name='Dumas 49ers')
    fighter_44 = Fighter(id=44,name='Michael Chandler', nickname='', prof_img='',body_img='', weight='157', team_name='Argyle Texans')
    fighter_45 = Fighter(id=45,name='Dustin Poirier', nickname='', prof_img='',body_img='', weight='157', team_name='Creekview Cowboys')
    fighter_46 = Fighter(id=46,name='Mateusz Gamrot', nickname='', prof_img='',body_img='', weight='157', team_name='Prosper Eagles')
    fighter_47 = Fighter(id=47,name='Rafael Fizziev', nickname='', prof_img='',body_img='', weight='157', team_name='Liberty Saints')
    fighter_48 = Fighter(id=48,name='Beneil Dariush', nickname='', prof_img='',body_img='', weight='157', team_name='Nazareth Chargers')
    fighter_95 = Fighter(id=59,name='Arman Tsarukyan', nickname='', prof_img='',body_img='', weight='157', team_name='A.M Consolidated Steelers')
    ####################### Welter ###########################
    fighter_49 = Fighter(id=49,name='Kamaru Usman', nickname='', prof_img='',body_img='', weight='174', team_name='Arlington Bills')
    fighter_50 = Fighter(id=50,name='Khamzat Chimaev', nickname='', prof_img='',body_img='', weight='174', team_name='Prosper Eagles')
    fighter_51 = Fighter(id=51,name='Canelo Alvarez', nickname='', prof_img='',body_img='', weight='174', team_name='Wylie Bengals')
    fighter_52 = Fighter(id=52,name='Kyle Dake', nickname='', prof_img='',body_img='', weight='174', team_name='Saginaw Seahawks')
    fighter_53 = Fighter(id=53,name='Mohamedkhabib Kadzimahamedov', nickname='', prof_img='',body_img='', weight='174', team_name='Haltom City Broncos')
    fighter_54 = Fighter(id=54,name='Leon Edwards', nickname='', prof_img='',body_img='', weight='174', team_name='Katy Raven')
    fighter_55 = Fighter(id=55,name='Vicente Luque', nickname='', prof_img='',body_img='', weight='174', team_name='Rockwall Vikings')
    fighter_56 = Fighter(id=56,name='Colby Covington', nickname='', prof_img='',body_img='', weight='174', team_name='Allen Chiefs')
    fighter_57 = Fighter(id=57,name='Gilber Burns', nickname='', prof_img='',body_img='', weight='174', team_name='Liberty Saints')
    fighter_58 = Fighter(id=58,name='Belal Mohammed', nickname='', prof_img='',body_img='', weight='174', team_name='A.M Consolidated Steelers')
    ######################## MIDDLE ############################
    fighter_59 = Fighter(id=59,name='Zander Emileanako', nickname='', prof_img='',body_img='', weight='185', team_name='Prosper Eagles')
    fighter_60 = Fighter(id=60,name='Bo Nickal', nickname='', prof_img='',body_img='', weight='185', team_name='A.M Consolidated Steelers')
    fighter_61 = Fighter(id=61,name='David Taylor', nickname='', prof_img='',body_img='', weight='185', team_name='Haltom City Broncos')
    fighter_62 = Fighter(id=62,name='Andre Muniz', nickname='', prof_img='',body_img='', weight='185', team_name='Dumas 49ers')
    fighter_63 = Fighter(id=63,name='Alex Pieriera', nickname='', prof_img='',body_img='', weight='185', team_name='Canyon Randall Packers')
    fighter_64 = Fighter(id=64,name='Hassan Yazdanicharati', nickname='', prof_img='',body_img='', weight='185', team_name='Wylie Bengals')
    fighter_65 = Fighter(id=65,name='Marvin Vettori', nickname='', prof_img='',body_img='', weight='185', team_name='Caprock Rams')
    fighter_66 = Fighter(id=66,name='Isreal Adesanya', nickname='', prof_img='',body_img='', weight='185', team_name='Katy Ravens')
    fighter_67 = Fighter(id=67,name='Kenan Cornelius', nickname='', prof_img='',body_img='', weight='185', team_name='Allen Chiefs')
    fighter_68 = Fighter(id=68,name='Robert Whittaker', nickname='', prof_img='',body_img='', weight='185', team_name='Rockwall Vikings')
    fighter_69 = Fighter(id=69,name='Makmud Muradov', nickname='', prof_img='',body_img='', weight='185', team_name='Seguin Cardinals')
    ########################## LIGHT HEAVY #######################
    fighter_70 = Fighter(id=70,name='Jon Jones', nickname='', prof_img='',body_img='', weight='205', team_name='Boswell Jaguars')
    fighter_71 = Fighter(id=71,name='Abdulrashid Saduliev', nickname='', prof_img='',body_img='', weight='205', team_name='College Station Jets')
    fighter_72 = Fighter(id=72,name='Jiri Prochazka', nickname='', prof_img='',body_img='', weight='205', team_name='Saginaw Seahawks')
    fighter_73 = Fighter(id=73,name='Vadim Nemkov', nickname='', prof_img='',body_img='', weight='205', team_name='Katy Ravens')
    fighter_74 = Fighter(id=74,name='Jack Dempsy', nickname='', prof_img='',body_img='', weight='205', team_name='Lamar Dolphins')
    fighter_75 = Fighter(id=75,name='Glover Teixeira', nickname='', prof_img='',body_img='', weight='205', team_name='Humble Lions')
    fighter_76 = Fighter(id=76,name='Paul Craig', nickname='', prof_img='',body_img='', weight='205', team_name='Colony Buccaneers')
    fighter_77 = Fighter(id=77,name='Khalil Roundtree', nickname='', prof_img='',body_img='', weight='205', team_name='Nazareth Chargers')
    fighter_78 = Fighter(id=78,name='Gordan Ryan', nickname='', prof_img='',body_img='', weight='205', team_name='Cypress Browns')
    fighter_79 = Fighter(id=79,name='Dae un Jung', nickname='', prof_img='',body_img='', weight='205', team_name='Frisco Giants')
    fighter_80 = Fighter(id=80,name='Mohamed Mohamadian', nickname='', prof_img='',body_img='', weight='205', team_name='Azle Titans')
    fighter_81 = Fighter(id=81,name='Kyle Snyder', nickname='', prof_img='',body_img='', weight='205', team_name='Rockwall Vikings')
    fighter_82 = Fighter(id=82,name='Vagner Rocha', nickname='', prof_img='',body_img='', weight='205', team_name='A.M Consolidated Steelers')
    ############################# HEAVY WEIGHT ########################
    fighter_83 = Fighter(id=83,name='Fedor Emileanako', nickname='', prof_img='',body_img='', weight='285', team_name='Cypress Browns')
    fighter_84 = Fighter(id=84,name='Mohamed Ali', nickname='', prof_img='',body_img='', weight='285', team_name='Rockwall Vikings')
    fighter_85 = Fighter(id=85,name='Francis Ngannou', nickname='', prof_img='',body_img='', weight='285', team_name='Wakeland Raiders')
    fighter_86 = Fighter(id=86,name='Deonte Wilder', nickname='', prof_img='',body_img='', weight='285', team_name='Caprock Rams')
    fighter_87 = Fighter(id=87,name='Gable Steveson', nickname='', prof_img='',body_img='', weight='285', team_name='Saginaw Seahawks')
    fighter_88 = Fighter(id=88,name='Amir Aliakbari', nickname='', prof_img='',body_img='', weight='285', team_name='Chisholm Trail Colts')
    fighter_89 = Fighter(id=89,name='Tom Aspinal', nickname='', prof_img='',body_img='', weight='285', team_name='Frisco Giants')
    fighter_90 = Fighter(id=90,name='Kenyan Duarte', nickname='', prof_img='',body_img='', weight='285', team_name='Lamar Dolphins')
    fighter_91 = Fighter(id=91,name='Ciryl Gane', nickname='', prof_img='',body_img='', weight='285', team_name='Colonu Buccaneers')
    fighter_92 = Fighter(id=92,name='Greg Kerkvliet', nickname='', prof_img='',body_img='', weight='285', team_name='Creekview Cowboys')
    fighter_93 = Fighter(id=93,name='Sergei Pavlovich', nickname='', prof_img='',body_img='', weight='285', team_name='Wylie Bengals')
    fighter_94 = Fighter(id=94,name='Mijan Lopez', nickname='', prof_img='',body_img='', weight='285', team_name='A.M Consolidated Steelers')



    seeds = [
    fighter_1, fighter_2, fighter_3, fighter_4, fighter_5, fighter_6, fighter_7, fighter_8,
    fighter_9, fighter_10, fighter_11, fighter_12, fighter_13, fighter_14, fighter_15,
    fighter_16, fighter_17, fighter_18, fighter_19, fighter_20, fighter_21, fighter_22,
    fighter_23, fighter_24, fighter_25, fighter_26, fighter_27, fighter_28, fighter_29,
    fighter_30, fighter_31, fighter_32, fighter_33, fighter_34, fighter_35, fighter_36,
    fighter_37, fighter_38, fighter_39, fighter_40, fighter_41, fighter_42, fighter_43,
    fighter_44, fighter_45, fighter_46, fighter_47, fighter_48, fighter_49, fighter_50,
    fighter_51, fighter_52, fighter_53, fighter_54, fighter_55, fighter_56, fighter_57,
    fighter_58, fighter_59, fighter_60, fighter_61, fighter_62, fighter_63, fighter_64,
    fighter_65, fighter_66, fighter_67, fighter_68, fighter_69, fighter_70, fighter_71,
    fighter_72, fighter_73, fighter_74, fighter_75, fighter_76, fighter_77, fighter_78,
    fighter_79, fighter_80, fighter_81, fighter_82, fighter_83, fighter_84, fighter_85,
    fighter_86, fighter_87, fighter_88, fighter_89, fighter_90, fighter_91, fighter_92,
    fighter_93, fighter_94, fighter_95
]

    #seeds = [f"fighter_{i}" for i in range(1, 51)]

    for seed in seeds:
        db.session.add(seed)
        db.session.commit()

def undo_fighters():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.users RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM fighters"))

    db.session.commit()
