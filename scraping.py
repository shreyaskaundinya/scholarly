import mechanicalsoup
import json
from bs4 import BeautifulSoup

browser = mechanicalsoup.StatefulBrowser()
all_scholarships = []


page_url = "https://www.buddy4study.com/scholarships?filter=eyJSRUxJR0lPTiI6W10sIkdFTkRFUiI6W10sIkVEVUNBVElPTiI6W10sIkNPVU5UUlkiOltdLCJDT1VSU0UiOltdLCJTVEFURSI6W10sIkZPUkVJR04iOltdLCJMRVZFTCI6W10sIlNQRUNJQUwiOltdLCJESVNBQkxFIjpbXSwic29ydE9yZGVyIjoiREVBRExJTkUifQ==&page={}"
for i in range(1, 23):
    site = browser.open(page_url.format(i))
    page = browser.page
    scholarships_script = page.find(
        'script', id="__NEXT_DATA__", type='application/json').string
    data = json.loads(scholarships_script)
    all_scholarships.extend(data['props']['initialState']
                            ['scholarship']['scholarshipList']['scholarships'])


# upcoming scholarships

page_url = "https://www.buddy4study.com/upcoming-scholarships?filter=eyJSRUxJR0lPTiI6W10sIkdFTkRFUiI6W10sIkVEVUNBVElPTiI6W10sIkNPVU5UUlkiOltdLCJDT1VSU0UiOltdLCJTVEFURSI6W10sIkZPUkVJR04iOltdLCJMRVZFTCI6W10sIlNQRUNJQUwiOltdLCJESVNBQkxFIjpbXSwic29ydE9yZGVyIjoiREVBRExJTkUifQ==&page={}"

for i in range(1, 88):
    site = browser.open(page_url.format(i))
    page = browser.page
    scholarships_script = page.find(
        'script', id="__NEXT_DATA__", type='application/json').string
    data = json.loads(scholarships_script)
    all_scholarships.extend(data['props']['initialState']
                            ['scholarship']['scholarshipList']['scholarships'])

with open('all_scholarships.txt', 'w') as f:
    for i in all_scholarships:
        # convert dict to string
        json_type = json.dumps(i)
        f.write('%s\n' % json_type)
