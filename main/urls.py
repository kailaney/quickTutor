from django.urls import path

from . import views

app_name = 'login'
urlpatterns = [
    path('', views.login, name='login'),
    path('loggedIn', views.loggedin, name='loggedin'),
    path('home', views.home, name = 'home'),
    path('tutoring', views.tutoring, name='tutor'),
    path('tuteeing', views.tuteeing, name='tutee'),
    path('newprofile',views.newprofile,name='newprofile'),
    path('userprofile',views.userprofile,name='userprofile'),
    path('question/', views.question, name='question'),
    path('results/', views.results, name='results')
]