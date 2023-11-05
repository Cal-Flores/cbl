from app.models import db, Medal, environment, SCHEMA
from sqlalchemy.sql import text

def seed_medals():
    #################################2016#########################################
    medal_1 = Medal(id=1,fighter='Demetrious Johnson',place='Champion',year='2016')
    medal_2 = Medal(id=2,fighter='John Lineker',place='Runner-Up',year='2016')
    medal_3 = Medal(id=3,fighter='Kyoji Horiguchi',place='3rd',year='2016')
    medal_4 = Medal(id=4,fighter='John Dodson',place='4th',year='2016')
    medal_5 = Medal(id=5,fighter='Henry Cejudo',place='5th',year='2016')
    medal_6 = Medal(id=6,fighter='Dustin Ortiz',place='6th',year='2016')
    medal_7 = Medal(id=7,fighter='Norifumi Yammamoto',place='7th',year='2016')
    medal_8 = Medal(id=8,fighter='Zach Makovsky',place='',year='')
    medal_9 = Medal(id=9,fighter='TJ Dillasaw',place='Champion',year='2016')
    medal_10 = Medal(id=10,fighter='Dominick Cruz',place='Runner-Up',year='2016')
    medal_11 = Medal(id=11,fighter='Renan Barao',place='3rd',year='2016')
    medal_12 = Medal(id=12,fighter='Urijah Faber',place='4th',year='2016')
    medal_13 = Medal(id=13,fighter='George Roop',place='5th',year='2016')
    medal_14 = Medal(id=14,fighter='Takeya Mizugaki',place='6th',year='2016')
    medal_15 = Medal(id=15,fighter='Raphael Assuncao',place='7th',year='2016')
    medal_16 = Medal(id=16,fighter='Mitch Gagnon',place='8th',year='2016')
    medal_17 = Medal(id=17,fighter='Jose Aldo',place='Champion',year='2016')
    medal_18 = Medal(id=18,fighter='Mike Brown',place='Runner-Up',year='2016')
    medal_19 = Medal(id=19,fighter='Conor Mcgregor',place='3rd',year='2016')
    medal_20 = Medal(id=20,fighter='Chad Mendes',place='4th',year='2016')
    medal_21 = Medal(id=21,fighter='Erick Koch',place='5th',year='2016')
    medal_22 = Medal(id=22,fighter='Daniel Strauss',place='6th',year='2016')
    medal_23 = Medal(id=23,fighter='Hatsu Hioki',place='7th',year='2016')
    medal_24 = Medal(id=24,fighter='Mark Hommonick',place='8th',year='2016')
    medal_25 = Medal(id=25,fighter='Khabib Nurmagomedov',place='Champion',year='2016')
    medal_26 = Medal(id=26,fighter='Rafael Dos Anjos',place='Runner-Up',year='2016')
    medal_27 = Medal(id=27,fighter='Anthony Pettis',place='3rd',year='2016')
    medal_28 = Medal(id=28,fighter='Benson Henderson',place='4th',year='2016')
    medal_29 = Medal(id=29,fighter='Will Brooks',place='5th',year='2016')
    medal_30 = Medal(id=30,fighter='Donald Cerrone',place='6th',year='2016')
    medal_31 = Medal(id=31,fighter='Takenori Gomi',place='7th',year='2016')
    medal_32 = Medal(id=32,fighter='Gilbert Melendez',place='8th',year='2016')
    medal_33 = Medal(id=33,fighter='Johny Hendricks',place='Champion',year='2016')
    medal_34 = Medal(id=34,fighter='Robbie Lawler',place='Runner-Up',year='2016')
    medal_35 = Medal(id=35,fighter='Karo Parisyan',place='3rd',year='2016')
    medal_36 = Medal(id=36,fighter='Georges St.Pierre',place='4th',year='2016')
    medal_37 = Medal(id=37,fighter='Carlos Condit',place='5th',year='2016')
    medal_38 = Medal(id=38,fighter='Hector Lombard',place='6th',year='2016')
    medal_39 = Medal(id=39,fighter='Demian Maia',place='7th',year='2016')
    medal_40 = Medal(id=40,fighter='Ben Askren',place='8th',year='2016')
    medal_41 = Medal(id=41,fighter='Chris Weidman',place='Champion',year='2016')
    medal_42 = Medal(id=42,fighter='Lyoto Machida',place='Runner-Up',year='2016')
    medal_43 = Medal(id=43,fighter='Ronaldo Souza',place='3rd',year='2016')
    medal_44 = Medal(id=44,fighter='Mahmed Khalidov',place='4th',year='2016')
    medal_45 = Medal(id=45,fighter='Dan Henderson',place='5th',year='2016')
    medal_46 = Medal(id=46,fighter='Luke Rockhold',place='6th',year='2016')
    medal_47 = Medal(id=47,fighter='Yoel Romero',place='7th',year='2016')
    medal_48 = Medal(id=48,fighter='Anderson Silva',place='8th',year='2016')
    medal_49 = Medal(id=49,fighter='Ryan Bader',place='Champion',year='2016')
    medal_50 = Medal(id=50,fighter='Jon Jones',place='Runner-Up',year='2016')
    medal_51 = Medal(id=51,fighter='Daniel Cormier',place='3rd',year='2016')
    medal_52 = Medal(id=52,fighter='Anthony Johnson',place='4th',year='2016')
    medal_53 = Medal(id=53,fighter='Alexander Gustuffson',place='5th',year='2016')
    medal_54 = Medal(id=54,fighter='Forrest Griffon',place='6th',year='2016')
    medal_55 = Medal(id=55,fighter='Cain Velasquez',place='Champion',year='2016')
    medal_56 = Medal(id=56,fighter='Junior Dos Santos',place='Runner-Up',year='2016')
    medal_57 = Medal(id=57,fighter='Shane Carwin',place='5th',year='2016')
    medal_58 = Medal(id=58,fighter='Frank Mir',place='6th',year='2016')
    #################################2017#########################################
    medal_59 = Medal(id=59,fighter='Demetrious Johnson',place='Champion',year='2017')
    medal_60 = Medal(id=60,fighter='Henry Cejudo',place='Runner-Up',year='2017')
    medal_61 = Medal(id=61,fighter='Joseph Benavidez',place='3rd',year='2017')
    medal_62 = Medal(id=62,fighter='John Lineker',place='4th',year='2017')
    medal_63 = Medal(id=63,fighter='Yuti Motoya',place='5th',year='2017')
    medal_64 = Medal(id=64,fighter='Tim Elliot',place='6th',year='2017')
    medal_65 = Medal(id=65,fighter='Gray Bardock',place='7th',year='2017')
    medal_66 = Medal(id=66,fighter='John Dodson',place='8th',year='2017')
    medal_67 = Medal(id=67,fighter='Takeya Mizugaki',place='Champion',year='2017')
    medal_68 = Medal(id=68,fighter='Dominick Cruz',place='Runner-Up',year='2017')
    medal_69 = Medal(id=69,fighter='TJ Dillasaw',place='3rd',year='2017')
    medal_70 = Medal(id=70,fighter='Iuri Alcantara',place='4th',year='2017')
    medal_71 = Medal(id=71,fighter='Cody Garbrandt',place='5th',year='2017')
    medal_72 = Medal(id=72,fighter='Raphael Assuncao',place='6th',year='2017')
    medal_73 = Medal(id=73,fighter='Pedro Munhoz',place='7th',year='2017')
    medal_74 = Medal(id=74,fighter='Mitsinori Tanaka',place='8th',year='2017')
    medal_75 = Medal(id=75,fighter='Conor Mcgregor',place='Champion',year='2017')
    medal_76 = Medal(id=76,fighter='Hatsu Hioki',place='Runner-Up',year='2017')
    medal_77 = Medal(id=77,fighter='Jose Aldo',place='3rd',year='2017')
    medal_78 = Medal(id=78,fighter='Frankie Edgar',place='4th',year='2017')
    medal_79 = Medal(id=79,fighter='Chad Mendes',place='5th',year='2017')
    medal_80 = Medal(id=80,fighter='Max Holloway',place='6th',year='2017')
    medal_81 = Medal(id=81,fighter='Do Ho Choi',place='7th',year='2017')
    medal_82 = Medal(id=82,fighter='BJ Penn',place='8th',year='2017')
    medal_83 = Medal(id=83,fighter='Tony Ferguson',place='Champion',year='2017')
    medal_84 = Medal(id=84,fighter='Khabib Nurmagomedov',place='Runner-Up',year='2017')
    medal_85 = Medal(id=85,fighter='Rafael Dos Anjos',place='3rd',year='2017')
    medal_86 = Medal(id=86,fighter='Anthony Pettis',place='4th',year='2017')
    medal_87 = Medal(id=87,fighter='Michael Chandler',place='5th',year='2017')
    medal_88 = Medal(id=88,fighter='Benson Henderson',place='6th',year='2017')
    medal_89 = Medal(id=89,fighter='Donald Cerrone',place='7th',year='2017')
    medal_90 = Medal(id=90,fighter='Dustin Poirier',place='8th',year='2017')
    medal_91 = Medal(id=91,fighter='Stephen Thompson',place='Champion',year='2017')
    medal_92 = Medal(id=92,fighter='Robbie Lawler',place='Runner-Up',year='2017')
    medal_93 = Medal(id=93,fighter='Rory Macdonald',place='3rd',year='2017')
    medal_94 = Medal(id=94,fighter='Georges St.Pieree',place='4th',year='2017')
    medal_95 = Medal(id=95,fighter='Demian Maia',place='5th',year='2017')
    medal_96 = Medal(id=96,fighter='Carlos Condit',place='6th',year='2017')
    medal_97 = Medal(id=97,fighter='Johny Hendricks',place='7th',year='2017')
    medal_98 = Medal(id=98,fighter='Karo Parisyan',place='8th',year='2017')
    medal_99 = Medal(id=99,fighter='Ronaldo Souza',place='Runner-Up',year='2017')
    medal_100 = Medal(id=100,fighter='Yoel Romero',place='Champion',year='2017')
    medal_101 = Medal(id=101, fighter='Luke Rockhold', place='3rd', year='2017')
    medal_102 = Medal(id=102,fighter='Chris Weidman',place='4th',year='2017')
    medal_103 = Medal(id=103,fighter='Lyoto Machida',place='5th',year='2017')
    medal_104 = Medal(id=104,fighter='Vitor Belfort',place='6th',year='2017')
    medal_105 = Medal(id=105,fighter='Chael Sonnen',place='7th',year='2017')
    medal_106 = Medal(id=106,fighter='Michael Bisping',place='',year='2017')
    medal_107 = Medal(id=107,fighter='Jon Jones',place='Champion',year='2017')
    medal_108 = Medal(id=108,fighter='Anthony Johnson',place='Runner-Up',year='2017')
    medal_109 = Medal(id=109,fighter='Daniel Cormier',place='3rd',year='2017')
    medal_110 = Medal(id=110,fighter='Liam Mcgreary',place='4th',year='2017')
    medal_111 = Medal(id=111,fighter='Ryan Bader',place='5th',year='2017')
    medal_112 = Medal(id=112,fighter='Randy Couture',place='6th',year='2017')
    medal_113 = Medal(id=113,fighter='Alexander Gustuffson',place='7th',year='2017')
    medal_114 = Medal(id=114,fighter='Rashad Evans',place='8th',year='2017')
    medal_115 = Medal(id=115,fighter='Fedor Emileanako',place='Champion',year='2017')
    medal_116 = Medal(id=116,fighter='S.Miocic',place='Runner-Up',year='2017')
    medal_117 = Medal(id=117,fighter='Alistair Overeem',place='3rd',year='2017')
    medal_118 = Medal(id=118,fighter='Fabricio Werdum',place='4th',year='2017')
    medal_119 = Medal(id=119,fighter='Cain Velasquez',place='5th',year='2017')
    medal_120 = Medal(id=120,fighter='Junior Dos Santos',place='6th',year='2017')
    medal_121 = Medal(id=121,fighter='Brock Lesnar',place='7th',year='2017')
    medal_122 = Medal(id=122,fighter='Mark Hunt',place='8th',year='2017')
    # medal_ = Medal(id=,fighter='',place='',year='2017')

    medalss = [
        #################################### 2018 #############################
        Medal(id=123,fighter='Henry Cejudo',place='Champion',year='2018'),
        Medal(id=124,fighter='Demetrious Johnson',place='Runner-Up',year='2018'),
        Medal(id=125,fighter='Miguel Torres',place='3rd',year='2018'),
        Medal(id=126,fighter='Gennady Golovkin',place='4th',year='2018'),
        Medal(id=127,fighter='Sergio Pettis',place='5th',year='2018'),
        Medal(id=128,fighter='Joseph Benavidez',place='6th',year='2018'),
        Medal(id=129,fighter='Raegan Penn',place='7th',year='2018'),
        Medal(id=130,fighter='John Lineker',place='8th',year='2018'),
        Medal(id=131,fighter='TJ Dillasaw',place='Champion',year='2018'),
        Medal(id=132,fighter='Chinzo Machida',place='Runner-Up',year='2018'),
        Medal(id=133,fighter='Cody Garbrandt',place='3rd',year='2018'),
        Medal(id=134,fighter='Dominick Cruz',place='4th',year='2018'),
        Medal(id=135,fighter='Takeya Mizugaki',place='5th',year='2018'),
        Medal(id=136,fighter='Chris Holdsworth',place='6th',year='2018'),
        Medal(id=137,fighter='Marlon Moraes',place='7th',year='2018'),
        Medal(id=138,fighter='Jimmie Rivera',place='8th',year='2018'),
        Medal(id=139,fighter='Max Holloway',place='Champion',year='2018'),
        Medal(id=140,fighter='Hatsu Hioki',place='Runner-Up',year='2018'),
        Medal(id=141,fighter='Jose Aldo',place='3rd',year='2018'),
        Medal(id=142,fighter='Zabit Magomedsharipov',place='4th',year='2018'),
        Medal(id=143,fighter='Brian Ortega',place='5th',year='2018'),
        Medal(id=144,fighter='Chad Mendes',place='6th',year='2018'),
        Medal(id=145,fighter='Frankie Edgar',place='7th',year='2018'),
        Medal(id=146,fighter='Mike Brown',place='8th',year='2018'),
        Medal(id=147,fighter='Khabib Nurmagomedov',place='Champion',year='2018'),
        Medal(id=148,fighter='Tony Ferguson',place='Runner-Up',year='2018'),
        Medal(id=149,fighter='Nate Diaz',place='3rd',year='2018'),
        Medal(id=150,fighter='Conor Mcgregor',place='4th',year='2018'),
        Medal(id=151,fighter='Kurt Pellegrino',place='5th',year='2018'),
        Medal(id=152,fighter='Kevin Lee',place='6th',year='2018'),
        Medal(id=153,fighter='Dustin Poirier',place='7th',year='2018'),
        Medal(id=154,fighter='Anthony Pettis',place='8th',year='2018'),
        Medal(id=155,fighter='Georges St.pierre',place='Champion',year='2018'),
        Medal(id=156,fighter='Tyron Woodley',place='Runner-Up',year='2018'),
        Medal(id=157,fighter='Robbie Lawler',place='3rd',year='2018'),
        Medal(id=158,fighter='Colby Covington',place='4th',year='2018'),
        Medal(id=159,fighter='Darren Till',place='5th',year='2018'),
        Medal(id=160,fighter='Stephen Thompson',place='6th',year='2018'),
        Medal(id=161,fighter='Kamaru Usman',place='7th',year='2018'),
        Medal(id=162,fighter='Ben Askren',place='8th',year='2018'),
        Medal(id=163,fighter='Robert Whittaker',place='Champion',year='2018'),
        Medal(id=164,fighter='Luke Rockhold',place='Runner-Up',year='2018'),
        Medal(id=165,fighter='Yoel Romero',place='3rd',year='2018'),
        Medal(id=166,fighter='Kelvin Gastelum',place='4th',year='2018'),
        Medal(id=167,fighter='Paulo Costa',place='5th',year='2018'),
        Medal(id=168,fighter='Rashad Evans',place='6th',year='2018'),
        Medal(id=169,fighter='Ronaldo Souza',place='7th',year='2018'),
        Medal(id=170,fighter='Chris Weidman',place='8th',year='2018'),
        Medal(id=171,fighter='Jon Jones',place='Champion',year='2018'),
        Medal(id=172,fighter='Daniel Cormier',place='Runner-Up',year='2018'),
        Medal(id=173,fighter='Anthony Johnson',place='3rd',year='2018'),
        Medal(id=179,fighter='Aleksander Emileanako',place='4th',year='2018'),
        Medal(id=174,fighter='Volkan Oezdmir',place='5th',year='2018'),
        Medal(id=175,fighter='Ryan Bader',place='6th',year='2018'),
        Medal(id=176,fighter='Alexander Gustuffsson',place='7th',year='2018'),
        Medal(id=177,fighter='Phil Davis',place='8th',year='2018'),
        Medal(id=178,fighter='Fedor Emileanako',place='Champion',year='2018'),
        Medal(id=180,fighter='Cain Velasquez',place='Runner-Up',year='2018'),
        Medal(id=181,fighter='Stipe Miocic',place='3rd',year='2018'),
        Medal(id=182,fighter='Francis Ngannou',place='4th',year='2018'),
        Medal(id=183,fighter='Junior Dos Santos',place='5th',year='2018'),
        Medal(id=184,fighter='Ben Rothwell',place='6th',year='2018'),
        Medal(id=185,fighter='Derick Lewis',place='7th',year='2018'),
        Medal(id=186,fighter='Aleksei Oleinik',place='8th',year='2018'),
        ############################## 2019 ##################################


        Medal(id=187,fighter='Deiveson Figueiredo',place='Champion',year='2019'),
        Medal(id=188,fighter='Demetrious Johnson',place='Runner-Up',year='2019'),
        Medal(id=189,fighter='Henry Cejudo',place='3rd',year='2019'),
        Medal(id=190,fighter='Tatsumitsu Wada',place='4th',year='2019'),
        Medal(id=191,fighter='Jack Mueller',place='5th',year='2019'),
        Medal(id=192,fighter='Tenshin Nasakawa',place='6th',year='2019'),
        Medal(id=193,fighter='Nakamizulu Zulu',place='7th',year='2019'),
        Medal(id=194,fighter='Miguel Torres',place='8th',year='2019'),
        Medal(id=195,fighter='Yianni Diakomihalis',place='Champion',year='2019'),
        Medal(id=196,fighter='Chinzo Machida',place='Runner-Up',year='2019'),
        Medal(id=197,fighter='Ricky Simon',place='3rd',year='2019'),
        Medal(id=198,fighter='Takeya Mizugaki',place='4th',year='2019'),
        Medal(id=199,fighter='Cory Sandhagen',place='5th',year='2019'),
        Medal(id=200,fighter='Yowlys Bonne',place='6th',year='2019'),
        Medal(id=201,fighter='Said Nurmagomedov',place='7th',year='2019'),
        Medal(id=202,fighter='Dominick Cruz',place='8th',year='2019'),
        Medal(id=203,fighter='Alexander Volkanovski',place='Champion',year='2019'),
        Medal(id=204,fighter='Zubaira Tukhugov',place='Runner-Up',year='2019'),
        Medal(id=205,fighter='Hatsu Hioki',place='3rd',year='2019'),
        Medal(id=206,fighter='Rashid Magomedov',place='4th',year='2019'),
        Medal(id=207,fighter='Zabit Magomedsharipov',place='5th',year='2019'),
        Medal(id=208,fighter='Jose Aldo',place='6th',year='2019'),
        Medal(id=209,fighter='Brian Ortega',place='7th',year='2019'),
        Medal(id=210,fighter='Bubba Jenkins',place='8th',year='2019'),
        Medal(id=211,fighter='Khabib Nurmagomedov',place='Champion',year='2019'),
        Medal(id=212,fighter='Tony Ferguson',place='Runner-Up',year='2019'),
        Medal(id=213,fighter='Zaurbek Sidakov',place='3rd',year='2019'),
        Medal(id=214,fighter='Conor Mcgregor',place='4th',year='2019'),
        Medal(id=215,fighter='Genki Sudo',place='5th',year='2019'),
        Medal(id=216,fighter='Kharma Worthy',place='6th',year='2019'),
        Medal(id=217,fighter='Dustin Poirier',place='7th',year='2019'),
        Medal(id=218,fighter='Max Holloway',place='8th',year='2019'),
        Medal(id=219,fighter='Kamaru Usman',place='Champion',year='2019'),
        Medal(id=220,fighter='Anuiar Geduev',place='Runner-Up',year='2019'),
        Medal(id=221,fighter='Kazushi Sakuraba',place='3rd',year='2019'),
        Medal(id=222,fighter='Colby Covington',place='4th',year='2019'),
        Medal(id=223,fighter='Stephen Thompson',place='5th',year='2019'),
        Medal(id=224,fighter='Jorge Masvidal',place='6th',year='2019'),
        Medal(id=225,fighter='Leon Edwards',place='7th',year='2019'),
        Medal(id=226,fighter='Carlos Newton',place='8th',year='2019'),
        Medal(id=227,fighter='Israel Adesanya',place='Champion',year='2019'),
        Medal(id=228,fighter='Robert Whittaker',place='Runner-Up',year='2019'),
        Medal(id=229,fighter='Kelvin Gastelum',place='3rd',year='2019'),
        Medal(id=230,fighter='Paulo Costa',place='4th',year='2019'),
        Medal(id=231,fighter='Yoel Romero',place='5th',year='2019'),
        Medal(id=232,fighter='Omari Akmedov',place='6th',year='2019'),
        Medal(id=233,fighter='Pazqual Lang',place='7th',year='2019'),
        Medal(id=234,fighter='Lyoto Machida',place='8th',year='2019'),
        Medal(id=235,fighter='Abdulrashid Saduliev',place='Champion',year='2019'),
        Medal(id=236,fighter='Jon Jones',place='Runner-Up',year='2019'),
        Medal(id=237,fighter='Kyle Snyder',place='3rd',year='2019'),
        Medal(id=238,fighter='Dominick Reyes',place='4th',year='2019'),
        Medal(id=239,fighter='Thiago Santos',place='5th',year='2019'),
        Medal(id=240,fighter='Aleksander Rakic',place='6th',year='2019'),
        Medal(id=241,fighter='Anthony Smith',place='7th',year='2019'),
        Medal(id=242,fighter='Senar Batirov',place='8th',year='2019'),
        Medal(id=243,fighter='Jack Dempsy',place='Champion',year='2019'),
        Medal(id=244,fighter='Stipe Miocic',place='Runner-Up',year='2019'),
        Medal(id=245,fighter='Fedor Emileanako',place='3rd',year='2019'),
        Medal(id=246,fighter='Taha Akgul',place='4th',year='2019'),
        Medal(id=247,fighter='Francis Ngannou',place='5th',year='2019'),
        Medal(id=248,fighter='Aleksandr Karelin',place='6th',year='2019'),
        Medal(id=249,fighter='Daniel Cormier',place='7th',year='2019'),
        Medal(id=250,fighter='Zhiwei Deng',place='8th',year='2019'),
        ################################## 2020 ####################################



        Medal(id=251,fighter='Brandon Moreno',place='Champion',year='2020'),
        Medal(id=252,fighter='Askar Askarov',place='Runner-Up',year='2020'),
        Medal(id=253,fighter='Spencer Lee',place='3rd',year='2020'),
        Medal(id=254,fighter='Tagir Ulanbekov',place='4th',year='2020'),
        Medal(id=255,fighter='Tatsumitsu Wada',place='5th',year='2020'),
        Medal(id=256,fighter='Alan Gomes',place='6th',year='2020'),
        Medal(id=257,fighter='Zaur Uguyev',place='7th',year='2020'),
        Medal(id=258,fighter='Demetrious Johnson',place='8th',year='2020'),
        Medal(id=259,fighter='Petr Yan',place='Champion',year='2020'),
        Medal(id=260,fighter='Seth Gross',place='Runner-Up',year='2020'),
        Medal(id=261,fighter='Cory Sandhagen',place='3rd',year='2020'),
        Medal(id=262,fighter='Henry Cejudo',place='4th',year='2020'),
        Medal(id=263,fighter='Chinzo Machida',place='5th',year='2020'),
        Medal(id=264,fighter='TJ Dillasaw',place='6th',year='2020'),
        Medal(id=265,fighter="Sean O'malley",place='7th',year='2020'),
        Medal(id=266,fighter='Merab Dvalishvili',place='8th',year='2020'),
        Medal(id=267,fighter='Alexander Volkanovski',place='Champion',year='2020'),
        Medal(id=268,fighter='Zabit Magomedsharipov',place='Runner-Up',year='2020'),
        Medal(id=269,fighter='Max Holloway',place='3rd',year='2020'),
        Medal(id=270,fighter='Yianni Diakomihalis',place='4th',year='2020'),
        Medal(id=271,fighter='Brian Ortega',place='5th',year='2020'),
        Medal(id=272,fighter='Zubaira Tukhugov',place='6th',year='2020'),
        Medal(id=273,fighter='Gadzimurad Rashidov',place='7th',year='2020'),
        Medal(id=274,fighter='Max Askren',place='8th',year='2020'),
        Medal(id=275,fighter='Charles Oliviera',place='Champion',year='2020'),
        Medal(id=276,fighter='Dustin Poirier',place='Runner-Up',year='2020'),
        Medal(id=277,fighter='Khabib Nurmagomedov',place='3rd',year='2020'),
        Medal(id=278,fighter='Jordan Burroughs',place='4th',year='2020'),
        Medal(id=279,fighter='Justin Gaethje',place='5th',year='2020'),
        Medal(id=280,fighter='Zaurbek Sidakov',place='6th',year='2020'),
        Medal(id=281,fighter='Denis Tsargush',place='7th',year='2020'),
        Medal(id=282,fighter='Tony Ferguson',place='8th',year='2020'),
        Medal(id=283,fighter='Kamaru Usman',place='Champion',year='2020'),
        Medal(id=284,fighter='Colby Covington',place='Runner-Up',year='2020'),
        Medal(id=285,fighter='Kyle Dake',place='3rd',year='2020'),
        Medal(id=286,fighter='Kazushi Sakuraba',place='4th',year='2020'),
        Medal(id=287,fighter='Usman Nurmagomedov',place='5th',year='2020'),
        Medal(id=288,fighter='Leon Edwards',place='6th',year='2020'),
        Medal(id=289,fighter='Anuiar Geduev',place='7th',year='2020'),
        Medal(id=290,fighter='Gilbert Burns',place='8th',year='2020'),
        Medal(id=291,fighter='Israel Adesanya',place='Champion',year='2020'),
        Medal(id=292,fighter='Zander Emileanako',place='Runner-Up',year='2020'),
        Medal(id=293,fighter='David Taylor',place='3rd',year='2020'),
        Medal(id=294,fighter='Hassan Yazdanicharati',place='4th',year='2020'),
        Medal(id=295,fighter="J'den Cox",place='5th',year='2020'),
        Medal(id=296,fighter='Zahid Valencia',place='6th',year='2020'),
        Medal(id=297,fighter='Robert Whittaker',place='7th',year='2020'),
        Medal(id=298,fighter='Jared Cannonier',place='8th',year='2020'),
        Medal(id=299,fighter='Abdulrashid Saduliev',place='Champion',year='2020'),
        Medal(id=300,fighter='Jan Blachowitz',place='Runner-Up',year='2020'),
        Medal(id=301,fighter='Jon Jones',place='3rd',year='2020'),
        Medal(id=302,fighter='Aleksander Rakic',place='4th',year='2020'),
        Medal(id=303,fighter='Khalil Roundtree',place='5th',year='2020'),
        Medal(id=304,fighter='Thiago Santos',place='6th',year='2020'),
        Medal(id=305,fighter='Kyle Snyder',place='7th',year='2020'),
        Medal(id=306,fighter='Bo Nickal',place='8th',year='2020'),
        Medal(id=307,fighter='Fedor Emileanako',place='Champion',year='2020'),
        Medal(id=308,fighter='Tyson Fury',place='Runner-Up',year='2020'),
        Medal(id=309,fighter='Francis Ngannou',place='3rd',year='2020'),
        Medal(id=310,fighter='Jack Dempsy',place='4th',year='2020'),
        Medal(id=311,fighter='Gable Steveson',place='5th',year='2020'),
        Medal(id=312,fighter='Stipe Miocic',place='6th',year='2020'),
        Medal(id=313,fighter='Geno Petriavili',place='7th',year='2020'),
        Medal(id=314,fighter='Taha Akgul',place='8th',year='2020'),
        # Medal(id=,fighter='',place='',year='2020'),


    ]

    db.session.add_all(medalss)
    db.session.commit()


    # medal_60 = Medal(id=60,fighter='Demetrious Johnson',place='Runner-Up',year='2018')
    # medal_61 = Medal(id=61,fighter='Demetrious Johnson',place='Runner-Up',year='2019')
    # medal_62 = Medal(id=62,fighter='Demetrious Johnson',place='8th',year='2020')
    # medal_63 = Medal(id=63,fighter='Charles Oliviera',place='Champion',year='2020')
    # medal_64 = Medal(id=64,fighter='Jordan Burroughs',place='4th',year='2020')
    # medal_ = Medal(id=,fighter='',place='',year='2016')


    seeds = [medal_1, medal_2, medal_3, medal_4, medal_5, medal_6, medal_7, medal_8, medal_9, medal_10, medal_11, medal_12, medal_13, medal_14, medal_15, medal_16, medal_17, medal_18, medal_19, medal_20, medal_21, medal_22, medal_23, medal_24, medal_25, medal_26, medal_27, medal_28, medal_29, medal_30, medal_31, medal_32, medal_33, medal_34, medal_35, medal_36, medal_37, medal_38, medal_39, medal_40, medal_41, medal_42, medal_43, medal_44, medal_45, medal_46, medal_47, medal_48, medal_49, medal_50, medal_51, medal_52, medal_53, medal_54, medal_55, medal_56, medal_57, medal_58, medal_59, medal_65, medal_66, medal_67, medal_68, medal_69, medal_70, medal_71, medal_72, medal_73, medal_74, medal_75, medal_76, medal_77, medal_78, medal_79, medal_80, medal_81, medal_82, medal_83, medal_84, medal_85, medal_86, medal_87, medal_88, medal_89, medal_90, medal_91, medal_92, medal_93, medal_94, medal_95, medal_96, medal_97, medal_98, medal_99, medal_100, medal_101, medal_102, medal_103, medal_104, medal_105, medal_106, medal_107, medal_108, medal_109, medal_110, medal_111, medal_112, medal_113, medal_114, medal_115, medal_116, medal_117, medal_118, medal_119, medal_120, medal_121
]
    #seeds = [f"medal_{i}" for i in range(1, 122)]
    for seed in seeds:
        db.session.add(seed)
        db.session.commit()

def undo_medals():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.users RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM medals"))

    db.session.commit()
