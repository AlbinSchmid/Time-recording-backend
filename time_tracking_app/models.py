from django.db import models


class TimeRecord(models.Model):
    staff_name = models.ForeignKey('StaffName', on_delete=models.CASCADE)
    project_name = models.ForeignKey('Project', on_delete=models.CASCADE)
    time_start = models.DateTimeField()
    time_end = models.DateTimeField(default=None, null=True)
    comment = models.TextField(default='', blank=True)

class StaffName(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Project(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
