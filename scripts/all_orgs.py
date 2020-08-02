from html.parser import HTMLParser
from students.models import StudentOrganization


class MyHTMLParser(HTMLParser):

    def handle_data(self, data):
        data = data.strip()
        data = data.split('>')
        if len(data) > 1 and data[1] != '' and len(data[1]) > 1:
            print(data[1])
            org = StudentOrganization.objects.create(name=data[1])

filepath = 'data/all_orgs.html'
with open(filepath) as fp:
    line = fp.readline()
    while line:
        parser = MyHTMLParser()
        parser.feed(line)
        line = fp.readline()
