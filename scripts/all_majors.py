from students.models import Major

filepath = 'data/all_majors.html'
with open(filepath) as fp:
    line = fp.readline()
    span = False
    current_major = ''
    all_majors = []
    while line:
        if "<button" in line and span:
            span = False
            all_majors.append(current_major)
            current_major = ''
        if span:
            current_major += line
        if "accordion__item__heading" in line:
            span = True
            current_major += line
        line = fp.readline()
    for major in all_majors:
        major = major.replace('\r', '')
        major = major.replace('\n', '')

        processed = major.split('>')

        name = processed[2]
        name = name.replace('<span', '')
        name = ' '.join(name.split())

        code = processed[3]
        code = code.replace('</span', '')
        code = code.replace('(', '')
        code = code.replace(')', '')

        m = Major.objects.create(name=name, code=code)