from django.db import models
from django.core.urlresolvers import reverse


class Course(models.Model):
    Course_Name = models.CharField(max_length=45)
    Ranking = models.IntegerField()

    def __unicode__(self):
        return self.Course_Name

    def get_absolute_url(self):
        return reverse('ed4all:course_edit', kwargs={'pk': self.pk})

    class Meta:
        managed = False
        db_table = 'Course'
        app_label = 'ed4all'

class Review(models.Model):
    course = models.ForeignKey(Course, models.DO_NOTHING)
    name = models.CharField(max_length=45)
    review = models.TextField()

    def __unicode__(self):
        return "Review from: " + self.name

    def get_absolute_url(self):
        return reverse('ed4all:review_edit', kwargs={'pk': self.pk})
    class Meta:
        managed = False
        db_table = 'Review'
        app_label = 'ed4all'


