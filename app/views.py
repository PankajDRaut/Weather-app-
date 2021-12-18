from django.shortcuts import render
import json
import urllib.request

# Create your views here.
def main1(request):
    if request.method == 'POST':
        city = request.POST['city']
        res = urllib.request.urlopen('https://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=7e5830072354f43ec28b777855c828a7').read()
        json_data = json.loads(res)
        data = {
            "country_code": str.upper(json_data['sys']['country']),
            "coordinate": str(json_data['coord']['lon']) + ' ' +
            str(json_data['coord']['lat']),
            "temp": str(json_data['main']['temp'])+'k',
            "pressure": str(json_data['main']['pressure']),
            "humidity": str(json_data['main']['humidity']),
        }

    else:
        city = ''
        data = {}
    return render(request, 'main.html', {'city': city, 'data': data})