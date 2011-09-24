# Create your views here.

from django.shortcuts import render_to_response, get_object_or_404
from web.models import Newsarticle, Member, Car, Sponsor

def news(request):
    newsList = Newsarticle.objects.all()
    return render_to_response('web/child_news.html', {'newsList': newsList})
    

def members(request):
    memberList = Member.objects.all()
    return render_to_response('web/child_members.html', {'memberList': memberList})

def memberDetail(request, member_id):
    member = get_object_or_404(Member, pk=member_id)
    return render_to_response('web/child_members_detail.html', {'member': member})

def sponsors(request):
    sponsorList = Sponsor.objects.all()
    return render_to_response('web/child_sponsors.html', {'sponsorList': sponsorList})

def imprint(request):
    return render_tp_response('web/child_imprint.html')
