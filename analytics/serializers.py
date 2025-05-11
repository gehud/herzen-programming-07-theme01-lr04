from rest_framework import serializers
from polls.models import Response, Survey, Question, Choice

class ChoiceSerializer(serializers.ModelSerializer):
    vote_count = serializers.SerializerMethodField()
    vote_percentage = serializers.SerializerMethodField()

    class Meta:
        model = Choice
        fields = ['id', 'text', 'vote_count', 'vote_percentage']

    def get_vote_count(self, obj):
        return obj.answers.count()

    def get_vote_percentage(self, obj):
        question = obj.question
        total = question.answers.count()
        return (obj.answers.count() / total * 100) if total > 0 else 0

class QuestionSerializer(serializers.ModelSerializer):
    choices = ChoiceSerializer(many=True, read_only=True)
    total_votes = serializers.SerializerMethodField()

    class Meta:
        model = Question
        fields = ['id', 'text', 'choices', 'total_votes']

    def get_total_votes(self, obj):
        return obj.answers.count()

class SurveySerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True, read_only=True)
    total_votes = serializers.SerializerMethodField()
    created_at = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')

    class Meta:
        model = Survey
        fields = ['id', 'title', 'created_at', 'total_votes', 'questions']

    def get_total_votes(self, obj):
        return Response.objects.filter(survey=obj).count()
