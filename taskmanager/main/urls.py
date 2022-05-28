from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='home'),
    path('math', views.math),
    path('history', views.history),
    path('ezrahut', views.ezrahut),
    path('hebrew', views.hebrew),
    path('english', views.english),
    path('art', views.art),
    path('russian', views.russian),
]
