from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Question
from django.utils import timezone
from .forms import QuestionForm, AnswerForm
from django.core.paginator import Paginator
from django.contrib import messages

def index(request):
    question_list = Question.objects.order_by('-create_date')
    page = request.GET.get('page', '1') #어떤 페이지를 보고 있을지 전달받는다. 전달되는게 없으면 기본적으로 1을받는다는 의미.
    paginator = Paginator(question_list, 10)  # 페이지당 10개씩 보여주겠다는 의미.
    question_list = paginator.get_page(page)  # page에 담긴 페이지에 해당하는 리스트를 담는다.
    context = {'question_list': question_list}
    return render(request, 'pybo/question_list.html', context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'pybo/question_detail.html', context)
     # 모델의 기본키를 이용하여 모델객체 한 건을 반환함. pk에 해당하는 건이 없으면 오류 대신 404 페이지를 반환


def question_create(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.writer = request.user
            question.create_date = timezone.now()
            question.save()
            return redirect('pybo:index')
    else:
        form = QuestionForm()
    context = {'form': form}
    return render(request, 'pybo/question_form.html', context)


def answer_create(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if not request.user.is_superuser:   # 관리자green으로 로그인시 답변기능 활성화, 일반유저는 불가
          messages.error(request, '권한이 없습니다')
          return redirect('pybo:detail', question_id=question.id)

    # 리퀘스트 받은 from의 메소드가 POST라면
    if request.method == "POST":
       form = AnswerForm(request.POST)

       if form.is_valid():
          answer = form.save(commit=False)
          answer.writer = request.user
          answer.create_date = timezone.now()
          answer.question = question
          answer.save()
          return redirect('pybo:detail',question_id=question.id)
    else:
        form = AnswerForm()
        context = {'question': question, 'form': form}
    return render(request, 'pybo/question_detail.html', context)
