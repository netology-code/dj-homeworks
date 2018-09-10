from django.contrib import admin
from .models import Section, Article, SectionMember

# Register your models here.
admin.site.register(Section)
admin.site.register(Article)
admin.site.register(SectionMember)