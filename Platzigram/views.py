#Vistas creadas 
from django.http import HttpResponse, JsonResponse
from datetime import datetime
import json

#Para leer los parametros recibidos en la url ?numbers=1,2,3,4
def sort_integers(request):
    numbers = sorted([int(number) for number in request.GET['numbers'].split(',')])
    data = {
        'status' : 200,
        'numbers': numbers,
        'message': 'OK'
    }
    return HttpResponse(
        json.dumps(data,indent=4), 
        content_type = 'application/json'
        )

#Si recibe parametros en el path.py los recibe despues del request
def say_hi(request,name,age):
    if age < 12 :
        message = 'Sorry {}, you are not allowed to pass here'.format(name)
    else:
        message = 'Hello {}, you are in!'.format(name)
    return HttpResponse(message)
    