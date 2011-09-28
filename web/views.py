# Create your views here.

from django.shortcuts import render_to_response, get_object_or_404, RequestContext
from web.models import Newsarticle, Member, Car, Sponsor

def news(request):
    newsList = Newsarticle.objects.all()
    return render_to_response('web/child_news.html', {'newsList': newsList}, context_instance=RequestContext(request))

def members(request):
    memberList = Member.objects.all()
    return render_to_response('web/child_members.html', {'memberList': memberList}, context_instance=RequestContext(request))

def memberDetail(request, member_id):
    member = get_object_or_404(Member, pk=member_id)
    if member:
        carList = member.car_set.all()
    return render_to_response('web/child_members_detail.html', {'member': member, 'carList': carList}, context_instance=RequestContext(request))

def sponsors(request):
    sponsorList = Sponsor.objects.all()
    return render_to_response('web/child_sponsors.html', {'sponsorList': sponsorList}, context_instance=RequestContext(request))

def imprint(request):
    return render_to_response('web/child_imprint.html', context_instance=RequestContext(request))

def contact(request):
    return render_to_response('web/child_contact.html', context_instance=RequestContext(request))
