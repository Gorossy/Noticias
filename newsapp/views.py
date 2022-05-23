from django.shortcuts import render
from pkg_resources import empty_provider
import requests
# Create your views here.

def index(request):
    r = requests.get('http://api.mediastack.com/v1/news?access_key=44d7392c6d00fbc65d5907678f788beb&countries=co&languages=es&limit=20&sort=published_desc')
    res = r.json()
    data = res['data']
    title = []
    description = []
    image = []
    url = []
    for i in data:
            title.append(i['title'])
            description.append(i['description'])
            image.append(i['image'])
            url.append(i['url'])
    news = zip(title,description,image,url)
    context = {'news':news}
    return render(request, 'index.html', context)
