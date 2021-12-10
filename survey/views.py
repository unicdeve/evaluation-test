from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import SurveyQuestion
from .serializers import SurveyQuestionSerializer


class SurveyQuestionViewSet(viewsets.ViewSet):
    permission_classes = (IsAuthenticated, )
    queryset = SurveyQuestion.objects.all()
    serializer_class = SurveyQuestionSerializer

    def list(self, request):
        survey_id = request.query_params.get('survey_id')
        qs = SurveyQuestion.objects.filter(survey=survey_id)
        serializer = SurveyQuestionSerializer(qs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


