from django.http import HttpResponse, HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.urls import reverse
from .models import Notice
from users.models import User
from django.core.paginator import Paginator


def index(request):
    notice_list = Notice.objects.order_by('-registered_date')
    paginator = Paginator(notice_list, 10)
    page = request.GET.get('page', '1')
    notice_list = paginator.get_page(page)
    context = {'notice_list':notice_list}

    return render(request,'notice/notice_list.html', context)

def detail(request, notice_id):
    notice = get_object_or_404(Notice, pk=notice_id)
    context = {'notice': notice}
    return render(request, 'notice/notice_detail.html', context)

def write(request):
    return render(request, 'notice/write.html')










