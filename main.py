from data import db_session
from data.jobs import Jobs
from data.users import User
import datetime

db_session.global_init(f"db/mars_explorer.db")
session = db_session.create_session()
# name_bd = input()
# global_init(f"{name_bd}")
# session = create_session()
for user in session.query(User).filter(User.address.like('module_1'), User.age < 21):
    user.address = 'module_3'
session.commit()

# db_session.global_init("db/mars_explorer.db")
# session = db_session.create_session()
#
# job = Jobs()
# job.team_leader = 4
# job.job = 'землю - крестьянам, фабрики - рабочим, cтатьи - ученым'
# job.work_size = 1917
# job.collaborators = ''
# job.start_date = datetime.datetime.now()
# job.is_finished = False
# session.add(job)
#
# session.commit()
#
# # # я уже запустил один раз, так что второй раз будет ошибка
# # # из за попытки добавить юзера с уже существующим в бд емайлом
# # user = User()
# # user.surname = "Scott"
# # user.name = "Ridley"
# # user.age = 21
# # user.position = "captain"
# # user.speciality = "research engineer"
# # user.address = "module_1"
# # user.email = "scott_chief@mars.org"
# # user.hashed_password = "cap347638476972386293623-6-034"
# # session.add(user)
# #
# # user = User()
# # user.name = "Денис"
# # user.surname = "Петров"
# # user.age = 23
# # user.position = "рядовой"
# # user.speciality = "связист"
# # user.address = "module_2"
# # user.email = "ABOBA@mars.org"
# # user.hashed_password = "rghu84hg94heuge4gu92hq4giknje4r"
# # session.add(user)
# #
# # user = User()
# # user.name = "Глад"
# # user.surname = "Валакас"
# # user.age = 65
# # user.position = "рядовой"
# # user.speciality = "связист"
# # user.address = "module_2"
# # user.email = "A_B_O_B_A@mars.org"
# # user.hashed_password = "fffffffffwwwwwwwwwww213414124123"
# # session.add(user)
# #
# # user = User()
# # user.name = "Богдан"
# # user.surname = "Богом-дан"
# # user.age = 8
# # user.position = "рядовой"
# # user.speciality = "связист"
# # user.address = "module_2"
# # user.email = "BOGDAN@mars.org"
# # user.hashed_password = "123456"
# # session.add(user)
# #
# # session.commit()
