__author__ = '12'
# -*- coding: utf-8 -*-


from django.contrib import admin
from BaseApp.models import CustomUser, Tutor, Additional_information, Pupil, Mail, Messages, Reviews

class ViewDispForCustomUser(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'patronymic', 'last_name', 'email', 'City', 'address')

class ViewDispForTutor(admin.ModelAdmin):
    list_display = ('avatar', 'username', 'experience', 'education', 'work', 'venue_of','rating')

class ViewDispForPupil(admin.ModelAdmin):
    list_display = ('avatar', 'username', 'work')

class ViewDispForAddInf(admin.ModelAdmin):
    list_display = ('tutor', 'subject_name', 'section', 'additions', 'pupil_category', 'price')

class ViewDispForMail(admin.ModelAdmin):
    list_display = ('user', 'from_email', 'from_user', 'date')

class ViewDispForMessages(admin.ModelAdmin):
    list_display = ('subject', 'message')

class ViewDispForReview(admin.ModelAdmin):
    list_display = ('tutor', 'review')


admin.site.register(CustomUser, ViewDispForCustomUser)
admin.site.register(Tutor, ViewDispForTutor)
admin.site.register(Pupil, ViewDispForPupil)
admin.site.register(Additional_information, ViewDispForAddInf)
admin.site.register(Mail, ViewDispForMail)
admin.site.register(Messages, ViewDispForMessages)
admin.site.register(Reviews, ViewDispForReview)