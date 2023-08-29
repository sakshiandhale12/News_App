from django.shortcuts import render
import requests
API_KEY = '7941071fa56745ccace716da05b4a8c1'


# Create your views here.

def home(request):
    country = request.GET.get('country')
    category = request.GET.get('category')
    
    if country:
        url= f'https://newsapi.org/v2/top-headlines?country={country}&apiKey={API_KEY}'
        # url=f'https://newsapi.org/v2/everything?q=tesla&from=2023-07-21&sortBy=publishedAt&apiKey={API_KEY}'
        response = requests.get(url)
        data = response.json()
        
        articles = data['articles']
    else:
        url= f'https://newsapi.org/v2/top-headlines?category={category}&apiKey={API_KEY}'
        response = requests.get(url)
        data = response.json()
        articles = data['articles']

    
    context = {
        'articles': articles
    }
    
    return render (request ,'news_api/home.html',context)