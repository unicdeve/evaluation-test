from django.contrib import admin

from .models import Answer, Evaluation, Survey, SurveyQuestion

# Register your models here.
admin.site.register(Survey)
admin.site.register(SurveyQuestion)
admin.site.register(Answer)
admin.site.register(Evaluation)
