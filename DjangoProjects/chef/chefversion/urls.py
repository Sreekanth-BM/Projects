from django.urls import path
from . import views
from . import chefversion as cv

urlpatterns = [
    path('',views.cv_homepage_view,name='cv_homepage'),
    path('cv_input/',cv.sshing_view,name='cv_solo_input'),
    path('cv_multi_input/',cv.multi_sshing_view,name='cv_multi_input')
]

