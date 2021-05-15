import pymysql
import pymysql.cursors


def fill_news(titl, tex):
    con = pymysql.connect(host='localhost', user='sDether',
                          password='1namQfeg1_', db='rsue_helper', charset='utf8mb4')
    with con:
        cur = con.cursor()
        сur.execute("truncate table schedule")
        con.commit()
        for t in range(titl.__len__()):
            inserter = str("insert into news (title, text) values (" + "'"+titl[t]+ "'" +", "+ "'"+ tex[t]+ "'" + ")")
            cur.execute(inserter)
        con.commit()

def fill_teachers(tc):
    con = pymysql.connect(host='localhost', user='sDether',
                          password='1namQfeg1_', db='rsue_helper', charset='utf8mb4')
    with con:
        cur = con.cursor()
        сur.execute("truncate table schedule")
        con.commit()
        for fak in tc.keys():
            for kaf in tc[fak].keys():
                for teach in tc[fak][kaf].keys():
                    inserter = str("insert into prepods (fio, fakulty, kafedra, link) values (" + "'"+teach+ "'" +", "+ "'"+fak+ "'" +", "+ "'"+kaf +"'"+", "+"'"+tc[fak][kaf][teach]+"'" +")")
                    cur.execute(inserter)
        con.commit()

def fill_schedule(tc):
    con = pymysql.connect(host='localhost', user='sDether',
                          password='1namQfeg1_', db='rsue_helper', charset='utf8mb4')
    with con:
        cur = con.cursor()
        #сur.execute("truncate table schedule")
        #con.commit()
        for fak in tc.keys():
            for year in tc[fak].keys():
                for group in tc[fak][year].keys():
                    for week_type in tc[fak][year][group].keys():
                        for day in tc[fak][year][group][week_type]:
                            #for sch in tc[fak][year][group][week_type][day]:
                                #print(group)
                            inserter = str()
                            if week_type == "Нечетная неделя":
                                inserter = str("insert into schedule (faculty, schedule.year, schedule.group, up_weak, schedule.day, schedule) values (" + "'"+fak+ "'" +", "+ year[0] +", "+ "'"+group +"'"+", 1, "+"'"+ day.lower()+"'"+ ", " + "'" +"".join(tc[fak][year][group][week_type][day])  +"'" +")")
                            elif week_type == "Четная неделя":
                                inserter = str("insert into schedule (faculty, schedule.year, schedule.group, up_weak, schedule.day, schedule) values (" + "'"+fak+ "'" +", "+ year[0] +", "+ "'"+group +"'"+", 0, "+"'"+ day.lower()+"'"+ ", " + "'" + "".join(tc[fak][year][group][week_type][day]) +"'" +")")
                            cur.execute(inserter)
        con.commit()


#fill_schedule({"Fak":{"1":{"Нечетная неделя":{"Day":["день", "вечер", "супер"]}}}})