from rest_framework.routers import DefaultRouter

from .views import SurveyQuestionViewSet

router = DefaultRouter()
router.register('', SurveyQuestionViewSet)


urlpatterns = router.urls
