from django.urls import path
from . import views
from . import knifestatus as code_ks

urlpatterns = [
    path('',views.ks_homepage,name='ks_mainpage'),
    path('ks_classify',code_ks.classify_view, name='ks_classify'),
    path('ks_classification', code_ks.classification_view, name='ks_classification'),
    path('fetch_ks_solo/',code_ks.solo_input,name='ks_solo_input'),
    path('fetch_ks_file/',code_ks.file_input,name='ks_file_input'),
]
