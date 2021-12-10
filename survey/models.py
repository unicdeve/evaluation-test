from django.contrib.auth import get_user_model
from django.db import models

UserModel = get_user_model()

# Create your models here.
class Survey(models.Model):
  user = models.ForeignKey(UserModel, on_delete=models.SET_NULL, null=True, blank=True, related_name='surveys')
  title = models.CharField(max_length=50, unique=True)


class SurveyQuestion(models.Model):
  QUESTION_TYPE_CHOICES = (
        ('accessibility_question', 'Accessibility question'),
        ('navigation_question', 'Navigation question'),
        ('attractiveness_question', 'attractiveness question'),
        ('understanability_question', 'understanability question'),
    )

  user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='survey_questions')
  question = models.CharField(max_length=150)
  question_type = models.CharField(max_length=150, choices=QUESTION_TYPE_CHOICES)
  question_number = models.IntegerField()

  class Meta:
    unique_together = [['question_number', 'question']]
    order_with_respect_to = 'question_number'


class Answer(models.Model):
  question = models.ForeignKey(SurveyQuestion, on_delete=models.CASCADE, related_name='question_answers')
  survey = models.ForeignKey(Survey, on_delete=models.CASCADE, related_name='answers')
  user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='user_answers')
  value = models.FloatField(max_length=10)


  class Meta:
    order_with_respect_to = 'question'


