import datetime
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Question(models.Model):
    question_text = models.TextField(max_length=500, verbose_name="Question")
    media_url = models.CharField(max_length=200, verbose_name="URL du média")
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200, verbose_name="Réponse")
    response = models.BooleanField(default=0, verbose_name="Bonne réponse")

    def __str__(self):
        return self.choice_text


class HistoryQuestion(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField()
    date = models.DateField()

    def __str__(self):
        return None
