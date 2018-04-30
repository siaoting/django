from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from datetime import datetime
from django.views.generic.edit import FormView
from demoapp.forms import RouteForm, UpdateTemperatureForm

GOOGLE_API_KEY = ""
# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the iot index.")

def template_index(request):
    template = loader.get_template('demoapp/helloworld.html')
    context = {'current_time': str(datetime.now()),}
    return HttpResponse(template.render(context, request))

class UpdateTemperatureFormView(FormView):
    template_name = 'demoapp/update_temperature_form.html'
    form_class = UpdateTemperatureForm

    def form_valid(self, form):
        city = form.cleaned_data['city']
        temperature = form.update_temperature(city.name)
        template = loader.get_template('demoapp/update_temperature_done.html')
        context = {'temperature': temperature, 'city': city, }
        return HttpResponse(template.render(context, self.request))

class RouteFormView(FormView):
    template_name = 'demoapp/route_form.html'
    form_class = RouteForm

    def form_valid(self, form):
        src = form.cleaned_data['src'].replace(" ", "+")
        dst = form.cleaned_data['dst'].replace(" ", "+")
        #https://developers.google.com/maps/documentation/embed/guide#directions_mode
        template = loader.get_template('demoapp/route_done.html')
        urllink = "https://www.google.com/maps/embed/v1/directions?key=%s&origin=%s&destination=%s" % \
                  (GOOGLE_API_KEY, src, dst)
        context = {'urllink': urllink, }
        return HttpResponse(template.render(context, self.request))


#def welcome(request):
#    template = loader.get_template('chatapp/welcome.html')
#    return HttpResponse(template.render(request=request))


