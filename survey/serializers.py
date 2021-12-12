from django.conf import settings
from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import Evaluation, SurveyQuestion


class SurveyQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SurveyQuestion
        fields = '__all__'

    
class SurveyEvaluationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evaluation
        fields = '__all__'
