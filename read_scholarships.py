import json
all_scholarships = []
scholarship_names = []
eligibility = []
awards = []
deadline_dates = []
links = []

# open file and read the content in a list


def get_scholarships(filter_keyword="all"):
    all_scholarships.clear()
    scholarship_names.clear()
    eligibility.clear()
    awards.clear()
    deadline_dates.clear()
    links.clear()
    with open('all_scholarships.txt', 'r') as f:
        for line in f:
            # remove linebreak which is the last character of the string
            scholarship = json.loads(line[:-1])

            # add item to the list
            all_scholarships.append(scholarship)

    for i in all_scholarships:
        if i["websiteName"] == "buddy4study":
            e = i['scholarshipMultilinguals'][0]['applicableFor']
            if filter_keyword != "all" and filter_keyword in e:
                eligibility.append(e)
                scholarship_names.append(i['scholarshipName'])
                awards.append(i['scholarshipMultilinguals'][0]['purposeAward'])
                deadline_dates.append(i['deadlineDate'])
                links.append(i['pageSlug'])
            if filter_keyword == "all":
                eligibility.append(e)
                scholarship_names.append(i['scholarshipName'])
                awards.append(i['scholarshipMultilinguals'][0]['purposeAward'])
                deadline_dates.append(i['deadlineDate'])
                links.append(i['pageSlug'])
        else:
            e = i['applicableFor']
            if filter_keyword != "all" and filter_keyword in e:
                eligibility.append(e)
                scholarship_names.append(i['scholarshipName'])
                awards.append(i['purposeAward'])
                deadline_dates.append(i['deadlineDate'])
                links.append(i['pageSlug'])
            if filter_keyword == "all":
                eligibility.append(e)
                scholarship_names.append(i['scholarshipName'])
                awards.append(i['purposeAward'])
                deadline_dates.append(i['deadlineDate'])
                links.append(i['pageSlug'])
