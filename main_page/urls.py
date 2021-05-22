from django.urls import path
import main_page.views


app_name = 'main_page'

urlpatterns = [
    path('', main_page.views.home, name='home'),
    path('inquire/', main_page.views.inquire, name='inquire'),
    path('H_car_charge/', main_page.views.H_car_charge, name='H_car_charge'),

]

