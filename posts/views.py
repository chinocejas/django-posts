from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime 

# Create your views here.
posts = [
    {
        'name': 'Pepito uno',
        'user': 'pepitouno',
        'timestamp': datetime.now().strftime('%b %d %Y - %H:%M'),
        'picture':'https://picsum.photos/id/618/200/200',
    },
        {
        'name': 'Pepito dos',
        'user': 'pepitodos',
        'timestamp': datetime.now().strftime('%b %d %Y - %H:%M'),
        'picture':'https://picsum.photos/id/356/200/200',  
    },
    {
        'name': 'Pepito tres',
        'user': 'pepitotres',
        'timestamp': datetime.now().strftime('%b %d %Y - %H:%M'),
        'picture':'https://picsum.photos/id/192/200/200',
    }
]
def list_posts(request):
    content = []

    #Renderiza la pag pasada como parametro. Pode fectro /templates/..
    return render(request,'feed.html',{'posts':  posts})