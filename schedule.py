import sqlsaver
import time
from selenium import webdriver
from selenium.webdriver.support.select import Select
faks_sch_to_db = dict()
driver = webdriver.Chrome()
driver.get("https://rsue.ru/raspisanie")
fak_get = driver.find_element_by_name("f")
select_fak = Select(fak_get)
faks = fak_get.find_elements_by_tag_name("option")
countF = int(0)
countK = int(0)
countG = int(0)
# select_fak.select_by_visible_text("Менеджмента и предпринемательства")
for ff in faks:
    if ff.text == "Факультет":
        faks.remove(ff)
fak_count = faks.__len__()
for f in range(fak_count):
    fak_get = driver.find_element_by_name("f")
    faks = fak_get.find_elements_by_tag_name("option")
    for ff in faks:
        if ff.text == "Факультет":
            faks.remove(ff)
    try:
        select_fak = Select(fak_get)
        time.sleep(1)
        fak_name = faks[f].text
        select_fak.select_by_visible_text(faks[f].text)
        time.sleep(1)
        kurs_get = driver.find_element_by_name("k")
        select_kurs = Select(kurs_get)
        time.sleep(1)
        kurss = kurs_get.find_elements_by_tag_name("option")
        for kk in kurss:
            if kk.text == "Курс" or kk.text == "5-й курс":
                kurss.remove(kk)
        kurs_len = kurss.__len__()
        kurs_sch_to_db = dict()
        for k in range(kurs_len):
            try:
                fak_get = driver.find_element_by_name("f")
                faks = fak_get.find_elements_by_tag_name("option")
                for ff in faks:
                    if ff.text == "Факультет":
                        faks.remove(ff)
                select_fak = Select(fak_get)
                time.sleep(1)
                select_fak.select_by_visible_text(faks[f].text)
                time.sleep(1)
                kurs_get = driver.find_element_by_name("k")
                kurss = kurs_get.find_elements_by_tag_name("option")
                for kk in kurss:
                    if kk.text == "Курс" or kk.text == "5-й курс":
                        kurss.remove(kk)
                select_kurs = Select(kurs_get)
                time.sleep(1)
                kurs_name = kurss[k].text
                select_kurs.select_by_visible_text(kurss[k].text)
                time.sleep(1)
                group_get = driver.find_element_by_name("g")
                groups = group_get.find_elements_by_tag_name("option")
                #print(groups)
                for g in groups:
                    if g.text == "Группа":
                        groups.remove(g)
                groups_len = groups.__len__()
                gr_sch_to_db = dict()
                for g in range(groups_len):
                    fak_get = driver.find_element_by_name("f")
                    faks = fak_get.find_elements_by_tag_name("option")
                    for ff in faks:
                        if ff.text == "Факультет":
                            faks.remove(ff)
                    time.sleep(1)
                    select_fak = Select(fak_get)
                    time.sleep(1)
                    select_fak.select_by_visible_text(faks[f].text)
                    time.sleep(1)
                    kurs_get = driver.find_element_by_name("k")
                    kurss = kurs_get.find_elements_by_tag_name("option")
                    for kk in kurss:
                        if kk.text == "Курс" or kk.text == "5-й курс":
                            kurss.remove(kk)
                    time.sleep(1)
                    select_kurs = Select(kurs_get)
                    time.sleep(1)
                    select_kurs.select_by_visible_text(kurss[k].text)
                    time.sleep(1)
                    group_get = driver.find_element_by_name("g")
                    select_group = Select(group_get)
                    time.sleep(1)
                    groups = group_get.find_elements_by_tag_name("option")
                    for gg in groups:
                        if gg.text == "Группа":
                            groups.remove(gg)
                    time.sleep(1)
                    try:
                        gr_name = groups[g].text
                        select_group.select_by_visible_text(groups[g].text)
                        time.sleep(1)
                        temp = driver.find_elements_by_class_name("container")
                        schedule = temp[temp.__len__()-1]
                        #print(schedule.text)
                        weeks = schedule.find_elements_by_class_name("ned")
                        for we in weeks:
                            if we=="Нечетная неделя":
                                we = 1
                            elif we=="Четная неделя":
                                we = 0
                        time.sleep(1)
                        scheds = schedule.find_elements_by_class_name("row")
                        time.sleep(1)
                        #print(weeks.__len__())
                        #print(scheds.__len__())
                        count_rows = scheds[0].find_elements_by_class_name("row").__len__()
                        f_week = scheds[0]
                        s_week = scheds[count_rows + 1]
                        f_week_days = dict()
                        for ff in f_week.find_elements_by_css_selector("div[class=\"col-lg-2 col-md-2 col-sm-2\"]"):
                            l = list()
                            for fff in ff.find_elements_by_css_selector("div[class=\"col-lg-12 day\"]"):
                                l.append(fff.text)
                            try:
                                f_week_days[ff.find_element_by_id("nedelya").text] = l
                            except:
                                continue
                        #print(f_week_days)
                        #print("lol")
                        s_week_days = dict()
                        for ff in s_week.find_elements_by_css_selector("div[class=\"col-lg-2 col-md-2 col-sm-2\"]"):
                            l = list()
                            for fff in ff.find_elements_by_css_selector("div[class=\"col-lg-12 day\"]"):
                                l.append(fff.text)
                            try:
                                s_week_days[ff.find_element_by_id("nedelya").text] = l
                            except:
                                continue
                    except:
                        continue
                    gr_sch_to_db[gr_name] = {weeks[0].text: f_week_days, weeks[1].text: s_week_days}

                kurs_sch_to_db[kurs_name] = gr_sch_to_db
            except:
                continue
        faks_sch_to_db[fak_name] = kurs_sch_to_db
    except:
        continue
driver.close()
sqlsaver.fill_schedule(faks_sch_to_db)
