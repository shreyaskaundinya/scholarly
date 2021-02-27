import json

all_scholarships = []
scholarship_names = []
eligibility = []
awards = []
deadline_dates = []
links = []

# open file and read the content in a list


def get_scholarships(filter_keyword=None):
    with open('all_scholarships.txt', 'r') as f:
        for line in f:
            # remove linebreak which is the last character of the string
            scholarship = json.loads(line[:-1])

            # add item to the list
            all_scholarships.append(scholarship)

    for i in all_scholarships:
        scholarship_names.append(i['scholarshipName'])
        eligibility.append(i['scholarshipMultilinguals'][0]['applicableFor'])
        awards.append(i['scholarshipMultilinguals'][0]['purposeAward'])
        deadline_dates.append(i['deadlineDate'])
        links.append(
            "https: // www.buddy4study.com/scholarships/"+i['pageSlug'])
