from django.contrib import admin
from .models import Reporter,Article,Comment,Contact,UserProfile
# Register your models here.
admin.site.register(Article)
admin.site.register(Comment)
admin.site.register(Reporter)
admin.site.register(Contact)
admin.site.register(UserProfile)
