from django.contrib import admin
from streetfighters.web.models import *



class CarInline(admin.TabularInline):
    model = Car
    extra = 2   
    class Meta:
        verbose_name = 'Auto'

class MemberAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,                  {'fields': [('firstName', 'lastName'), 'job', 'email']}),
        ('Foto', {'fields': ['photo']}),
    ]
    inlines = [CarInline]







class NewsAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Datumsinformationen",         {'fields': ['pub_date']}),
        ("Allgemeine Informationen",    {'fields': ['title']}),
        ("Artikel",                     {'fields': ['header', 'body']}),
    ]


class SponsorAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Allgemeine Informationen",    {'fields': [('name', 'website'), 'descr', 'banner']}),
        ("Gesponsort",                  {'fields': ['sponsored']}),
        ("Sonstiges",                   {'fields': ['otherInfos']}),
    ]




admin.site.register(Member, MemberAdmin)
admin.site.register(Newsarticle, NewsAdmin)
admin.site.register(Sponsor, SponsorAdmin)
