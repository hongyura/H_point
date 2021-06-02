from django.urls import path
import main_page.views


app_name = 'main_page'

urlpatterns = [
    path('', main_page.views.home, name='home'),
    path('inquire/', main_page.views.inquire, name='inquire'),
    path('H_car_recap/', main_page.views.H_car_recap, name='H_car_recap'),
    path('Related_Sites/', main_page.views.Related_Sites, name='Related_Sites'),
    path('H_car_charge/', main_page.views.H_car_charge, name='H_car_charge'),
    path('prediction/', main_page.views.prediction, name='prediction'),
    path('material/', main_page.views.material, name='material'),
    path('press_release/', main_page.views.press_release, name='press_release'),

]




