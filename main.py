import json

test_list =\
    [{"Title":"Harry Potter", "DVD":"T", "Form":"C", "Genre":"Fantasy", "Date":"2003", "Alt Title 1":"", "Alt Title 2":"", "Count":1, \
    "Director":"Jon","Writer":"Rowling", "Language":"English", "Date Watched":"2019", "Spec":""}, \
    {"Title":"Transformers", "DVD":"F", "Form":"B", "Genre":"Action", "Date":"2005", "Alt Title 1":"Worst Movie", "Alt Title 2":"", "Count":1, \
    "Director":"Mike","Writer":"Bay", "Language":"English", "Date Watched":"2010", "Spec":""}]

#Create dict of various columns requested by user
database = []

#for loop to put test list into database
for entry in test_list:
    database.append(test_list)
final_database = json.dumps(database)
with open ('final_database.json','w') as outfile:
    json.dump(final_database,outfile)