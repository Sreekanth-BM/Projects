from django.urls import path
from . import views
from . import wssh

urlpatterns = [
    path('',views.homepage_view,name='wssh_homepage'),
    path('windows_solo_input/', wssh.solo_winrming, name='windows_solo_input'),
    path('windows_multi_input', wssh.multi_winrming, name='windows_multi_input')
#    path('linux_input/',ssh.sshing_view,name='linux_solo_input'),
#    path('linux_multi_input/',ssh.multi_sshing_view,name='linux_multi_input')
]
