from django.urls import path
from . import views

app_name = 'notice'

urlpatterns = [
      path('', views.index, name='index'),
      path('<int:notice_id>/', views.detail, name='detail'),

]



