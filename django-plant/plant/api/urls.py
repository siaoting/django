from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
from .views import SetSensorData, GetLastSensorData, GetSensorData

urlpatterns = [
	path('getLastSensorData', GetLastSensorData.as_view(), name = 'getLastSensorData'),
	path('getSensorData', GetSensorData.as_view(), name = 'getSensorData'),
	path('setSensorData', SetSensorData.as_view(), name = 'setSensorData'),

    #path('setLastestTemperature')
	#http://127.0.0.1:8000/demoapp/template_index/
    #path('route/', views.RouteFormView.as_view(), name='route_form'),
	#http://127.0.0.1:8000/demoapp/update_temperature/
    #path('update_temperature/', views.UpdateTemperatureFormView.as_view(), name='update_temperature_form'),
    #path('welcome/', views.welcome, name='welcome'),

]

urlpatterns = format_suffix_patterns(urlpatterns)
