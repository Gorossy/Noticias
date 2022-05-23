from django.shortcuts import render
from pkg_resources import empty_provider
import requests
# Create your views here.

def index(request):
    #r = requests.get('http://api.mediastack.com/v1/news?access_key=44d7392c6d00fbc65d5907678f788beb&countries=co&languages=es&limit=20&sort=published_desc')
    r = requests.get('https://newsapi.org/v2/top-headlines?'
        'country=co&'
        'language=es&'
        'apiKey=5a4d363171aa476788659a53b1cc999f')
    res = r.json()
    data = res['articles']
    title = []
    description = []
    urlToImage = []
    url = []
    for i in data:
            title.append(i['title'])
            description.append(i['description'])
            urlToImage.append(i['urlToImage'])
            url.append(i['url'])
    news = zip(title,description,urlToImage,url)
    context = {'news':news}
    return render(request, 'index.html', context)
