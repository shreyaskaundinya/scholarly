import json
# define an empty list
all_scholarships = []

# open file and read the content in a list
with open('all_scholarships.txt', 'r') as f:
    for line in f:
        # remove linebreak which is the last character of the string
        scholarship = json.loads(line[:-1])

        # add item to the list
        all_scholarships.append(scholarship)
