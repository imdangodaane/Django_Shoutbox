from django.db import models

# Create your models here.
class Shout(models.Model):
    shout_name = models.CharField(max_length=200)
    shout_text = models.CharField(max_length=200)
    shout_date = models.DateTimeField('date published')

    def __str__(self):
        date = self.shout_date.strftime('(%Y/%m/%d %H:%M:%S)')
        name = self.shout_name
        text = self.shout_text
        content = '-'.join([date, name])
        content = ': '.join([content, text])
        return content
