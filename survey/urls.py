from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import (SurveyEvauluation, SurveyEvauluationReport,
                    SurveyQuestionViewSet)

router = DefaultRouter()
router.register('questions', SurveyQuestionViewSet)

urlpatterns = [
    path('evaluation/', SurveyEvauluation.as_view(), name='survey-evaluation'),
    path('evaluation/report/', SurveyEvauluationReport.as_view(), name='evaluation-report'),
]


urlpatterns += router.urls
