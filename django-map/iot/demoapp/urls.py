from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'), #http://localhost:8000/demoapp/
	#http://127.0.0.1:8000/demoapp/template_index/
    path('template_index/', views.template_index, name='template_index'),
	#http://127.0.0.1:8000/demoapp/route/
    path('route/', views.RouteFormView.as_view(), name='route_form'),
	#http://127.0.0.1:8000/demoapp/update_temperature/
    path('update_temperature/', views.UpdateTemperatureFormView.as_view(), name='update_temperature_form'),
    #path('welcome/', views.welcome, name='welcome'),

]
