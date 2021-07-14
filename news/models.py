from django.db import models

# Create your models here.


class News(models.Model):
    title = models.CharField(max_length=300)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add = True)
    author = models.CharField(max_length=30)
    label = models.IntegerField()


    def __str__(self):
        return self.title


class UnratedNews(models.Model):
    title = models.CharField(max_length=300)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add = True)
    author = models.CharField(max_length=30)
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return u'/entries/%d' % self.id
