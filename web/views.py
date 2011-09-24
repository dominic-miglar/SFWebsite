# Create your views here.

from django.shortcuts import render_to_response
from web.models import News, Member

def news(request):
    newsList = News.objects.all()
    return render_to_response('web/child_news.html', {'newsList': newsList})
    

def members(request):
    memberList = Member.objects.all()
    return render_to_response('web/members.html', {'memberList': memberList})
