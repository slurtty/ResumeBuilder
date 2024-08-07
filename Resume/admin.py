from django.contrib import admin

from Resume.models import Profile, Experience, Education, Language, Skill

admin.site.register(Profile)
admin.site.register(Experience)
admin.site.register(Education)
admin.site.register(Language)
admin.site.register(Skill)
