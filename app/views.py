from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Tag, Profile, LikesForQuestion, Question, LikesForAnswer, Answer 

# Create your views here.

questions = [
    {
        "title": f"Title {i}",
        "text": f"Text for {i} question"
    } for i in range(100)
]

qa = [
    {
        "title": f"Title {i}",
        "text": f"{i} answer on question"
    } for i in range(4)
]

def paginate(objects, request, per_page = 10):
    paginator = Paginator(objects, per_page)
    page = request.GET.get('page')
    return paginator.get_page(page)


def settings(request):
    return render(request, 'settings.html', {})


def index(request):
    num_questions = Question.objects.all().count()
    likes_4q_count = LikesForQuestion.objects.all().count()
    num_profiles = Profile.objects.all().count()
    num_answers = Answer.objects.all().count()
    likes_4a_count = LikesForAnswer.objects.all().count()
    num_tags = Tag.objects.all().count() 
    content = {
        'num_questions' : num_questions,
        'likes_4q_count': likes_4q_count,
        'num_profiles' : num_profiles,
        'num_answers' : num_answers,
        'likes_4a_count': likes_4a_count,
        'num_tags'  : num_tags 
    }
    return render(request, 'index.html', context=content)


def hot(request):
    hot_questions = Question.objects.popular()[:100]
    hot_questions_per_page = paginate(hot_questions, request, 5)
    content = {
        'questions' : hot_questions_per_page,
    }
    return render(request, 'hot.html', content)


def new(request):
    questions = Question.objects.popular()[:100]
    content = paginate(questions, request, 5)
    return render(request, 'new.html', {'questions': content})


def tag(request, id):
    tag = Tag.objects.get(id=id)
    questions = Question.objects.tag(tag)
    questions_per_page = paginate(questions, request, 10)
    content = {
        'tag' : tag,
        'questions_count' : questions.count,
        'questions': questions_per_page
    }
    return render(request, 'tag.html', content)


def question(request, id):
    question = Question.objects.get(id=id)
    answers = Answer.objects.get_answers(question)
    answers_by_page = paginate(answers, request, 5)
    content = {
        'question' : question,
        'answers' : answers_by_page 
    }
    return render(request, 'question.html', content)


def login(request):
    return render(request, 'login.html', {})


def signup(request):
    return render(request, 'register.html', {})


def ask(request):
    return render(request, 'ask.html', {})
