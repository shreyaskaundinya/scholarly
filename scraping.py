from bs4 import BeautifulSoup
import mechanicalsoup
import json
import re
browser = mechanicalsoup.StatefulBrowser()
all_scholarships = []


def get_data():
    global browser

    # Scraping buddy4study

    # current scholarships
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

    with open('all_scholarships.txt', 'w') as f:
        for i in all_scholarships:
            # convert dict to json
            i["websiteName"] = "buddy4study"
            i["pageSlug"] = "https://www.buddy4study.com/" + i["pageSlug"]
            json_type = json.dumps(i)
            f.write('%s\n' % json_type)

    # Scraping Study Abroad Shiksha -------------------------------------------------------------------
    url2 = "https://studyabroad.shiksha.com/scholarships/bachelors-courses-{}?ss=240"

    with open('all_scholarships.txt', 'a') as f:
        for i in range(1, 6):
            browser.open(url2.format(i))
            page = browser.page

            scholarship_container = page.find("div", id="tuples")
            scholarship_cards = scholarship_container.find_all(
                "div", class_="card")

            for i in scholarship_cards:
                s = {}
                details = i.find("div", class_="dtls-bar")
                s['websiteName'] = "shiksha"
                s['scholarshipName'] = i.find("a").text.strip()
                s['applicableFor'] = details.find_all(
                    "div", class_="n-col-1")[0].find("p", class_="fnt-sbold").text.strip()
                s['purposeAward'] = details.find_all(
                    "div", class_="n-col-1")[1].find("p", class_="fnt-sbold").text.strip()
                s['deadlineDate'] = details.find_all(
                    "div", class_="n-col-3")[1].find("p", class_="fnt-sbold").text.strip()
                try:
                    s['pageSlug'] = i.find("a").href
                except:
                    s['pageSlug'] = ""
                # convert dict to json
                json_type = json.dumps(s)
                f.write('%s\n' % json_type)

    # Scraping Get My Uni -----------------------------------------------------------------------------
    urll = "https://www.getmyuni.com/scholarships"
    browser.open(urll)
    page = browser.page

    scholarship_container = page.find("div", id="scholarship_container")
    all_scholarship_cards = scholarship_container.find_all(
        "div", class_="info-card")
    details = scholarship_container.find_all("div", class_="hidden-sm")

    with open('all_scholarships.txt', 'a') as f:
        for i in all_scholarship_cards:
            scholarship_details = [j for j in i.find_all(
                "div", class_="hidden-sm")[1].text.strip().split("\n") if j != ""]
            name = i.find_all("p", class_="no-margin")[0].text.strip()
            link = i.find('a', href=True)
            if link is not None:
                link = link.attrs['href']
            s = {}
            s['websiteName'] = "getmyuni"
            s['scholarshipName'] = name
            s['applicableFor'] = scholarship_details[2].strip()
            s['purposeAward'] = scholarship_details[1].strip()
            s['deadlineDate'] = scholarship_details[0].strip()
            s['pageSlug'] = link
            # convert dict to json
            json_type = json.dumps(s)
            f.write('%s\n' % json_type)
