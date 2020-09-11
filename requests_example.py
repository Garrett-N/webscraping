import requests
from bs4 import BeautifulSoup

BASE_URL = 'https://news.ycombinator.com'
USERNAME = ""
PASSWORD = ""

s = requests.Session()

data = {"gogo": "news", "acct": USERNAME, "pw": PASSWORD}
r = s.post(f'{BASE_URL}/login', data=data)

soup = BeautifulSoup(r.text, 'html.parser')
if soup.find(id='logout') is not None:
	print('Successfuly logged in')
else:
	print('Authentication Error')

r = requests.get('https://news.ycombinator.com')
soup = BeautifulSoup(r.text, 'html.parser')
links = soup.findAll('tr', class_='athing')

formatted_links = []

for link in links:
	data = {
		'id': link['id'],
		'title': link.find_all('td')[2].a.text,
		"url": link.find_all('td')[2].a['href'],
		"rank": int(links[0].td.span.text.replace('.', ''))
	}
	formatted_links.append(data)

print(formatted_links)