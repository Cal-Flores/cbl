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
    fighter_1 = Fighter(id=1,name='Tatsumitsu Wada', nickname='', prof_img='https://cdn.onefc.com/wp-content/uploads/2021/04/Wang_Shuo-avatar-500x345-1.png',body_img='', weight='125', team_name='Frisco Giants')
    fighter_2 = Fighter(id=2,name='Spencer Lee', nickname='', prof_img='../../../images/spencerl.png',body_img='', weight='125', team_name='Argyle Texans')
    fighter_3 = Fighter(id=3,name='Roman Vlasov', nickname='', prof_img='../../../images/romanv.png',body_img='', weight='125', team_name='Arlington Bills')
    fighter_4 = Fighter(id=4,name='Tagir Ulanbekov', nickname='', prof_img='https://dmxg5wxfqgb4u.cloudfront.net/2022-11/ULANBEKOV_TAGIR_11-05.png',body_img='', weight='125', team_name='Canyon Randall Packers')
    fighter_5 = Fighter(id=5,name='David Dvorak', nickname='', prof_img='https://dmxg5wxfqgb4u.cloudfront.net/2023-06/DVORAK_DAVID_06-10.png',body_img='', weight='125', team_name='Nazareth Chargers')
    fighter_7 = Fighter(id=7,name='Nurisam Sanayev', nickname='', prof_img='../../../images/nsanayev.png',body_img='', weight='125', team_name='Liberty Saints')
    fighter_6 = Fighter(id=6,name='Askar Askarov', nickname='', prof_img='https://dmxg5wxfqgb4u.cloudfront.net/2020-07/ASKAROV_ASKAR_09-21.png?WG2hBq4Mn3jykU2WDrJKgAI.zyMfjnTQ&itok=PmJwFRrn',body_img='', weight='125', team_name='Lamar Dolphins')
    fighter_8 = Fighter(id=8,name='Kai Kara-France', nickname='', prof_img='https://dmxg5wxfqgb4u.cloudfront.net/2021-12/d7530648-87b8-4a5b-b87e-4a2c61e57a8e_KARA-FRANCE_KAI_12-11.png?itok=Sg62WV_D',body_img='', weight='125', team_name='Colony Buccaneers')
    fighter_9 = Fighter(id=9,name='Brandon Moreno', nickname='', prof_img='https://dmxg5wxfqgb4u.cloudfront.net/styles/event_results_athlete_headshot/s3/2022-07/MORENO_BRANDON_07-30.png?itok=F4lW0PsJ',body_img='', weight='125', team_name='Haltom City Broncos')
    fighter_10 = Fighter(id=10,name='Adriano Moraes', nickname='', prof_img='https://cdn.onefc.com/wp-content/uploads/sites/4/2016/11/Adriano_Moraes-avatar-500x345-champion-2.png',body_img='', weight='125', team_name='Centennial Patriots')
    fighter_11 = Fighter(id=11,name='Alexandre Pantoja', nickname='', prof_img='https://dmxg5wxfqgb4u.cloudfront.net/2021-08/67251%252Fprofile-galery%252Fprofile-picture%252FPANTOJA_ALEXANDRE_08-21.png?itok=BpQa_Axd',body_img='', weight='125', team_name='Humble Lions')
    fighter_12 = Fighter(id=12,name='Thomas Gilman', nickname='', prof_img='../../../images/tgilman.png',body_img='', weight='125', team_name='Boswell Jaguars')
    fighter_13 = Fighter(id=13,name='Nick Suriano', nickname='', prof_img='../../../images/nsuriano.png',body_img='', weight='125', team_name='Carter Riverside Panthers')
    fighter_14 = Fighter(id=14,name='Yowlys Bonne', nickname='', prof_img='../../../images/ybonne.png',body_img='', weight='125', team_name='Woodland Bears')
    fighter_15 = Fighter(id=15,name='Alan Gomes', nickname='', prof_img='../../../images/allang.png',body_img='', weight='125', team_name='Azle Titans')
    fighter_16 = Fighter(id=16,name='Demetrious Johnson', nickname='Mighty Mouse', prof_img='https://dmxg5wxfqgb4u.cloudfront.net/image/fighter_images/Demitrious_Johnson/JOHNSON_DEMETRIOUS_BELT_LS.png?VersionId=ja07yc5FMt1dRehw6sAhh1HUnei8Shuf',body_img='', weight='125', team_name='College Station Jets')
    fighter_29 = Fighter(id=29,name='Kumar Ravi', nickname='', prof_img='../../../images/ravi.png',body_img='', weight='125', team_name='A.M Consolidated Steelers')
    fighter_96 = Fighter(id=96,name='Zaur Uguev', nickname='', prof_img='../../../images/uguev.png',body_img='', weight='125', team_name='Katy Ravens')
    fighter_97 = Fighter(id=97,name='Brandon Royval', nickname='', prof_img='https://dmxg5wxfqgb4u.cloudfront.net/2021-08/71607%252Fprofile-galery%252Fprofile-picture%252FROYVAL_BRANDON_08-21.png?itok=fV_xL7k_',body_img='', weight='125', team_name='Saginaw Seahawks')
    fighter_98 = Fighter(id=98,name='Jack Mueller', nickname='', prof_img='../../../images/jmueller.png',body_img='', weight='125', team_name='Creekview Cowboys')
    fighter_99 = Fighter(id=99,name='Yuki Takahashi', nickname='', prof_img='../../../images/yuki.png',body_img='', weight='125', team_name='Seguin Cardinals')
    fighter_100 = Fighter(id=100,name='Matheus Nicalau', nickname='', prof_img='https://rankingmma.com/wp-content/uploads/2017/06/NICOLAU_MATHEUS.png',body_img='', weight='125', team_name='Dumas 49ers')
    fighter_101 = Fighter(id=101,name='Greg Diakomihalis', nickname='', prof_img='../../../images/gdiak.png',body_img='', weight='125', team_name='Grapevine Falcons')
    fighter_102 = Fighter(id=102,name='Matt Schnell', nickname='', prof_img='https://dmxg5wxfqgb4u.cloudfront.net/2022-03/3f72d1fb-f5f9-426f-9655-68879e7e2695%252FSCHNELL_MATT_02-12.png',body_img='', weight='125', team_name='Chisholm Trail Colts')
    fighter_103 = Fighter(id=103,name='Patrick Mckee', nickname='', prof_img='../../../images/pmckee.png',body_img='', weight='125', team_name='Prosper Eagles')
    fighter_104 = Fighter(id=104,name='Vitali Arujau', nickname='', prof_img='https://res.cloudinary.com/usopc-prod/image/upload/ar_1.5,c_fill,g_faces,w_616/q_auto/f_auto/dpr_2.0/c_scale,w_400/v1/NGB%20Wrestling/Athlete%20Profiles/Vitali%20Arujau/vito-arujau-800x533?_a=BAJFJtWIA',body_img='', weight='125', team_name='Heritage Coyotes')
    fighter_105 = Fighter(id=105,name='Tim Elliot', nickname='', prof_img='https://dmxg5wxfqgb4u.cloudfront.net/2021-10/69388%252Fprofile-galery%252Fprofile-picture%252FELLIOTT_TIM_10-09.png?itok=7KhoVzis',body_img='', weight='125', team_name='Wakeland Raiders')
    fighter_106 = Fighter(id=106,name='Daton Fix', nickname='', prof_img='../../../images/datonf.png',body_img='', weight='125', team_name='Allen Chiefs')
    fighter_107 = Fighter(id=107,name='Patrick Glory', nickname='', prof_img='../../../images/patglory.png',body_img='', weight='125', team_name='Wylie Bengals')
    fighter_108 = Fighter(id=108,name='Cody Garbrandt', nickname='', prof_img='https://dmxg5wxfqgb4u.cloudfront.net/2023-03/GARBRANDT_CODY_03-05.png',body_img='', weight='125', team_name='Rockwall Vikings')
    fighter_109 = Fighter(id=109,name='Alex Perez', nickname='', prof_img='https://dmxg5wxfqgb4u.cloudfront.net/image/ufc-fighter-container/67217/profile-galery/profile-picture/PEREZ_ALEX.png?0vDQB9NlIC5rm1X4jjdGP3L4qaj1rZB3&itok=-KO6fF7R',body_img='', weight='125', team_name='Caprock Rams')
    fighter_110 = Fighter(id=110,name='Tenshin Nasakawa', nickname='', prof_img='../../../images/tenshin.png',body_img='', weight='125', team_name='Cypress Browns')
    #################### BANTAM ####################
    fighter_17 = Fighter(id=17,name='Yusup Saduliev', nickname='', prof_img='https://conandaily.files.wordpress.com/2020/12/yusup-saadulaev.png',body_img='', weight='133', team_name='Argyle Texans')
    fighter_18 = Fighter(id=18,name='Jose Aldo', nickname='', prof_img='https://dmxg5wxfqgb4u.cloudfront.net/2022-03/25c66698-f1f5-4a7d-8069-7e93d6de2fc3%252FALDO_JOSE_12-04.png',body_img='', weight='133', team_name='A.M Consolidated Steelers')
    fighter_19 = Fighter(id=19,name='Petr Yan', nickname='', prof_img='https://gossipbiography.com/wp-content/uploads/2020/12/Petr-Yan.png',body_img='', weight='133', team_name='Caprock Rams')
    fighter_20 = Fighter(id=20,name='Seth Gross', nickname='', prof_img='../../../images/sgross.png',body_img='', weight='133', team_name='Haltom City Broncos')
    fighter_21 = Fighter(id=21,name='Deiveson Figueiredo', nickname='', prof_img='https://dmxg5wxfqgb4u.cloudfront.net/2020-03/FIGUEIREDO_DEIVESON.png?VersionId=n5u8hh.CukSaDtuz54g_pNs70ak4MFx2',body_img='', weight='133', team_name='Allen Chiefs')
    fighter_22 = Fighter(id=22,name='Marcos Maidana', nickname='', body_img='',prof_img='../../../images/mmaidana.png', weight='133', team_name='Carter Riverside Panthers')
    fighter_23 = Fighter(id=23,name='Cory Sandhagen', nickname='', prof_img='https://dmxg5wxfqgb4u.cloudfront.net/2023-08/SANDHAGEN_CORY_08-05.png',body_img='', weight='133', team_name='Centennial Patriots')
    fighter_24 = Fighter(id=24,name='Aljamain Sterling', nickname='', prof_img='https://dmxg5wxfqgb4u.cloudfront.net/image/ufc-fighter-container/67275/profile-galery/profile-picture/STERLING_ALJAMAIN.png?VersionId=qTeHnBm.btBK8o1YU6Yxnw2w0EeX0uOc',body_img='', weight='133', team_name='Frisco Giants')
    fighter_25 = Fighter(id=25,name='Khasan Magomedsharipov', nickname='', prof_img='https://a.espncdn.com/combiner/i?img=/i/headshots/mma/players/full/4715264.png&w=350&h=254',body_img='', weight='133', team_name='Rockwall Vikings')
    fighter_26 = Fighter(id=26,name="Sean O'Malley", nickname='', prof_img='https://dmxg5wxfqgb4u.cloudfront.net/2023-08/OMALLEY_SEAN_BELTMOCK.png',body_img='', weight='133', team_name='Azle Titans')
    fighter_27 = Fighter(id=27,name='Roman Bravo-Young', nickname='', prof_img='../../../images/rby.png',body_img='', weight='133', team_name='Saginaw Seahawks')
    fighter_111 = Fighter(id=111,name='Jack Shore', nickname='', prof_img='https://dmxg5wxfqgb4u.cloudfront.net/2023-03/SHORE_JACK_03-18.png',body_img='', weight='133', team_name='Grapevine Falcons')
    fighter_112 = Fighter(id=112,name='Rahman Amouzdkhalil', nickname='', prof_img='../../../images/rahman.png',body_img='', weight='133', team_name='Seguin Cardinals')
    fighter_113 = Fighter(id=113,name='TJ Dillasaw', nickname='', prof_img='https://dmxg5wxfqgb4u.cloudfront.net/2022-10/DILLASHAW_TJ_10-22.png',body_img='', weight='133', team_name='Heritage Coyotes')
    fighter_114 = Fighter(id=114,name='Chito Vera', nickname='', prof_img='https://dmxg5wxfqgb4u.cloudfront.net/2023-08/VERA_MARLON_08-19.png',body_img='', weight='133', team_name='Liberty Saints')
    fighter_115 = Fighter(id=115,name='Dominick Cruz', nickname='', prof_img='https://dmxg5wxfqgb4u.cloudfront.net/2022-03/cdbd82b0-b482-4dd4-b768-8ffb55c4a5de%252FCRUZ_DOMINICK_12-11.png',body_img='', weight='133', team_name='Humble Lions')
    fighter_116 = Fighter(id=116,name='Umar Nurmagomedov', nickname='', prof_img='https://dmxg5wxfqgb4u.cloudfront.net/2023-01/NURMAGOMEDOV_UMAR_01-14.png',body_img='', weight='133', team_name='Dumas 49ers')
    fighter_117 = Fighter(id=117,name='Merab Dvalishvili', nickname='', prof_img='https://dmxg5wxfqgb4u.cloudfront.net/2023-03/DVALISHVILI_MERAB_03-11.png',body_img='', weight='133', team_name='College Station Jets')
    fighter_118 = Fighter(id=118,name='Adrian Yanez', nickname='', prof_img='https://dmxg5wxfqgb4u.cloudfront.net/2023-04/YANEZ_ADRIAN_04-08.png',body_img='', weight='133', team_name='Prosper Eagles')
    fighter_119 = Fighter(id=119,name='Coleman Scott', nickname='', prof_img='../../../images/cscott.png',body_img='', weight='133', team_name='Wylie Bengals')
    fighter_120 = Fighter(id=120,name='Stephan Micic', nickname='', prof_img='../../../images/stephm.png',body_img='', weight='133', team_name='Lamar Dolphins')
    fighter_121 = Fighter(id=121,name='Said Nurmagomedov', nickname='', prof_img='https://dmxg5wxfqgb4u.cloudfront.net/2023-03/NURMAGOMEDOV_SAID_03-11.png',body_img='', weight='133', team_name='Creekview Cowboys')
    fighter_122 = Fighter(id=122,name='Chinzo Machida', nickname='', prof_img='../../../images/cmachida.png',body_img='', weight='133', team_name='Canyon Randall Packers')
    fighter_123 = Fighter(id=123,name='Ricky Simon', nickname='', prof_img='https://dmxg5wxfqgb4u.cloudfront.net/image/ufc-fighter-container/69096/profile-galery/profile-picture/SIMON_RICKY.png?VersionId=eE9q1g_8i5Nd8tqGGSKwWKR67x63g0Zl',body_img='', weight='133', team_name='Cypress Browns')
    fighter_124 = Fighter(id=124,name='Bryce Meredith', nickname='', prof_img='../../../images/bmeredith.png',body_img='', weight='133', team_name='Wakeland Raiders')
    fighter_125 = Fighter(id=125,name='Rob Font', nickname='', prof_img='https://dmxg5wxfqgb4u.cloudfront.net/2023-08/FONT_ROB_08-05.png',body_img='', weight='133', team_name='Nazareth Chargers')
    fighter_126 = Fighter(id=126,name='Austin Desanto', nickname='', prof_img='../../../images/adesanto.png',body_img='', weight='133', team_name='Boswell Jaguars')
    fighter_127 = Fighter(id=127,name='Darion Caldwell', nickname='', prof_img='https://a.espncdn.com/combiner/i?img=/i/headshots/mma/players/full/2984782.png&w=350&h=254',body_img='', weight='133', team_name='Chisholm Trail Colts')
    fighter_128 = Fighter(id=128,name='Frankie Edgar', nickname='', prof_img='https://dmxg5wxfqgb4u.cloudfront.net/2021-11/67978%252Fprofile-galery%252Fprofile-picture%252FEDGAR_FRANKIE_11-06.png',body_img='', weight='133', team_name='Colony Buccaneers')
    fighter_129 = Fighter(id=129,name='Rei Higuchi', nickname='', prof_img='../../../images/rhiguchi.png',body_img='', weight='133', team_name='Arlington Bills')
    fighter_130 = Fighter(id=130,name='Takeya Mizugaki', nickname='', prof_img='https://dmxg5wxfqgb4u.cloudfront.net/2022-03/3db9b639-f10a-44be-ac60-8716e473f645%252FTakeyaMizugaki_Headshot151.png',body_img='', weight='133', team_name='Katy Ravens')
    fighter_131 = Fighter(id=131,name='Brad Katona', nickname='', prof_img='https://dmxg5wxfqgb4u.cloudfront.net/2023-08/KATONA_BRAD_08-19.png',body_img='', weight='133', team_name='Woodland Bears')
    ################### FEATHER #######################
    fighter_28 = Fighter(id=28,name='Alexander Volkanovski', nickname='', prof_img='https://dmxg5wxfqgb4u.cloudfront.net/2021-09/67233%252Fprofile-galery%252Fprofile-picture%252FVOLKANOVSKI_ALEXANDER_BELT_09-25.png?itok=7nsgFV4e',body_img='', weight='149', team_name='Dumas 49ers')
    fighter_30 = Fighter(id=30,name='Giga Chikadze', nickname='', prof_img='https://dmxg5wxfqgb4u.cloudfront.net/2023-08/CHIKADZE_GIGA_08_26.png',body_img='', weight='149', team_name='Chisholm Trail Colts')
    fighter_31 = Fighter(id=31,name='Bryce Mitchell', nickname='', prof_img='https://dmxg5wxfqgb4u.cloudfront.net/2023-09/MITCHELL_BRYCE_09-23.png',body_img='', weight='149', team_name='Creekview Cowboys')
    fighter_32 = Fighter(id=32,name='Max Holloway', nickname='', prof_img='https://dmxg5wxfqgb4u.cloudfront.net/2023-04/HOLLOWAY_MAX_04-15.png',body_img='', weight='149', team_name='A.M Consolidated Steelers')
    fighter_33 = Fighter(id=33,name='Yair Rodriguez', nickname='', prof_img='https://dmxg5wxfqgb4u.cloudfront.net/2023-02/RODRIGUEZ_YAIR_02-11.png',body_img='', weight='149', team_name='Carter Riverside Panthers')
    fighter_34 = Fighter(id=34,name='Yianni Diakomihalis', nickname='', prof_img='../../../images/ydiak.png',body_img='', weight='149', team_name='Heritage Coyotes')
    fighter_35 = Fighter(id=35,name='Ilia Topuria', nickname='', prof_img='https://dmxg5wxfqgb4u.cloudfront.net/2023-06/TOPURIA_ILIA_06-24.png',body_img='', weight='149', team_name='Azle Titans')
    fighter_36 = Fighter(id=36,name='Henry Cejudo', nickname='', prof_img='https://dmxg5wxfqgb4u.cloudfront.net/2023-05/CEJUDO_HENRY_05-06.png',body_img='', weight='149', team_name='Haltom City Broncos')
    fighter_37 = Fighter(id=37,name='Arnold Allen', nickname='', prof_img='https://dmxg5wxfqgb4u.cloudfront.net/2023-04/ALLEN_ARNOLD_04-15.png',body_img='', weight='149', team_name='Arlington Bills')
    fighter_38 = Fighter(id=38,name='Gadzimurad Rashidov', nickname='', prof_img='../../../images/gadzhi.png',body_img='', weight='149', team_name='College Station Jets')
    fighter_132 = Fighter(id=132,name='Max Askren', nickname='', prof_img='https://dmxg5wxfqgb4u.cloudfront.net/2023-05/HOOPER_CHASE_05-20.png',body_img='', weight='149', team_name='Colony Buccaneers')
    fighter_133 = Fighter(id=133,name='Movsar Evloev', nickname='', prof_img='https://dmxg5wxfqgb4u.cloudfront.net/2023-05/EVLOEV_MOVSAR_05-06.png',body_img='', weight='149', team_name='Frisco Giants')
    fighter_134 = Fighter(id=134,name='Herbert Burns', nickname='', prof_img='https://dmxg5wxfqgb4u.cloudfront.net/2022-07/BURNS_HERBERT_07-16.png',body_img='', weight='149', team_name='Liberty Saints')
    fighter_135 = Fighter(id=135,name='Dan Hooker', nickname='', prof_img='https://dmxg5wxfqgb4u.cloudfront.net/2023-07/HOOKER_DAN_07-08.png',body_img='', weight='149', team_name='Wylie Bengals')
    fighter_136 = Fighter(id=136,name='Shane Burgos', nickname='', prof_img='https://dmxg5wxfqgb4u.cloudfront.net/2022-07/BURGOS_SHANE_07-16.png',body_img='', weight='149', team_name='Boswell Jaguars')
    fighter_137 = Fighter(id=137,name='Brian Ortega', nickname='', prof_img='https://dmxg5wxfqgb4u.cloudfront.net/2022-07/ORTEGA_BRIAN_07-16.png',body_img='', weight='149', team_name='Humble Lions')
    fighter_138 = Fighter(id=138,name='Takuto Otoguro', nickname='', prof_img='../../../images/takuto.png',body_img='', weight='149', team_name='Seguin Cardinals')
    fighter_139 = Fighter(id=139,name='Haji Aliyev', nickname='', prof_img='../../../images/haliyev.png',body_img='', weight='149', team_name='Prosper Eagles')
    fighter_140 = Fighter(id=140,name='Nick Lee', nickname='', prof_img='https://res.cloudinary.com/usopc-prod/image/upload/ar_1.5,c_fill,g_faces,w_616/q_auto/f_auto/dpr_2.0/c_scale,w_400/v1/NGB%20Wrestling/Athlete%20Profiles/Nick%20Lee/800x533-template-update?_a=BAJFJtWIA',body_img='', weight='149', team_name='Canyon Randall Packers')
    fighter_141 = Fighter(id=141,name='Sodiq Yusuff', nickname='', prof_img='https://dmxg5wxfqgb4u.cloudfront.net/2022-09/YUSUFF_SODIQ_10-01.png',body_img='', weight='149', team_name='Centennial Patriots')
    fighter_142 = Fighter(id=142,name='Calvin Kattar', nickname='', prof_img='https://dmxg5wxfqgb4u.cloudfront.net/2022-06/6d4e6a94-5ec4-4f97-a08d-21cfb816f459%252FKATTAR_CALVIN_06-18.png',body_img='', weight='149', team_name='Saginaw Seahawks')
    fighter_143 = Fighter(id=143,name='Rashid Magomedov', nickname='', prof_img='https://rankingmma.com/wp-content/uploads/2017/06/MAGOMEDOV_RASHID.png',body_img='', weight='149', team_name='Katy Ravens')
    fighter_144 = Fighter(id=144,name='Luke Pletcher', nickname='', prof_img='../../../images/pletcher.png',body_img='', weight='149', team_name='Caprock Rams')
    fighter_145 = Fighter(id=145,name='Zain Retherford', nickname='', prof_img='https://res.cloudinary.com/usopc-prod/image/upload/ar_1.5,c_fill,g_faces,w_616/q_auto/f_auto/dpr_2.0/c_scale,w_400/v1/NGB%20Wrestling/Athlete%20Profiles/Zain%20Retherford/zain-retherford-800x533?_a=BAJFJtWIA',body_img='', weight='149', team_name='Rockwall Vikings')
    fighter_146 = Fighter(id=146,name='AJ Mckee', nickname='', prof_img='https://a.espncdn.com/i/headshots/mma/players/full/3821379.png',body_img='', weight='149', team_name='Allen Chiefs')
    fighter_147 = Fighter(id=147,name='Joey Mckenna', nickname='', prof_img='../../../images/joeym.png',body_img='', weight='149', team_name='Nazareth Chargers')
    fighter_148 = Fighter(id=148,name='Jaydin Eierman', nickname='', prof_img='../../../images/jeierman.png',body_img='', weight='149', team_name='Argyle Texans')
    fighter_149 = Fighter(id=149,name='Dean Heil', nickname='', prof_img='../../../images/deanh.png',body_img='', weight='149', team_name='Lamar Dolphins')
    fighter_150 = Fighter(id=150,name='Marlon Moraes', nickname='', prof_img='https://dmxg5wxfqgb4u.cloudfront.net/2021-09/68724%252Fprofile-galery%252Fprofile-picture%252FMORAES_MARLON_09-25.png',body_img='', weight='149', team_name='Wakeland Raiders')
    fighter_151 = Fighter(id=151,name='Zubaira Tukhugov', nickname='', prof_img='https://dmxg5wxfqgb4u.cloudfront.net/2023-02/TUKHUGOV_ZUBAIRA_02-11.png',body_img='', weight='149', team_name='Cypress Browns')
    fighter_152 = Fighter(id=152,name='Gray Bardock', nickname='', prof_img='https://dmxg5wxfqgb4u.cloudfront.net/image/fighter_images/Elias_Theodorou/THEODOROU_ELIAS.png?VersionId=f7AvgrpZdUZJ7nS3hNXs_DJk2rqGHRmK',body_img='', weight='149', team_name='Woodland Bears')
    fighter_153 = Fighter(id=153,name='Ismail Musukaev', nickname='', prof_img='../../../images/ismail.png',body_img='', weight='149', team_name='Grapevine Falcons')
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
    fighter_95 = Fighter(id=59,name='Arman Tsarukyan', nickname='', prof_img='https://dmxg5wxfqgb4u.cloudfront.net/styles/event_results_athlete_headshot/s3/2023-06/TSARUKYAN_ARMAN_06-17.png?itok=VAZ4GKsZ',body_img='', weight='157', team_name='A.M Consolidated Steelers')
    ####################### Welter ###########################
    fighter_49 = Fighter(id=49,name='Kamaru Usman', nickname='', prof_img='',body_img='', weight='174', team_name='Arlington Bills')
    fighter_50 = Fighter(id=50,name='Khamzat Chimaev', nickname='', prof_img='',body_img='', weight='174', team_name='Prosper Eagles')
    fighter_51 = Fighter(id=51,name='Canelo Alvarez', nickname='', prof_img='',body_img='', weight='174', team_name='Wylie Bengals')
    fighter_52 = Fighter(id=52,name='Kyle Dake', nickname='', prof_img='',body_img='', weight='174', team_name='Saginaw Seahawks')
    fighter_53 = Fighter(id=53,name='Mohamedkhabib Kadzimahamedov', nickname='', prof_img='',body_img='', weight='174', team_name='Haltom City Broncos')
    fighter_54 = Fighter(id=54,name='Leon Edwards', nickname='', prof_img='',body_img='', weight='174', team_name='Katy Ravens')
    fighter_55 = Fighter(id=55,name='Vicente Luque', nickname='', prof_img='',body_img='', weight='174', team_name='Rockwall Vikings')
    fighter_56 = Fighter(id=56,name='Colby Covington', nickname='', prof_img='',body_img='', weight='174', team_name='Allen Chiefs')
    fighter_57 = Fighter(id=57,name='Gilbert Burns', nickname='', prof_img='',body_img='', weight='174', team_name='Liberty Saints')
    fighter_58 = Fighter(id=58,name='Belal Mohammed', nickname='', prof_img='https://dmxg5wxfqgb4u.cloudfront.net/2023-05/MUHAMMAD_BELAL_05-06.png',body_img='', weight='174', team_name='A.M Consolidated Steelers')
    ######################## MIDDLE ############################
    fighter_59 = Fighter(id=59,name='Zander Emileanako', nickname='', prof_img='',body_img='', weight='185', team_name='Prosper Eagles')
    fighter_60 = Fighter(id=60,name='Bo Nickal', nickname='', prof_img='https://dmxg5wxfqgb4u.cloudfront.net/2023-07/NICKAL_BO_07-08.png',body_img='', weight='185', team_name='A.M Consolidated Steelers')
    fighter_61 = Fighter(id=61,name='David Taylor', nickname='', prof_img='',body_img='', weight='185', team_name='Haltom City Broncos')
    fighter_62 = Fighter(id=62,name='Andre Muniz', nickname='', prof_img='',body_img='', weight='185', team_name='Dumas 49ers')
    fighter_63 = Fighter(id=63,name='Alex Pereira', nickname='', prof_img='',body_img='', weight='185', team_name='Canyon Randall Packers')
    fighter_64 = Fighter(id=64,name='Hassan Yazdanicharati', nickname='', prof_img='',body_img='', weight='185', team_name='Wylie Bengals')
    fighter_65 = Fighter(id=65,name='Marvin Vettori', nickname='', prof_img='',body_img='', weight='185', team_name='Caprock Rams')
    fighter_66 = Fighter(id=66,name='Israel Adesanya', nickname='', prof_img='',body_img='', weight='185', team_name='Katy Ravens')
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
    fighter_82 = Fighter(id=82,name='Vagner Rocha', nickname='', prof_img='https://dmxg5wxfqgb4u.cloudfront.net/image/fighter_images/Vagner_Rocha/VagnerRocha_Headshot.png?VersionId=M0A7b5zWO1YUoUppJ6cgiKlAHR_BEKXz',body_img='', weight='205', team_name='A.M Consolidated Steelers')
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
    fighter_94 = Fighter(id=94,name='Mijain Lopez', nickname='', prof_img='../../../images/mijain.png',body_img='', weight='285', team_name='A.M Consolidated Steelers')



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
    fighter_93, fighter_94, fighter_95, fighter_96, fighter_97, fighter_98, fighter_99,
    fighter_100, fighter_101, fighter_102, fighter_103, fighter_104, fighter_105, fighter_106,
    fighter_107, fighter_108, fighter_109, fighter_110,    fighter_111, fighter_112, fighter_113,
    fighter_114,fighter_115, fighter_116, fighter_117, fighter_118,  fighter_119,  fighter_120, fighter_121,fighter_122,fighter_123, fighter_124,fighter_125, fighter_126,
    fighter_127, fighter_128, fighter_129, fighter_130, fighter_131,    fighter_131,fighter_132,fighter_133,fighter_134,fighter_135,fighter_136,fighter_137,fighter_138,fighter_139,fighter_140,fighter_141,fighter_142,fighter_143,fighter_144,fighter_145,fighter_146,fighter_147,fighter_148,fighter_149,fighter_150,fighter_151,fighter_152,fighter_153
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
