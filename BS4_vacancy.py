import requests
from bs4 import BeautifulSoup
from pprint import pprint
from urllib.parse import urljoin


headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'}
url = 'https://hh.ru/search/resume?text=%D0%BE%D1%84%D0%B8%D1%81+%D0%BC%D0%B5%D0%BD%D0%B5%D0%B4%D0%B6%D0%B5%D1%80&logic=normal&pos=full_text&exp_period=all_time&exp_company_size=any&exp_industry=any&area=1424&relocation=living_or_relocation&salary_from=&salary_to=&currency_code=RUR&education=none&age_from=&age_to=&gender=unknown&order_by=relevance&search_period=0&items_on_page=50&no_magic=false'
params = {'search_field': 'name', 'text': '"text=офис+менеджер"', 'page': 0}
session = requests.Session()
response = session.get(url, params=params)



dom = BeautifulSoup(response.text, 'html.parser')
vacancies = dom.find_all('div', {'class': 'resume-search-item__content-wrapper'})


vacancy_list = []
params = {'search_field': 'name', 'text': '"РѕС„РёСЃ РјРµРЅРµРґР¶РµСЂ"', 'page': 0, 'hhtmFrom': 'vacancy_search_list'}
while True:
    response = session.get(url=url, params=params, headers=headers)
    dom = BeautifulSoup(response.text, 'html.parser')
    vacancies = dom.find_all('div', {'class': 'resume-search-item__content-layout'})
    if len(vacancies) == 0:
        break
    params['page'] += 1
    for vacancy in vacancies:
        vacancy_data = {}
        name_of_vacancy = vacancy.find('a', {'class': 'serp-item__name'})
        href = name_of_vacancy.get('href')
        href = urljoin(url, href)
        # href = vacancy.get("//a[@class='serp-item__name']/@href")
        name = name_of_vacancy.text
        age = vacancy.find('div', {'class': 'resume-search-item__fullname'})
        age = age.text
        previose_job = vacancy.find('span', {'class': 'bloko-text bloko-text_strong'})
        # previose_job = previose_job.text
        if previose_job is None:
           previose_job = 'нет инфы'
        else:
            previose_job
        compensation = vacancy.find('div', {'class': 'bloko-text bloko-text_large bloko-text_strong'})
        compensation = compensation.text

        vacancy_data['name'] = name
        vacancy_data['href'] = href
        vacancy_data['website'] = 'hh.ru'
        vacancy_data['age'] = age
        vacancy_data['previose_job'] = previose_job
        vacancy_data['compensation'] = compensation

        vacancy_list.append(vacancy_data)


#
## def process_age(value):
##     value = value.replace('\xa0', ' ')
##     try:
##         value = int(value)
##     except:
##         pass
##     return value

print(len(vacancy_list))
pprint(vacancy_list)