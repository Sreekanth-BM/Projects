from django.urls import path
from . import views
from . import runlists as rl

urlpatterns = [
    path('',views.homepage,name='runlist_mainpage'),
    path('append/',views.input_page,name='append_to_runlist'),
    path('append_from_solo/',rl.solo_input,name='runlist_solo_input'),
    path('append_from_file/',rl.file_input,name='runlist_file_input')
]
