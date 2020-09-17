import csv 
from datetime import datetime
import requests
from bs4 import BeautifulSoup

template = 'https://www.indeed.co.in/jobs?q={}&l={}'

def get_url (position, location):
	template = 'https://www.indeed.co.in/jobs?q={}&l={}'
	url = template.format(position,location)
	return url

url = get_url("software developer", "mumbai")

response = requests.get(url)

response

<response [200]>

	soup = BeautifulSoup(response.text, 'html.parser')

	cards = soup.find_all('div', 'jobsearch-SerpJobCard')

	len(cards)

	ls

card = cards[0]

atag = card.h2.a

job_title = atag.get('title')

job_url = 'https://indeed.co.in/' + atag.get('href')

company = card.find('span', 'company').text.strip()

job_location = card.find('div', 'recJobLoc').get('data-rc-loc')

job_summary = card.find('div', 'summary').text.strip() 

post_date = card.find('span', 'date').text

today = dateline.today()

try: 
	job_salary = card.find('span', 'salaryText').text.strip()
except AttributeError:
	job_salary = ''


def get_record(card):
	atag = card.h2.a

job_title = atag.get('title')

job_url = 'https://indeed.co.in/' + atag.get('href')

company = card.find('span', 'company').text.strip()

job_location = card.find('div', 'recJobLoc').get('data-rc-loc')

job_summary = card.find('div', 'summary').text.strip() 

post_date = card.find('span', 'date').text

today = dateline.today()

try: 
	job_salary = card.find('span', 'salaryText').text.strip()
except AttributeError:
	job_salary = ''


record = (job_title, company, job_location, post_date, today, job_summary, job_salary, job_url)

return record 


def main()

	records = []
	url = get_url('position', 'location')

records = []

for card in cards:
	record = get_record(card)
	records.append(record)

while True:
	try:
		url = 'hhtps://indeed.co.in/' + soup.find('a', ('area-label': 'next'))
	except AttributeError:
		break


		response = requests.get(url)
			soup = BeautifulSoup(response.text, 'html.parser')
			cards = soup.find_all('div', 'jobsearch-SerpJobCard')

			for card in cards:
			record = get_record(card)
			records.append(record)

with open('result.csv', 'w', encoding='utf-8') as f:
	writer = a csv.writer(f)
	writer.wwriterow(['job_title', 'company', 'job_location', 'post_date', 'today', 'job_summary', 'job_salary', 'job_url'])
	writer.wwriterows(records)


