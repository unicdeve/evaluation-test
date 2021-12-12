from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import SurveyEvauluation, SurveyQuestionViewSet

router = DefaultRouter()
router.register('questions', SurveyQuestionViewSet)

urlpatterns = [
    path('evaluation/', SurveyEvauluation.as_view(), name='survey-evaluation'),
]


urlpatterns += router.urls
