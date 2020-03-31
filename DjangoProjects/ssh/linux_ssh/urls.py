from django.urls import path
from . import views
from . import ssh

urlpatterns = [
    path('',views.homepage_view,name='ssh_homepage'),
    path('linux_input/',ssh.sshing_view,name='linux_solo_input'),
    path('linux_multi_input/',ssh.multi_sshing_view,name='linux_multi_input')
]
