from django.http import request
from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Tag, Profile, LikesForQuestion, Question, LikesForAnswer, Answer 

# Create your views here.

def updateBaseTags():
    popular_tags = Tag.objects.popular()
    content = {
        'tags': popular_tags
    }
    return render('base.html', content)

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
    popular_tags = Tag.objects.popular()[:10]
    hot_questions = Question.objects.popular()
    hot_questions_per_page = paginate(hot_questions, request, 10)
    content = {
        'popular_tags' : popular_tags,
        'questions' : hot_questions_per_page,
    }
    return render(request, 'hot.html', content)


def new(request):
    popular_tags = Tag.objects.popular()[:10]
    questions = Question.objects.new()
    new_questions_per_page = paginate(questions, request, 10)
    content = {
        'popular_tags' : popular_tags,
        'questions' : new_questions_per_page,
    }
    return render(request, 'new.html', content)


def tag(request, id):
    popular_tags = Tag.objects.popular()[:10]
    tag = Tag.objects.get(id=id)
    questions = Question.objects.tag(tag)
    questions_per_page = paginate(questions, request, 10)
    content = {
        'tag' : tag,
        'popular_tags' : popular_tags,
        'questions_count' : questions.count,
        'questions': questions_per_page
    }
    return render(request, 'tag.html', content)


def question(request, id):
    popular_tags = Tag.objects.popular()[:10]
    question = Question.objects.get(id=id)
    answers = Answer.objects.get_answers(question)
    answers_by_page = paginate(answers, request, 5)
    content = {
        'popular_tags' : popular_tags,
        'question' : question,
        'answers' : answers_by_page 
    }
    return render(request, 'question.html', content)


def login(request):
    popular_tags = Tag.objects.popular()[:10]
    content = {
        'popular_tags' : popular_tags,
    }
    return render(request, 'login.html', content)


def signup(request):
    popular_tags = Tag.objects.popular()[:10]
    content = {
        'popular_tags' : popular_tags,
    }
    return render(request, 'register.html', content)


def ask(request):
    popular_tags = Tag.objects.popular()[:10]
    content = {
        'popular_tags' : popular_tags,
    }
    return render(request, 'ask.html', content)
