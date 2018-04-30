from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'), #http://localhost:8000/demoapp/
	#http://127.0.0.1:8000/demoapp/template_index/
    #path('route/', views.RouteFormView.as_view(), name='route_form'),
	#http://127.0.0.1:8000/demoapp/update_temperature/
    #path('update_temperature/', views.UpdateTemperatureFormView.as_view(), name='update_temperature_form'),
    path('history/', views.history, name='history'),
    path('status/', views.status, name='status'),
    path('control/', views.control, name='control'),
]
