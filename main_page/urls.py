from django.urls import path
import main_page.views

app_name = 'main_page'

urlpatterns = [
    path('', main_page.views.home, name='home'),
]