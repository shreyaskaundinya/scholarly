import mechanicalsoup
import json
from bs4 import BeautifulSoup

browser = mechanicalsoup.StatefulBrowser()
all_scholarships = []


def scrape_buddy4study():
    global browser
    page_url = "https://www.buddy4study.com/scholarships?filter=eyJSRUxJR0lPTiI6W10sIkdFTkRFUiI6W10sIkVEVUNBVElPTiI6W10sIkNPVU5UUlkiOltdLCJDT1VSU0UiOltdLCJTVEFURSI6W10sIkZPUkVJR04iOltdLCJMRVZFTCI6W10sIlNQRUNJQUwiOltdLCJESVNBQkxFIjpbXSwic29ydE9yZGVyIjoiREVBRExJTkUifQ==&page={}"

    for i in range(1, 23):
        browser.open(page_url.format(i))
        page = browser.page
        scholarships_script = page.find(
            'script', id="__NEXT_DATA__", type='application/json').string
        data = json.loads(scholarships_script)
        all_scholarships.extend(data['props']['initialState']
                                ['scholarship']['scholarshipList']['scholarships'])

    # upcoming scholarships

    page_url = "https://www.buddy4study.com/upcoming-scholarships?filter=eyJSRUxJR0lPTiI6W10sIkdFTkRFUiI6W10sIkVEVUNBVElPTiI6W10sIkNPVU5UUlkiOltdLCJDT1VSU0UiOltdLCJTVEFURSI6W10sIkZPUkVJR04iOltdLCJMRVZFTCI6W10sIlNQRUNJQUwiOltdLCJESVNBQkxFIjpbXSwic29ydE9yZGVyIjoiREVBRExJTkUifQ==&page={}"

    for i in range(1, 88):
        browser.open(page_url.format(i))
        page = browser.page
        scholarships_script = page.find(
            'script', id="__NEXT_DATA__", type='application/json').string
        data = json.loads(scholarships_script)
        all_scholarships.extend(data['props']['initialState']
                                ['scholarship']['scholarshipList']['scholarships'])


scrape_buddy4study()

with open('all_scholarships.txt', 'w') as f:
    for i in all_scholarships:
        # convert dict to string
        json_type = json.dumps(i)
        f.write('%s\n' % json_type)

'''
gov_url = "https://scholarships.gov.in/"

browser.open(gov_url)
gov_scholarships = browser.page.find_all("div", class_="col-md-5")

gov_scholarships = [i for i in gov_scholarships if i.text != ""]

for i in gov_scholarships:
    print(i.text.strip())
'''

'''url = "https://www.letsintern.com/internships"
browser.open(url)
print(browser.page.find("div", class_="single-job-card"))'''
