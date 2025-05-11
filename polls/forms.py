from django import forms
from .models import Survey, Question

class SurveyForm(forms.ModelForm):
    choices = forms.CharField(
        widget=forms.Textarea,
        help_text="Enter choices, one per line",
        required=False
    )

    class Meta:
        model = Survey
        fields = ['title']

    def save(self, commit=True):
        survey = super().save(commit=commit)
        question_text = self.cleaned_data.get('question_text', '')
        choices_text = self.cleaned_data.get('choices', '')

        if question_text:
            question = Question.objects.create(
                survey=survey,
                text=question_text
            )

            if choices_text:
                for choice in choices_text.split('\n'):
                    choice = choice.strip()
                    if choice:
                        question.choices.create(text=choice)

        return survey
