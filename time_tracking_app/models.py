from django.db import models


class TimeRecord(models.Model):
    staff_name = models.ForeignKey('StaffName', on_delete=models.CASCADE)
    project_name = models.ForeignKey('Project', on_delete=models.CASCADE)
    date = models.DateField()
    time_start = models.TimeField()
    time_end = models.TimeField(default=None, null=True)
    comment = models.TextField(default='', blank=True)

    def __str__(self):
        return self.staff_name.name + ' - ' + str(self.date) + ' (' + str(self.time_start) + ' to ' + str(self.time_end) + ')'

class StaffName(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Project(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
