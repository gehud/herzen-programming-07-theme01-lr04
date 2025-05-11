from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Survey, Question, Choice, Response, Answer
from .forms import SurveyForm

def home(request):
    surveys = Survey.objects.all()
    return render(request, 'polls/home.html', {'surveys': surveys})

@login_required
def survey_create(request):
    if request.method == 'POST':
        form = SurveyForm(request.POST)
        if form.is_valid():
            survey = form.save(commit=False)
            survey.creator = request.user
            survey.save()
            messages.success(request, 'Survey created successfully!')
            return redirect('survey_detail', pk=survey.pk)
    else:
        form = SurveyForm()
    return render(request, 'polls/survey_create.html', {'form': form})

def survey_detail(request, pk):
    survey = get_object_or_404(Survey, pk=pk)
    return render(request, 'polls/survey_detail.html', {'survey': survey})

@login_required
def survey_vote(request, pk):
    survey = get_object_or_404(Survey, pk=pk)
    question = survey.questions.first()  # Simplified for single question surveys

    if request.method == 'POST':
        choice_id = request.POST.get('choice')
        if choice_id:
            choice = Choice.objects.get(pk=choice_id)
            response = Response.objects.create(survey=survey, user=request.user)
            Answer.objects.create(response=response, choice=choice)
            messages.success(request, 'Your vote has been recorded!')
            return redirect('survey_results', pk=survey.pk)
        else:
            messages.error(request, 'Please select an option')

    return render(request, 'polls/survey_vote.html', {
        'survey': survey,
        'question': question,
    })

def survey_results(request, pk):
    survey = get_object_or_404(Survey, pk=pk)
    question = survey.questions.first()

    # Get vote counts for each choice
    results = []
    for choice in question.choices.all():
        count = Answer.objects.filter(choice=choice).count()
        results.append({
            'choice': choice,
            'count': count,
            'percentage': count / question.answers.count() * 100 if question.answers.count() > 0 else 0
        })

    return render(request, 'polls/survey_results.html', {
        'survey': survey,
        'question': question,
        'results': results,
    })
