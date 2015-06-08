# See http://docs.python-guide.org/en/latest/scenarios/scrape/
# for a tutorial on scraping html

from lxml import html
import requests
import datetime

page = requests.get('http://www.acueductospr.com/AAARepresas/reservoirlist')
tree = html.fromstring(page.text)

#This will create a list of reservoir levels:
embalses = tree.xpath('//div[@class="locationLevel"]/text()')

today = datetime.date.today()
print str(today),
for location in embalses:
    if location.startswith("Carra"):
        place, level = location.split()
        print level
