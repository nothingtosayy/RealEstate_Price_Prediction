from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd
import numpy as np
import pickle
import sklearn


# Create your views here.
def home(request):
    return render(request, 'main.html')


def predict_price(location, area, bath, bedrooms):

    file = open("Sav Files\MyModel.sav", 'rb')
    model = pickle.load(file)
    file.close()

    f = open("Sav Files\columns.sav", 'rb')
    cols = pickle.load(f)
    f.close()

    locationList = cols
    loc_index = locationList.index(location)
    a = np.zeros(len(locationList), dtype='int')
    a[0] = bath
    a[1] = bedrooms
    a[2] = area
    if loc_index >= 0:
        a[loc_index] = 1
    # print(locationList)
    return str(round(model.predict([a])[0], 2)) + " " + "Lakh Rupees Only"


def returnPrice(request):
    if request.method == 'POST':
        location = request.POST['location'].lower()
        area = float(request.POST['area'])
        bath = int(request.POST['bath'])
        bedrooms = int(request.POST['bedrooms'])

        res = predict_price(location=location, area=area, bath=bath, bedrooms=bedrooms)
        return render(request, 'result.html', {'res': res})
