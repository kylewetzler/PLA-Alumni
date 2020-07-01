import csv
from network.models import Alumni

with open('data/alumni_network.csv', newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    row_count = 0
    for row in csvreader:
        if row_count!= 0:
            email = row[1]
            full_name = row[2]
            hometown = row[3]
            residence = row[4]
            degree = row[5]
            changed_major = row[6]
            original_major = row[7]
            leadership = row[8]
            grad_date = row[9]
            current_occupation = row[10]
            career_long_term = row[11]
            expected_career = row[12]
            career_path = row[13]
            favorites = row[14]
            mentorship_selections = row[15]
            conference_location = row[16]
            conference_topics = row[17]
            contact_method = row[18]

            a = Alumni(email=email,
                       full_name=full_name,
                       hometown=hometown,
                       residence=residence,
                       degree=degree,
                       changed_major=changed_major,
                       original_major=original_major,
                       leadership=leadership,
                       grad_date=grad_date,
                       current_occupation=current_occupation,
                       career_long_term=career_long_term,
                       expected_career=expected_career,
                       career_path=career_path,
                       favorites=favorites,
                       mentorship_selections=mentorship_selections,
                       conference_location=conference_location,
                       conference_topics=conference_topics,
                       contact_method=contact_method
            )
            a.save()
        row_count += 1
        print(row_count)