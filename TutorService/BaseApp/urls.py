from django.conf.urls import patterns, url
from BaseApp.views import LoginView, add_subject, homepage, mail, views
from BaseApp.decorators import is_anonymous
from django.contrib.auth.decorators import login_required
urlpatterns = patterns('BaseApp.views',
    url(r'^my account/homepage$', login_required(homepage.as_view()), name='homepage'),
    url(r'^my account/views$', views.as_view(), name='views'),
    url(r'^my account/homepage/statement$', login_required(mail.as_view()), name='send_contact_form'),
    url(r'^my account/homepage/page/(?P<page>\d+)$', login_required(homepage.as_view()), name='list_homepage'),
    url(r'^$', is_anonymous(LoginView.as_view()), name='login'),
    url(r'^page/(?P<page>\d+)$', is_anonymous(LoginView.as_view()), name='list'),
    url(r'^logout/$', 'log_out', name='logout'),
    url(r'^registration$', 'registration', name='registration'),
    url(r'^my account/my profile/edit$', 'settings_for_questionnaire', name='settings'),
    url(r'^my account/my profile/add subject$', add_subject.as_view(), name='add_subject'),
)

