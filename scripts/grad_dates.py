from students.models import GraduationDate

semesters = ['Spring', 'Summer', 'Fall']
year = 2005

while year < 2101:
    for semester in semesters:
        grad = GraduationDate.objects.create(semester=semester, year=year)
    year += 1