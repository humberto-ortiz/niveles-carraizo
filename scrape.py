# http://docs.python-guide.org/en/latest/scenarios/scrape/

from lxml import html
import requests
import datetime

page = requests.get('http://www.acueductospr.com/NIVELES_COE/niveles.html')
tree = html.fromstring(page.text)

#This will create a list of embalses:
embalses = tree.xpath('//h3/strong/text()')

today = datetime.date.today()
print str(today), embalses[1]
