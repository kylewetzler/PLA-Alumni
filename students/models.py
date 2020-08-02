from django.db import models


class OfferedMajor(models.Model):
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=50)

    def __str__(self):
        return self.name + ' ' + self.code


class StudentOrganization(models.Model):
    name = models.CharField(max_length=400)

    def __str__(self):
        return self.name


class GraduationDate(models.Model):
    semester = models.CharField(max_length=6)
    year = models.IntegerField()

    def __str__(self):
        return self.semester + '\t ' + str(self.year)