from django.db.models import Q
from django.shortcuts import get_object_or_404
from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Evaluation, Survey, SurveyQuestion
from .serializers import SurveyEvaluationSerializer, SurveyQuestionSerializer


class SurveyQuestionViewSet(viewsets.ViewSet):
    permission_classes = (IsAuthenticated, )
    queryset = SurveyQuestion.objects.all()
    serializer_class = SurveyQuestionSerializer

    def list(self, request):
        survey_id = request.query_params.get('survey_id')
        qs = SurveyQuestion.objects.filter(survey=survey_id)
        serializer = SurveyQuestionSerializer(qs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class SurveyEvauluation(APIView):
    def post(self, request, *args, **kwargs):
        '''
            You should pass an array of answer objects

            [
                {
                    "question": 1,
                    "answer": 0.2
                }
            ]
            where question is the question_number
        '''
        survey_id = request.query_params.get('survey_id', None)
        data = request.data

        if survey_id is None:
            return Response({ "message": "You must pass the survey_id as a query parameter"}, status=status.HTTP_400_BAD_REQUEST)

        # find survey
        survey = get_object_or_404(Survey, pk=survey_id)

        if len(data) != 10:
            return Response({ "message": "You must answer all 10 questions."}, status=status.HTTP_400_BAD_REQUEST)

        accessibility_questions_answers = [] 
        navigation_questions_answers = []
        attractiveness_questions_answers= [] 
        understanability_questions_answers = []
        
        # get all question categories
        for d in data:
            if d["question"] == 1 or d["question"] == 2 or d["question"] == 7 or d["question"] == 10:
                accessibility_questions_answers.append(d["answer"])
            
            if d["question"] == 3 or d["question"] == 5:
                navigation_questions_answers.append(d["answer"])
            
            if d["question"] == 8 or d["question"] == 9:
                attractiveness_questions_answers.append(d["answer"])

            if d["question"] == 4 or d["question"] == 6:
                understanability_questions_answers.append(d["answer"])

        # Final calculations for each category
        accessibility = sum(accessibility_questions_answers) / 4
        navigation = sum(navigation_questions_answers) / 2
        attractiveness = sum(attractiveness_questions_answers) / 2
        understanability = sum(understanability_questions_answers) / 2
        
        # store user's response
        evaluation = Evaluation.objects.create(
            accessibility=accessibility, 
            navigation=navigation, 
            attractiveness=attractiveness,
            understanability=understanability,
            user=request.user,
            survey=survey,
        )

        evaluation_qs = SurveyEvaluationSerializer(evaluation, many=False)

        return Response(evaluation_qs.data, status=status.HTTP_200_OK)


