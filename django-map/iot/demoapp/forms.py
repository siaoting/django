from django import forms
from demoapp.models import City
from weather import Weather, Unit


class UpdateTemperatureForm(forms.Form):
    city = forms.ModelChoiceField(queryset=City.objects.all(),
                  to_field_name="name",
                  label="City", empty_label=None)
    
    def update_temperature(self, city):
        weather = Weather(unit=Unit.CELSIUS)
        location = weather.lookup_by_location(city)
        #print(city, location.location().city())
        temperature = location.condition().temp()
        db_city = City.objects.filter(name__contains=city)
        db_city.update(temperature=temperature)
        return temperature

class RouteForm(forms.Form):
    # update temperature
    cities = City.objects.all()
    choices = []
    weather = Weather(unit=Unit.CELSIUS)
    for city in cities:
        location = weather.lookup_by_location(city)
        temperature = location.condition().temp()
        db_city = City.objects.filter(name__contains=city)
        db_city.update(temperature=temperature)

        choices.append((city, "%s(%s°c)" % (city, temperature)))

        src = forms.ChoiceField(choices=choices, label="Source City")
        dst = forms.ChoiceField(choices=choices, label="Destination City")
    #src = forms.ModelChoiceField(queryset=City.objects.all(), 
    #              label="Source City", empty_label=None)
    #dest = forms.ModelChoiceField(queryset=City.objects.all(), 
    #              label="Destination City", empty_label=None)


    #message = forms.CharField(widget=forms.Textarea)

    #def send_email(self):
    #    # send email using the self.cleaned_data dictionary
    #    pass
