from bs4 import BeautifulSoup
import requests as req
import re
import sqlsaver

men_fak = {"Финансовый менеджмент":"https://rsue.ru/fakultety/FMIP/kaf-FM/",
           "Общий и стратегический менеджмент" :"https://rsue.ru/fakultety/FMIP/kaf-OISM/",
           "Управление персоналом и социологии":"https://rsue.ru/fakultety/FMIP/kaf-UPIS/",
        "Государственное, муниципальное управление и экономическая безопасность":"https://rsue.ru/fakultety/FMIP/kaf-GMUIEB/",
           "Инновационный менеджмент и предпринимательство":"https://rsue.ru/fakultety/FMIP/kaf-IMIP/",
          "Антикризисное и корпоративное управление":"https://rsue.ru/fakultety/FMIP/kaf-AIKU/"}
td_fak = {"Философии и культурологии":"https://rsue.ru/fakultety/FTD/kaf-FIK/",
          "Коммерции и логистики":"https://rsue.ru/fakultety/FTD/kaf-KIL/",
          "Маркетинга и рекламы":"https://rsue.ru/fakultety/FTD/kaf-MIR/",
          "Международной торговли и таможенного дела":"https://rsue.ru/fakultety/FTD/kaf-MTITD/",
         "Экономической теории":"https://rsue.ru/fakultety/FTD/kaf-et/",
         "Товароведения и управления качеством":"https://rsue.ru/fakultety/FTD/kaf-tiuk/"}
ktib_fak = {"Информационных систем и прикладной информатики":"https://rsue.ru/fakultety/FKTIB/kaf-ISIPI/",
            "Фундаментальной и прикладной математики":"https://rsue.ru/fakultety/FKTIB/kaf-FIPM/",
            "Информационных технологий и защиты информации":"https://rsue.ru/fakultety/FKTIB/kaf-ITIZI/",
            "Физического воспитания, спорта и туризма":"https://rsue.ru/fakultety/FKTIB/kaf-FVSIT/"}
yk_fak = {"Бухгалтерского учета":"https://rsue.ru/fakultety/UEF/kaf-BU/",
          "Аудита":"https://rsue.ru/fakultety/UEF/kaf-A/",
          "Кафедра Анализа хозяйственной деятельности и прогнозирования":"https://rsue.ru/fakultety/UEF/kaf-AXDIP/",
          "Статистики, эконометрики и оценки рисков":"https://rsue.ru/fakultety/UEF/ochnoe-otdelenie/",
          "Мировой политики и глобализации":"https://rsue.ru/fakultety/UEF/kaf-MEIMB"}
if_fak = {"Банковского дела":"https://rsue.ru/fakultety/FEIF/kaf-BD/",
          "Финансов":"https://rsue.ru/fakultety/FEIF/kaf-F/",
          "Налоги и налогообложение":"https://rsue.ru/fakultety/FEIF/kaf-NIN/",
          "Финансового мониторинга и финансовых рынков":"https://rsue.ru/fakultety/FEIF/kaf-FMIFR/",
          "Экономики региона, отраслей и предприятий":"https://rsue.ru/fakultety/FEIF/kaf-EROIP/",
          "Мировой экономики":"https://rsue.ru/fakultety/FEIF/kaf-ME"}
uf_fak = {"Гражданского права":"https://rsue.ru/fakultety/YF/kaf-GP/",
          "Исторических наук и политологии":"https://rsue.ru/fakultety/YF/kaf-INIP/",
          "Конституционного и муниципального права":"https://rsue.ru/fakultety/YF/kaf-KIMP/",
          "Судебной экспертизы и криминалистики":"https://rsue.ru/fakultety/YF/kaf-SEIK/",
          "Теории и истории государства и права":"https://rsue.ru/fakultety/YF/kaf-TIIGIP/",
          "Уголовного и уголовно-исполнительного права, криминологии":"https://rsue.ru/fakultety/YF/kaf-UIUIPK/",
          "Финансового и административного права":"https://rsue.ru/fakultety/YF/kaf-FIAP/",
          "Гражданского процесса":"https://rsue.ru/fakultety/YF/kaf-GrP/"}
lij_fak = {"Иностранных языков для экономических специальностей":"https://rsue.ru/fakultety/FLIZ/kaf-IYDES/",
           "Иностранных языков для гуманитарных специальностей":"https://rsue.ru/fakultety/FLIZ/kaf-IYDGS/",
           "Журналистики":"https://rsue.ru/fakultety/FLIZ/kaf-Z/",
           "Лингвистики и межкультурной коммуникации":"https://rsue.ru/fakultety/FLIZ/kaf-LIMK/",
           "Русского языка и культуры речи":"https://rsue.ru/fakultety/FLIZ/kaf-RYIKR/"}
fak_names = ["Факультет Менеджмента и предпринимательства", "Факультет Торгового дела", "Факультет Компьютерных технологий и информационной безопасности",
             "Учетно-экономический факультет", "Факультет Экономики и финансов", "Юридический факультет", "Факультет Лингвистики и журналистики"]
kaf_names = []
fak = [men_fak, td_fak, ktib_fak, yk_fak, if_fak, uf_fak, lij_fak]

g={}
#for k in fak:
    #kaf_names.append(k.values())
x = 0
for f in fak:
    parsed_kafs = {}
    i=0
    for kaf in f.values():
        #print(kaf)
        resp = req.get(kaf)
        soup = BeautifulSoup(resp.text, features="html.parser")
        teachers = soup.find_all("div", {"class" : "col-lg-5 col-md-5 col-sm-5"})
        k={}
        for t in teachers:
            k[t.find("a").get_text()] ="https://rsue.ru/"+ t.find("a").get("href")
        parsed_kafs[list(f.keys())[i]] = k
        i+=1
    g[fak_names[x]] = parsed_kafs
    x+=1
#print(g)
sqlsaver.fill_teachers(g)