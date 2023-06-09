from bs4 import BeautifulSoup
import requests
import pandas as pd
import datetime


current_week = 1
last_sunday = datetime.date(2023, 2, 5)

# Способ получить текущую неделю в семестре на основании сравнения с последним записаным воскресеньем
# (сейчас последнее воскресенье захардкожено)
def update_current_week():
    global current_week, last_sunday
    cur_time = datetime.date.today()
    if cur_time - last_sunday > datetime.timedelta(days=7):
        new_sunday = cur_time - datetime.timedelta((cur_time.weekday() + 1) % 7)
        current_week += (new_sunday - last_sunday).days // 7


# Парсинг таблицы с ссылками на расписание групп
def get_link_table(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'lxml')
    table = soup.find('table', attrs={"cellspacing": "1", "width": "680"})
    rows = []
    for tr in table.findAll('tr'):
        row = []
        for td in tr.find_all('td'):
            text = td.get_text(strip=True).lower()
            a = td.find('a', href=True)
            href = None
            if a != None:
                href = a['href']
                row.append((text, href))
            else:
                row.append(text)
        rows.append(row)

    dftable = pd.DataFrame(rows[1:], columns=rows[0])
    return dftable


# Переход по таблице ссылок и парс главной таблицы расписания
def get_timetable(year, group):
    global current_week
    update_current_week()
    year_column = str(year) + ' курс'
    table = get_link_table('https://rtf.sfedu.ru/raspis/')
    full_link = 'https://rtf.sfedu.ru/raspis/'
    for (name, link) in table[year_column]:
        if name == group.lower():
            full_link += link
            break
    full_link += f"&week={current_week}"
    page = requests.get(full_link)
    soup = BeautifulSoup(page.text, 'lxml')
    table = soup.find('table', attrs={"cellspacing": "3"})
    rows = []
    print(full_link)
    for tr in table.findAll('tr'):
        row = []
        for td in tr.find_all('td'):
            text = td.get_text(' ', strip=True).lower()
            a = td.find('a', href=True)
            href = None
            if a != None:
                href = a['href']
                row.append((text, href))
            else:
                row.append(text)
        rows.append(row)
    #dftable = pd.DataFrame(rows[1:], columns=rows[0])
    # транспонируем получившийся результат для удобства
    return list(map(list, zip(*rows[1:])))

if __name__ == "__main__":
    for row in get_timetable(1, 'РТао1-12'):
        print(row)
    print(current_week)
